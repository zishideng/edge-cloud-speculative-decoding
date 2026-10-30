# Progress probe: smoke_newarms

State: complete; 12/12 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low; pooled = low.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | picospec_g2 | 3 | 458 | 35.003 | 0.2279 | 0 | 48.64 |
| all/low | picospec_g8 | 3 | 458 | 37.480 | 0.2816 | 0 | 47.20 |
| all/low | markov_w0_fresh4_int | 3 | 458 | 38.328 | 0.2337 | 0 | 54.34 |
| all/low | markov_w0_int | 3 | 458 | 34.910 | 0.2184 | 0 | 57.31 |
| all/pooled | picospec_g2 | 3 | 458 | 35.003 | 0.2279 | 0 | 48.64 |
| all/pooled | picospec_g8 | 3 | 458 | 37.480 | 0.2816 | 0 | 47.20 |
| all/pooled | markov_w0_fresh4_int | 3 | 458 | 38.328 | 0.2337 | 0 | 54.34 |
| all/pooled | markov_w0_int | 3 | 458 | 34.910 | 0.2184 | 0 | 57.31 |
| humaneval/low | picospec_g2 | 1 | 188 | 47.127 | 0.1752 | 0 | 65.78 |
| humaneval/low | picospec_g8 | 1 | 188 | 83.832 | 0.1312 | 0 | 84.32 |
| humaneval/low | markov_w0_fresh4_int | 1 | 188 | 66.593 | 0.1325 | 0 | 84.66 |
| humaneval/low | markov_w0_int | 1 | 188 | 56.596 | 0.1429 | 0 | 79.37 |
| humaneval/pooled | picospec_g2 | 1 | 188 | 47.127 | 0.1752 | 0 | 65.78 |
| humaneval/pooled | picospec_g8 | 1 | 188 | 83.832 | 0.1312 | 0 | 84.32 |
| humaneval/pooled | markov_w0_fresh4_int | 1 | 188 | 66.593 | 0.1325 | 0 | 84.66 |
| humaneval/pooled | markov_w0_int | 1 | 188 | 56.596 | 0.1429 | 0 | 79.37 |
| mtbench/low | picospec_g2 | 1 | 109 | 28.307 | 0.2768 | 0 | 37.17 |
| mtbench/low | picospec_g8 | 1 | 109 | 24.188 | 0.3810 | 0 | 18.18 |
| mtbench/low | markov_w0_fresh4_int | 1 | 109 | 25.950 | 0.3175 | 0 | 32.77 |
| mtbench/low | markov_w0_int | 1 | 109 | 26.158 | 0.2775 | 0 | 42.61 |
| mtbench/pooled | picospec_g2 | 1 | 109 | 28.307 | 0.2768 | 0 | 37.17 |
| mtbench/pooled | picospec_g8 | 1 | 109 | 24.188 | 0.3810 | 0 | 18.18 |
| mtbench/pooled | markov_w0_fresh4_int | 1 | 109 | 25.950 | 0.3175 | 0 | 32.77 |
| mtbench/pooled | markov_w0_int | 1 | 109 | 26.158 | 0.2775 | 0 | 42.61 |
| gsm8k/low | picospec_g2 | 1 | 161 | 30.698 | 0.2563 | 0 | 37.85 |
| gsm8k/low | picospec_g8 | 1 | 161 | 29.428 | 0.3899 | 0 | 26.67 |
| gsm8k/low | markov_w0_fresh4_int | 1 | 161 | 32.685 | 0.2952 | 0 | 37.43 |
| gsm8k/low | markov_w0_int | 1 | 161 | 28.593 | 0.2665 | 0 | 45.45 |
| gsm8k/pooled | picospec_g2 | 1 | 161 | 30.698 | 0.2563 | 0 | 37.85 |
| gsm8k/pooled | picospec_g8 | 1 | 161 | 29.428 | 0.3899 | 0 | 26.67 |
| gsm8k/pooled | markov_w0_fresh4_int | 1 | 161 | 32.685 | 0.2952 | 0 | 37.43 |
| gsm8k/pooled | markov_w0_int | 1 | 161 | 28.593 | 0.2665 | 0 | 45.45 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | picospec_g8_vs_picospec_g2 | 3 | 7.08 [-14.55, 77.89] | -23.57 [-52.14, 25.11] | 0 | 0 |
| all/low | markov_w0_fresh4_int_vs_picospec_g2 | 3 | 9.50 [-8.33, 41.31] | -2.56 [-15.19, 24.37] | 0 | 0 |
| all/low | markov_w0_int_vs_picospec_g2 | 3 | -0.27 [-7.59, 20.09] | 4.18 [-3.99, 18.47] | 0 | 0 |
| all/pooled | picospec_g8_vs_picospec_g2 | 3 | 7.08 [-14.55, 77.89] | -23.57 [-52.14, 25.11] | 0 | 0 |
| all/pooled | markov_w0_fresh4_int_vs_picospec_g2 | 3 | 9.50 [-8.33, 41.31] | -2.56 [-15.19, 24.37] | 0 | 0 |
| all/pooled | markov_w0_int_vs_picospec_g2 | 3 | -0.27 [-7.59, 20.09] | 4.18 [-3.99, 18.47] | 0 | 0 |
| humaneval/low | picospec_g8_vs_picospec_g2 | 1 | 77.89 [77.89, 77.89] | 25.11 [25.11, 25.11] | 0 | 0 |
| humaneval/low | markov_w0_fresh4_int_vs_picospec_g2 | 1 | 41.31 [41.31, 41.31] | 24.37 [24.37, 24.37] | 0 | 0 |
| humaneval/low | markov_w0_int_vs_picospec_g2 | 1 | 20.09 [20.09, 20.09] | 18.47 [18.47, 18.47] | 0 | 0 |
| humaneval/pooled | picospec_g8_vs_picospec_g2 | 1 | 77.89 [77.89, 77.89] | 25.11 [25.11, 25.11] | 0 | 0 |
| humaneval/pooled | markov_w0_fresh4_int_vs_picospec_g2 | 1 | 41.31 [41.31, 41.31] | 24.37 [24.37, 24.37] | 0 | 0 |
| humaneval/pooled | markov_w0_int_vs_picospec_g2 | 1 | 20.09 [20.09, 20.09] | 18.47 [18.47, 18.47] | 0 | 0 |
| mtbench/low | picospec_g8_vs_picospec_g2 | 1 | -14.55 [-14.55, -14.55] | -37.64 [-37.64, -37.64] | 0 | 0 |
| mtbench/low | markov_w0_fresh4_int_vs_picospec_g2 | 1 | -8.33 [-8.33, -8.33] | -14.70 [-14.70, -14.70] | 0 | 0 |
| mtbench/low | markov_w0_int_vs_picospec_g2 | 1 | -7.59 [-7.59, -7.59] | -0.24 [-0.24, -0.24] | 0 | 0 |
| mtbench/pooled | picospec_g8_vs_picospec_g2 | 1 | -14.55 [-14.55, -14.55] | -37.64 [-37.64, -37.64] | 0 | 0 |
| mtbench/pooled | markov_w0_fresh4_int_vs_picospec_g2 | 1 | -8.33 [-8.33, -8.33] | -14.70 [-14.70, -14.70] | 0 | 0 |
| mtbench/pooled | markov_w0_int_vs_picospec_g2 | 1 | -7.59 [-7.59, -7.59] | -0.24 [-0.24, -0.24] | 0 | 0 |
| gsm8k/low | picospec_g8_vs_picospec_g2 | 1 | -4.14 [-4.14, -4.14] | -52.14 [-52.14, -52.14] | 0 | 0 |
| gsm8k/low | markov_w0_fresh4_int_vs_picospec_g2 | 1 | 6.47 [6.47, 6.47] | -15.19 [-15.19, -15.19] | 0 | 0 |
| gsm8k/low | markov_w0_int_vs_picospec_g2 | 1 | -6.86 [-6.86, -6.86] | -3.99 [-3.99, -3.99] | 0 | 0 |
| gsm8k/pooled | picospec_g8_vs_picospec_g2 | 1 | -4.14 [-4.14, -4.14] | -52.14 [-52.14, -52.14] | 0 | 0 |
| gsm8k/pooled | markov_w0_fresh4_int_vs_picospec_g2 | 1 | 6.47 [6.47, 6.47] | -15.19 [-15.19, -15.19] | 0 | 0 |
| gsm8k/pooled | markov_w0_int_vs_picospec_g2 | 1 | -6.86 [-6.86, -6.86] | -3.99 [-3.99, -3.99] | 0 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
