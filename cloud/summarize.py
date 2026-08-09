"""Build results/comparison.md from per-run JSON files.

Idempotent: re-running just rebuilds the table from whatever
result files currently exist in $PROJECT_ROOT/results/.
"""
import json
import os
import pathlib

from tabulate import tabulate

PROJECT_ROOT = os.environ.get("PROJECT_ROOT")
if not PROJECT_ROOT:
    raise SystemExit("ERROR: source env.sh first so PROJECT_ROOT is set.")

RESULTS = pathlib.Path(PROJECT_ROOT) / "results"
OUT = RESULTS / "comparison.md"

ROWS = [
    ("B1_AR", "Autoregressive (target only)", RESULTS / "B1_AR.json"),
    ("B2_SD", "Speculative Decoding (γ=5)",   RESULTS / "B2_SD.json"),
]


def load(path):
    if not path.exists():
        return None
    with path.open() as f:
        return json.load(f)["summary"]


records = []
for tag, desc, path in ROWS:
    s = load(path)
    if s is None:
        records.append((tag, desc, "—", "—", "—", "—", "—"))
        continue
    records.append((
        tag,
        desc,
        f"{s['n_samples']}",
        f"{s['accuracy']*100:.1f}%",
        f"{s['aggregate_tokens_per_second']:.1f}",
        f"{s['avg_latency_s']:.2f}",
        f"{s['avg_output_tokens']:.0f}",
    ))

headers = [
    "Tag", "Method", "N", "Accuracy",
    "Agg tok/s", "Avg latency (s)", "Avg out tok",
]
table = tabulate(records, headers=headers, tablefmt="github")

ar = load(RESULTS / "B1_AR.json")
sd = load(RESULTS / "B2_SD.json")
speedup_block = ""
if ar and sd:
    spd = sd["aggregate_tokens_per_second"] / ar["aggregate_tokens_per_second"]
    lat = ar["avg_latency_s"] / sd["avg_latency_s"]
    speedup_block = (
        f"\n## Headline\n"
        f"- **Throughput speedup (SD vs AR):** **{spd:.2f}×**\n"
        f"- **Latency speedup (SD vs AR):** **{lat:.2f}×**\n"
        f"- **Accuracy preserved:** "
        f"AR {ar['accuracy']*100:.1f}% vs SD {sd['accuracy']*100:.1f}% "
        f"(Δ = {(sd['accuracy']-ar['accuracy'])*100:+.1f} pp)\n"
    )

md = (
    "# Day 1 — H200 Baseline Comparison (Slurm)\n\n"
    "Dataset: GSM8K test (first 200), greedy decoding, max_tokens=512.\n\n"
    f"{table}\n"
    f"{speedup_block}"
)
OUT.write_text(md)
print(md)
print(f"\nWrote {OUT}")
