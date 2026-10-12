# CAPE manuscript draft (IEEE conference format)

**Title:** CAPE: Critical-Path-Aware Prefetching for Fast and Energy-Aware Edge–Cloud Speculative Decoding

Draft first written on 2026-10-10 and revised on 2026-10-12 to use the full 110-prompt evaluation (1,540 requests) as the main result. Author: Zishi Deng, University of Auckland. The venue is not yet chosen; for a double-blind venue, anonymize the author block and the campus-network details.

## Contents

| Path | Purpose |
|---|---|
| `main.tex` | Main file (IEEEtran conference class) |
| `sections/*.tex` | Abstract, introduction, measurement study, design, implementation, evaluation, related work, discussion, conclusion, appendix |
| `figures/*.pdf`, `figures/timeline.tex` | Data figures (Matplotlib) and the TikZ timeline |
| `tables/*.tex` | Generated table bodies |
| `numbers.tex` | Generated values; the text prints them with `\E{key}` |
| `references.bib` | 27 references, all cited; metadata checked on 2026-10-12 against publisher pages (PMLR, ACL Anthology, NeurIPS, ICLR, MLSys, ACM/IEEE DOIs) or arXiv; no GitHub or other non-archival sources |
| `data/evidence.json` | Every extracted number, with the paths of its source records |
| `scripts/` | Evidence extraction, asset generation and build script |
| `main.pdf` | Compiled draft (10 pages including references and appendix) |

## Compile

- **Overleaf:** upload the zip, set `main.tex` as the main file. pdfLaTeX and XeLaTeX both work (the preamble selects Times fonts for either engine).
- **Locally:** `bash scripts/build.sh` (uses `latexmk` or Tectonic).

## Regenerate the numbers, tables and figures

Run from the repository root (no model or sensor access; only the retained raw records):

```bash
python3 paper/cape_20261010/scripts/extract_evidence.py   # raw records -> data/evidence.json
python3 paper/cape_20261010/scripts/make_assets.py        # evidence -> numbers.tex, tables/, figures/
```

Undefined numbers compile as **??** and are reported in the LaTeX log as `Undefined CAPE number`.

## Evidence used

Only the 2 ms and 100 ms delay conditions (low, high, pooled) are used; 300 ms is not reported.

| Role | Directory | Prompts | Requests |
|---|---|---:|---:|
| Main evaluation (7 methods) | `results/compare_20261010/full_110` | 110 | 1,540 |
| Held-out Set 1 (default CAPE, Regime) | `results/pipeline_research_20261009/confirm_markov` | 9 | 72 |
| Held-out Set 2 (default CAPE, robust variant) | `results/pipeline_research_20261009/final_markov_v2` | 12 | 72 |

The earlier 6-prompt comparison set is no longer used: its prompts are part of the 110. The main evaluation was resumed once after a cloud connection reset; host activity during the run is logged in `results/compare_20261010/full_110_maintenance.log`, and excluding the overlapping blocks leaves the results unchanged.

Method names: `fixed_fast` = Fixed-4, `fixed_g2`/`fixed_g8` = Fixed-2/Fixed-8, `sync_g4` = Sync-4, `adaedl` = AdaEDL, `regime_short` = Regime, `markov` = CAPE (w=0.25), `markov_w0` = CAPE-S, `markov_w05` = CAPE-E, `markov_v2` = robust variant.

## Known limitations of this draft

- One run per prompt, method and delay; one device, one model pair, constant injected delays, edge board energy only.
- CAPE-S buys its speed with 3.2% more J/token overall (10.4% more at 100 ms); CAPE-E saves energy at equal speed.
- Outputs differ between methods in 45 of 220 prompt–delay blocks because near-tied scores of the quantized target depend on the verified window size; GSM8K accuracy is unchanged (72–74/100 for every method). HumanEval pass@1 and MT-Bench scores were not evaluated.
- The controller's power ratio r = 2.3 came from development runs; fits on our data give 1.8–3.2.
