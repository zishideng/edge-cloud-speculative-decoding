"""make_figures.py — generate the three paper figures from result JSONs.

Run on Jetson (or anywhere the b3_results/*.json are reachable).
Outputs PDF (vector, for LaTeX) + PNG (preview) into ./figs/.

Figures:
  fig_coldstart   — acceptance vs round index (γ=3 and γ=5), shows -50pp round-0
  fig_fb_vs_accept— fallback rate vs task acceptance (3 tasks)
  fig_threshold   — threshold knob: tok/s and fallback rate vs τ (GSM8K sweep)

Data sources (edit paths if yours differ):
  ROUND : B3_remote_g3.json, B3_remote_g5.json   (have per-round 'rounds')
  FB    : S_*_{gsm8k,humaneval,mtbench}.json with fallback_rate + acceptance
  SWEEP : S_fb_t*_gsm8k.json with fallback_thresh, fallback_rate, agg_tok_s

Style: grayscale-friendly, no chartjunk, TrueType fonts embedded for camera-ready.
"""
import json, glob, os, sys
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams.update({
    "pdf.fonttype": 42, "ps.fonttype": 42,    # embed TrueType (camera-ready)
    "font.size": 11, "axes.spines.top": False, "axes.spines.right": False,
    "figure.dpi": 150,
})
import matplotlib.pyplot as plt

RESULTS = os.environ.get("RESULTS_DIR", "/home/jetson/b3_results")
OUT = os.environ.get("FIG_DIR", "./figs")
os.makedirs(OUT, exist_ok=True)

def load(name):
    p = os.path.join(RESULTS, name)
    if not os.path.exists(p):
        print(f"  [warn] missing {p}")
        return None
    return json.load(open(p))

def save(fig, stem):
    for ext in ("pdf", "png"):
        fp = os.path.join(OUT, f"{stem}.{ext}")
        fig.savefig(fp, bbox_inches="tight")
    print(f"  wrote {stem}.pdf/.png")
    plt.close(fig)

# --------------------------------------------------------------------------- #
def round_profile(d, max_round=22, min_n=5):
    """acceptance-by-round-position from a result JSON's records[].rounds[]."""
    by = {}
    for rec in d["records"]:
        rounds = rec.get("rounds")
        if not rounds:
            continue
        for i, rnd in enumerate(rounds):
            g = rnd.get("gamma", 1)
            if not g:
                continue
            by.setdefault(i, []).append(rnd["n_accepted"] / g)
    xs, ys = [], []
    for i in sorted(by):
        if i > max_round or len(by[i]) < min_n:
            continue
        xs.append(i); ys.append(sum(by[i]) / len(by[i]))
    return xs, ys

def fig_coldstart():
    g3 = load("B3_remote_g3.json")
    g5 = load("B3_remote_g5.json")
    if not g3 and not g5:
        print("  [skip] coldstart — no B3 data")
        return
    fig, ax = plt.subplots(figsize=(4.2, 2.8))
    if g3:
        x, y = round_profile(g3)
        ax.plot(x, y, marker="o", ms=3, lw=1.3, color="#1f3b73", label=r"$\gamma=3$")
    if g5:
        x, y = round_profile(g5)
        ax.plot(x, y, marker="s", ms=3, lw=1.3, color="#9a3b3b",
                label=r"$\gamma=5$", linestyle="--")
    # Annotate round-0 drop
    if g3:
        x, y = round_profile(g3)
        if x and x[0] == 0:
            ax.annotate("cold-start\nround 0",
                        xy=(0, y[0]), xytext=(6, y[0] - 0.02),
                        fontsize=9, color="#333",
                        arrowprops=dict(arrowstyle="->", color="#333", lw=0.8))
    ax.set_xlabel("Round index")
    ax.set_ylabel("Mean acceptance")
    ax.set_ylim(0, 1.0)
    ax.legend(frameon=False, loc="lower right")
    ax.grid(axis="y", alpha=0.25)
    save(fig, "fig_coldstart")

# --------------------------------------------------------------------------- #
def fig_fb_vs_accept():
    """Fallback rate vs task acceptance. One point per task at tau=0.65."""
    # task -> (acceptance, fallback_rate). Prefer the tau=0.65 fallback runs.
    candidates = {
        "HumanEval": ["S_fb_t065_humaneval.json", "S_b0_fk3_humaneval.json", "S_fb_humaneval.json"],
        "GSM8K":     ["S_fb_t065_gsm8k.json", "S_b0_fk3_gsm8k.json"],
        "MT-Bench":  ["S_fb_t065_mtbench.json", "S_b0_fk3_mtbench.json"],
    }
    # baseline acceptance per task (from base runs); fall back to summary's acceptance
    pts = []
    for task, files in candidates.items():
        s = None
        for f in files:
            d = load(f)
            if d and "acceptance" in d["summary"] and "fallback_rate" in d["summary"]:
                s = d["summary"]; break
        if not s:
            print(f"  [warn] no usable fallback file for {task}")
            continue
        pts.append((task, s["acceptance"], s["fallback_rate"]))
    if not pts:
        print("  [skip] fb_vs_accept — no data")
        return
    pts.sort(key=lambda t: t[1])
    fig, ax = plt.subplots(figsize=(4.2, 2.8))
    accs = [p[1]*100 for p in pts]
    fbs  = [p[2]*100 for p in pts]
    ax.plot(accs, fbs, marker="o", ms=6, lw=1.3, color="#1f3b73")
    for task, a, fb in pts:
        ax.annotate(task, xy=(a*100, fb*100), xytext=(4, 4),
                    textcoords="offset points", fontsize=9)
    ax.set_xlabel("Task draft acceptance (%)")
    ax.set_ylabel("Fallback rate (%)")
    ax.set_ylim(bottom=-2)
    ax.grid(alpha=0.25)
    ax.invert_xaxis()  # higher acceptance (less fallback) on the right
    save(fig, "fig_fb_vs_accept")

# --------------------------------------------------------------------------- #
def fig_threshold():
    """tok/s and fallback rate vs threshold on GSM8K."""
    files = sorted(glob.glob(os.path.join(RESULTS, "S_fb_t*_gsm8k.json")))
    pts = []
    for f in files:
        s = json.load(open(f))["summary"]
        thr = s.get("fallback_thresh")
        if thr is None:
            continue
        pts.append((thr, s["agg_tok_s"], s["fallback_rate"]))
    # de-dup by threshold (keep last)
    dedup = {}
    for thr, tps, fb in pts:
        dedup[round(thr, 3)] = (tps, fb)
    pts = sorted((thr, v[0], v[1]) for thr, v in dedup.items())
    if len(pts) < 2:
        print("  [skip] threshold — need >=2 sweep points, have", len(pts))
        return
    thrs = [p[0] for p in pts]
    tps  = [p[1] for p in pts]
    fbs  = [p[2]*100 for p in pts]

    fig, ax1 = plt.subplots(figsize=(4.6, 2.9))
    c1, c2 = "#1f3b73", "#9a3b3b"
    ax1.plot(thrs, tps, marker="o", ms=5, lw=1.4, color=c1)
    ax1.set_xlabel(r"Fallback threshold $\tau$")
    ax1.set_ylabel("Throughput (tok/s)", color=c1)
    ax1.tick_params(axis="y", labelcolor=c1)
    ax1.grid(alpha=0.2)

    ax2 = ax1.twinx()
    ax2.spines["top"].set_visible(False)
    ax2.plot(thrs, fbs, marker="s", ms=5, lw=1.4, color=c2, linestyle="--")
    ax2.set_ylabel("Fallback rate (%)", color=c2)
    ax2.tick_params(axis="y", labelcolor=c2)
    ax2.set_ylim(0, 100)

    # Shade the "cliff" region if present (between 0.65 and 0.70)
    if min(thrs) <= 0.65 and max(thrs) >= 0.70:
        ax1.axvspan(0.65, 0.70, color="grey", alpha=0.12)
        ax1.annotate("cliff", xy=(0.675, max(tps)*0.45), fontsize=9,
                     ha="center", color="#555")
    save(fig, "fig_threshold")

# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    print(f"RESULTS_DIR = {RESULTS}")
    print(f"FIG_DIR     = {OUT}")
    fig_coldstart()
    fig_fb_vs_accept()
    fig_threshold()
    print("Done. LaTeX usage:")
    print(r"  \includegraphics[width=.8\linewidth]{figs/fig_coldstart.pdf}")
