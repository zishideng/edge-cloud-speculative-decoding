# Research log

## 2026-09-28 — Intake and preserved baseline

Goal: reproducible, correctness-first research on acceptance-aware edge/cloud
speculative decoding. A positive speedup is not a completion criterion.

Initial code: `7d2336d`, with pre-existing user modifications and deleted historical
figures. These changes are preserved; they are not attributed to this work.
Source snapshot, SHA-256 manifest and complete initial diff:
`results/research_20260928_135549/`.

Architecture: Jetson llama.cpp draft; remote FastAPI/vLLM AWQ target; synchronous
draft/verify loop; strict K=1 or explicitly lossy budgeted K>1 acceptance; optional
gamma controller. Existing pipeline measures batch-visible TTFT, throughput,
draft/verify/network residual timing, and GSM8K final-number accuracy. Network
conditions are application sleeps. Synthetic results are not LLM measurements.

Historical run `20260922_165127_613688_bbf68018`: 672 successful requests but just
4 independent prompts, repeated twice over 7 network conditions. Strict A had
0/56 exact token matches to its saved reference, despite 56/56 correct final
answers. C scored 42/56 and Proposed 55/56. Neither correctness equivalence nor
quality preservation follows from these results. Cross-scenario pooled speeds
are descriptive only. Raw historical data remain untouched.

Baseline validation: `python -m unittest discover -s tests -v`: 51 tests passed.
Full output: `results/research_20260928_135549/logs/baseline_tests.log`.
Current remote `/info`: Llama-3.1-8B-Instruct AWQ INT4, vLLM 0.26.0,
torch 2.11.0, protocol 1, diagnostics available. Remote code is not identical to
the local snapshot (additional diagnostics); capture service responses explicitly.

### Experiment R001 — Restore draft service

Hypothesis: the default llama.cpp memory-fitting or mmap mode causes allocation
failure, rather than missing/corrupt model weights.
Configuration: local Llama-3.2-1B-Instruct-Q4_K_M, context 4096, NGL=99,
llama.cpp commit `063d9c156e816ae3cf62db01f429a07a099afe97`.
Commands: default start script; then `LLAMA_ARG_FIT=off`; then additionally
`LLAMA_ARG_MMAP=0`. Each attempt has its own log and process metadata in the
research artifact directory.
Results: all three fail allocating 762.81 MiB CUDA model buffer. No benchmark
result was produced. Existing desktop applications were left running.
Decision: REJECT the fit/mmap workaround hypothesis.
Next: reduce GPU layer count as a diagnostic; preserve full-GPU as the intended
performance baseline. CPU/partial-GPU timing must be labeled separately.

### Experiment R002 — Strict-output differential diagnosis (pre-registered)

Hypothesis: target prefill verification and autoregressive decoding choose
different tokens at near-tied positions, possibly because of numerical kernels.
Alternatives: incorrect token alignment, ties, EOS, template or protocol errors.
Modification: add a separate diagnostic runner; do not change acceptance policy.
Design: save exact prompt IDs, repeat AR reference and K=1 gamma variants; at the
first mismatch replay the identical prefix through generate and diagnostic verify,
including target top-k probabilities. Check all returned prefix decisions.
Expected: determine whether the first divergent token follows each backend's own
top-1, and distinguish repeat instability from evaluation-path differences.
Decision: pending. Do not claim numerical causation from text divergence alone.

Primary references consulted for the diagnosis:
- https://docs.vllm.ai/en/stable/usage/reproducibility/
- https://github.com/vllm-project/vllm/blob/main/docs/features/speculative_decoding/README.md
- https://arxiv.org/abs/2211.17192

Next research steps: establish measured baseline including cloud AR; diagnose
correctness; profile dominant cost; pre-register one-variable optimization,
repeat across prompts and network conditions; record failed hypotheses as well.

### Experiment R003 — Strict acceptance under tied global ranks

Hypothesis: the K=1 path accidentally accepts a noncanonical tied rank-1 token
through its relaxed predicate, even though `strict_accepted` is false.
Modification: require effective K > 1 for the relaxed acceptance branch.
Reason: strict greedy selection must use the same canonical top token on every
path; an exhausted quality budget must also restore strict behavior.
Configuration: two rank-1 tokens (IDs 10 and 20), both probability 0.4, draft 20.
Expected: K=1 rejects 20 and corrects to 10; K=2 may accept the alternate;
budget-exhausted K=2 behaves as K=1.
Actual: original code accepted 20; patched code rejects and corrects to 10.
Validation: 53 tests passed. A controlled original-vs-patched simulation over
3 seeds × 4 gamma values × 4 prompts (128 tokens) produced 48/48 unchanged,
reference-identical non-tie sequences. This is algorithm testing, not measured
model performance. Raw results: `results/research_20260928_135549/tie_regression.json`.
Historical scan found zero observed K=1 tie-bypass decisions, so this defect
does NOT explain the historical divergence.
Decision: ACCEPT as a correctness fix; no performance claim.
Next: complete R002; probe target behavior at fixed prefixes across gamma values.

### Experiment R004 — Teacher-forced target path sensitivity (pre-registered)

Hypothesis: the target's prefill and generation paths have reproducible top-1
differences across fixed prefixes; changing verification window length may
also change these decisions. A correct acceptance rule alone cannot repair that.
Design: 4 prompts each from GSM8K, HumanEval, MT-Bench; current template and
exact token IDs saved. Generate up to 128 reference tokens. Probe prefix offsets
0, 1, 2, 3, 7, 15, 31, 63 where available. At each identical prefix compare
single-token AR and strict verification with reference-token proposals of length
1, 2, 4, 8, repeated three times in seeded random order.
Only gamma changes within a prefix. Record all responses, including mismatches,
ties and failures. Distinguish original long-AR, single-token AR, and prefill
top-1. Teacher forcing is diagnostic and is NOT a deployable draft method or a
performance result. Prompts, not prefixes/repeats, are the independent clusters.
Expected result: quantify repeat stability and window/path sensitivity without
requiring a working Jetson CUDA draft. No task accuracy claim from truncated
128-token references. Decision: pending.

R002 outcome: 16 completed strict runs, zero failures. Gamma=2 matched its paired
AR reference in 5/8 cases, gamma=8 in 4/8. One of four AR prompts changed between
repeats (163 vs 233 output tokens). Selected mismatch-prefix replays disagreed
between prefill and single-token AR in 12/21 calls; this selection-biased fraction
is not an error-rate estimate. The diagnosis establishes an unresolved backend
path/history effect, not its exact kernel cause. Source/report:
`results/research_20260928_135549/strict_audit/20260928_135950_915091_3315ac8f/`
and `strict_report/20260928_141117_309954_6b95fc4e/` under the same research root.
Decision: ACCEPT existence of a strict-reference discrepancy; INCONCLUSIVE cause.

R004 outcome: 1,149 checks over 12 prompts (4 per workload), three repeats and
gamma 1/2/4/8. All sampled positions matched both original and single-token AR;
0/383 prefix/gamma groups varied over repeats, 0/288 prefix/repeat groups varied
over gamma. Decision: REJECT broad sensitivity at these sampled positions.
The predeclared offsets omitted the known differences at positions 20, 25 and 29.
Preserve this null result; do not substitute a later targeted result for it.
Raw: `results/research_20260928_135549/target_path_audit/20260928_141000_936568_be4a3312/`.

R001 follow-up: ordinary CUDA allocations up to 256 MiB succeeded; 448/763 MiB
and an 800 MiB managed allocation failed. After R004, stopped only the NGL=0
server started by this session and advised `POSIX_FADV_DONTNEED` for the GGUF
file. This changes page-cache residency, not file content. The original NGL=99
startup then succeeded. No user applications were terminated, no sudo used.
Decision: ACCEPT a working recovery procedure for this session; memory-pressure
causation remains an inference from this intervention, not a general driver fix.
Full-GPU R002 replication started separately with identical prompts/repeats/gammas.

### Experiment R005 — Targeted low-margin replay (pre-registered)

Problem: coarse fixed offsets missed observed strict mismatches.
Hypothesis: a small subset of low-margin positions accounts for path sensitivity.
Change only prefix selection relative to R004: score the full saved AR reference
in one diagnostic prefill, prioritize disagreements, then smallest top-1/top-2
logprob margin; select eight non-EOS positions per prompt. Retain three repeats,
gamma 1/2/4/8 and the same 12 workload prompts. Save screening distributions and
all selected/rejected positions. This is deliberately failure-enriched sampling,
not a population error-rate estimator. Screening uses a long batch solely for
selection; confirmation uses the original gamma range. Decision: pending.

## Researcher clarification — 2026-09-28

The researcher explicitly states that strict token equality is NOT required
("不需要严格一致"). Operational correctness, task quality, latency and throughput
are the research criteria. Token-level path differences remain descriptive
diagnostics, not an admission gate or a reason to block performance experiments.
R005 has not started and is deferred as lower priority. The in-flight GPU baseline
will finish and be retained. Remote SSH access is useful for backend profiling,
but is not required to continue the authorized approximate-decoding research.
Next: run quality/performance baselines over more independent GSM8K prompts,
then test a measured bottleneck with paired repetitions and explicit quality loss.

### Experiment R006 — Quality/performance pilot (pre-registered)

Hypothesis: joint K/gamma control improves request throughput relative to fixed
strict A under high communication delay, but local regret constraints may still
reduce task accuracy. A direct cloud AR baseline may dominate all edge SD methods.
Configuration: first 8 GSM8K prompts (increase independent prompts from 4 to 8),
512-token cap, 2 repeats, seed 42; injected RTT 2 and 100 ms; same running AWQ
target and restored NGL=99 Jetson draft. Methods: cloud_AR, A, B, C, Proposed.
Only network condition varies between scenario blocks. Existing algorithm/config
parameters remain fixed. Paired analysis clusters repeats by prompt.
New measurement support: method selection avoids duplicate sweep methods in a
baseline pilot; cloud_AR issues a fresh timed request for each job and includes
template/tokenization/detokenization plus one injected network round trip. Its
non-streaming TTFT/TPOT and acceptance are null. Cached quality references are
not reused as timing samples. Queue injection is unsupported for AR and errors.
Expected: establish end-to-end latency/throughput and absolute quality, assess
whether a larger sweep is warranted. Exact token equality is descriptive only.
Command: `python -m experiments.run --mode real --config configs/research.pilot.json
--methods cloud_AR A B C Proposed --output-root results/research_20260928_135549/quality_pilot`.
Decision: pending. Do not infer noninferiority from a small pilot or zero observed
accuracy loss; report truncation and uncertainty explicitly.

### Experiment R007 — Remove unused draft probability telemetry (pre-registered)

Observed bottleneck: historical low-RTT A spent 36.9% of request wall time in
draft calls. A fit to its gamma sweep estimates ~32.5 ms per draft token and
~8.2 ms fixed cost, so a large fixed-overhead window-model rewrite is not the
first choice. Source inspection of this installed llama.cpp shows `n_probs>0`
triggers a vocabulary-wide probability/softmax pass for every token. EdgeClient
always requests `n_probs=1`, but the current acceptance rule uses only TARGET
probabilities; draft logprobs are unused compatibility telemetry.
Hypothesis: `n_probs=0` lowers draft latency without changing the greedy sampler.
Design: after R006 finishes, 4 saved prompts × offsets 0/32/64 where available ×
gamma 1/2/4/8 × 10 paired repeats; randomize n_probs=0/1 order with seed 42.
Save warmups separately; retain response IDs, timings and payload sizes. No
concurrent main benchmark. Acceptance threshold: >=3% draft latency reduction
and a prompt-cluster paired CI excluding zero, followed by real end-to-end task
quality/performance validation. Negative results are retained. This is an
engineering ablation, not by itself a publication contribution. Decision: pending.

### Analysis R008 — Acceptance-only optimistic trace replay (pre-registered)

Hypothesis: improving acceptance alone cannot close the observed gap to cloud AR
on this deployment. For every completed R006 SD request, credit each measured
round with gamma+1 output tokens while retaining its measured round cost, then
compare that optimistic rate to its paired cloud_AR request. Exclude request
setup cost, making the projection favorable to SD. Report all pairs.
This freezes measured trajectories and is not a general upper bound: policy
changes can change context length, later round costs and cache behavior. It is
an explanatory replay, never a measured optimization result. Decision: pending.

### Literature audit — contribution boundary

Primary-source review is saved in `docs/RELATED_WORK_AUDIT.md`. Probability-ratio
lossy acceptance plus adaptive drafting, and communication-aware draft-length
selection, already have close prior work. A local telemetry optimization or
a single-device negative latency result is not sufficient evidence of novelty.
Continue R006/R007; do not replace the objective with multi-tenant serving
without researcher agreement. No experimental outcome is inferred from papers.

### Source audit — cloud verifier cost

Upstream vLLM v0.26.0 defaults to bypassing prefix-cache reads for prompt
logprobs, which the current verifier requests across the complete context.
See `docs/VERIFIER_COST_AUDIT.md` and preserved source hashes. This is a
deployment-specific bottleneck hypothesis; remote installed source was not
inspected and no cloud-side causal intervention was run. Do not generalize
the current HTTP result to native suffix-scoring or all distributed SD.

### R006 / R007 / R008 results — reviewed 2026-09-30

R006: 160/160 requests completed without failures. Eight independent prompts.
Proposed vs A paired throughput gains: low +4.94% (95% descriptive prompt
bootstrap +0.07 to +9.28%), high +22.77% (+15.43 to +29.71%). Against B,
intervals include zero in both scenarios. Pooled task accuracy: AR 29/32,
A 28/32, B 27/32, C 24/32, Proposed 27/32. These are repeated observations,
not 32 independent quality examples. Cloud AR remains roughly 10–12x faster.
R008: all 128 SD traces remain below paired AR even in optimistic fixed-cost
full-acceptance replay. This is deployment-specific, not a general SD bound.
R007: 440 complete pairs, no failures; n_probs=0 draft latency reduction 7.36%,
4-prompt bootstrap [6.09%, 8.51%]. All pairs emitted matching token IDs,
a descriptive finding. ACCEPT microbenchmark hypothesis; end-to-end pending.
Sources: quality_pilot_analysis and draft_payload_analysis under the research root.

### Experiment R009 — End-to-end draft telemetry ablation (pre-registered)

Hypothesis: R007's saved draft cost produces measurable Proposed end-to-end
throughput gain without an observed task-quality regression. Only n_probs changes.
Use first 8 GSM8K pilot prompts, 2 repeats, 512 cap, low injected RTT 2ms,
randomized prompt order and paired variant order (seed 42), 32 requests.
Same-day paired controls avoid comparing September 30 directly with September 28.
Primary threshold: >=2% paired TPS gain and prompt-cluster CI low >0; report
quality changes and truncations separately. Small pilot cannot certify formal
quality noninferiority. Default n_probs remains 1 pending this result.
Command: python -m experiments.draft_payload_e2e --output-root
results/research_20260928_135549/draft_payload_e2e
Decision: pending. If unsupported, retain the negative end-to-end result.

### Researcher scope clarification — 2026-09-30

Only relative speculative-decoding performance is the optimization objective.
Do not use direct cloud AR as an acceptance criterion or require beating it.
Retain existing AR observations as historical evidence. Main comparisons are
A/B SD baselines and Proposed component ablations, with task quality reported.
R009 compares Proposed against its own unchanged n_probs=1 control and continues.

### Experiment R010 — Held-out controller ablation (pre-registered)

Hypothesis: jointly adapting K and draft length adds throughput beyond adapting
length alone, or fixed-K relaxed acceptance with adaptive length. Existing pilot
did not establish a gain against B; only ~1% of accepted tokens were relaxed.
Compare B (strict/adaptive window), D (fixed K=2/adaptive window), and Proposed
(joint adaptation). Use GSM8K rows 8–15, disjoint from tuning pilot rows 0–7,
2 repeats, 512-token cap, low/high injected delays 2/100 ms, seed 42.
All three methods use the SAME draft telemetry setting; R009's decision chooses
whether that common setting is 0 or historical 1. This cannot attribute a
telemetry improvement selectively to Proposed. No direct cloud speed baseline.
Primary comparisons: Proposed vs B and vs D by condition, paired TPS, latency,
answer quality and truncation. Report both comparisons including null results.
At least 5% mean TPS gain with positive prompt-bootstrap lower limit is the
practical speed threshold; observed quality loss prevents an unqualified win.
This remains exploratory (8 new independent prompts), not a noninferiority trial.
Decision: pending; run after R009 finishes. Optional method D and dataset offset
are added to the standard runner so all variants share the measurement path.

R010 runner validation: B/D/Proposed each executed in synthetic mode at dataset
offset 8 with expected K/window settings. Analysis initially failed on missing
synthetic task-quality scores (None); retain failure log and fix missing-value
handling. Synthetic quality is unavailable, not zero. This validation supplies
no real performance evidence.

R010 analysis validation retry passed after handling missing task scores.
The original failed analysis and its log remain. Sequential R009→analysis→R010
continuation is saved in research-root `followup_r009.py`; its runtime status
is distinct from immutable experiment outputs. No concurrent model benchmarks.

### R009 outcome — end-to-end gain not established

32/32 requests, 16 complete pairs, 8 independent prompt clusters. Paired mean
throughput gain +2.5718%, descriptive 95% cluster interval [-0.7323%, +5.8367%].
The preregistered positive-lower-bound condition fails. Latency reduction +2.64%,
interval [-9.62%, +13.71%]. Control correct 13/16, candidate 14/16; truncations
1/0. Quality observations are small and repeated; do not claim improved accuracy.
Interpretation: draft microbenchmark savings did not establish a stable full
system improvement. Retain DRAFT_N_PROBS=1 by default; no speedup claim from this
candidate. Decision: INCONCLUSIVE for positive end-to-end hypothesis.
R010 has started with n_probs=1 for ALL B/D/Proposed groups, as preregistered.
Source: draft_payload_e2e_analysis under the research root; complete raw data
and per-pair token counts preserved. Existing reports are not overwritten.

### Experiment R011 — Fixed early drafting (user requested)

Hypothesis: overlap a fixed amount of edge drafting with target verification
and network waiting to improve throughput over synchronous speculative decoding.
Both variants use K=1, gamma=4, unchanged n_probs=1. Candidate drafts h=5 ahead
on context+current_draft while verify runs. The first ahead token predicts the
target bonus; the full verified prefix must match before any continuation is
reused. Ahead tokens are never committed directly and all reused candidates
still pass target verification. Rejected/mismatched work is discarded.
Measure 4 first GSM8K prompts × 2 repeats × 2 injected-delay conditions (2/100ms)
× 2 variants = 32 requests. Randomize prompts and paired variant order with seed
42. Token cap 512. No direct cloud-generation speed comparison.
Record raw per-request throughput, latency, task quality, truncation, prefetch
service time, foreground stall, bridge matches, draft reuse and discarded work.
All pending prefetch tasks are joined at request end and charged to wall time.
Overlapping service durations must not be added as serial cost components.
Preregister >=5% paired TPS gain and prompt-bootstrap lower bound >0 as an
exploratory positive signal per condition; any quality regression is reported.
Four prompt clusters are not sufficient for generalization/noninferiority.
The ongoing R010 retains exclusive benchmark access; R011 follows serially.
Command: python -m experiments.fixed_lookahead --n 4 --repeats 2 --gamma 4
--lookahead 5 --output-root results/research_20260928_135549/fixed_lookahead
Validation: direct prefix/bonus mismatch, EOS, partial reuse, concurrent verify,
and orphan-work drain tests. Initial full-loop test failed because its mocked
input list was mutated between the two variants; return a fresh token list per
call and retain the initial test log. No real model experiment failed here.
Decision: pending.

### R011 outcome — fixed lookahead positive pilot signal

32/32 requests completed. Both variants use strict K=1, gamma=4; candidate
ahead length h=5 includes the predicted bonus token. Four independent GSM8K
prompts, two repeats, injected delays 2/100 ms. Low: control 13.337 TPS,
lookahead 15.008 TPS; paired gain +12.65%, descriptive prompt-bootstrap
95% interval [8.82%, 16.66%]. High: 9.237→13.188 TPS; paired gain +42.82%,
interval [38.22%, 47.42%]. All eight observations per variant per condition
were correct; this does not prove quality noninferiority. Each condition
generated 1,242 ahead tokens: 482 reused as draft, 122 matching bridge,
630 discarded, 8 terminal/excess unused. Foreground waits were 16.932 s
(low) and 0.461 s (high), pooled over eight candidate requests.
Interpretation: fixed lookahead has an exploratory positive speed signal,
especially with larger waiting time; approximately half of ahead tokens are
discarded. A lightweight gate has a plausible cost-saving opportunity, but
has not been shown to outperform fixed lookahead. Larger disjoint prompts
and repeated confirmation remain necessary. Sources: fixed_lookahead and
fixed_lookahead_analysis under the research root. Decision: ACCEPT feasibility
hypothesis for this pilot; do not claim general or paper-level validation.

## 2026-10-02 — Compact configurable experiment suite

Added `experiments.suite` as the shell/PowerShell entrypoint. Default real
quick plan is 96 timed requests: six SD methods, four prompts, two repeats,
two injected-delay conditions. Fixed lookahead is included; no direct-cloud
speed baseline is selected. Configuration, service endpoints and model registry
are selectable without editing the experiment code. Stop strings follow the
selected model configuration. Each run writes a Chinese-first/English-second
SUMMARY.md, paired tables, throughput figures, source/config snapshots and logs;
failed runs are explicitly incomplete. Smoke/simulation cannot establish speedup.

Validation: 70 unit/regression tests passed; git diff --check passed. The initial
real smoke failed because the cloud endpoint refused connections. After the user
restored cloud connectivity, all six real smoke requests completed successfully:
`results/suite_validation/20261002_132440_305109_3322efdf/SUMMARY.md`.
This checks real dispatch including lookahead and final report generation, not
performance or task quality (64-token smoke cap). Full 96-request quick suite
and other model pairs were not run in this implementation validation. PowerShell
wrapper was updated but not executed on this Linux host.

## 2026-10-02 — Pause Proposed and inspect high-delay slowdown

User requested temporarily excluding Proposed. Removed it from all one-command
suite profiles, preserving the low-level implementation and historical data.
Real quick now runs 80 requests; real smoke runs 5. Plan regression tests cover
quick and full exclusion. Report definitions omit Proposed when unselected.

Read-only analysis of results/suites/20261002_144828_552805_212067ad:
actual gamma=4, h=2 (not default h=5), completed 96 historical requests.
Lookahead low/high throughput 14.938/10.226 tokens/s; high remains +11.56%
paired over A (9.160 tokens/s). Both A and Lookahead average 35.5 rounds/request.
Injected delay averages 0.071 s low vs 3.550 s high: +3.479 s per request.
Lookahead wall time 9.072 vs 13.344 s (+4.272 s); injection difference is about
81% of that observed difference, not an additive causal decomposition because
prefetch overlaps verification. Each condition generated 560 ahead tokens,
reused 132 (23.6%), discarded 288 (51.4%); bridge/unused account for the rest.
With h=2, a matching one-token bonus leaves at most one token for next-round
reuse. Total foreground prefetch wait across 8 requests is 644.29 ms low vs
5.19 ms high: unfinished background drafting is not the main high-delay bottleneck.
Other timing differences need controlled repeated runs; no new speed claim.

## 2026-10-02 — Paired gamma 2/4/6 and lookahead sweep

Added --gamma-lookahead-sweep to run fixed strict K=1 windows gamma=2,4,6
with matching asynchronous h=gamma+1 (3,5,7). Six method identities are
preserved in raw records and report pairs compare identical gamma only.
The preceding window-only scope change is included: default suites exclude
C/D/Proposed and K sweeps. CLI/README/PowerShell updated. Full 71-test suite
passed before execution; subsequently added report pairing/figure regression
and all 7 suite tests passed. PowerShell not executed on Linux.

Executed 48 real requests (4 prompts, 1 repetition, low/high) with command:
bash run_all_experiments.sh --mode real --gamma-lookahead-sweep 2 4 6 --repeats 1
Output: results/suites/20261002_180445_474513_a82bf69f/SUMMARY.md
All requests completed; all task scores 1, no truncations. Paired throughput
gains for gamma 2/4/6 are -3.93/-15.41/-27.55% low and
+19.46/+8.14/+58.75% high. High gamma4 CI crosses zero. Highest observed high
throughput is gamma6/h7 at 11.250 tokens/s; low is fixed gamma2 at 10.623.
These are exploratory four-prompt, single-repeat results, not established
optima. Gamma and h covary; separate effects cannot be inferred. Sequential
method blocks and service-timing variation may confound between-method and
historical-run comparisons. Repeat confirmation needed before claiming the
large gamma6 speedup as stable. Original raw evidence and code snapshots kept.
# 2026-10-05 — Fixed-gamma adaptive lookahead implementation

User requested implementing the previously discussed h controller and a one-command runner.
Added `AdaptiveLookahead`: strict K=1, fixed gamma, h chosen from 0/2/3/5
(bounded by gamma+1), measured draft/verify costs, smoothed whole-prefix-plus-bonus
alignment, three-round updates and periodic short probes after disabling.
State resets per request; all probing, foreground waits and terminal drain are timed.
This is a heuristic; no claim of improved performance is made.

`run_adaptive_lookahead.sh` compares h=0, fixed h and adaptive h using seeded
within-prompt method order. Optional `--start-draft` starts an owned local service,
waits for health, refuses occupied ports and terminates only that service on exit.
Reports include comparisons against BOTH controls, per-round decisions and reuse/wait
statistics. Existing suite profiles remain available. See
`docs/RUNBOOK_ADAPTIVE_LOOKAHEAD.md` for commands and limitations.

Validation: 85 unit/integration/regression tests passed; static AST checks,
shell syntax and diff whitespace checks passed. Real Qwen GPU-draft startup
failed twice with CUDA allocation errors; the second attempt followed releasing
reclaimable cache for the same GGUF. Both startup logs are preserved under
`results/draft_startup/` (`adaptive-mGEmaB.log`, `adaptive-UYcDHX.log`).
No user application was terminated and no GPU speed result was produced.

An explicitly CPU-draft (`NGL=0`) smoke run completed 3/3 real requests against
the remote Qwen2.5-3B verifier, using the one-command auto-start runner:
`results/adaptive_validation_cpu/20261005_142517_550175_7cbf37bc/SUMMARY.md`.
The adaptive trace includes warmup h=0, h=2 probes, holds and disabling after
negative predicted gain. Raw records have no pending lookahead events; both
comparison pairs and CSV decision export were checked. The launcher exited
successfully and port 8080 was released. The 64-token, one-prompt CPU smoke
validates functionality only, not speedup, GPU behavior or task quality.
PowerShell argument forwarding was updated but not executed on Linux.

## 2026-10-08 — Revised manuscript objective

The user changed the paper objective to improving decoding speed while avoiding
a substantial increase in energy consumption, and requested that this guide
future paper revisions. The English manuscript now treats energy overhead as a
constraint rather than requiring an energy reduction. Persistent instructions
are recorded in `paper/edge_cloud_latency_adaptive_20261008/WRITING_GUIDELINES.md`
and linked from both READMEs. No acceptable numerical overhead was specified.
The frozen experiment protocol, raw data and earlier failed joint decision are
preserved; the revised objective is not presented as a prospectively confirmed
threshold. No new inference experiment was launched for this writing revision.

## 2026-10-08 — Retire superseded implementations and unreferenced results

The user requested removal of obsolete code and results. The maintained live
entrypoint is `run_downloaded_benchmarks.sh`, using the local 50/30/30 datasets
and only `fixed`, `fixed_fast`, and `regime`, once per condition. The earlier
suite runners, independent benchmark clients, superseded research prototypes,
their tests/runbooks and unrelated old outputs were removed. Earlier journal
entries describe historical paths and are not current operating instructions.

The active downloaded-data run, completed paper reproduction, and all cited
October 7 raw measurements and frozen source snapshots remain. Shared greedy
drafting, fixed lookahead, target verification and the final latency-regime
algorithm are unchanged. Archived report regeneration now validates archived
source hashes; current code is allowed to evolve. Source recovery information
and the deletion inventory are in `docs/CLEANUP_20261008.json`.

The downloaded GSM8K run was already active during this maintenance; it was
not stopped or rerun. Maintenance timestamps are recorded separately, because
gross board energy includes concurrent host activity. Validation uses offline
fixtures and local fake HTTP services, without real-model inference.

## 2026-10-09 — Progress review findings retained before deletion

`results/progress_review_20261009/` (regime_guard/regime_short probes) is
deleted at the user's request; the findings that still matter are kept here.
Pilot (48 requests, 6 prompts): fixed gamma2/h3 vs fixed_fast was +12.30%
TPS [2.32, 21.41] and +17.47% J/token saving at 2 ms, but -21.67% TPS at
300 ms. Follow-up (72 requests, 6 prompts, 2 repeats): regime_short vs
fixed_fast low +4.69% TPS [-2.35, 11.02], J/token saving +9.59% [0.84, 16.32];
low+high pooled +1.74% [-0.22, 3.89] and +5.23% [1.95, 7.90]. The guard fix
alone did not improve on regime. Online replay showed that the target
probability cap changes strict output: tied logprobs (e.g. MT-Bench p2,
tokens 7384/1933 both -1.0888996) return a different rank1 for cap1 vs cap4,
so every arm must use the same cap. vLLM 0.26 skips prefix-cache reads for
prompt-logprob requests, so each verification recomputes the whole context.
regime_short and regime_guard are dropped; `regime` itself is unchanged.

## 2026-10-09 — Critical-path-aware pipelined lookahead (Markov window controller)

Goal: faster edge-cloud SD without a substantial Jetson energy increase,
edge-side only (no cloud SSH; verify server unchanged). Campaign directory:
`results/pipeline_research_20261009/`; full write-up in its `REPORT.md`.

Diagnosis. Cloud verify time is ~14 + 0.30*context ms and nearly independent
of gamma (85/92/97 ms for gamma 2/4/6). Draft cost is ~15 ms per call plus
~24 ms/token. Board energy fits J = 4.33 W*wall + 10.0 W*draft-busy (R2
0.999), so discarded lookahead is expensive. Batched multi-branch drafting
is not cheap on this board (2/3/4 concurrent slots: 2.0/3.4/4.6x one draft).

Method. Fresh draft tokens sit on the critical path; lookahead tokens overlap
verification. `common/pipeline_model.py` models a two-state (prefetch
hit/miss) chain and picks, every round, the fresh window and lookahead
length minimizing (T*(1+w) + w*2.3*B)/tokens from online per-state
acceptance, round trip and draft cost (`edge/edge_client_pipeline.py`).

Held-out results vs fixed_fast (prompt-cluster bootstrap 95% CI). Set 1
(9 prompts, 108 requests): markov w0.25 low+high +4.8% TPS [1.2, 9.3], J/token
saving +3.7% [-1.5, 7.6]; markov w0.5 +0.0% TPS, +6.8% saving [0.2, 11.2];
markov vs regime_short +3.8% TPS [1.4, 6.2]. Set 2 (12 new prompts, 108
requests): markov low+high +6.0% [1.1, 10.7], saving +3.6% [-0.6, 9.0]; all
three delays +8.0% [2.9, 12.7]. MT-Bench lost 4-5% TPS at 100/300 ms; GSM8K
at 2 ms was unstable. A robust-estimator variant (markov_v2) was not better
(+1.0% [-1.9, 4.0] vs markov) and is retired. The budget-only pipeline dev
phase (+11.2% TPS but -2.5% J/token) is deleted; it motivated the energy term.
All campaign phases ran on a draft server restarted with --parallel 4
--kv-unified --ctx-size 8192 (single-stream speed unchanged).

## 2026-10-10 — Small baseline comparison (low/high delays only)

`results/compare_20261010/small_compare/` (plan `small_plan.json`, frozen before
the run): 7 arms, 6 previously unused prompts (2 per dataset), 1 repeat; 126/126
requests complete, power valid, no failures. The 300 ms very_high scenario was run,
but at the user's request it is no longer run or reported: reports show only
`primary_scenarios` (low 2 ms, high 100 ms) and pooled = low+high.
Pooled low+high vs fixed_fast (throughput; J/token saving): sync_g4 -21.5%
[-29.1, -16.4], +10.2% [-2.0, 16.7]; fixed_g2 -16.6%, +3.0%; fixed_g8 -12.9%,
-32.0%; AdaEDL -20.4% [-24.1, -18.4], -0.9%; markov_w0 +3.8% [-0.7, 13.4], -2.6%
[-6.9, 6.0]; markov_w05 -1.8% [-5.2, 8.3], +7.0% [-1.7, 11.0]. At 2 ms markov_w05
saved 12.0% J/token [7.2, 15.2] at +1.5% speed. markov_w0 by dataset: GSM8K +11.1%,
HumanEval +10.0%, MT-Bench -2.1% (J/token +7.9%). Prefetch matters: fixed_fast is
+27.4% [19.6, 41.1] faster than sync_g4 at 11.3% higher J/token; AdaEDL is only
+1.5% faster than sync_g4 with 12.3% higher J/token (top-20 probabilities and
streaming cost). All paired outputs identical; no extra truncations. With two
prompts per dataset, per-dataset intervals are not meaningful.

## 2026-10-10 — Full 110-prompt comparison started; CAPE manuscript draft

Started `results/compare_20261010/full_110` (plan `full_110_plan.json`): all 110
local prompts, the seven small_compare arms, low/high only, 1,540 requests,
seed 20261015. `progress_probe` gained `--resume` (same plan bytes; records
with invalid energy are moved to `failed/` and rerun). At the user's request a
paper draft was written while the run was active: analysis scripts and LaTeX
compilation ran under nice 19 and every CPU burst is timestamped in
`results/compare_20261010/full_110_maintenance.log`, so affected requests can
be identified or excluded.

Draft: `paper/cape_20261010/` (IEEEtran, 8 pages, package
`cape_20261010_latex.zip`). It names the markov controller CAPE and uses only
existing 2/100 ms evidence (held-out sets 1 and 2, small_compare: 228
requests, 27 prompts). All numbers are generated from raw records into
`numbers.tex`. Re-fitting the energy model on small_compare gives
5.73 W*T + 7.24 W*B (R2 0.996, r 1.26), lower than the controller's r = 2.3
from development runs; the draft discusses this as an energy-weight offset.

## 2026-10-11 — Full 110-prompt comparison (low/high delays)

`results/compare_20261010/full_110/` is complete: 1540/1540 requests, all
power traces valid. A cloud connection reset stopped the run at 761/1540
(2026-10-10 20:46:32 NZDT, cloud uptime shows no restart); it was resumed with
`--resume`, the interrupted request was re-executed, and the traceback is kept
in status.json. Pooled low+high vs fixed_fast over 110 prompts: markov_w0
+9.9% TPS [8.0, 12.0] with J/token +3.2% (saving -3.2% [-4.8, -1.6]); at 2 ms
+6.2% [3.6, 8.9] and saving +4.9% [2.9, 7.0]; at 100 ms +12.5% [10.2, 14.9]
with J/token +10.4%. markov_w05 +0.7% [-1.3, 3.1] and saving +6.1% [4.5, 7.7].
sync_g4 -23.4%, fixed_g2 -18.8%, fixed_g8 -6.5% (J/token +30.9%), adaedl
-24.3%. markov_w0 is +43.4% vs sync_g4 and +45.1% vs adaedl; markov_w05 is
+32.9% vs adaedl with saving +3.9% [2.6, 5.2]. markov_w0 by dataset: GSM8K
+8.9%, HumanEval +17.8%, MT-Bench +5.7% (all intervals above zero).
Excluding the 6 blocks that overlap logged maintenance (19 requests), or using
only the 80 prompts absent from earlier recorded phases, leaves the results
unchanged (markov_w0 +9.8%; markov_w05 saving 6.0% and 5.8%). Output sequences
differ in 45 of 220 prompt-delay blocks (pairs vs fixed_fast: markov_w0 19/220,
fixed_g2 20, fixed_g8 26, sync_g4 1), consistent with near-ties in the
quantized target that depend on the verification shape; GSM8K accuracy is
72-74/100 for every arm, and only 83-86 of 220 outputs per arm equal the cloud
autoregressive reference. The CAPE draft's "rare ties" wording, based on 2/54
blocks in the small sets, must be revised if these data are used.

## 2026-10-12 — CAPE manuscript revised with the full 110-prompt evaluation

At the user's request the draft (`paper/cape_20261010/`) now uses `full_110` as
its main evaluation (1,540 requests; the 6-prompt comparison set is dropped)
and keeps held-out sets 1 and 2 for the default w=0.25. Evidence extraction now
strips power samples on load (the full set exhausted memory) and uses the
energy check stored with each record. Re-fitted on full_110 the energy model is
3.25 W*T + 10.56 W*B (R2 0.990, r 3.2); fits across data sets give r 1.8-3.2,
so the controller's 2.3 lies within the range. The paper now reports output
differences honestly (45/220 blocks; window-size dependent; GSM8K accuracy
unchanged), compares CAPE-S with a per-delay oracle fixed window (Fixed-4 at
2 ms, Fixed-8 at 100 ms), and states CAPE-S's +3.2% J/token. Two review passes
corrected four claims against the data (Fixed-4 is fastest only pooled; Fixed-2
is marginally more frugal than CAPE-E at 2 ms; AdaEDL, not Sync-4, is slowest;
"never used" prompts restated as outside recorded phases).

## 2026-10-12 — CAPE manuscript: related work moved to Section II, 27 verified references

Related work now follows the introduction and covers speculative decoding
variants (survey, SpecInfer, Sequoia, BiLD, Medusa, EAGLE, lookahead decoding),
adaptive draft length, PEARL, on-device and edge-cloud systems (EdgeLLM, SLED,
SpecEdge, DSD, PicoSpec, WISP, "Speculation at a Distance") and LLM energy
benchmarks. Every reference was checked online (publisher page, DOI via
OpenAlex, or arXiv); the llama.cpp GitHub citation and the arXiv-only DISCO
entry were removed and AWQ now cites its MLSys 2024 version. Server details
(RTX 3080 10 GB workstation, both endpoints on campus Wi-Fi, dedicated during
runs) and the author block were added at the user's request.

## 2026-10-12 — Delete early and non-result data; publish current state

At the user's request (scope "keep only the CAPE paper's data, also delete the
old manuscript") the following were deleted locally: the 6-prompt pilot
`results/compare_20261010/small_compare` (superseded by full_110), the
October 8 regime benchmarks `results/downloaded_benchmarks`, the October 7
regime research and paper evidence `results/adaptive_research_20261007`,
`results/paper_reproduction`, console and draft-server logs, LaTeX build
directories, the October 8 manuscript `paper/edge_cloud_latency_adaptive_20261008`
with its Overleaf zips, and `analysis/adaptive_research_summary.py`, which only
summarized the deleted October 7 data. Kept: `full_110` (with its plan and
maintenance log), held-out sets `confirm_markov` and `final_markov_v2`, their
plans and REPORT.md. The writing guidelines moved to `docs/WRITING_GUIDELINES.md`.
The CAPE evidence script now lists the pilot prompts explicitly; regenerated
evidence is identical apart from the controller timing. Earlier entries that
cite deleted paths are historical.
