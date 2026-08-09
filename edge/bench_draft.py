"""Benchmark the Jetson llama-server alone on a fixed prompt set.

This isn't an Edge-Cloud benchmark — it's a single-machine baseline
that tells us:
  - tokens/sec on Jetson with Llama-3.2-1B
  - latency per request
  - any obvious draft-quality issues

The number you get here is your "draft model speed ceiling" — the rest of
the project is about not wasting that capacity.

Run after `bash start_server.sh &` is up on the same host.
"""
import argparse
import json
import os
import pathlib
import re
import time

from openai import OpenAI
from tqdm import tqdm

SYSTEM_PROMPT = (
    "You are a math tutor. Solve the problem step by step. "
    "End your answer with exactly: 'Final answer: <number>'."
)

ANSWER_RE = re.compile(r"final answer\s*[:\-]?\s*\$?(-?[\d,]+(?:\.\d+)?)", re.I)


def extract_numeric(text):
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
    ap.add_argument("--base-url", default="http://localhost:8080/v1")
    ap.add_argument("--model", default="llama-3.2-1b",
                    help="ID llama-server reports; usually the gguf basename")
    ap.add_argument("--data", default="common/data/gsm8k_test_50.jsonl",
                    help="JSONL with question/gold_answer; auto-built if missing")
    ap.add_argument("--n", type=int, default=50,
                    help="how many GSM8K samples to fetch & test")
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--out", default="jetson_draft_baseline.json")
    args = ap.parse_args()

    # ---- Build sample file on the fly if missing ---------------------------
    data_path = pathlib.Path(args.data)
    if not data_path.exists():
        print(f"[bench] {data_path} not found; fetching GSM8K from HF...")
        try:
            from datasets import load_dataset
        except ImportError:
            raise SystemExit(
                "Need `datasets` for first-time data fetch. "
                "pip install datasets, or copy gsm8k_test_50.jsonl from H200."
            )
        ds = load_dataset("openai/gsm8k", "main", split="test")
        with data_path.open("w") as f:
            for i, ex in enumerate(ds.select(range(args.n))):
                gold = ex["answer"].split("####")[-1].strip().replace(",", "")
                f.write(json.dumps({
                    "id": i,
                    "question": ex["question"],
                    "gold_answer": gold,
                }) + "\n")
        print(f"[bench] wrote {args.n} samples → {data_path}")

    samples = []
    with data_path.open() as f:
        for line in f:
            samples.append(json.loads(line))
    samples = samples[:args.n]

    # ---- Connect to local llama-server ------------------------------------
    client = OpenAI(base_url=args.base_url, api_key="EMPTY")
    print(f"[bench] hitting {args.base_url}")

    print("[bench] warmup")
    client.chat.completions.create(
        model=args.model,
        messages=[{"role": "user", "content": "Hi"}],
        max_tokens=8, temperature=0.0,
    )

    # ---- Loop --------------------------------------------------------------
    records = []
    for ex in tqdm(samples, desc="bench"):
        t0 = time.perf_counter()
        resp = client.chat.completions.create(
            model=args.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": ex["question"]},
            ],
            max_tokens=args.max_tokens,
            temperature=0.0,
            seed=42,
        )
        wall = time.perf_counter() - t0

        text = resp.choices[0].message.content
        usage = resp.usage
        pred = normalize(extract_numeric(text))
        gold = normalize(ex["gold_answer"])

        records.append({
            "id": ex["id"],
            "wall_time_s": wall,
            "prompt_tokens": usage.prompt_tokens,
            "output_tokens": usage.completion_tokens,
            "tokens_per_second": (usage.completion_tokens / wall) if wall > 0 else 0,
            "pred": pred,
            "gold": gold,
            "correct": pred == gold,
        })

    # ---- Aggregate ---------------------------------------------------------
    n = len(records)
    sum_out = sum(r["output_tokens"] for r in records)
    sum_wall = sum(r["wall_time_s"] for r in records)
    summary = {
        "model": args.model,
        "n_samples": n,
        "accuracy": sum(r["correct"] for r in records) / n,
        "aggregate_tokens_per_second": sum_out / sum_wall if sum_wall else 0,
        "avg_latency_s": sum_wall / n,
        "avg_output_tokens": sum_out / n,
    }

    with open(args.out, "w") as f:
        json.dump({"summary": summary, "records": records}, f, indent=2)

    print("\n=== Jetson draft baseline ===")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
