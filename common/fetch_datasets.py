"""fetch_extra_datasets.py — Fetch MT-Bench prompts + HumanEval problems to JSONL.

Run ONCE on Jetson to cache datasets. Outputs in same format as gsm8k_test_50.jsonl.

For MT-Bench: 80 single-turn questions, no ground-truth eval (we'll measure
only tok/s and acceptance). For HumanEval: 30 coding problems with prompt+test.
"""
import argparse, json, pathlib

def fetch_mtbench(n: int = 30, out_path: str = "mtbench_30.jsonl"):
    """MT-Bench questions are hosted on lmsys's github."""
    import requests
    url = "https://raw.githubusercontent.com/lm-sys/FastChat/main/fastchat/llm_judge/data/mt_bench/question.jsonl"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    lines = r.text.strip().split("\n")
    with open(out_path, "w") as f:
        for i, line in enumerate(lines[:n]):
            q = json.loads(line)
            # MT-Bench format: {"question_id": int, "category": str, "turns": [str, str]}
            f.write(json.dumps({
                "id": q.get("question_id", i),
                "category": q.get("category", ""),
                "question": q["turns"][0],   # first turn only (single-turn eval)
                "gold_answer": "",
            }) + "\n")
    print(f"Wrote {min(n, len(lines))} MT-Bench samples → {out_path}")

def fetch_humaneval(n: int = 30, out_path: str = "humaneval_30.jsonl"):
    from datasets import load_dataset
    ds = load_dataset("openai/openai_humaneval", split="test")
    with open(out_path, "w") as f:
        for ex in ds.select(range(min(n, len(ds)))):
            f.write(json.dumps({
                "id": ex["task_id"],
                "question": ex["prompt"],
                "gold_answer": ex["canonical_solution"],
            }) + "\n")
    print(f"Wrote {min(n, len(ds))} HumanEval samples → {out_path}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=30)
    ap.add_argument("--mtbench-out", default="mtbench_30.jsonl")
    ap.add_argument("--humaneval-out", default="humaneval_30.jsonl")
    args = ap.parse_args()
    fetch_mtbench(args.n, args.mtbench_out)
    fetch_humaneval(args.n, args.humaneval_out)
