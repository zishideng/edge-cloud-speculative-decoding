# Progress probe: confirm_markov

State: complete; 108/108 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high; pooled = low+high. Run but not reported: very_high.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | fixed_fast | 9 | 2650 | 15.795 | 0.7951 | 1 | 36.15 |
| all/low | regime_short | 9 | 2650 | 16.272 | 0.7368 | 1 | 38.41 |
| all/low | markov | 9 | 2650 | 16.640 | 0.7292 | 1 | 43.15 |
| all/low | markov_w05 | 9 | 2650 | 16.199 | 0.7125 | 1 | 43.28 |
| all/high | fixed_fast | 9 | 2650 | 11.702 | 0.9024 | 1 | 36.31 |
| all/high | regime_short | 9 | 2650 | 11.634 | 0.9207 | 1 | 37.06 |
| all/high | markov | 9 | 2673 | 12.226 | 0.9041 | 1 | 42.08 |
| all/high | markov_w05 | 9 | 2650 | 11.491 | 0.8704 | 1 | 42.57 |
| all/pooled | fixed_fast | 18 | 5300 | 13.444 | 0.8487 | 2 | 36.23 |
| all/pooled | regime_short | 18 | 5300 | 13.567 | 0.8288 | 2 | 37.72 |
| all/pooled | markov | 18 | 5323 | 14.086 | 0.8170 | 2 | 42.58 |
| all/pooled | markov_w05 | 18 | 5300 | 13.445 | 0.7914 | 2 | 42.93 |
| mtbench/low | fixed_fast | 3 | 1185 | 12.357 | 1.0136 | 1 | 23.43 |
| mtbench/low | regime_short | 3 | 1185 | 13.302 | 0.8872 | 1 | 28.05 |
| mtbench/low | markov | 3 | 1185 | 13.667 | 0.8649 | 1 | 33.39 |
| mtbench/low | markov_w05 | 3 | 1185 | 13.211 | 0.8252 | 1 | 32.51 |
| mtbench/high | fixed_fast | 3 | 1185 | 9.713 | 1.1154 | 1 | 23.70 |
| mtbench/high | regime_short | 3 | 1185 | 9.263 | 1.1439 | 1 | 25.32 |
| mtbench/high | markov | 3 | 1208 | 9.520 | 1.0813 | 1 | 30.61 |
| mtbench/high | markov_w05 | 3 | 1185 | 8.850 | 1.0253 | 1 | 26.34 |
| mtbench/pooled | fixed_fast | 6 | 2370 | 10.877 | 1.0645 | 2 | 23.57 |
| mtbench/pooled | regime_short | 6 | 2370 | 10.921 | 1.0156 | 2 | 26.63 |
| mtbench/pooled | markov | 6 | 2393 | 11.204 | 0.9741 | 2 | 31.94 |
| mtbench/pooled | markov_w05 | 6 | 2370 | 10.599 | 0.9253 | 2 | 29.75 |
| gsm8k/low | fixed_fast | 3 | 433 | 24.323 | 0.5524 | 0 | 52.71 |
| gsm8k/low | regime_short | 3 | 433 | 23.128 | 0.5448 | 0 | 51.48 |
| gsm8k/low | markov | 3 | 433 | 20.970 | 0.5855 | 0 | 51.47 |
| gsm8k/low | markov_w05 | 3 | 433 | 22.969 | 0.5534 | 0 | 54.15 |
| gsm8k/high | fixed_fast | 3 | 433 | 17.128 | 0.6551 | 0 | 52.71 |
| gsm8k/high | regime_short | 3 | 433 | 16.773 | 0.6637 | 0 | 52.71 |
| gsm8k/high | markov | 3 | 433 | 18.642 | 0.6784 | 0 | 52.63 |
| gsm8k/high | markov_w05 | 3 | 433 | 17.019 | 0.6833 | 0 | 55.12 |
| gsm8k/pooled | fixed_fast | 6 | 866 | 20.101 | 0.6037 | 0 | 52.71 |
| gsm8k/pooled | regime_short | 6 | 866 | 19.445 | 0.6043 | 0 | 52.10 |
| gsm8k/pooled | markov | 6 | 866 | 19.738 | 0.6320 | 0 | 52.09 |
| gsm8k/pooled | markov_w05 | 6 | 866 | 19.551 | 0.6184 | 0 | 54.66 |
| humaneval/low | fixed_fast | 3 | 1032 | 19.083 | 0.6460 | 0 | 48.97 |
| humaneval/low | regime_short | 3 | 1032 | 18.746 | 0.6447 | 0 | 47.44 |
| humaneval/low | markov | 3 | 1032 | 19.885 | 0.6337 | 0 | 52.85 |
| humaneval/low | markov_w05 | 3 | 1032 | 18.752 | 0.6499 | 0 | 51.86 |
| humaneval/high | fixed_fast | 3 | 1032 | 13.035 | 0.7617 | 0 | 48.97 |
| humaneval/high | regime_short | 3 | 1032 | 13.936 | 0.7722 | 0 | 47.63 |
| humaneval/high | markov | 3 | 1032 | 15.062 | 0.7914 | 0 | 51.89 |
| humaneval/high | markov_w05 | 3 | 1032 | 14.479 | 0.7709 | 0 | 51.79 |
| humaneval/pooled | fixed_fast | 6 | 2064 | 15.489 | 0.7038 | 0 | 48.97 |
| humaneval/pooled | regime_short | 6 | 2064 | 15.987 | 0.7085 | 0 | 47.54 |
| humaneval/pooled | markov | 6 | 2064 | 17.141 | 0.7126 | 0 | 52.33 |
| humaneval/pooled | markov_w05 | 6 | 2064 | 16.341 | 0.7104 | 0 | 51.82 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | regime_short | 9 | 3.02 [-2.04, 6.99] | 7.33 [1.65, 11.59] | 0 | 0 |
| all/low | markov | 9 | 5.35 [-2.38, 11.04] | 8.28 [0.18, 14.73] | 0 | 0 |
| all/low | markov_w05 | 9 | 2.56 [-2.54, 6.36] | 10.38 [1.64, 16.62] | 0 | 0 |
| all/high | regime_short | 9 | -0.58 [-6.19, 6.15] | -2.02 [-10.36, 3.47] | 0 | 0 |
| all/high | markov | 9 | 4.48 [-1.02, 13.19] | -0.18 [-3.57, 2.02] | 1 | 0 |
| all/high | markov_w05 | 9 | -1.81 [-8.45, 7.93] | 3.56 [-1.04, 6.70] | 0 | 0 |
| all/pooled | regime_short | 9 | 0.92 [-2.42, 4.06] | 2.36 [-2.92, 6.69] | 0 | 0 |
| all/pooled | markov | 9 | 4.78 [1.18, 9.27] | 3.74 [-1.50, 7.63] | 1 | 0 |
| all/pooled | markov_w05 | 9 | 0.01 [-3.41, 4.54] | 6.75 [0.24, 11.24] | 0 | 0 |
| mtbench/low | regime_short | 3 | 7.65 [4.38, 14.08] | 12.46 [10.15, 17.63] | 0 | 0 |
| mtbench/low | markov | 3 | 10.60 [5.75, 24.15] | 14.67 [8.53, 24.09] | 0 | 0 |
| mtbench/low | markov_w05 | 3 | 6.91 [3.90, 13.00] | 18.59 [15.26, 23.30] | 0 | 0 |
| mtbench/high | regime_short | 3 | -4.63 [-8.69, 0.84] | -2.55 [-22.02, 7.00] | 0 | 0 |
| mtbench/high | markov | 3 | -1.98 [-3.68, -0.54] | 3.06 [1.66, 4.76] | 1 | 0 |
| mtbench/high | markov_w05 | 3 | -8.89 [-13.04, -5.78] | 8.07 [5.47, 10.56] | 0 | 0 |
| mtbench/pooled | regime_short | 3 | 0.41 [-3.18, 3.18] | 4.60 [-6.58, 12.01] | 0 | 0 |
| mtbench/pooled | markov | 3 | 3.01 [0.17, 6.73] | 8.49 [5.62, 13.38] | 1 | 0 |
| mtbench/pooled | markov_w05 | 3 | -2.55 [-5.62, -0.53] | 13.08 [11.55, 16.57] | 0 | 0 |
| gsm8k/low | regime_short | 3 | -4.91 [-13.95, 4.48] | 1.37 [-8.88, 11.12] | 0 | 0 |
| gsm8k/low | markov | 3 | -13.79 [-19.44, -2.93] | -6.00 [-10.28, 6.87] | 0 | 0 |
| gsm8k/low | markov_w05 | 3 | -5.57 [-9.13, 6.55] | -0.19 [-4.39, 11.67] | 0 | 0 |
| gsm8k/high | regime_short | 3 | -2.07 [-2.98, -0.59] | -1.32 [-2.76, -0.12] | 0 | 0 |
| gsm8k/high | markov | 3 | 8.84 [0.87, 12.52] | -3.56 [-7.07, -2.18] | 0 | 0 |
| gsm8k/high | markov_w05 | 3 | -0.63 [-9.59, 2.89] | -4.31 [-10.99, 0.94] | 0 | 0 |
| gsm8k/pooled | regime_short | 3 | -3.27 [-7.27, 1.43] | -0.09 [-5.22, 3.54] | 0 | 0 |
| gsm8k/pooled | markov | 3 | -1.81 [-4.85, 4.80] | -4.68 [-8.51, 1.78] | 0 | 0 |
| gsm8k/pooled | markov_w05 | 3 | -2.73 [-3.61, -2.43] | -2.42 [-3.83, -0.71] | 0 | 0 |
| humaneval/low | regime_short | 3 | -1.77 [-4.98, 0.21] | 0.20 [-1.57, 2.31] | 0 | 0 |
| humaneval/low | markov | 3 | 4.20 [-0.59, 8.62] | 1.90 [-5.29, 15.06] | 0 | 0 |
| humaneval/low | markov_w05 | 3 | -1.74 [-5.87, 0.88] | -0.60 [-5.13, 7.53] | 0 | 0 |
| humaneval/high | regime_short | 3 | 6.92 [-4.36, 18.16] | -1.39 [-3.30, 0.20] | 0 | 0 |
| humaneval/high | markov | 3 | 15.55 [2.57, 26.60] | -3.91 [-6.57, -1.48] | 0 | 0 |
| humaneval/high | markov_w05 | 3 | 11.08 [-3.92, 23.22] | -1.20 [-1.63, -0.93] | 0 | 0 |
| humaneval/pooled | regime_short | 3 | 3.21 [-2.49, 10.08] | -0.66 [-1.84, 0.37] | 0 | 0 |
| humaneval/pooled | markov | 3 | 10.66 [5.03, 17.50] | -1.24 [-6.00, 4.53] | 0 | 0 |
| humaneval/pooled | markov_w05 | 3 | 5.50 [-2.31, 13.13] | -0.93 [-3.20, 2.90] | 0 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
