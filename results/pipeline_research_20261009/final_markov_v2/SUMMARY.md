# Progress probe: final_markov_v2

State: complete; 108/108 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high; pooled = low+high. Run but not reported: very_high.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | fixed_fast | 12 | 2580 | 17.514 | 0.7355 | 1 | 40.40 |
| all/low | markov | 12 | 2580 | 18.603 | 0.6690 | 1 | 46.08 |
| all/low | markov_v2 | 12 | 2580 | 18.814 | 0.6722 | 1 | 44.21 |
| all/high | fixed_fast | 12 | 2580 | 12.919 | 0.8414 | 1 | 40.81 |
| all/high | markov | 12 | 2580 | 13.683 | 0.8513 | 1 | 44.10 |
| all/high | markov_v2 | 12 | 2540 | 13.407 | 0.8734 | 1 | 42.25 |
| all/pooled | fixed_fast | 24 | 5160 | 14.870 | 0.7885 | 2 | 40.61 |
| all/pooled | markov | 24 | 5160 | 15.768 | 0.7602 | 2 | 45.02 |
| all/pooled | markov_v2 | 24 | 5120 | 15.677 | 0.7720 | 2 | 43.13 |
| gsm8k/low | fixed_fast | 4 | 812 | 20.126 | 0.6529 | 0 | 46.89 |
| gsm8k/low | markov | 4 | 812 | 19.124 | 0.6353 | 0 | 52.15 |
| gsm8k/low | markov_v2 | 4 | 812 | 21.298 | 0.5945 | 0 | 49.50 |
| gsm8k/high | fixed_fast | 4 | 812 | 14.658 | 0.7489 | 0 | 47.53 |
| gsm8k/high | markov | 4 | 812 | 15.870 | 0.7643 | 0 | 50.00 |
| gsm8k/high | markov_v2 | 4 | 812 | 15.300 | 0.7898 | 0 | 48.10 |
| gsm8k/pooled | fixed_fast | 8 | 1624 | 16.962 | 0.7009 | 0 | 47.21 |
| gsm8k/pooled | markov | 8 | 1624 | 17.346 | 0.6998 | 0 | 50.99 |
| gsm8k/pooled | markov_v2 | 8 | 1624 | 17.808 | 0.6921 | 0 | 48.73 |
| mtbench/low | fixed_fast | 4 | 680 | 14.507 | 0.9143 | 0 | 24.23 |
| mtbench/low | markov | 4 | 680 | 16.417 | 0.7462 | 0 | 34.10 |
| mtbench/low | markov_v2 | 4 | 680 | 16.076 | 0.7634 | 0 | 32.72 |
| mtbench/high | fixed_fast | 4 | 680 | 11.099 | 1.0220 | 0 | 24.35 |
| mtbench/high | markov | 4 | 680 | 10.678 | 1.0090 | 0 | 30.11 |
| mtbench/high | markov_v2 | 4 | 640 | 10.158 | 1.0637 | 0 | 27.35 |
| mtbench/pooled | fixed_fast | 8 | 1360 | 12.576 | 0.9682 | 0 | 24.29 |
| mtbench/pooled | markov | 8 | 1360 | 12.940 | 0.8776 | 0 | 31.99 |
| mtbench/pooled | markov_v2 | 8 | 1320 | 12.535 | 0.9090 | 0 | 29.83 |
| humaneval/low | fixed_fast | 4 | 1088 | 18.106 | 0.6855 | 1 | 47.93 |
| humaneval/low | markov | 4 | 1088 | 19.851 | 0.6460 | 1 | 49.33 |
| humaneval/low | markov_v2 | 4 | 1088 | 19.185 | 0.6733 | 1 | 47.72 |
| humaneval/high | fixed_fast | 4 | 1088 | 13.101 | 0.7975 | 1 | 48.39 |
| humaneval/high | markov | 4 | 1088 | 14.759 | 0.8178 | 1 | 48.47 |
| humaneval/high | markov_v2 | 4 | 1088 | 14.828 | 0.8239 | 1 | 46.93 |
| humaneval/pooled | fixed_fast | 8 | 2176 | 15.202 | 0.7415 | 2 | 48.16 |
| humaneval/pooled | markov | 8 | 2176 | 16.930 | 0.7319 | 2 | 48.87 |
| humaneval/pooled | markov_v2 | 8 | 2176 | 16.728 | 0.7486 | 2 | 47.28 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | markov | 12 | 6.22 [-2.88, 14.36] | 9.04 [2.91, 17.07] | 0 | 0 |
| all/low | markov_v2 | 12 | 7.42 [3.52, 11.74] | 8.60 [3.28, 15.06] | 0 | 0 |
| all/high | markov | 12 | 5.91 [-0.04, 11.30] | -1.18 [-3.72, 1.97] | 0 | 0 |
| all/high | markov_v2 | 12 | 3.78 [-3.97, 10.41] | -3.80 [-9.37, 1.31] | 1 | 0 |
| all/pooled | markov | 12 | 6.04 [1.12, 10.70] | 3.59 [-0.56, 8.97] | 0 | 0 |
| all/pooled | markov_v2 | 12 | 5.43 [0.39, 9.48] | 2.08 [-2.21, 7.37] | 1 | 0 |
| gsm8k/low | markov | 4 | -4.98 [-21.07, 11.15] | 2.69 [-8.60, 10.85] | 0 | 0 |
| gsm8k/low | markov_v2 | 4 | 5.82 [-7.77, 13.28] | 8.94 [-0.33, 14.24] | 0 | 0 |
| gsm8k/high | markov | 4 | 8.27 [4.82, 12.28] | -2.05 [-7.39, 1.45] | 0 | 0 |
| gsm8k/high | markov_v2 | 4 | 4.39 [-0.77, 9.89] | -5.45 [-11.43, -2.75] | 0 | 0 |
| gsm8k/pooled | markov | 4 | 2.26 [-5.31, 8.40] | 0.15 [-7.97, 5.71] | 0 | 0 |
| gsm8k/pooled | markov_v2 | 4 | 4.99 [-3.76, 11.30] | 1.25 [-6.35, 4.15] | 0 | 0 |
| mtbench/low | markov | 4 | 13.17 [2.04, 28.33] | 18.38 [7.88, 29.82] | 0 | 0 |
| mtbench/low | markov_v2 | 4 | 10.82 [3.32, 23.12] | 16.51 [8.08, 26.14] | 0 | 0 |
| mtbench/high | markov | 4 | -3.79 [-7.90, 3.12] | 1.28 [-3.50, 7.57] | 0 | 0 |
| mtbench/high | markov_v2 | 4 | -8.49 [-14.39, -1.51] | -4.08 [-17.58, 10.86] | 1 | 0 |
| mtbench/pooled | markov | 4 | 2.89 [-3.85, 11.50] | 9.35 [2.04, 18.34] | 0 | 0 |
| mtbench/pooled | markov_v2 | 4 | -0.33 [-5.88, 7.24] | 6.11 [-4.59, 18.24] | 1 | 0 |
| humaneval/low | markov | 4 | 9.64 [7.77, 13.36] | 5.77 [-0.01, 14.00] | 0 | 0 |
| humaneval/low | markov_v2 | 4 | 5.96 [5.66, 7.23] | 1.78 [-2.04, 8.88] | 0 | 0 |
| humaneval/high | markov | 4 | 12.65 [10.20, 20.22] | -2.54 [-5.09, 2.78] | 0 | 0 |
| humaneval/high | markov_v2 | 4 | 13.18 [5.03, 20.58] | -3.31 [-5.93, 1.93] | 0 | 0 |
| humaneval/pooled | markov | 4 | 11.37 [9.35, 16.77] | 1.30 [-2.39, 7.26] | 0 | 0 |
| humaneval/pooled | markov_v2 | 4 | 10.04 [5.68, 14.12] | -0.96 [-3.78, 4.92] | 0 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
