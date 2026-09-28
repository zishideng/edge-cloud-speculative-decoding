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
