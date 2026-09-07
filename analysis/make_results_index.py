#!/usr/bin/env python3
"""make_results_index.py — scan a results dir, emit an index table (MD + CSV).

Reads every *.json that looks like a benchmark result (has a 'summary' or
top-level metrics) and tabulates the key fields. Safe, read-only.

Usage:
    python3 make_results_index.py /home/jetson/b3_results --out-md RESULTS_INDEX.md
    python3 make_results_index.py /data/zliu604/specdecode-day1/results
"""
import json, sys, os, glob, argparse, csv

# Fields we try to pull from each result's summary (any subset may exist)
FIELDS = [
    "tag", "task", "method", "mode", "power_mode", "schedule",
    "n_samples", "accuracy", "acceptance",
    "agg_tok_s", "aggregate_tokens_per_second", "tokens_per_second",
]

# Categorize by filename prefix → experiment group
def categorize(fn):
    b = os.path.basename(fn)
    rules = [
        ("B1", "Baseline: Cloud-AR"),
        ("B2", "Baseline: Cloud-SD"),
        ("B3", "Baseline: Edge-Cloud SD"),
        ("B4", "Baseline: N-gram"),
        ("B5_C1", "Failed: C1 adaptive-gamma"),
        ("B5", "B5: SLO routing"),
        ("C3", "C3: energy grid"),
        ("W_fixed", "Warmup: fixed baseline"),
        ("W_warmup", "Warmup: schedule"),
        ("P_sync", "Prefetch: sync baseline"),
        ("P_prefetch", "Failed: prefetch async"),
    ]
    for prefix, label in rules:
        if b.startswith(prefix):
            return label
    return "Other"

def get(summary, *keys):
    for k in keys:
        if k in summary and summary[k] is not None:
            return summary[k]
    return None

def load_summary(path):
    try:
        d = json.load(open(path))
    except Exception:
        return None
    if isinstance(d, dict) and "summary" in d and isinstance(d["summary"], dict):
        return d["summary"]
    # some result files are flat (e.g. C3 with 'cells') — synthesize a row
    if isinstance(d, dict) and ("aggregate_tokens_per_second" in d or "accuracy" in d):
        return d
    if isinstance(d, dict) and "power_mode" in d and "cells" in d:
        # C3 grid file: summarize best cell
        best = min(d["cells"], key=lambda c: c.get("joules_per_token", 9e9))
        return {"tag": f"C3_{d['power_mode']}", "power_mode": d["power_mode"],
                "n_samples": d.get("n_samples"),
                "joules_per_token": best.get("joules_per_token"),
                "agg_tok_s": best.get("agg_tok_s"),
                "gamma": best.get("gamma")}
    return None

def fmt(v):
    if v is None: return ""
    if isinstance(v, float):
        return f"{v:.3f}" if abs(v) < 100 else f"{v:.1f}"
    return str(v)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("results_dir")
    ap.add_argument("--out-md", default="RESULTS_INDEX.md")
    ap.add_argument("--out-csv", default="RESULTS_INDEX.csv")
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(args.results_dir, "*.json")))
    rows = []
    for f in files:
        s = load_summary(f)
        if not s:
            rows.append({"file": os.path.basename(f), "group": "Unparsed", "_raw": True})
            continue
        row = {"file": os.path.basename(f), "group": categorize(f)}
        row["tok/s"] = fmt(get(s, "agg_tok_s", "aggregate_tokens_per_second", "tokens_per_second"))
        row["acc"]   = fmt(get(s, "accuracy"))
        row["accept"]= fmt(get(s, "acceptance"))
        row["lat_s"] = fmt(get(s, "avg_latency_s"))
        row["J/tok"] = fmt(get(s, "joules_per_token"))
        row["n"]     = fmt(get(s, "n_samples"))
        rows.append(row)

    # sort by group then file
    rows.sort(key=lambda r: (r.get("group", "zzz"), r["file"]))

    # Markdown
    cols = ["file", "group", "tok/s", "acc", "accept", "lat_s", "J/tok", "n"]
    with open(args.out_md, "w") as f:
        f.write(f"# Results Index — `{args.results_dir}`\n\n")
        f.write(f"{len(files)} JSON files.\n\n")
        f.write("| " + " | ".join(cols) + " |\n")
        f.write("|" + "|".join("---" for _ in cols) + "|\n")
        cur = None
        for r in rows:
            if r.get("_raw"):
                f.write(f"| {r['file']} | _unparsed_ | | | | | | | |\n")
                continue
            f.write("| " + " | ".join(str(r.get(c, "")) for c in cols) + " |\n")
    # CSV
    with open(args.out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            if r.get("_raw"): continue
            w.writerow({c: r.get(c, "") for c in cols})

    print(f"Wrote {args.out_md} and {args.out_csv}  ({len(files)} files)")
    # quick group counts
    from collections import Counter
    c = Counter(r.get("group", "?") for r in rows)
    for g, n in sorted(c.items()):
        print(f"  {g}: {n}")

if __name__ == "__main__":
    main()
