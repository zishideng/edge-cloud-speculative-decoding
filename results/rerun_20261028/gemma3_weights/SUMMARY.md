# Progress probe: gemma3_weights

State: complete; 150/150 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: dynamic; pooled = dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/dynamic | markov_w0_dist_int | 30 | 8139 | 22.251 | 0.3535 | 4 | 38.12 |
| all/dynamic | markov_w025_dist_int | 30 | 8139 | 21.676 | 0.3262 | 4 | 42.37 |
| all/dynamic | markov_w05_dist_int | 30 | 8113 | 21.245 | 0.3221 | 4 | 42.20 |
| all/dynamic | markov_w1_dist_int | 30 | 8114 | 21.133 | 0.3178 | 4 | 41.33 |
| all/dynamic | markov_w2_dist_int | 30 | 8209 | 20.928 | 0.3168 | 5 | 40.87 |
| all/pooled | markov_w0_dist_int | 30 | 8139 | 22.251 | 0.3535 | 4 | 38.12 |
| all/pooled | markov_w025_dist_int | 30 | 8139 | 21.676 | 0.3262 | 4 | 42.37 |
| all/pooled | markov_w05_dist_int | 30 | 8113 | 21.245 | 0.3221 | 4 | 42.20 |
| all/pooled | markov_w1_dist_int | 30 | 8114 | 21.133 | 0.3178 | 4 | 41.33 |
| all/pooled | markov_w2_dist_int | 30 | 8209 | 20.928 | 0.3168 | 5 | 40.87 |
| mtbench/dynamic | markov_w0_dist_int | 10 | 3279 | 15.390 | 0.4874 | 3 | 20.20 |
| mtbench/dynamic | markov_w025_dist_int | 10 | 3279 | 15.148 | 0.4363 | 3 | 21.01 |
| mtbench/dynamic | markov_w05_dist_int | 10 | 3252 | 15.235 | 0.4250 | 3 | 20.18 |
| mtbench/dynamic | markov_w1_dist_int | 10 | 3248 | 15.470 | 0.4110 | 3 | 19.05 |
| mtbench/dynamic | markov_w2_dist_int | 10 | 3248 | 15.120 | 0.4155 | 3 | 19.50 |
| mtbench/pooled | markov_w0_dist_int | 10 | 3279 | 15.390 | 0.4874 | 3 | 20.20 |
| mtbench/pooled | markov_w025_dist_int | 10 | 3279 | 15.148 | 0.4363 | 3 | 21.01 |
| mtbench/pooled | markov_w05_dist_int | 10 | 3252 | 15.235 | 0.4250 | 3 | 20.18 |
| mtbench/pooled | markov_w1_dist_int | 10 | 3248 | 15.470 | 0.4110 | 3 | 19.05 |
| mtbench/pooled | markov_w2_dist_int | 10 | 3248 | 15.120 | 0.4155 | 3 | 19.50 |
| humaneval/dynamic | markov_w0_dist_int | 10 | 1718 | 46.253 | 0.1812 | 0 | 75.16 |
| humaneval/dynamic | markov_w025_dist_int | 10 | 1718 | 45.018 | 0.1848 | 0 | 74.78 |
| humaneval/dynamic | markov_w05_dist_int | 10 | 1718 | 43.859 | 0.1850 | 0 | 74.36 |
| humaneval/dynamic | markov_w1_dist_int | 10 | 1718 | 43.875 | 0.1848 | 0 | 73.81 |
| humaneval/dynamic | markov_w2_dist_int | 10 | 1718 | 41.770 | 0.1886 | 0 | 72.23 |
| humaneval/pooled | markov_w0_dist_int | 10 | 1718 | 46.253 | 0.1812 | 0 | 75.16 |
| humaneval/pooled | markov_w025_dist_int | 10 | 1718 | 45.018 | 0.1848 | 0 | 74.78 |
| humaneval/pooled | markov_w05_dist_int | 10 | 1718 | 43.859 | 0.1850 | 0 | 74.36 |
| humaneval/pooled | markov_w1_dist_int | 10 | 1718 | 43.875 | 0.1848 | 0 | 73.81 |
| humaneval/pooled | markov_w2_dist_int | 10 | 1718 | 41.770 | 0.1886 | 0 | 72.23 |
| gsm8k/dynamic | markov_w0_dist_int | 10 | 3142 | 27.186 | 0.3081 | 1 | 47.58 |
| gsm8k/dynamic | markov_w025_dist_int | 10 | 3142 | 26.000 | 0.2887 | 1 | 48.22 |
| gsm8k/dynamic | markov_w05_dist_int | 10 | 3143 | 24.318 | 0.2905 | 1 | 47.48 |
| gsm8k/dynamic | markov_w1_dist_int | 10 | 3148 | 23.346 | 0.2942 | 1 | 45.74 |
| gsm8k/dynamic | markov_w2_dist_int | 10 | 3243 | 23.793 | 0.2859 | 2 | 45.49 |
| gsm8k/pooled | markov_w0_dist_int | 10 | 3142 | 27.186 | 0.3081 | 1 | 47.58 |
| gsm8k/pooled | markov_w025_dist_int | 10 | 3142 | 26.000 | 0.2887 | 1 | 48.22 |
| gsm8k/pooled | markov_w05_dist_int | 10 | 3143 | 24.318 | 0.2905 | 1 | 47.48 |
| gsm8k/pooled | markov_w1_dist_int | 10 | 3148 | 23.346 | 0.2942 | 1 | 45.74 |
| gsm8k/pooled | markov_w2_dist_int | 10 | 3243 | 23.793 | 0.2859 | 2 | 45.49 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/dynamic | markov_w025_dist_int_vs_markov_w0_dist_int | 30 | -2.58 [-5.06, 0.36] | 7.72 [5.88, 9.52] | 2 | 0 |
| all/dynamic | markov_w05_dist_int_vs_markov_w0_dist_int | 30 | -4.52 [-7.80, -1.37] | 8.89 [6.20, 11.05] | 2 | 0 |
| all/dynamic | markov_w1_dist_int_vs_markov_w0_dist_int | 30 | -5.03 [-9.63, -0.76] | 10.11 [6.57, 12.83] | 4 | 0 |
| all/dynamic | markov_w2_dist_int_vs_markov_w0_dist_int | 30 | -5.95 [-9.59, -2.30] | 10.39 [7.12, 12.95] | 5 | 1 |
| all/pooled | markov_w025_dist_int_vs_markov_w0_dist_int | 30 | -2.58 [-5.06, 0.36] | 7.72 [5.88, 9.52] | 2 | 0 |
| all/pooled | markov_w05_dist_int_vs_markov_w0_dist_int | 30 | -4.52 [-7.80, -1.37] | 8.89 [6.20, 11.05] | 2 | 0 |
| all/pooled | markov_w1_dist_int_vs_markov_w0_dist_int | 30 | -5.03 [-9.63, -0.76] | 10.11 [6.57, 12.83] | 4 | 0 |
| all/pooled | markov_w2_dist_int_vs_markov_w0_dist_int | 30 | -5.95 [-9.59, -2.30] | 10.39 [7.12, 12.95] | 5 | 1 |
| mtbench/dynamic | markov_w025_dist_int_vs_markov_w0_dist_int | 10 | -1.57 [-4.79, 3.07] | 10.48 [8.55, 13.26] | 1 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_markov_w0_dist_int | 10 | -1.01 [-4.39, 3.22] | 12.79 [10.79, 15.00] | 1 | 0 |
| mtbench/dynamic | markov_w1_dist_int_vs_markov_w0_dist_int | 10 | 0.52 [-3.34, 4.98] | 15.68 [13.27, 17.84] | 2 | 0 |
| mtbench/dynamic | markov_w2_dist_int_vs_markov_w0_dist_int | 10 | -1.76 [-5.30, 2.36] | 14.75 [12.20, 16.87] | 3 | 0 |
| mtbench/pooled | markov_w025_dist_int_vs_markov_w0_dist_int | 10 | -1.57 [-4.79, 3.07] | 10.48 [8.55, 13.26] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_markov_w0_dist_int | 10 | -1.01 [-4.39, 3.22] | 12.79 [10.79, 15.00] | 1 | 0 |
| mtbench/pooled | markov_w1_dist_int_vs_markov_w0_dist_int | 10 | 0.52 [-3.34, 4.98] | 15.68 [13.27, 17.84] | 2 | 0 |
| mtbench/pooled | markov_w2_dist_int_vs_markov_w0_dist_int | 10 | -1.76 [-5.30, 2.36] | 14.75 [12.20, 16.87] | 3 | 0 |
| humaneval/dynamic | markov_w025_dist_int_vs_markov_w0_dist_int | 10 | -2.67 [-6.61, 2.29] | -2.00 [-4.40, 0.02] | 0 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_markov_w0_dist_int | 10 | -5.18 [-8.86, -0.93] | -2.12 [-5.44, 0.78] | 0 | 0 |
| humaneval/dynamic | markov_w1_dist_int_vs_markov_w0_dist_int | 10 | -5.14 [-10.89, 0.26] | -1.98 [-5.85, 1.26] | 0 | 0 |
| humaneval/dynamic | markov_w2_dist_int_vs_markov_w0_dist_int | 10 | -9.69 [-15.06, -3.26] | -4.06 [-8.55, -0.14] | 0 | 0 |
| humaneval/pooled | markov_w025_dist_int_vs_markov_w0_dist_int | 10 | -2.67 [-6.61, 2.29] | -2.00 [-4.40, 0.02] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_markov_w0_dist_int | 10 | -5.18 [-8.86, -0.93] | -2.12 [-5.44, 0.78] | 0 | 0 |
| humaneval/pooled | markov_w1_dist_int_vs_markov_w0_dist_int | 10 | -5.14 [-10.89, 0.26] | -1.98 [-5.85, 1.26] | 0 | 0 |
| humaneval/pooled | markov_w2_dist_int_vs_markov_w0_dist_int | 10 | -9.69 [-15.06, -3.26] | -4.06 [-8.55, -0.14] | 0 | 0 |
| gsm8k/dynamic | markov_w025_dist_int_vs_markov_w0_dist_int | 10 | -4.36 [-7.76, -0.19] | 6.29 [4.98, 7.52] | 1 | 0 |
| gsm8k/dynamic | markov_w05_dist_int_vs_markov_w0_dist_int | 10 | -10.55 [-14.71, -6.19] | 5.72 [1.20, 8.04] | 1 | 0 |
| gsm8k/dynamic | markov_w1_dist_int_vs_markov_w0_dist_int | 10 | -14.13 [-18.97, -9.06] | 4.50 [0.40, 7.29] | 2 | 0 |
| gsm8k/dynamic | markov_w2_dist_int_vs_markov_w0_dist_int | 10 | -12.48 [-16.68, -7.40] | 7.20 [2.83, 10.53] | 2 | 1 |
| gsm8k/pooled | markov_w025_dist_int_vs_markov_w0_dist_int | 10 | -4.36 [-7.76, -0.19] | 6.29 [4.98, 7.52] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_int_vs_markov_w0_dist_int | 10 | -10.55 [-14.71, -6.19] | 5.72 [1.20, 8.04] | 1 | 0 |
| gsm8k/pooled | markov_w1_dist_int_vs_markov_w0_dist_int | 10 | -14.13 [-18.97, -9.06] | 4.50 [0.40, 7.29] | 2 | 0 |
| gsm8k/pooled | markov_w2_dist_int_vs_markov_w0_dist_int | 10 | -12.48 [-16.68, -7.40] | 7.20 [2.83, 10.53] | 2 | 1 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
