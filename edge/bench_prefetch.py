"""bench_prefetch.py — Compare sync vs prefetch async SD.

--mode sync     : enable_prefetch=False (baseline, same code path)
--mode prefetch : enable_prefetch=True

Same data/tasks/energy as bench_warmup.py.

Usage:
    python bench_prefetch.py --mode sync     --gamma 3 --task gsm8k \
        --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl --n 30 \
        --profile-energy --out ~/b3_results/P_sync_gsm8k.json
    python bench_prefetch.py --mode prefetch --gamma 3 --task gsm8k \
        --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl --n 30 \
        --profile-energy --out ~/b3_results/P_prefetch_gsm8k.json
"""
import argparse, json, pathlib, re, time
from tqdm import tqdm

from edge.edge_client_prefetch import PrefetchEdgeClient
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

def extract_numeric(t):
    m = ANSWER_RE.search(t or "")
    if m: return m.group(1).replace(",", "").rstrip(".")
    nums = re.findall(r"-?\d+(?:\.\d+)?", t or "")
    return nums[-1] if nums else None

def normalize(x):
    if x is None: return None
    x = x.replace(",", "").strip()
    try:
        f = float(x); return str(int(f)) if f.is_integer() else str(f)
    except ValueError: return x

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["sync", "prefetch"], required=True)
    ap.add_argument("--gamma", type=int, default=3)
    ap.add_argument("--task", choices=["gsm8k","humaneval","mtbench"], default="gsm8k")
    ap.add_argument("--remote-url", default="http://localhost:9090")
    ap.add_argument("--draft-url", default="http://localhost:8080")
    ap.add_argument("--data", required=True)
    ap.add_argument("--n", type=int, default=30)
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--profile-energy", action="store_true")
    ap.add_argument("--out", required=True)
    ap.add_argument("--tag", default=None)
    args = ap.parse_args()

    tag = args.tag or f"P_{args.mode}_g{args.gamma}_{args.task}"
    enable = (args.mode == "prefetch")
    client = PrefetchEdgeClient(draft_url=args.draft_url, enable_prefetch=enable)
    verifier = RemoteVerifier(url=args.remote_url)
    print(f"[{tag}] verify: {verifier.health()}  prefetch={enable}")

    samples = []
    with open(args.data) as f:
        for line in f: samples.append(json.loads(line))
    samples = samples[:args.n]
    sys_prompt = SYSTEM_PROMPTS[args.task]

    client.generate(messages=[{"role":"user","content":"Hi"}],
                    verifier=verifier, gamma=args.gamma, max_tokens=16,
                    temperature=args.temperature)

    def run_loop():
        records = []
        t0 = time.perf_counter()
        for ex in tqdm(samples, desc=tag):
            q = ex.get("question") or ex.get("prompt") or ex.get("turns", [""])[0]
            text, m = client.generate(
                messages=[{"role":"system","content":sys_prompt},
                          {"role":"user","content":q}],
                verifier=verifier, gamma=args.gamma,
                max_tokens=args.max_tokens, temperature=args.temperature,
            )
            correct = None
            if args.task == "gsm8k":
                correct = normalize(extract_numeric(text)) == normalize(ex.get("gold_answer",""))
            records.append({
                "id": ex.get("id"),
                "wall_time_s": m.wall_time_s,
                "output_tokens": m.total_output_tokens,
                "n_accepted": m.n_accepted,
                "n_proposed": m.n_draft_proposed,
                "n_rounds": m.n_rounds,
                "prefetch_hits": m.n_prefetch_hits,
                "prefetch_miss": m.n_prefetch_miss,
                "draft_time_ms": m.draft_time_ms,
                "verify_time_ms": m.verify_time_ms,
                "network_time_ms": m.network_time_ms,
                "correct": correct,
            })
        return records, time.perf_counter() - t0

    if args.profile_energy:
        with EnergyProfiler(label=tag) as ep:
            records, wall = run_loop()
        ep_sum = ep.summary()
    else:
        records, wall = run_loop()
        ep_sum = {"joules":0,"avg_watts":0,"n_samples":0}

    n = len(records)
    sum_out  = sum(r["output_tokens"] for r in records)
    sum_wall = sum(r["wall_time_s"]  for r in records)
    sum_acc  = sum(r["n_accepted"]   for r in records)
    sum_prop = sum(r["n_proposed"]   for r in records)
    sum_hits = sum(r["prefetch_hits"] for r in records)
    sum_miss = sum(r["prefetch_miss"] for r in records)
    acc = (sum(r["correct"] for r in records if r["correct"] is not None)/n
           if args.task=="gsm8k" else None)

    summary = {
        "tag": tag, "mode": args.mode, "gamma": args.gamma, "task": args.task,
        "n_samples": n, "accuracy": acc,
        "agg_tok_s": sum_out/sum_wall if sum_wall else 0,
        "acceptance": sum_acc/max(1,sum_prop),
        "avg_latency_s": sum_wall/n,
        "avg_output_tokens": sum_out/n,
        "prefetch_hit_rate": sum_hits/max(1,sum_hits+sum_miss),
        "avg_draft_ms": sum(r["draft_time_ms"] for r in records)/n,
        "avg_verify_ms": sum(r["verify_time_ms"] for r in records)/n,
        "avg_network_ms": sum(r["network_time_ms"] for r in records)/n,
        "joules": ep_sum["joules"], "avg_watts": ep_sum["avg_watts"],
        "joules_per_token": (ep_sum["joules"]/sum_out) if sum_out and ep_sum["joules"] else 0,
        "total_wall_s": wall,
    }
    out = pathlib.Path(args.out); out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        json.dump({"summary": summary, "records": records}, f, indent=2)
    print(f"\n[{tag}] Summary:")
    for k,v in summary.items(): print(f"  {k}: {v}")
    print(f"  → {out}")

if __name__ == "__main__":
    main()
