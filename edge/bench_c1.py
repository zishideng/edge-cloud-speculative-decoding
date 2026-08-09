"""bench_c1.py — benchmark C1 adaptive γ controller.

Mirrors bench_edge_cloud.py but uses EdgeClientC1.
Outputs JSON in same format so it slots into existing summarize tools.
"""
import argparse, json, pathlib, re, time
from typing import Optional
from tqdm import tqdm

from edge.edge_client_c1 import EdgeClientC1, C1Config
from edge.verifier import RemoteVerifier, MockVerifier

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

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", choices=["mock", "remote"], default="remote")
    ap.add_argument("--draft-url", default="http://localhost:8080")
    ap.add_argument("--remote-url", default="http://localhost:9090")
    ap.add_argument("--gamma-init", type=int, default=3)
    ap.add_argument("--gamma-min", type=int, default=2)
    ap.add_argument("--gamma-max", type=int, default=8)
    ap.add_argument("--thresh-hi", type=float, default=0.80)
    ap.add_argument("--thresh-lo", type=float, default=0.55)
    ap.add_argument("--lp-thresh", type=float, default=-1.5)
    ap.add_argument("--beta", type=float, default=0.7)
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--data", required=True)
    ap.add_argument("--n", type=int, default=50)
    ap.add_argument("--out", required=True)
    ap.add_argument("--tag", default="B5_C1")
    args = ap.parse_args()

    cfg = C1Config(
        gamma_init=args.gamma_init, gamma_min=args.gamma_min, gamma_max=args.gamma_max,
        thresh_hi=args.thresh_hi, thresh_lo=args.thresh_lo,
        lp_thresh=args.lp_thresh, beta=args.beta,
    )
    client = EdgeClientC1(draft_url=args.draft_url, c1_cfg=cfg)
    if args.verifier == "remote":
        verifier = RemoteVerifier(url=args.remote_url)
        print(f"[{args.tag}] verify: {verifier.health()}")
    else:
        verifier = MockVerifier(base_url=args.draft_url)

    samples = []
    with open(args.data) as f:
        for line in f: samples.append(json.loads(line))
    samples = samples[:args.n]
    print(f"[{args.tag}] {len(samples)} samples, C1: {cfg}")

    # Warmup
    client.generate(
        messages=[{"role": "user", "content": "Hi"}],
        verifier=verifier, max_tokens=16, temperature=args.temperature,
    )

    records = []
    t0 = time.perf_counter()
    for ex in tqdm(samples, desc=args.tag):
        text, m = client.generate(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": ex["question"]},
            ],
            verifier=verifier, max_tokens=args.max_tokens,
            temperature=args.temperature,
        )
        pred = normalize(extract_numeric(text))
        gold = normalize(ex["gold_answer"])
        # Compute avg γ used across rounds
        gammas = [r["gamma"] for r in m.rounds]
        avg_gamma = sum(gammas) / max(1, len(gammas))
        records.append({
            "id": ex["id"],
            "wall_time_s": m.wall_time_s,
            "output_tokens": m.total_output_tokens,
            "tokens_per_second": m.tokens_per_second,
            "n_rounds": m.n_rounds,
            "n_accepted": m.n_accepted,
            "n_proposed": m.n_draft_proposed,
            "acceptance_rate": m.acceptance_rate,
            "avg_gamma": avg_gamma,
            "draft_time_ms": m.draft_time_ms,
            "verify_time_ms": m.verify_time_ms,
            "network_time_ms": m.network_time_ms,
            "pred": pred, "gold": gold,
            "correct": pred == gold,
            "rounds": m.rounds,
        })
    total_wall = time.perf_counter() - t0

    n = len(records)
    sum_out = sum(r["output_tokens"] for r in records)
    sum_wall = sum(r["wall_time_s"] for r in records)
    summary = {
        "tag": args.tag,
        "method": "C1_adaptive_gamma",
        "c1_config": cfg.__dict__,
        "n_samples": n,
        "accuracy": sum(r["correct"] for r in records) / n,
        "aggregate_tokens_per_second": sum_out / sum_wall if sum_wall else 0,
        "avg_latency_s": sum_wall / n,
        "avg_output_tokens": sum_out / n,
        "acceptance_rate": sum(r["n_accepted"] for r in records) / max(1, sum(r["n_proposed"] for r in records)),
        "avg_gamma_overall": sum(r["avg_gamma"] for r in records) / n,
        "avg_draft_ms_per_req": sum(r["draft_time_ms"] for r in records) / n,
        "avg_verify_ms_per_req": sum(r["verify_time_ms"] for r in records) / n,
        "avg_network_ms_per_req": sum(r["network_time_ms"] for r in records) / n,
        "total_wall_s": total_wall,
    }

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        json.dump({"summary": summary, "records": records}, f, indent=2)

    print(f"\n[{args.tag}] Summary:")
    for k, v in summary.items():
        if k != "c1_config":
            print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
