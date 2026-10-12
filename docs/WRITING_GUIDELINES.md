# Persistent manuscript objective

Moved here on 2026-10-12 when the October 8 manuscript (`paper/edge_cloud_latency_adaptive_20261008`) and its evidence were deleted at the user's request; the objective below applies to the current CAPE manuscript (`paper/cape_20261010`). Paths below that refer to the deleted manuscript or results are historical.

User instruction recorded on October 8, 2026. Apply this objective to subsequent revisions of this English manuscript:

**Improve decoding speed while avoiding a substantial increase in energy consumption.**

Use energy per generated token (J/token) as the principal reported energy-efficiency measure; report J/request and average power separately with output-length and quality context. An energy reduction is desirable, but it is no longer a mandatory component of the research objective.

The user has not specified a numerical acceptable increase. Do not invent an approved percentage or choose a tolerance after inspecting results. A future confirmatory evaluation must specify the tolerance, fixed control, scenarios and uncertainty rule in advance. A nonsignificant increase does not establish that the increase is practically negligible.

Preserve raw measurements, confidence intervals and the frozen experimental protocol. The earlier protocol required a strict energy reduction and did not meet its joint primary target; retain that historical outcome without making it the revised paper's central objective. Existing results can inform the revised narrative but cannot be relabeled as a prospectively confirmed overhead constraint.

Keep manuscript text in English. Continue to distinguish gross Jetson board energy from unmeasured cloud and network energy, and matched-backend adaptation effects from overall configuration changes.

## Dataset scope for subsequent experiments

The user subsequently restricted new experiments to their already downloaded
test files: `common/data/gsm8k_test_50.jsonl` (50 questions),
`common/data/humaneval_30.jsonl` (30), and `common/data/mtbench_30.jsonl` (30).
Do not substitute the full official GSM8K test split or download additional
benchmarks for those experiments. Use all local rows with one observation per
condition. The current entrypoint is `run_downloaded_benchmarks.sh`.

This is a prospective scope preference, not evidence that these experiments
have completed. Do not change the historical eight-prompt cohort or claim
HumanEval pass@1 or MT-Bench quality scores without the required evaluators.

## Cleanup and historical evidence

On October 8, the user requested removal of obsolete code and results. The
maintained live methods are `fixed`, `fixed_fast`, and `regime`. Historical
implementations needed for scientific provenance remain in the research
campaign's frozen source snapshots and the manuscript evidence bundle; they
are not current experiment entrypoints. Preserve cited raw evidence and
negative findings when revising the paper after this cleanup.
