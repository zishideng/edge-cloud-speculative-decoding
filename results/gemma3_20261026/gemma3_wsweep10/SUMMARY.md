# Progress probe: gemma3_wsweep10

State: complete; 50/50 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low; pooled = low.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | markov_w0_dist_int | 10 | 2490 | 30.360 | 0.2667 | 2 | 46.89 |
| all/low | markov_w025_dist_int | 10 | 2490 | 29.592 | 0.2587 | 2 | 44.98 |
| all/low | markov_w05_dist_int | 10 | 2510 | 29.182 | 0.2544 | 2 | 44.73 |
| all/low | markov_w1_dist_int | 10 | 2510 | 29.105 | 0.2516 | 2 | 43.39 |
| all/low | markov_w2_dist_int | 10 | 2490 | 28.718 | 0.2527 | 2 | 42.81 |
| all/pooled | markov_w0_dist_int | 10 | 2490 | 30.360 | 0.2667 | 2 | 46.89 |
| all/pooled | markov_w025_dist_int | 10 | 2490 | 29.592 | 0.2587 | 2 | 44.98 |
| all/pooled | markov_w05_dist_int | 10 | 2510 | 29.182 | 0.2544 | 2 | 44.73 |
| all/pooled | markov_w1_dist_int | 10 | 2510 | 29.105 | 0.2516 | 2 | 43.39 |
| all/pooled | markov_w2_dist_int | 10 | 2490 | 28.718 | 0.2527 | 2 | 42.81 |
| mtbench/low | markov_w0_dist_int | 3 | 973 | 22.480 | 0.3338 | 1 | 29.66 |
| mtbench/low | markov_w025_dist_int | 3 | 973 | 22.199 | 0.3233 | 1 | 25.30 |
| mtbench/low | markov_w05_dist_int | 3 | 973 | 22.119 | 0.3177 | 1 | 23.26 |
| mtbench/low | markov_w1_dist_int | 3 | 973 | 22.414 | 0.3078 | 1 | 23.32 |
| mtbench/low | markov_w2_dist_int | 3 | 973 | 22.360 | 0.3104 | 1 | 22.97 |
| mtbench/pooled | markov_w0_dist_int | 3 | 973 | 22.480 | 0.3338 | 1 | 29.66 |
| mtbench/pooled | markov_w025_dist_int | 3 | 973 | 22.199 | 0.3233 | 1 | 25.30 |
| mtbench/pooled | markov_w05_dist_int | 3 | 973 | 22.119 | 0.3177 | 1 | 23.26 |
| mtbench/pooled | markov_w1_dist_int | 3 | 973 | 22.414 | 0.3078 | 1 | 23.32 |
| mtbench/pooled | markov_w2_dist_int | 3 | 973 | 22.360 | 0.3104 | 1 | 22.97 |
| gsm8k/low | markov_w0_dist_int | 4 | 1016 | 34.741 | 0.2467 | 1 | 52.71 |
| gsm8k/low | markov_w025_dist_int | 4 | 1016 | 32.737 | 0.2389 | 1 | 51.52 |
| gsm8k/low | markov_w05_dist_int | 4 | 1036 | 31.848 | 0.2357 | 1 | 51.57 |
| gsm8k/low | markov_w1_dist_int | 4 | 1036 | 31.201 | 0.2365 | 1 | 49.54 |
| gsm8k/low | markov_w2_dist_int | 4 | 1016 | 30.508 | 0.2375 | 1 | 48.04 |
| gsm8k/pooled | markov_w0_dist_int | 4 | 1016 | 34.741 | 0.2467 | 1 | 52.71 |
| gsm8k/pooled | markov_w025_dist_int | 4 | 1016 | 32.737 | 0.2389 | 1 | 51.52 |
| gsm8k/pooled | markov_w05_dist_int | 4 | 1036 | 31.848 | 0.2357 | 1 | 51.57 |
| gsm8k/pooled | markov_w1_dist_int | 4 | 1036 | 31.201 | 0.2365 | 1 | 49.54 |
| gsm8k/pooled | markov_w2_dist_int | 4 | 1016 | 30.508 | 0.2375 | 1 | 48.04 |
| humaneval/low | markov_w0_dist_int | 3 | 501 | 52.806 | 0.1769 | 0 | 74.07 |
| humaneval/low | markov_w025_dist_int | 3 | 501 | 53.992 | 0.1734 | 0 | 73.15 |
| humaneval/low | markov_w05_dist_int | 3 | 501 | 52.777 | 0.1705 | 0 | 73.57 |
| humaneval/low | markov_w1_dist_int | 3 | 501 | 52.046 | 0.1734 | 0 | 72.69 |
| humaneval/low | markov_w2_dist_int | 3 | 501 | 50.672 | 0.1715 | 0 | 71.92 |
| humaneval/pooled | markov_w0_dist_int | 3 | 501 | 52.806 | 0.1769 | 0 | 74.07 |
| humaneval/pooled | markov_w025_dist_int | 3 | 501 | 53.992 | 0.1734 | 0 | 73.15 |
| humaneval/pooled | markov_w05_dist_int | 3 | 501 | 52.777 | 0.1705 | 0 | 73.57 |
| humaneval/pooled | markov_w1_dist_int | 3 | 501 | 52.046 | 0.1734 | 0 | 72.69 |
| humaneval/pooled | markov_w2_dist_int | 3 | 501 | 50.672 | 0.1715 | 0 | 71.92 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | markov_w025_dist_int_vs_markov_w0_dist_int | 10 | -2.53 [-6.63, -0.29] | 2.98 [-0.75, 4.72] | 1 | 0 |
| all/low | markov_w05_dist_int_vs_markov_w0_dist_int | 10 | -3.88 [-7.84, -0.76] | 4.59 [1.53, 6.56] | 2 | 0 |
| all/low | markov_w1_dist_int_vs_markov_w0_dist_int | 10 | -4.14 [-9.06, -0.90] | 5.67 [-0.16, 8.13] | 2 | 0 |
| all/low | markov_w2_dist_int_vs_markov_w0_dist_int | 10 | -5.41 [-11.38, -0.98] | 5.24 [1.31, 7.23] | 1 | 0 |
| all/pooled | markov_w025_dist_int_vs_markov_w0_dist_int | 10 | -2.53 [-6.63, -0.29] | 2.98 [-0.75, 4.72] | 1 | 0 |
| all/pooled | markov_w05_dist_int_vs_markov_w0_dist_int | 10 | -3.88 [-7.84, -0.76] | 4.59 [1.53, 6.56] | 2 | 0 |
| all/pooled | markov_w1_dist_int_vs_markov_w0_dist_int | 10 | -4.14 [-9.06, -0.90] | 5.67 [-0.16, 8.13] | 2 | 0 |
| all/pooled | markov_w2_dist_int_vs_markov_w0_dist_int | 10 | -5.41 [-11.38, -0.98] | 5.24 [1.31, 7.23] | 1 | 0 |
| mtbench/low | markov_w025_dist_int_vs_markov_w0_dist_int | 3 | -1.25 [-12.78, 0.08] | 3.12 [-13.85, 5.51] | 1 | 0 |
| mtbench/low | markov_w05_dist_int_vs_markov_w0_dist_int | 3 | -1.61 [-4.65, 0.25] | 4.82 [-2.05, 7.92] | 1 | 0 |
| mtbench/low | markov_w1_dist_int_vs_markov_w0_dist_int | 3 | -0.30 [-8.22, 0.52] | 7.77 [-4.96, 9.38] | 1 | 0 |
| mtbench/low | markov_w2_dist_int_vs_markov_w0_dist_int | 3 | -0.53 [-6.18, 1.09] | 7.00 [-3.36, 8.28] | 1 | 0 |
| mtbench/pooled | markov_w025_dist_int_vs_markov_w0_dist_int | 3 | -1.25 [-12.78, 0.08] | 3.12 [-13.85, 5.51] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_markov_w0_dist_int | 3 | -1.61 [-4.65, 0.25] | 4.82 [-2.05, 7.92] | 1 | 0 |
| mtbench/pooled | markov_w1_dist_int_vs_markov_w0_dist_int | 3 | -0.30 [-8.22, 0.52] | 7.77 [-4.96, 9.38] | 1 | 0 |
| mtbench/pooled | markov_w2_dist_int_vs_markov_w0_dist_int | 3 | -0.53 [-6.18, 1.09] | 7.00 [-3.36, 8.28] | 1 | 0 |
| gsm8k/low | markov_w025_dist_int_vs_markov_w0_dist_int | 4 | -5.77 [-11.95, -2.14] | 3.15 [-1.84, 5.52] | 0 | 0 |
| gsm8k/low | markov_w05_dist_int_vs_markov_w0_dist_int | 4 | -8.33 [-10.76, -3.06] | 4.47 [0.80, 6.37] | 1 | 0 |
| gsm8k/low | markov_w1_dist_int_vs_markov_w0_dist_int | 4 | -10.19 [-14.40, -8.51] | 4.13 [-9.15, 8.49] | 1 | 0 |
| gsm8k/low | markov_w2_dist_int_vs_markov_w0_dist_int | 4 | -12.18 [-15.99, -5.33] | 3.75 [-2.06, 7.52] | 0 | 0 |
| gsm8k/pooled | markov_w025_dist_int_vs_markov_w0_dist_int | 4 | -5.77 [-11.95, -2.14] | 3.15 [-1.84, 5.52] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_int_vs_markov_w0_dist_int | 4 | -8.33 [-10.76, -3.06] | 4.47 [0.80, 6.37] | 1 | 0 |
| gsm8k/pooled | markov_w1_dist_int_vs_markov_w0_dist_int | 4 | -10.19 [-14.40, -8.51] | 4.13 [-9.15, 8.49] | 1 | 0 |
| gsm8k/pooled | markov_w2_dist_int_vs_markov_w0_dist_int | 4 | -12.18 [-15.99, -5.33] | 3.75 [-2.06, 7.52] | 0 | 0 |
| humaneval/low | markov_w025_dist_int_vs_markov_w0_dist_int | 3 | 2.25 [-2.05, 10.05] | 1.99 [0.03, 2.59] | 0 | 0 |
| humaneval/low | markov_w05_dist_int_vs_markov_w0_dist_int | 3 | -0.05 [-3.28, 2.90] | 3.63 [1.64, 7.25] | 0 | 0 |
| humaneval/low | markov_w1_dist_int_vs_markov_w0_dist_int | 3 | -1.44 [-3.73, 0.92] | 1.98 [-7.93, 7.49] | 0 | 0 |
| humaneval/low | markov_w2_dist_int_vs_markov_w0_dist_int | 3 | -4.04 [-15.27, 4.46] | 3.03 [2.21, 4.24] | 0 | 0 |
| humaneval/pooled | markov_w025_dist_int_vs_markov_w0_dist_int | 3 | 2.25 [-2.05, 10.05] | 1.99 [0.03, 2.59] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_markov_w0_dist_int | 3 | -0.05 [-3.28, 2.90] | 3.63 [1.64, 7.25] | 0 | 0 |
| humaneval/pooled | markov_w1_dist_int_vs_markov_w0_dist_int | 3 | -1.44 [-3.73, 0.92] | 1.98 [-7.93, 7.49] | 0 | 0 |
| humaneval/pooled | markov_w2_dist_int_vs_markov_w0_dist_int | 3 | -4.04 [-15.27, 4.46] | 3.03 [2.21, 4.24] | 0 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
