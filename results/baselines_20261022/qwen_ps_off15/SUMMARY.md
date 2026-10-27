# Progress probe: qwen_ps_off15

State: complete; 45/45 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low; pooled = low.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | pearl | 15 | 4699 | 30.398 | 0.2748 | 2 | 0.00 |
| all/low | markov_w0_dist | 15 | 4712 | 31.622 | 0.3405 | 2 | 32.04 |
| all/low | markov_w05_dist | 15 | 4712 | 31.341 | 0.3111 | 2 | 33.71 |
| all/pooled | pearl | 15 | 4699 | 30.398 | 0.2748 | 2 | 0.00 |
| all/pooled | markov_w0_dist | 15 | 4712 | 31.622 | 0.3405 | 2 | 32.04 |
| all/pooled | markov_w05_dist | 15 | 4712 | 31.341 | 0.3111 | 2 | 33.71 |
| humaneval/low | pearl | 5 | 1841 | 32.813 | 0.2546 | 0 | 0.00 |
| humaneval/low | markov_w0_dist | 5 | 1841 | 36.837 | 0.3058 | 0 | 41.51 |
| humaneval/low | markov_w05_dist | 5 | 1841 | 35.037 | 0.2900 | 0 | 40.99 |
| humaneval/pooled | pearl | 5 | 1841 | 32.813 | 0.2546 | 0 | 0.00 |
| humaneval/pooled | markov_w0_dist | 5 | 1841 | 36.837 | 0.3058 | 0 | 41.51 |
| humaneval/pooled | markov_w05_dist | 5 | 1841 | 35.037 | 0.2900 | 0 | 40.99 |
| mtbench/low | pearl | 5 | 1639 | 26.115 | 0.3188 | 2 | 0.00 |
| mtbench/low | markov_w0_dist | 5 | 1639 | 24.377 | 0.4173 | 2 | 17.59 |
| mtbench/low | markov_w05_dist | 5 | 1639 | 24.922 | 0.3585 | 2 | 19.46 |
| mtbench/pooled | pearl | 5 | 1639 | 26.115 | 0.3188 | 2 | 0.00 |
| mtbench/pooled | markov_w0_dist | 5 | 1639 | 24.377 | 0.4173 | 2 | 17.59 |
| mtbench/pooled | markov_w05_dist | 5 | 1639 | 24.922 | 0.3585 | 2 | 19.46 |
| gsm8k/low | pearl | 5 | 1219 | 34.129 | 0.2463 | 0 | 0.00 |
| gsm8k/low | markov_w0_dist | 5 | 1232 | 38.742 | 0.2901 | 0 | 42.60 |
| gsm8k/low | markov_w05_dist | 5 | 1232 | 38.456 | 0.2797 | 0 | 43.52 |
| gsm8k/pooled | pearl | 5 | 1219 | 34.129 | 0.2463 | 0 | 0.00 |
| gsm8k/pooled | markov_w0_dist | 5 | 1232 | 38.742 | 0.2901 | 0 | 42.60 |
| gsm8k/pooled | markov_w05_dist | 5 | 1232 | 38.456 | 0.2797 | 0 | 43.52 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
