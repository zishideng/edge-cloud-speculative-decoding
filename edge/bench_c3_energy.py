"""bench_c3_energy.py — Power-mode × γ grid sweep with energy measurement.

For each (power_mode, γ) cell, runs N samples through edge-cloud SD and
records: tokens/sec, accuracy, acceptance, joules, J/token.

Outputs a single JSON with all cells. Final paper Table 2.

IMPORTANT: this script does NOT change power mode itself (requires sudo).
You set it manually before each run; the script reports what jtop sees.

Usage:
    # Set power mode (you, once per run)
    sudo nvpmodel -m 0   # 15W
    sudo jetson_clocks

    # Then run sweep at that mode
    python bench_c3_energy.py \
        --power-mode 15W \
        --remote-url http://localhost:9090 \
        --gammas 2 3 5 \
        --n 30 \
        --out ~/b3_results/C3_15W.json

Repeat with --power-mode 7W (after nvpmodel -m 1) and --power-mode MAXN
(after nvpmodel -m 2).

Combine with summarize_c3.py at the end.
"""
import argparse, json, pathlib, re, time
from tqdm import tqdm
from edge.edge_client import EdgeClient
from edge.verifier import RemoteVerifier
from edge.energy_profiler import EnergyProfiler

SYSTEM_PROMPT = (
    "You are a math tutor. Solve the problem step by step. "
    "End your answer with exactly: 'Final answer: <number>'."
)
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

def run_cell(client, verifier, samples, gamma, max_tokens, temperature):
    """Run N samples at fixed γ, profile energy. Return cell summary dict."""
    # Warmup (not measured)
    client.generate(messages=[{"role": "user", "content": "Hi"}],
                    verifier=verifier, gamma=gamma, max_tokens=16,
                    temperature=temperature)

    records = []
    with EnergyProfiler(label=f"gamma={gamma}") as ep:
        t0 = time.perf_counter()
        for ex in tqdm(samples, desc=f"γ={gamma}", leave=False):
            text, m = client.generate(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": ex["question"]},
                ],
                verifier=verifier, gamma=gamma,
                max_tokens=max_tokens, temperature=temperature,
            )
            pred = normalize(extract_numeric(text))
            gold = normalize(ex["gold_answer"])
            records.append({
                "id": ex["id"],
                "wall_time_s": m.wall_time_s,
                "output_tokens": m.total_output_tokens,
                "n_accepted": m.n_accepted,
                "n_proposed": m.n_draft_proposed,
                "correct": pred == gold,
            })
        wall = time.perf_counter() - t0
    ep_sum = ep.summary()

    n = len(records)
    sum_out = sum(r["output_tokens"] for r in records)
    sum_wall = sum(r["wall_time_s"] for r in records)
    sum_acc  = sum(r["n_accepted"] for r in records)
    sum_prop = sum(r["n_proposed"] for r in records)

    cell = {
        "gamma": gamma,
        "n_samples": n,
        "wall_s": wall,
        "accuracy": sum(r["correct"] for r in records) / n,
        "agg_tok_s": sum_out / sum_wall if sum_wall else 0,
        "acceptance": sum_acc / max(1, sum_prop),
        "avg_latency_s": sum_wall / n,
        "avg_output_tokens": sum_out / n,
        # Energy
        "joules": ep_sum["joules"],
        "avg_watts": ep_sum["avg_watts"],
        "peak_watts": ep_sum["peak_watts"],
        "energy_samples": ep_sum["n_samples"],
        "joules_per_token": (ep_sum["joules"] / sum_out) if sum_out else 0,
    }
    return cell

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--power-mode", required=True, help="label like 7W/15W/MAXN")
    ap.add_argument("--remote-url", default="http://localhost:9090")
    ap.add_argument("--draft-url", default="http://localhost:8080")
    ap.add_argument("--gammas", type=int, nargs="+", default=[2, 3, 5])
    ap.add_argument("--n", type=int, default=30)
    ap.add_argument("--data", required=True)
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    client = EdgeClient(draft_url=args.draft_url)
    verifier = RemoteVerifier(url=args.remote_url)
    print(f"[C3] verify health: {verifier.health()}")

    samples = []
    with open(args.data) as f:
        for line in f: samples.append(json.loads(line))
    samples = samples[:args.n]

    print(f"[C3] power_mode={args.power_mode}, γs={args.gammas}, n={args.n}")
    cells = []
    for g in args.gammas:
        print(f"\n[C3] === γ={g} ===")
        cell = run_cell(client, verifier, samples, g, args.max_tokens, args.temperature)
        cells.append(cell)
        print(f"     tok/s={cell['agg_tok_s']:.2f}  acc={cell['accuracy']:.0%}  "
              f"accept={cell['acceptance']:.0%}  W={cell['avg_watts']:.1f}  "
              f"J/tok={cell['joules_per_token']:.3f}")

    result = {
        "power_mode": args.power_mode,
        "n_samples": args.n,
        "cells": cells,
    }
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        json.dump(result, f, indent=2)
    print(f"\n[C3] wrote {out}")

if __name__ == "__main__":
    main()
