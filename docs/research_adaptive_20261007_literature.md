# Adaptive lookahead: literature audit and testable hypotheses

Final scope correction: the user subsequently required keeping drafting enabled. Earlier disable/enable hypotheses below are historical alternatives, not actions in the final controller. The final latency-regime policy always drafts and retains a complete gamma+1 background continuation when it can be consumed; only EOS and terminal output capacity suppress unnecessary continuation work.

Research date: 2026-10-07. Scope: fixed verification window gamma=4, strict K=1, unchanged draft and target models, real Jetson board energy. These notes distinguish published mechanisms from hypotheses for this implementation. No experiment results are claimed here.

## Primary sources and what transfers

| Work | Verified primary source | Mechanism and applicability |
|---|---|---|
| PEARL, ICLR 2025 | [Publisher PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/03b1043052700b1a471996b0baf309d4-Paper-Conference.pdf); [author code](https://github.com/smart-lty/ParallelSpeculativeDecoding) | Uses pre-verify and post-verify to overlap target and draft execution. Post-verify continues drafting while previous tokens are verified; rejection discards the invalid continuation. The current project already implements a constrained post-verify style mechanism, so overlap alone is not a new contribution. The full pre-verify mechanism changes verification scheduling and is a separate experiment. |
| SpecEdge, NeurIPS 2025 | [Publisher PDF](https://papers.nips.cc/paper_files/paper/2025/file/8587069d00a69d0ea498d547fffad6dd-Paper-Conference.pdf); [author code](https://github.com/kaist-ina/specedge) | Proactive edge drafting overlaps remote verification; pipeline-aware scheduling interleaves users. Its tree drafting and multi-user server capacity gains are not directly equivalent to this single-request linear h controller. Proactive work must be evaluated against useful reuse and extra edge computation. |
| DSD, 2025 preprint | [Paper](https://arxiv.org/abs/2511.21669); [full text](https://arxiv.org/html/2511.21669v1) | Adaptive Window Control uses measured acceptance, RTT, TPOT, queue depth, and prior window. It controls gamma rather than this project's additional h. It motivates observing actual costs and stabilizing decisions, but neither its trained predictor nor its simulator speedup transfers automatically to Jetson. |
| PicoSpec, 2026 preprint | [Paper](https://arxiv.org/abs/2603.19133); [full text](https://arxiv.org/html/2603.19133v1) | Asynchronous drafting, early verification, rejection interrupt/rollback, and latency-aware truncation address pipeline bubbles. Rejection-aware stopping and bounded drafting are applicable design ideas. Separate rejection sampling and sparse probability compression concern stochastic distribution handling and are unnecessary for this strict greedy K=1 experiment. The paper's claims are not performance evidence for our implementation. |
| WISP, 2026 preprint, v2 | [Paper](https://arxiv.org/abs/2601.11652); [full text](https://arxiv.org/html/2601.11652v2) | Formalizes wasted drafting time and verification interference. A small predictor uses draft confidence, entropy, margin, and dispersion to stop before likely rejection. Applicable lesson: optimize useful work rather than raw draft throughput. Its server batching results and variable draft windows require separate scope. Draft-side uncertainty is a proxy that needs calibration on this quantized pair. |
| AdaEDL, NeurIPS 2024 workshop preprint | [Paper](https://arxiv.org/abs/2410.18351) | Stops drafting using an entropy-based lower bound on acceptance. Potentially useful for additional h token budgeting, provided unsaturated logits or correctly defined probabilities can be collected cheaply. Current top-k=1 response logprobs must not be assumed to provide entropy. |
| Learning To Draft, ICLR 2026 | [Publisher page](https://proceedings.iclr.cc/paper_files/paper/2026/hash/34345e243156da67605d4b63d71c8d98-Abstract-Conference.html) | Learns coordinated draft/verify policies with true cycle throughput as objective, explicitly addressing proxy objectives that ignore time. For a small online Jetson experiment, measured marginal time/energy is preferable to training a large policy before identifying the bottleneck. |
| Benchmarking the Energy Savings with Speculative Decoding Strategies, Findings of EACL 2026 | [Publisher page](https://aclanthology.org/2026.findings-eacl.249/); [PDF](https://aclanthology.org/2026.findings-eacl.249.pdf) | Reports that faster configurations can consume more energy; draft/target runtime, backend, and task all matter. Hardware is A5000/A6000 and energy uses CodeCarbon, so quantitative energy results should not be transplanted to Jetson INA3221 board measurements. Our J/token must be measured directly. |

## Audit of the current implementation

Source files read: `common/lookahead_controller.py`, `edge/edge_client_lookahead.py`, and `edge/edge_client.py`.

- The candidate h is extra drafting during verification, not gamma. With gamma=4, h=5 spends the first speculative token predicting the verifier's bonus, leaving at most four reusable draft tokens.
- Reuse requires the entire draft prefix and verifier bonus to match. Token acceptance rate is not this all-prefix-and-bonus probability.
- `_take` currently waits for the entire future before testing compatibility. If a previously drafted token was rejected, incompatibility is already knowable from the immutable prefix; waiting can pay for useless remaining drafting.
- An HTTP request cannot be cancelled by `Future.cancel()` after it begins. The server's active generation must actually stop, and all activity must finish before the next measured request.
- The existing model uses `p*(h-1)*d - max(0,h*d-v) - 1ms`, with a single average d for both foreground and background calls. It ignores fixed per-call costs, prompt suffix work, per-h cost, response parsing, and possible KV-cache changes after rejection.
- A short background request and a partial foreground refill can cost more than a single long request even at the same token count. In particular, h=2 followed by three foreground tokens incurs an additional service call on matching rounds.
- Current greedy draft requests force top_k=1. `draft()` also substitutes zero logprobs when response fields are unavailable. Neither zeros nor an already filtered top-1 distribution should be used as model confidence without checking raw response semantics.
- `cache_prompt=true` is enabled. Upstream documentation warns that different batch shapes can change logits slightly. Streaming/chunking changes therefore need output sequence checks, even when the acceptance rule itself is unchanged.

## A finite, directly testable time and energy model

Let F(k,s) be measured wall time of a foreground call for k draft tokens at prefix state s. Let B(h,s) be total background service time, V the observed verification interval available for overlap, p the complete-prefix-plus-bonus compatibility probability, and R(h) the reusable token count (at most min(gamma,h-1)). Ignore EOS for this local comparison and charge actual terminal drain separately.

Expected local critical-path cost associated with drafting the next round is approximately:

`C(h) = E[max(0,B(h,s)-V)] + p E[F(gamma-R(h),s_hit)] + (1-p) E[F(gamma,s_miss)]`.

This is a hypothesis model, not a proved speedup bound. A direct measured F(0)=0 is essential: h=5 can eliminate a complete foreground call on a hit, whereas shorter h often cannot. Using only `tokens*d` misses this discrete gain. Estimate costs separately for hit, miss, prefix length, and requested count when data support it; avoid overfitting tiny datasets.

Approximate gross board energy is `E_board = P_idle*T_wall + E_dynamic_foreground + E_dynamic_background + E_other`. Reducing hidden background work can lower energy without changing wall time, while reducing wall time also lowers the idle component. To achieve both objectives, optimize measured J/token subject to a latency improvement requirement, or use a time-equivalent penalty whose weight is calibrated on development measurements. Do not infer cloud or network energy from the Jetson sensor.

At high delay, if every B(5) is hidden and h=5 fully replaces a foreground draft on a match, h-only shortening cannot improve that hit's ideal critical path. A >5% gain then needs enough miss-side savings, avoided request overhead, better conditional decisions, cache behavior, or another scheduling improvement. Measure this ceiling before promising repeated h tuning will succeed.

## Ranked hypotheses for quick experiments

1. **Account for per-request overhead and the h=5 full-call elimination.** Fit a nonnegative intercept and marginal token cost from completed calls, or use empirical per-length costs. Compare against the current linear heuristic. Expected benefit: prevent overvaluing partial reuse and choose h=5 when the whole call fits; at low delay favor h near the measured overlap budget. Failure: predicted cost ranking fails to track actual wall times or J/token.
2. **Consume streamed prefixes at verifier completion; stop useless suffix work.** Keep background draft token IDs as they arrive. On early rejection, stop the live request; on a compatible prefix, consume only the available valid cached tokens and refill the remainder. This requires verifying actual server cancellation and accurate power/wall-time accounting. Expected benefit: remove post-verifier tail waits and discarded tokens. Failure: cancellation lag, extra HTTP calls, or cache disturbance exceeds savings.
3. **Condition enable/disable on recent complete-prefix outcomes.** Track rejection runs and optionally current draft confidence only after validating its meaning. Disable low-value rounds and probe sparingly; charge the probe cost. Expected benefit: energy saving in poorly aligned regions. Failure: low alignment is not predictable and disabled rounds lose too much useful reuse.
4. **Explicitly account for terminal and near-limit rounds.** Do not launch a full extra batch when EOS is already in the current draft (already implemented); additionally restrict work when remaining output capacity makes reuse impossible. Expected benefit: remove terminal drains and unnecessary energy. Failure: too rare to matter; must report its actual contribution rather than generalize.

First isolate the change at gamma=4, K=1. Keep fixed h=5 as a major baseline, but inspect fixed h=2/3/4 if a new policy wins simply by matching a better fixed setting. All optimizations must preserve target verification of emitted tokens.

## Actual local llama.cpp cancellation evidence

Local checkout: `/home/jetson/specdecode/llama.cpp`, commit `063d9c156e816ae3cf62db01f429a07a099afe97` at inspection. This is implementation evidence, not a claim that every downloaded llama-server binary matches that commit.

- `tools/server/server-context.cpp:39`: `HTTP_POLLING_SECONDS = 1`.
- Nonstream completion calls `rd.wait_for_all(req.should_stop)` near line 3888.
- Streaming reads `rd.next(req.should_stop)` and checks the stop callback between chunks.
- `tools/server/server-queue.h:183`: response reader destructor calls `stop()`.
- `tools/server/server-queue.cpp:441`: `stop()` posts cancellation for remaining tasks.

For a ~100 ms h batch, nonstream socket cancellation may arrive too late because polling waits up to one second. Streaming wakes the consumer as tokens arrive and is the plausible low-lag route. Confirm with the actual running binary using server-side slot state/logs and measured task completion; a closed client response alone is not proof of stopped GPU work. Current upstream [server documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README-dev.md) also distinguishes ordinary socket-bound streams from optional resumable streams, so avoid a resumable conversation mode for abortable background drafts.

## Fresh GSM8K confirmation data

Official [repository](https://github.com/openai/grade-school-math) and [test JSONL](https://raw.githubusercontent.com/openai/grade-school-math/master/grade_school_math/data/test.jsonl) were inspected. The official test split has 1,319 records. Each record has `question` and `answer`; the worked solution ends in a `####` final numeric answer marker.

The local `common/data/gsm8k_test_50.jsonl` was compared against the downloaded official source: all 50 question strings exactly match official rows 0–49. Its schema is `id`, `question`, and `gold_answer`. The inspected official raw file SHA-256 is `3730d312f6e3440559ace48831e51066acaca737f6eabec99bccb9e4b3c39d14` and it contains 1,319 records.

Preserve canonical zero-based row indices and source hashes when converting to the project's schema. Reserve official rows 50–61 for the first independent confirmation block, after development on original rows 0–7. Do not relabel previously used local questions as unseen. If confirmation feedback triggers another design change, reserve a new block, such as rows 62–73.
