"""bench_warmup.py — Compare fixed-γ vs warmup-aware γ schedule.

Drop-in for B3 comparison. Same data + tasks as bench_b5.py but with
schedule selector.

Usage:
    # Baseline: fixed γ=3
    python bench_warmup.py --schedule fixed --gamma 3 --task gsm8k \
        --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl --n 30 \
        --out ~/b3_results/W_fixed_g3_gsm8k.json

    # Warmup-aware (γ ramps 1→2→3 then steady at 3)
    python bench_warmup.py --schedule warmup --gamma 3 --task gsm8k \
        --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl --n 30 \
        --out ~/b3_results/W_warmup_g3_gsm8k.json
"""
import argparse, json, pathlib, re, time
from tqdm import tqdm

from edge.edge_client import EdgeClient
from edge.edge_client_warmup import WarmupAwareEdgeClient, WarmupConfig
from edge.verifier import RemoteVerifier
from edge.energy_profiler import EnergyProfiler

SYSTEM_PROMPTS = {
    "gsm8k": ("You are a math tutor. Solve the problem step by step. "
              "End your answer with exactly: 'Final answer: <number>'."),
    "humaneval": ("You are a Python expert. Provide a complete function "
                  "implementation. Output only the function code."),
    "mtbench": "You are a helpful assistant. Provide a clear, concise answer.",
}

ANSWER_RE = re.compile(r"final answer\s*[:\-]?\s*\$?(-?[\d,]+(?:\.\d+)?)", re.I)

def extract_numeric(text):
    m = ANSWER_RE.search(text or "")
    if m: return m.group(1).replace(",", "").rstrip(".")
    nums = re.findall(r"-?\d+(?:\.\d+)?", text or "")
    return nums[-1] if nums else None

def normalize(x):
    if x is None: return None
    x = x.replace(",", "").strip()
    try:
        f = float(x); return str(int(f)) if f.is_integer() else str(f)
    except ValueError: return x

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schedule", choices=["fixed", "warmup"], required=True)
    ap.add_argument("--gamma", type=int, default=3,
                    help="for fixed: γ used every round; for warmup: γ_steady")
    ap.add_argument("--warmup-rounds", type=int, default=3)
    ap.add_argument("--warmup-step", type=int, default=1)
    ap.add_argument("--warmup-init", type=int, default=1)
    ap.add_argument("--task", choices=["gsm8k", "humaneval", "mtbench"],
                    default="gsm8k")
    ap.add_argument("--remote-url", default="http://localhost:9090")
    ap.add_argument("--draft-url", default="http://localhost:8080")
    ap.add_argument("--data", required=True)
    ap.add_argument("--n", type=int, default=30)
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--profile-energy", action="store_true",
                    help="run with EnergyProfiler (Jetson only)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--tag", default=None)
    args = ap.parse_args()

    tag = args.tag or f"W_{args.schedule}_g{args.gamma}_{args.task}"

    # Pick client
    if args.schedule == "warmup":
        wcfg = WarmupConfig(
            gamma_steady=args.gamma,
            warmup_rounds=args.warmup_rounds,
            warmup_step=args.warmup_step,
            gamma_init=args.warmup_init,
        )
        client = WarmupAwareEdgeClient(draft_url=args.draft_url, wcfg=wcfg)
        print(f"[{tag}] warmup: {wcfg}")
    else:
        client = EdgeClient(draft_url=args.draft_url)
        print(f"[{tag}] fixed γ={args.gamma}")

    verifier = RemoteVerifier(url=args.remote_url)
    print(f"[{tag}] verify: {verifier.health()}")

    samples = []
    with open(args.data) as f:
        for line in f: samples.append(json.loads(line))
    samples = samples[:args.n]

    sys_prompt = SYSTEM_PROMPTS[args.task]

    # Warmup (model load + KV alloc; not measured)
    client.generate(messages=[{"role": "user", "content": "Hi"}],
                    verifier=verifier, gamma=args.gamma, max_tokens=16,
                    temperature=args.temperature)

    # Run
    def run_loop():
        records = []
        t0 = time.perf_counter()
        for ex in tqdm(samples, desc=tag):
            question = ex.get("question") or ex.get("prompt") or ex.get("turns", [""])[0]
            text, m = client.generate(
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": question},
                ],
                verifier=verifier, gamma=args.gamma,
                max_tokens=args.max_tokens, temperature=args.temperature,
            )
            correct = None
            if args.task == "gsm8k":
                pred = normalize(extract_numeric(text))
                gold = normalize(ex.get("gold_answer", ""))
                correct = pred == gold
            records.append({
                "id": ex.get("id"),
                "wall_time_s": m.wall_time_s,
                "output_tokens": m.total_output_tokens,
                "n_accepted": m.n_accepted,
                "n_proposed": m.n_draft_proposed,
                "correct": correct,
                "rounds": m.rounds,
            })
        wall = time.perf_counter() - t0
        return records, wall

    if args.profile_energy:
        with EnergyProfiler(label=tag) as ep:
            records, wall = run_loop()
        ep_sum = ep.summary()
    else:
        records, wall = run_loop()
        ep_sum = {"joules": 0, "avg_watts": 0, "peak_watts": 0,
                  "n_samples": 0, "available": False}

    n = len(records)
    sum_out  = sum(r["output_tokens"] for r in records)
    sum_wall = sum(r["wall_time_s"]  for r in records)
    sum_acc  = sum(r["n_accepted"]   for r in records)
    sum_prop = sum(r["n_proposed"]   for r in records)
    if args.task == "gsm8k":
        acc = sum(r["correct"] for r in records if r["correct"] is not None) / n
    else:
        acc = None

    # Per-round acceptance (the key analysis for this paper!)
    by_pos = {}
    for rec in records:
        for i, rnd in enumerate(rec["rounds"]):
            g = rnd.get("gamma", 1)
            ap_ = rnd["n_accepted"] / max(1, g)
            by_pos.setdefault(i, []).append(ap_)
    round_profile = {
        str(i): {
            "mean_accept": sum(v) / len(v),
            "n": len(v),
        }
        for i, v in sorted(by_pos.items()) if len(v) >= 5
    }

    summary = {
        "tag": tag,
        "schedule": args.schedule,
        "gamma": args.gamma,
        "warmup_rounds": args.warmup_rounds if args.schedule == "warmup" else None,
        "task": args.task,
        "n_samples": n,
        "accuracy": acc,
        "agg_tok_s": sum_out / sum_wall if sum_wall else 0,
        "acceptance": sum_acc / max(1, sum_prop),
        "avg_latency_s": sum_wall / n,
        "avg_output_tokens": sum_out / n,
        "round_0_accept": round_profile.get("0", {}).get("mean_accept"),
        "round_2plus_accept": (
            sum(round_profile[str(i)]["mean_accept"]
                * round_profile[str(i)]["n"] for i in range(2, 30) if str(i) in round_profile)
            / max(1, sum(round_profile[str(i)]["n"] for i in range(2, 30) if str(i) in round_profile))
        ) if any(str(i) in round_profile for i in range(2, 30)) else None,
        "joules": ep_sum["joules"],
        "avg_watts": ep_sum["avg_watts"],
        "joules_per_token": (ep_sum["joules"] / sum_out) if sum_out and ep_sum["joules"] else 0,
        "total_wall_s": wall,
    }

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        json.dump({"summary": summary, "round_profile": round_profile,
                   "records": records}, f, indent=2)

    print(f"\n[{tag}] Summary:")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print(f"  → wrote {out}")

if __name__ == "__main__":
    main()
