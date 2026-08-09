"""summarize_c3.py — build Pareto table + offline lookup table from per-mode JSONs.

Reads C3_7W.json, C3_15W.json, C3_MAXN.json (or whatever files passed)
and produces:
  - comparison_c3.md (paper Table 2)
  - lookup_table.json (the C3 controller's offline-profiled map)

Lookup table is keyed by (power_mode, slo_latency_ms). For a target SLO,
picks the (power_mode, γ) cell with lowest J/token among cells whose
avg_latency_s × 1000 ≤ slo.
"""
import argparse, json, pathlib
from tabulate import tabulate

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+", help="C3_*.json files from bench_c3_energy.py")
    ap.add_argument("--md-out", default="comparison_c3.md")
    ap.add_argument("--lookup-out", default="lookup_table.json")
    args = ap.parse_args()

    all_cells = []
    for f in args.files:
        d = json.load(open(f))
        mode = d["power_mode"]
        for c in d["cells"]:
            row = dict(c)
            row["power_mode"] = mode
            all_cells.append(row)

    # ---- Main table ----
    rows = []
    for c in all_cells:
        rows.append([
            c["power_mode"], f"γ={c['gamma']}",
            f"{c['agg_tok_s']:.1f}",
            f"{c['accuracy']*100:.0f}%",
            f"{c['acceptance']*100:.0f}%",
            f"{c['avg_watts']:.1f}",
            f"{c['joules_per_token']:.3f}",
            f"{c['avg_latency_s']:.2f}",
        ])
    headers = ["Mode", "γ", "tok/s", "Acc", "Accept", "Avg W",
               "J/tok ★", "Lat (s)"]
    table = tabulate(rows, headers=headers, tablefmt="github")

    # ---- Pareto frontier: keep cells not strictly dominated on (J/tok, latency)
    pareto = []
    for c in all_cells:
        dominated = False
        for o in all_cells:
            if o is c: continue
            if (o["joules_per_token"] <= c["joules_per_token"]
                and o["avg_latency_s"] <= c["avg_latency_s"]
                and (o["joules_per_token"] < c["joules_per_token"]
                     or o["avg_latency_s"] < c["avg_latency_s"])):
                dominated = True; break
        if not dominated:
            pareto.append(c)
    pareto.sort(key=lambda x: x["avg_latency_s"])

    pareto_rows = [[c["power_mode"], f"γ={c['gamma']}",
                    f"{c['joules_per_token']:.3f}",
                    f"{c['avg_latency_s']:.2f}",
                    f"{c['accuracy']*100:.0f}%"] for c in pareto]
    pareto_table = tabulate(pareto_rows,
        headers=["Mode", "γ", "J/tok", "Lat (s)", "Acc"], tablefmt="github")

    # ---- Best J/tok overall ----
    best = min(all_cells, key=lambda c: c["joules_per_token"]) if all_cells else None

    # ---- Lookup table for runtime SLO routing ----
    # For each SLO in a few buckets, find the lowest J/tok config that fits.
    lookup = {}
    for slo_s in [12, 13, 14, 15, 20, 30, 60]:
        feasible = [c for c in all_cells if c["avg_latency_s"] <= slo_s]
        if feasible:
            chosen = min(feasible, key=lambda c: c["joules_per_token"])
            lookup[f"slo_{slo_s}s"] = {
                "power_mode": chosen["power_mode"],
                "gamma": chosen["gamma"],
                "expected_joules_per_token": chosen["joules_per_token"],
                "expected_latency_s": chosen["avg_latency_s"],
                "expected_accuracy": chosen["accuracy"],
            }
        else:
            lookup[f"slo_{slo_s}s"] = None

    # ---- Write outputs ----
    md = (
        "# C3 — Energy × γ × Power Mode (paper Table 2)\n\n"
        f"Total cells: {len(all_cells)}\n\n"
        "## Full grid\n\n" + table + "\n\n"
        "## Pareto frontier (energy-latency)\n\n" + pareto_table + "\n\n"
    )
    if best:
        md += (f"## Best energy efficiency\n"
               f"**{best['power_mode']} γ={best['gamma']}**: "
               f"{best['joules_per_token']:.3f} J/tok, "
               f"{best['agg_tok_s']:.1f} tok/s, "
               f"{best['accuracy']*100:.0f}% acc\n")

    pathlib.Path(args.md_out).write_text(md)
    pathlib.Path(args.lookup_out).write_text(json.dumps(lookup, indent=2))
    print(md)
    print(f"\nWrote {args.md_out} and {args.lookup_out}")

if __name__ == "__main__":
    main()
