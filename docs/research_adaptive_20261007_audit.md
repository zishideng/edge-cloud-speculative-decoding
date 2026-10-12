# Adaptive lookahead implementation and trace audit — 2026-10-07

Read-only audit of current implementation and archived real-model traces. No model or power benchmark was started by this audit.

## Evidence and current baseline

The latest complete suite is `results/suites/20261007_102930_314875_3f168317/`: **300/300** requests, the local 50 GSM8K prompts, one run per prompt/method/scenario, gamma=4, strict K=1, fixed h=5 versus original adaptive candidates {0,2,3,5}, injected delays 2/100 ms. It supersedes the four-prompt manuscript pilot as an empirical baseline. All six groups emit 9,926 output tokens, task accuracy 33/50, with three truncations per group. All 50 paired output sequences are identical across all three methods in each scenario. Only 16/50 match each cached cloud reference exactly; this is not an AR-equivalence proof.

The suite SUMMARY reports the mean of individual request TPS. The requested primary metric, total tokens / total wall time, is different:

| Scenario | Method | Total wall s | Aggregate TPS | Board J/token |
|---|---|---:|---:|---:|
| low | A | 765.2165 | 12.9715 | 0.6183 |
| low | Original adaptive | 573.2105 | 17.3165 | 0.6514 |
| low | Fixed h=5 | 567.0733 | 17.5039 | 0.6966 |
| high | A | 1082.4948 | 9.1696 | 0.7411 |
| high | Original adaptive | 795.5976 | 12.4762 | 0.7530 |
| high | Fixed h=5 | 774.6156 | 12.8141 | 0.7577 |

The paired mean TPS change original adaptive/fixed is -0.96% low and -3.64% high; aggregate changes are -1.07% and -2.64%. Original adaptive already saves low-scenario energy substantially (~6.49% aggregate J/token; 7.75% mean paired saving), but does not accelerate against fixed. Do not interchange these estimators.

## Exact execution and correctness constraints

`FixedLookaheadClient` drafts gamma candidates in the foreground. Its overlapped verifier launches h candidates on `prompt + current_draft` concurrently with the remote verifier. The first ahead token predicts the bonus/correction following the entire proposed draft. The next foreground draft synchronously calls `future.result()` before checking prefix compatibility, regardless of whether the current draft was rejected. Thus even known-invalid background work is awaited in full.

Reuse requires the entire true committed prefix to be a prefix of `prefetch_prefix + ahead_ids`; a bonus match alone is insufficient. With full acceptance and matching bonus, one ahead token is the bridge, leaving at most h-1 candidates. At h=5 and gamma=4, a match eliminates the next foreground model HTTP call completely. h=2 or h=3 still needs a fresh HTTP call to fill gamma, with its call overhead and cache/prefill costs. Reused tokens are candidates and still undergo strict target verification. Speculative work never directly commits outputs. EOS-containing draft suppresses launch. Terminal pending work is drained and charged to request wall time, and the pool shuts down before the next request.

Strict K=1 is canonical target rank-one acceptance (smallest token ID resolves ties) and gamma stays 4. This is not the stochastic p/q speculative sampling algorithm. Optimizations must retain the full-prefix check, verification of reused candidates, finite output cap, stop semantics, and all outstanding-work accounting. Any streaming cancellation implementation must demonstrate that the server really stops work before the next request; closing an HTTP stream without accounting for asynchronous server work is insufficient.

## Measured bottlenecks and headroom

In the full-subset fixed run there are 2,550 low and 2,548 high background events. Whole-prefix/bonus match is ~52.8%; ~46.7% of generated ahead tokens are discarded. Full gamma acceptance itself is ~59.6%, so bonus mismatch adds losses. Recent full acceptance is weakly predictive: next-round full acceptance is ~66.5% after a full-accept round, versus 45–53% after partial/rejected rounds. This is a possible state variable, not a validated classifier.

| Fixed h=5 event measure | Low | High |
|---|---:|---:|
| Mean background service ms | 142.90 | 157.78 |
| Total foreground waits s | 73.988 | 0.625 |
| Waits on mismatched work s | 36.511 | 0.269 |
| Waits on reused work s | 37.477 | 0.355 |
| Mean verify/round non-draft ms | 132.16 | 233.16 |

The verify cost increases with context length because the HTTP verifier scores the complete context. Low-scenario fixed h=5 stalls are concentrated early:

| Ahead prefix tokens | Events | Mean wait ms | Mean background service ms |
|---|---:|---:|---:|
| <200 | 1191 | 47.20 | 143.75 |
| 200–299 | 734 | 21.67 | 136.67 |
| 300–399 | 327 | 5.31 | 141.04 |
| >=400 | 298 | 0.46 | 156.89 |

The original adaptive already chooses mostly h=3 below 200 tokens and mostly h=5 above 300. High delay hides almost all fixed background service, and original adaptive loses from request reset plus one warmup round h=0 and three h=2 selections per request. Simply removing this cautious startup can recover the existing gap but provides no clear >5% advantage over fixed.

Optimistic trace projection: zero-cost instantaneous cancellation of every mismatched low event saves at most the recorded 36.51 s of waits, assuming every other cost and trajectory stays fixed. Against combined fixed wall 1,341.69 s, this is only ~2.8% throughput increase. It is not an upper bound under changed cache trajectories; it shows that cancellation of measured waits alone does not explain a >5% combined target. Additional energy savings can still be important. High-delay cancellation offers negligible direct time headroom.

## Controller model issues and a better local objective

The current controller uses sixteen-sample means of verify time, draft service per token, and a smoothed whole-prefix match probability. It scores `p*(h-1)*d - max(0,h*d-v) - 1ms`. It mixes foreground and background costs, extrapolates a per-token cost despite call/cache overhead, uses unconditional p, and predicts a hinge of means rather than the mean of a positive tail. In particular it omits the h=gamma+1 discontinuity where the next model call disappears.

A closer expected local saving is:

`G(h) = p(state) * [D(gamma, state) - D(max(0, gamma-h+1), state)] - E[max(0, B(h,state)-V(state))]`,

with `D(0)=0`, positive-length D including fixed call cost, B a separately fitted background cost, and V the verification wall time. Energy can add `-lambda * estimated incremental board joules`, with a reported fixed trade-off parameter rather than claiming a physical power model from latency alone. Compare h=0,2,3,5 under the same overhead model, update on completed observations only, and estimate enough uncertainty to avoid unstable action changes. Prefer an affine cost fit with separate foreground/background intercepts and context-dependent V over unmotivated complex machinery. It must include warmup and exploration costs.

## Recommended hypotheses and tests

1. **Affine/context-conditioned controller:** separate foreground/background cost models and explicitly D(0)=0; use prefix length and recent target round latency, retaining h=5 first-choice when its full-call elimination dominates. Measure h distribution, per-state predicted versus realized costs, wall/TPS, and J/token. This can plausibly improve current adaptive but >5% versus fixed is unestablished, especially high delay.
2. **Verification-aware streaming cancellation:** stream ahead tokens with token IDs; on a known rejection, cancel pending wrong-prefix generation immediately; on a match, weigh waiting for the remaining ahead tokens against a fresh call using the empirical model. Requires server-side cancellation verification and output/correctness tests. Speed opportunity is concentrated in short low-delay prefixes; energy opportunity includes all discarded work that has not yet executed.
3. **Confidence-conditioned gate:** parsing real draft token probabilities plus recent accepted-prefix patterns may help avoid costly invalid work. Current draft logprob parser does not handle all possible llama.cpp nested formats; never assume zero-filled absent telemetry is calibrated confidence. Confidence must be tested on development data and the extra probability extraction cost counted. At high delay, disabling low-confidence work generally trades speed for energy, so choose it only under a declared joint objective.
4. **Larger lookahead/carry-forward cache:** h>gamma+1 requires redesign to preserve unused suffixes across verifications; evaluate only after smaller changes. Full-prefix compatibility and pending-work accounting remain mandatory. Longer ahead chains magnify rejection waste, and are not automatically faster.

Meaningful unit tests: h=5 match removes all fresh-draft calls; partial h requires exactly correct remaining length; earlier draft mismatch plus coincidentally matching bonus cannot reuse; cancelled/rejected partial streams do not contribute output; terminal/exception cancellation does not leave server work contaminating a later request; deterministic timing model tests demonstrate D(0) discontinuity and tail cost; every generated draft either reused, bridge, discarded, or unused with exact token conservation.

## Existing work that must not be rediscovered or misattributed

`research_log.md` R007 already measured removing `n_probs=1`: 440 paired draft calls, matching IDs, 7.36% mean draft-latency reduction, four-prompt interval [6.09,8.51]%. R009 end-to-end result was +2.57% TPS, interval [-0.73,5.84]%, hence inconclusive and default retained at 1. This is an engineering ablation, not new algorithm evidence. R010 correctly required the same telemetry setting for all competing methods. If a new candidate uses n_probs=0, also include fixed h=5 with n_probs=0 so a generic payload saving is not selectively attributed to adaptive control.

`docs/VERIFIER_COST_AUDIT.md` describes full-context prompt-logprob requests in vLLM 0.26.0 and upstream prefix-cache bypass. This explains context-length dependence but remote internals were not causally profiled. Changing cloud verifier scoring is a separate system intervention; apply and validate consistently across methods, preserve every required suffix probability, and do not infer gains from an untested patch.

## Experimental boundary

All 50 local prompts have historical baseline measurements. New development/confirmation division can keep confirmation data unused for policy design from now on, but cannot honestly claim a wholly never-observed task set. Freeze question IDs before experiments and do not tune on confirmation outcomes. Use one timed run per condition as requested; randomize method order within prompt/scenario. Do not pool unequal output counts as apparent speed gains; report all sequences, answer scores, truncations and anomalies. Board energy is gross Jetson input only, not cloud/network energy. Unsuccessful methods and benchmark logs must be retained.
