# CAPE manuscript draft (IEEE conference format)

**Title:** CAPE: Critical-Path-Aware Prefetching for Fast and Energy-Aware Edge–Cloud Speculative Decoding

Rewritten on 2026-10-30 from the 2026-10-28 rerun (`results/rerun_20261028`); the main comparison is against synchronous speculative decoding (Sync-4). Author: Zishi Deng, University of Auckland. The venue is not yet chosen; for a double-blind venue, anonymize the author block and the campus-network details.

## Contents

| Path | Purpose |
|---|---|
| `main.tex` | Main file (IEEEtran conference class) |
| `sections/*.tex` | Abstract, introduction, related work, background, design, implementation, evaluation, discussion, conclusion, appendix |
| `figures/frontier.pdf`, `figures/sweep.pdf`, `figures/timeline.tex` | Speed–energy plane under dynamic delay, delay sweep, TikZ timeline |
| `tables/{speedup,ablation,weights}.tex` | Generated table bodies |
| `numbers.tex` | Generated values; the text prints them with `\E{key}` |
| `references.bib` | 34 references, all cited |
| `data/records.json` | One summary per timed request of the rerun (tokens, wall time, joules, quality, controller windows); the raw records stay on the Jetson |
| `scripts/make_assets.py` | Records → numbers, tables and figures |
| `cape_20261010_latex.zip` | Sources for Overleaf |

## Compile

- **Overleaf:** upload the zip, set `main.tex` as the main file. pdfLaTeX and XeLaTeX both work (the preamble selects Times fonts for either engine).
- **Locally:** `bash scripts/build.sh` (uses `latexmk` or Tectonic; the Jetson has neither).

## Regenerate the numbers, tables and figures

Run from the repository root:

```bash
python3 paper/cape_20261010/scripts/make_assets.py
```

It reads `data/records.json`; delete that file to rebuild it from the raw records in `results/rerun_20261028/*/raw` (about two minutes on the Jetson). The bootstrap intervals are drawn exactly as in `results/rerun_20261028/analysis_vs_sync.py`, so the two agree to the last digit. Undefined numbers compile as **??** and are reported in the LaTeX log as `Undefined CAPE number`.

## Evidence used

All methods of a session run interleaved, so each comparison is within one session.

| Role | Session (`results/rerun_20261028/`) | Size |
|---|---|---|
| Main comparison, nine methods × low / high / dynamic | `gemma3_main`, `llama_main`, `qwen_main`: 110 prompts; `gemma2_main`: the 61 / 52 / 61 prompts all methods completed | 10,476 paired requests |
| Delay sweep (Gemma-3, 10 / 25 / 50 / 200 ms) | `gemma3_sweep` (2 and 100 ms: the same 30 prompts of `gemma3_main`) | 600 |
| Ablation (Gemma-3) | `gemma3_ablation` | 360 |
| Energy-weight sweep (Gemma-3, dynamic) | `gemma3_weights` | 150 |

Method names: `sync_g4` = Sync-4, `picospec_g2` / `picospec` / `picospec_g8` = PicoSpec-2/4/8 (with interruption), `markov_w0_dist_int` = CAPE-S, `markov_w05_dist_int` = CAPE-E, `pearl`, `pipesd`, `hf_default` = HF assisted; ablation `markov_w0_fresh4_int` = adaptive lookahead with fresh window 4.
