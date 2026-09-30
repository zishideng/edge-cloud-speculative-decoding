# Related-work audit — 2026-09-28

This is a positioning note, not a claim that the current experiments establish novelty.
Task accuracy and performance are primary; exact token identity is not required by
the researcher. All three sources below were inspected at their primary arXiv pages.

| Work | Relevant overlap | Implication for this project |
|---|---|---|
| [AdaptiveSpec: Margins, Not Windows](https://arxiv.org/html/2609.02897v1) | Target probability-ratio acceptance plus adaptive draft-tree shape; downstream task accuracy is empirical, not distribution preservation. | The broad combination of lossy verification and adaptive speculation is already represented. A rank cap and cumulative regret budget need their own evidence of added value; neither automatically guarantees task quality. |
| [Quantize-Sample-and-Verify](https://arxiv.org/html/2507.00605v3) | Communication-aware draft-length and quantization adaptation in edge–cloud SD. | Network-aware window selection alone is insufficient as a novelty claim. Its distribution-preserving quantized sampling differs from this project's greedy, lossy rank/ratio rule. |
| [Speculation at a Distance](https://arxiv.org/html/2606.25091v2) | Conditions for latency benefit over cloud AR and a model of multi-client capacity. | Finding that a slow edge draft cannot beat fast cloud AR is not by itself a new theoretical result. Real deployment measurements can validate boundaries, but broad claims require more than one model pair and one device. |

The first source's displayed submission date (July 3, 2026) is inconsistent with
its September identifier. Retain the exact identifier/version above and recheck
bibliographic metadata before preparing a manuscript; do not silently fix it.

The capacity argument in the third paper assumes enough independent clients to
overlap their edge work with cloud verification. Its comparison against AR also
depends on verification cost relative to one AR step. Current single-client
HTTP timings do not establish GPU occupancy, saturated throughput, or that
assumption. Injected queue sleeps cannot substitute for a multi-client experiment.

## Consequences for the next experiment

1. Complete the preregistered quality/latency pilot and the draft-telemetry ablation.
2. Keep acceptance-only trace projections separate from actual measurements.
3. Treat a successful telemetry optimization as engineering evidence, not a new
   decoding algorithm or enough evidence for a paper.
4. Before adopting a new algorithm, identify a specific failure in the measured
   baseline, a mechanism that addresses it, and a comparison against the closest
   existing method. Do not tune on the same small prompt set and report it as
   held-out quality evidence.
5. A move to multi-tenant cloud capacity changes the research question and needs
   researcher agreement plus a controlled, observable cloud serving setup.

These are deductions from the overlap and the local deployment, not conclusions
claimed by the cited authors about this repository.
