# Small paired probes (`experiments.progress_probe`)

A research runner separate from the maintained downloaded benchmark. It reuses the running local draft and cloud verify services and saves every request, power trace, failure, protocol and source snapshot.

## Methods

All methods use temperature 0, strict K1, target probability cap 1 and the same token parser/model pair. Draft `n_probs` is 0 except AdaEDL.

- `sync_g4`: synchronous SD, gamma 4, no lookahead.
- `fixed_g2`, `fixed_fast` (gamma 4), `fixed_g8`: fixed gamma with lookahead h = gamma + 1.
- `adaedl`: AdaEDL entropy-based early draft stopping (arXiv:2410.18351) re-implemented as synchronous SD with streamed top-20 draft probabilities (`edge/edge_client_adaedl.py`).
- `markov` (w 0.25), `markov_w0` (speed only), `markov_w05` (energy-leaning): two-state pipeline controller (`edge/edge_client_pipeline.py`, `common/pipeline_model.py`).

## Run a phase

Write a plan JSON with a new unique `phase`, `campaign` directory, `methods`, `indices`, `scenarios` (low 2 ms and high 100 ms only; the 300 ms very_high scenario is no longer run), `primary_scenarios`, `repeats`, `max_tokens`, optional `baselines` (default `["fixed_fast"]`), then:

```bash
python3 -u -m experiments.progress_probe --plan path/to/plan.json
python3 -m experiments.progress_probe --report <campaign>/<phase>   # recompute report only
```

The runner refuses an existing phase directory, checks services and board power, generates untimed references and equal 16-token warmups, randomizes method order in prompt/scenario blocks, and never retries. Example plans: `results/pipeline_research_20261009/*_plan.json`.

Report total tokens / total wall time and integrated board joules / total tokens. Bootstrap clusters are dataset/prompt; independent sample size is the number of prompts. Reports show only `primary_scenarios` (default: every scenario in the plan); `pooled` rows combine them. Older phases that also ran very_high keep those raw records, but they are not reported. Do not run model benchmarks, simulations or other CPU-heavy work concurrently: board energy is gross.
