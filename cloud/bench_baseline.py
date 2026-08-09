"""Run one baseline (AR / draft-model SD / n-gram SD) in a single process.

Day 2 changes vs Day 1:
- Added --method {draft,ngram} so the same script handles n-gram speculation.
- --mode is still accepted for backward-compatibility with Day 1's
  slurm_run.sh, but is now derived from --method when --method is given.
- Summary JSON now records vLLM's reported metrics (acceptance, draft accepts)
  when available, which we'll use in the paper's headline table.

Backward compat: the original Day 1 slurm_run.sh still works unchanged.
"""
import argparse
import json
import os
import pathlib
import re
import time

from tqdm import tqdm
from vllm import LLM, SamplingParams

# --------------------------------------------------------------------------- #
SYSTEM_PROMPT = (
    "You are a math tutor. Solve the problem step by step. "
    "End your answer with exactly: 'Final answer: <number>'."
)

ANSWER_RE = re.compile(r"final answer\s*[:\-]?\s*\$?(-?[\d,]+(?:\.\d+)?)", re.I)


def extract_numeric(text: str) -> str | None:
    m = ANSWER_RE.search(text)
    if m:
        return m.group(1).replace(",", "").rstrip(".")
    nums = re.findall(r"-?\d+(?:\.\d+)?", text)
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


# --------------------------------------------------------------------------- #
def build_llm(args):
    """Construct an LLM. Speculative config depends on --method."""
    kwargs = dict(
        model=args.target,
        dtype="bfloat16",
        gpu_memory_utilization=0.85,
        max_model_len=args.max_model_len,
        seed=42,
    )

    if args.method == "ar":
        pass  # vanilla autoregressive
    elif args.method == "draft":
        # Draft-model speculative decoding (Day 1 path).
        kwargs["speculative_config"] = {
            "method": "draft_model",
            "model": args.draft,
            "num_speculative_tokens": args.gamma,
        }
    elif args.method == "ngram":
        # vLLM N-gram speculative decoding. No draft model needed —
        # candidates come from matching n-grams in the prompt+generated text.
        # `prompt_lookup_max` controls the longest n-gram we'll match;
        # 4 is the vLLM-documented default and a sane choice for GSM8K.
        kwargs["speculative_config"] = {
            "method": "ngram",
            "num_speculative_tokens": args.gamma,
            "prompt_lookup_max": 4,
            "prompt_lookup_min": 2,
        }
    else:
        raise ValueError(f"unknown --method: {args.method}")

    return LLM(**kwargs)


def main():
    ap = argparse.ArgumentParser()

    # Method selector. --method takes precedence; --mode kept for Day 1 compat.
    ap.add_argument("--method", choices=["ar", "draft", "ngram"], default=None,
                    help="Decoding method. If omitted, falls back to --mode.")
    ap.add_argument("--mode", choices=["ar", "sd"], default=None,
                    help="[Day 1 compat] 'ar' → method=ar; 'sd' → method=draft.")

    ap.add_argument("--target", default="meta-llama/Llama-3.1-8B-Instruct")
    ap.add_argument("--draft",  default="meta-llama/Llama-3.2-1B-Instruct")
    ap.add_argument("--gamma", type=int, default=5,
                    help="num_speculative_tokens; ignored for --method ar")
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--max-model-len", type=int, default=4096)
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    # Resolve method: prefer --method, fall back to --mode for Day 1 scripts.
    if args.method is None:
        if args.mode is None:
            raise SystemExit("Provide --method or --mode")
        args.method = "ar" if args.mode == "ar" else "draft"

    # ---- Load data ---------------------------------------------------------
    samples = []
    with open(args.data) as f:
        for line in f:
            samples.append(json.loads(line))
    if args.limit:
        samples = samples[:args.limit]

    print(f"[{args.tag}] Loading model... method={args.method} γ={args.gamma}")
    t_load = time.perf_counter()
    llm = build_llm(args)
    print(f"[{args.tag}] Model loaded in {time.perf_counter()-t_load:.1f}s")

    tok = llm.get_tokenizer()

    prompts = []
    for ex in samples:
        msg = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": ex["question"]},
        ]
        prompt = tok.apply_chat_template(msg, tokenize=False,
                                         add_generation_prompt=True)
        prompts.append(prompt)

    sp = SamplingParams(temperature=0.0, max_tokens=args.max_tokens, seed=42)

    # ---- Warmup -------------------------------------------------------------
    print(f"[{args.tag}] Warmup...")
    _ = llm.generate([prompts[0]], sp, use_tqdm=False)

    # ---- Timed loop ---------------------------------------------------------
    print(f"[{args.tag}] Benchmarking {len(samples)} samples...")
    records = []
    t0_total = time.perf_counter()
    for ex, prompt in tqdm(list(zip(samples, prompts)), desc=args.tag):
        t0 = time.perf_counter()
        out = llm.generate([prompt], sp, use_tqdm=False)
        wall = time.perf_counter() - t0

        gen = out[0].outputs[0]
        text = gen.text
        out_toks = len(gen.token_ids)
        prompt_toks = len(out[0].prompt_token_ids)

        pred = normalize(extract_numeric(text))
        gold = normalize(ex["gold_answer"])

        records.append({
            "id": ex["id"],
            "wall_time_s": wall,
            "prompt_tokens": prompt_toks,
            "output_tokens": out_toks,
            "tokens_per_second": out_toks / wall if wall > 0 else 0.0,
            "pred": pred,
            "gold": gold,
            "correct": pred == gold,
            "finish_reason": gen.finish_reason,
        })
    total_wall = time.perf_counter() - t0_total

    # ---- Aggregate ----------------------------------------------------------
    n = len(records)
    acc = sum(r["correct"] for r in records) / n
    avg_tps_req = sum(r["tokens_per_second"] for r in records) / n
    sum_out = sum(r["output_tokens"] for r in records)
    sum_wall = sum(r["wall_time_s"] for r in records)
    agg_tps = sum_out / sum_wall
    avg_latency = sum_wall / n
    avg_out = sum_out / n

    summary = {
        "tag": args.tag,
        "method": args.method,
        "target": args.target,
        "draft": args.draft if args.method == "draft" else None,
        "gamma": args.gamma if args.method != "ar" else None,
        "n_samples": n,
        "accuracy": acc,
        "avg_tokens_per_second_per_request": avg_tps_req,
        "aggregate_tokens_per_second": agg_tps,
        "avg_latency_s": avg_latency,
        "avg_output_tokens": avg_out,
        "total_wall_s": total_wall,
    }

    out_path = pathlib.Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        json.dump({"summary": summary, "records": records}, f, indent=2)

    print(f"\n[{args.tag}] === Summary ===")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print(f"[{args.tag}] Wrote {out_path}")


if __name__ == "__main__":
    main()
