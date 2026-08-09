"""bench_edge_cloud.py — main Edge-Cloud SD benchmark.

Reuses the GSM8K data file from Day 3. Runs full GSM8K samples through
the edge_client + verifier (mock or remote) and writes a JSON summary
similar to Day 1/2 results so summarize_day2.py can pick it up.

Output JSON shape matches Day 1 results format so it slots into
the existing comparison.md generator on H200.
"""
import argparse
import json
import pathlib
import re
import sys
import time
from typing import Optional

from tqdm import tqdm

from edge.edge_client import EdgeClient
from edge.verifier import MockVerifier, RemoteVerifier, VerifierBase


SYSTEM_PROMPT = (
    "You are a math tutor. Solve the problem step by step. "
    "End your answer with exactly: 'Final answer: <number>'."
)

ANSWER_RE = re.compile(r"final answer\s*[:\-]?\s*\$?(-?[\d,]+(?:\.\d+)?)", re.I)


def extract_numeric(text: str) -> Optional[str]:
    m = ANSWER_RE.search(text or "")
    if m:
        return m.group(1).replace(",", "").rstrip(".")
    nums = re.findall(r"-?\d+(?:\.\d+)?", text or "")
    return nums[-1] if nums else None


def normalize(x):
    if x is None:
        return None
    x = x.replace(",", "").strip()
    try:
        f = float(x)
        return str(int(f)) if f.is_integer() else str(f)
    except ValueError:
        return x


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", choices=["mock", "remote"], required=True)
    ap.add_argument("--draft-url", default="http://localhost:8080",
                    help="Local Jetson llama-server")
    ap.add_argument("--remote-url", default=None,
                    help="H200 verify_server, e.g. http://foscsmlprd03.its.auckland.ac.nz:9090")
    ap.add_argument("--gamma", type=int, default=5)
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--data", default="common/data/gsm8k_test_50.jsonl",
                    help="Reuses Day 3's data file by default")
    ap.add_argument("--n", type=int, default=50)
    ap.add_argument("--tag", default=None,
                    help="label for the run; defaults to <verifier>_g<gamma>")
    ap.add_argument("--out", required=True)
    ap.add_argument("--model-config", default=None,
                    help="name of a pair in models.yaml (e.g. llama3, qwen25)")
    ap.add_argument("--models-yaml", default=None)
    ap.add_argument("--no-think", action="store_true",
                    help="append /no_think to the user turn to disable Qwen3 thinking")
    args = ap.parse_args()

    mcfg = None
    eos_id = None
    if args.model_config:
        from model_config import load_model_config
        mcfg = load_model_config(args.model_config, args.models_yaml)
        eos_id = mcfg["eos_id"]
        print(f"[model_config] '{mcfg['_name']}': target={mcfg['target']}, "
              f"eos_id={eos_id}, vocab={mcfg['vocab_size']}")

    if args.tag is None:
        args.tag = f"B3_{args.verifier}_g{args.gamma}"

    # ---- Set up client + verifier ----------------------------------------
    client = EdgeClient(draft_url=args.draft_url)
    if args.verifier == "mock":
        verifier: VerifierBase = MockVerifier(base_url=args.draft_url)
    else:
        if not args.remote_url:
            raise SystemExit("--remote-url is required for --verifier remote")
        verifier = RemoteVerifier(url=args.remote_url)
        # Smoke health check so we fail fast if H200 is down
        try:
            h = verifier.health()
            print(f"[{args.tag}] H200 verify server: {h}")
            i = verifier.info()
            print(f"[{args.tag}] H200 target model: {i.get('target_model')}, "
                  f"vocab={i.get('vocab_size')}")
        except Exception as e:
            raise SystemExit(f"cannot reach remote verifier: {e}")
        if mcfg is not None:
            from model_config import validate_pair
            # strict_vocab:false in models.yaml downgrades a vocab-size mismatch
            # from fatal to a warning. Needed for pairs whose tokenizer is
            # identical but whose embedding matrix is padded to a different
            # vocab_size (e.g. DeepSeek-R1-Distill-Qwen 1.5B=151936 vs 32B).
            validate_pair(client, verifier, mcfg,
                          strict=mcfg.get("strict_vocab", True))

    # ---- Load data --------------------------------------------------------
    data_path = pathlib.Path(args.data)
    if not data_path.exists():
        raise SystemExit(f"data file not found: {data_path}; "
                         "run day3's bench_draft.py once to create it.")
    samples = []
    with data_path.open() as f:
        for line in f:
            samples.append(json.loads(line))
    samples = samples[:args.n]
    print(f"[{args.tag}] {len(samples)} samples, γ={args.gamma}, verifier={args.verifier}")

    # ---- Warmup -----------------------------------------------------------
    print(f"[{args.tag}] warmup")
    _, _ = client.generate(
        messages=[{"role": "user", "content": "Hi"}],
        verifier=verifier,
        gamma=args.gamma,
        max_tokens=16,
        temperature=args.temperature,
        eos_id=eos_id,
        no_think=args.no_think,
    )

    # ---- Main loop --------------------------------------------------------
    records = []
    t0_total = time.perf_counter()
    for ex in tqdm(samples, desc=args.tag):
        text, m = client.generate(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": ex["question"]},
            ],
            verifier=verifier,
            gamma=args.gamma,
            max_tokens=args.max_tokens,
            temperature=args.temperature,
            eos_id=eos_id,
            no_think=args.no_think,
        )
        pred = normalize(extract_numeric(text))
        gold = normalize(ex["gold_answer"])
        records.append({
            "id": ex["id"],
            "wall_time_s": m.wall_time_s,
            "output_tokens": m.total_output_tokens,
            "tokens_per_second": m.tokens_per_second,
            "n_rounds": m.n_rounds,
            "n_accepted": m.n_accepted,
            "n_proposed": m.n_draft_proposed,
            "acceptance_rate": m.acceptance_rate,
            "draft_time_ms": m.draft_time_ms,
            "verify_time_ms": m.verify_time_ms,
            "network_time_ms": m.network_time_ms,
            "pred": pred,
            "gold": gold,
            "correct": pred == gold,
            "rounds": m.rounds,
        })
    total_wall = time.perf_counter() - t0_total

    # ---- Aggregate --------------------------------------------------------
    n = len(records)
    acc = sum(r["correct"] for r in records) / n
    sum_out = sum(r["output_tokens"] for r in records)
    sum_wall = sum(r["wall_time_s"] for r in records)
    agg_tps = sum_out / sum_wall if sum_wall else 0
    avg_lat = sum_wall / n
    avg_out = sum_out / n
    sum_acc = sum(r["n_accepted"] for r in records)
    sum_prop = sum(r["n_proposed"] for r in records)
    sum_rounds = sum(r["n_rounds"] for r in records)
    agg_accept = sum_acc / max(1, sum_prop)
    # Effective tokens per verification round (comparable to Venkatesha et al.
    # 2025, "Avg Tokens tau" in their Table 6). Each verification yields the
    # accepted prefix plus one bonus/correction token, so tau = (accepted +
    # rounds) / rounds. tau_accepted excludes the bonus token.
    tau_accepted = sum_acc / max(1, sum_rounds)
    tau_tokens_per_verify = (sum_acc + sum_rounds) / max(1, sum_rounds)
    avg_draft  = sum(r["draft_time_ms"]   for r in records) / n
    avg_verify = sum(r["verify_time_ms"]  for r in records) / n
    avg_network= sum(r["network_time_ms"] for r in records) / n

    summary = {
        "tag": args.tag,
        "verifier": args.verifier,
        "remote_url": args.remote_url if args.verifier == "remote" else None,
        "gamma": args.gamma,
        "n_samples": n,
        "accuracy": acc,
        "aggregate_tokens_per_second": agg_tps,
        "avg_latency_s": avg_lat,
        "avg_output_tokens": avg_out,
        "acceptance_rate": agg_accept,
        "tau_tokens_per_verify": tau_tokens_per_verify,
        "tau_accepted_per_round": tau_accepted,
        "avg_draft_ms_per_req": avg_draft,
        "avg_verify_ms_per_req": avg_verify,
        "avg_network_ms_per_req": avg_network,
        "total_wall_s": total_wall,
    }

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        json.dump({"summary": summary, "records": records}, f, indent=2)

    print(f"\n[{args.tag}] === Summary ===")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print(f"[{args.tag}] Wrote {out}")


if __name__ == "__main__":
    main()
