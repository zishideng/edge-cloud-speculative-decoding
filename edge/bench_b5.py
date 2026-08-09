"""bench_b5.py — Run B5 (SLO-routed Ours) on a dataset.

Picks γ via the C3 lookup table for the given SLO, runs the bench,
also profiles energy so we can compare J/tok to C3 cells.

Usage:
    # Set Jetson power mode to match what router picks for your SLO
    sudo nvpmodel -m 0   # 15W (for SLO 15s)
    python bench_b5.py \
        --lookup ~/b3_results/C3_lookup.json \
        --slo 15 --power-mode 15W \
        --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl \
        --n 30 \
        --out ~/b3_results/B5_slo15_15W.json
"""
import argparse, json, pathlib, re, time
from tqdm import tqdm

from edge.edge_client_b5 import EdgeClientB5, SLORouter
from edge.verifier import RemoteVerifier
from edge.energy_profiler import EnergyProfiler

SYSTEM_PROMPT_MATH = (
    "You are a math tutor. Solve the problem step by step. "
    "End your answer with exactly: 'Final answer: <number>'."
)
SYSTEM_PROMPT_CODE = (
    "You are a Python expert. Provide a complete function implementation. "
    "Output only the function code."
)
SYSTEM_PROMPT_CHAT = "You are a helpful assistant. Provide a clear, concise answer."

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
    ap.add_argument("--lookup", required=True)
    ap.add_argument("--slo", type=float, default=15.0)
    ap.add_argument("--power-mode", required=True,
                    help="What power mode you SET on Jetson (label only)")
    ap.add_argument("--remote-url", default="http://localhost:9090")
    ap.add_argument("--draft-url", default="http://localhost:8080")
    ap.add_argument("--data", required=True)
    ap.add_argument("--n", type=int, default=30)
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--task", choices=["gsm8k", "humaneval", "mtbench"], default="gsm8k")
    ap.add_argument("--out", required=True)
    ap.add_argument("--tag", default=None)
    args = ap.parse_args()

    tag = args.tag or f"B5_slo{int(args.slo)}_{args.power_mode}"

    router = SLORouter(args.lookup, current_power_mode=args.power_mode)
    chosen = router.route(args.slo)
    print(f"[{tag}] SLO {args.slo}s → router picks: {chosen}")
    if chosen["power_mode"] != args.power_mode:
        print(f"  WARNING: router wants {chosen['power_mode']} but Jetson is on {args.power_mode}.")
        print(f"  Run `sudo nvpmodel -m <N>` to match, then re-run for accurate energy.")

    client = EdgeClientB5(draft_url=args.draft_url, router=router,
                          slo_latency_s=args.slo)
    verifier = RemoteVerifier(url=args.remote_url)
    print(f"[{tag}] verify: {verifier.health()}")

    samples = []
    with open(args.data) as f:
        for line in f: samples.append(json.loads(line))
    samples = samples[:args.n]

    # Pick system prompt based on task
    sys_prompt = {
        "gsm8k": SYSTEM_PROMPT_MATH,
        "humaneval": SYSTEM_PROMPT_CODE,
        "mtbench": SYSTEM_PROMPT_CHAT,
    }[args.task]

    # Warmup
    g = client.get_routed_gamma()
    client.generate(messages=[{"role": "user", "content": "Hi"}],
                    verifier=verifier, gamma=g, max_tokens=16,
                    temperature=args.temperature)

    records = []
    with EnergyProfiler(label=tag) as ep:
        t0 = time.perf_counter()
        for ex in tqdm(samples, desc=tag):
            g = client.get_routed_gamma()
            question = ex.get("question") or ex.get("prompt") or ex.get("turns", [""])[0]
            text, m = client.generate(
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": question},
                ],
                verifier=verifier, gamma=g,
                max_tokens=args.max_tokens, temperature=args.temperature,
            )
            # Eval only meaningful for gsm8k / humaneval
            correct = None
            if args.task == "gsm8k":
                pred = normalize(extract_numeric(text))
                gold = normalize(ex.get("gold_answer", ""))
                correct = pred == gold
            records.append({
                "id": ex.get("id"),
                "gamma_used": g,
                "wall_time_s": m.wall_time_s,
                "output_tokens": m.total_output_tokens,
                "n_accepted": m.n_accepted,
                "n_proposed": m.n_draft_proposed,
                "correct": correct,
                "answer_text": text[:200] if args.task != "gsm8k" else None,
                "rounds": m.rounds,
            })
        wall = time.perf_counter() - t0
    ep_sum = ep.summary()

    n = len(records)
    sum_out  = sum(r["output_tokens"] for r in records)
    sum_wall = sum(r["wall_time_s"]  for r in records)
    sum_acc  = sum(r["n_accepted"]   for r in records)
    sum_prop = sum(r["n_proposed"]   for r in records)
    if args.task == "gsm8k":
        accuracy = sum(r["correct"] for r in records if r["correct"] is not None) / n
    else:
        accuracy = None

    summary = {
        "tag": tag,
        "task": args.task,
        "slo": args.slo,
        "power_mode": args.power_mode,
        "routed_config": chosen,
        "n_samples": n,
        "accuracy": accuracy,
        "agg_tok_s": sum_out / sum_wall if sum_wall else 0,
        "acceptance": sum_acc / max(1, sum_prop),
        "avg_latency_s": sum_wall / n,
        "avg_output_tokens": sum_out / n,
        "joules": ep_sum["joules"],
        "avg_watts": ep_sum["avg_watts"],
        "joules_per_token": (ep_sum["joules"] / sum_out) if sum_out else 0,
        "total_wall_s": wall,
    }

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        json.dump({"summary": summary, "records": records}, f, indent=2)

    print(f"\n[{tag}] Summary:")
    for k, v in summary.items():
        if k != "routed_config":
            print(f"  {k}: {v}")
    print(f"  → wrote {out}")

if __name__ == "__main__":
    main()
