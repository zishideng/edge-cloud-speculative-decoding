# Progress probe: gemma3_int15

State: complete; 120/120 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: high, dynamic; pooled = high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/high | markov_w0_dist | 15 | 3714 | 16.360 | 0.4637 | 2 | 30.66 |
| all/high | markov_w0_dist_int | 15 | 3714 | 16.384 | 0.4690 | 2 | 30.21 |
| all/high | markov_w05_dist | 15 | 3714 | 14.517 | 0.4333 | 2 | 37.39 |
| all/high | markov_w05_dist_int | 15 | 3714 | 14.817 | 0.4275 | 2 | 39.01 |
| all/dynamic | markov_w0_dist | 15 | 3686 | 20.631 | 0.3560 | 2 | 33.68 |
| all/dynamic | markov_w0_dist_int | 15 | 3673 | 21.513 | 0.3654 | 2 | 37.98 |
| all/dynamic | markov_w05_dist | 15 | 3686 | 19.931 | 0.3317 | 2 | 38.80 |
| all/dynamic | markov_w05_dist_int | 15 | 3673 | 20.519 | 0.3328 | 2 | 42.16 |
| all/pooled | markov_w0_dist | 30 | 7400 | 18.241 | 0.4100 | 4 | 31.93 |
| all/pooled | markov_w0_dist_int | 30 | 7387 | 18.587 | 0.4175 | 4 | 33.44 |
| all/pooled | markov_w05_dist | 30 | 7400 | 16.789 | 0.3827 | 4 | 38.10 |
| all/pooled | markov_w05_dist_int | 30 | 7387 | 17.192 | 0.3804 | 4 | 40.57 |
| humaneval/high | markov_w0_dist | 5 | 855 | 38.010 | 0.2020 | 0 | 72.27 |
| humaneval/high | markov_w0_dist_int | 5 | 855 | 38.044 | 0.2021 | 0 | 72.70 |
| humaneval/high | markov_w05_dist | 5 | 855 | 35.390 | 0.2105 | 0 | 71.26 |
| humaneval/high | markov_w05_dist_int | 5 | 855 | 36.246 | 0.2066 | 0 | 71.66 |
| humaneval/dynamic | markov_w0_dist | 5 | 855 | 42.588 | 0.1935 | 0 | 70.34 |
| humaneval/dynamic | markov_w0_dist_int | 5 | 855 | 43.664 | 0.1861 | 0 | 72.37 |
| humaneval/dynamic | markov_w05_dist | 5 | 855 | 36.841 | 0.2034 | 0 | 68.08 |
| humaneval/dynamic | markov_w05_dist_int | 5 | 855 | 40.438 | 0.1982 | 0 | 70.51 |
| humaneval/pooled | markov_w0_dist | 10 | 1710 | 40.169 | 0.1978 | 0 | 71.30 |
| humaneval/pooled | markov_w0_dist_int | 10 | 1710 | 40.660 | 0.1941 | 0 | 72.54 |
| humaneval/pooled | markov_w05_dist | 10 | 1710 | 36.101 | 0.2070 | 0 | 69.66 |
| humaneval/pooled | markov_w05_dist_int | 10 | 1710 | 38.227 | 0.2024 | 0 | 71.09 |
| gsm8k/high | markov_w0_dist | 5 | 1387 | 20.602 | 0.3772 | 1 | 42.15 |
| gsm8k/high | markov_w0_dist_int | 5 | 1387 | 20.837 | 0.3775 | 1 | 42.33 |
| gsm8k/high | markov_w05_dist | 5 | 1387 | 17.195 | 0.3821 | 1 | 38.50 |
| gsm8k/high | markov_w05_dist_int | 5 | 1387 | 17.680 | 0.3742 | 1 | 43.94 |
| gsm8k/dynamic | markov_w0_dist | 5 | 1369 | 24.691 | 0.3121 | 1 | 39.59 |
| gsm8k/dynamic | markov_w0_dist_int | 5 | 1369 | 25.594 | 0.3169 | 1 | 47.22 |
| gsm8k/dynamic | markov_w05_dist | 5 | 1369 | 22.591 | 0.2994 | 1 | 43.14 |
| gsm8k/dynamic | markov_w05_dist_int | 5 | 1369 | 23.963 | 0.2977 | 1 | 48.54 |
| gsm8k/pooled | markov_w0_dist | 10 | 2756 | 22.449 | 0.3449 | 2 | 41.07 |
| gsm8k/pooled | markov_w0_dist_int | 10 | 2756 | 22.956 | 0.3474 | 2 | 44.45 |
| gsm8k/pooled | markov_w05_dist | 10 | 2756 | 19.509 | 0.3410 | 2 | 40.86 |
| gsm8k/pooled | markov_w05_dist_int | 10 | 2756 | 20.328 | 0.3362 | 2 | 46.19 |
| mtbench/high | markov_w0_dist | 5 | 1472 | 10.729 | 0.6971 | 1 | 13.85 |
| mtbench/high | markov_w0_dist_int | 5 | 1472 | 10.694 | 0.7103 | 1 | 14.27 |
| mtbench/high | markov_w05_dist | 5 | 1472 | 9.748 | 0.6109 | 1 | 15.97 |
| mtbench/high | markov_w05_dist_int | 5 | 1472 | 9.904 | 0.6060 | 1 | 13.37 |
| mtbench/dynamic | markov_w0_dist | 5 | 1462 | 14.175 | 0.4922 | 1 | 16.30 |
| mtbench/dynamic | markov_w0_dist_int | 5 | 1449 | 14.836 | 0.5170 | 1 | 20.37 |
| mtbench/dynamic | markov_w05_dist | 5 | 1462 | 14.457 | 0.4371 | 1 | 16.72 |
| mtbench/dynamic | markov_w05_dist_int | 5 | 1449 | 14.384 | 0.4455 | 1 | 18.13 |
| mtbench/pooled | markov_w0_dist | 10 | 2934 | 12.208 | 0.5950 | 2 | 14.81 |
| mtbench/pooled | markov_w0_dist_int | 10 | 2921 | 12.413 | 0.6144 | 2 | 16.63 |
| mtbench/pooled | markov_w05_dist | 10 | 2934 | 11.637 | 0.5243 | 2 | 16.34 |
| mtbench/pooled | markov_w05_dist_int | 10 | 2921 | 11.714 | 0.5264 | 2 | 15.75 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/high | markov_w0_dist_int_vs_markov_w0_dist | 15 | 0.15 [-1.51, 2.13] | -1.15 [-3.56, 0.79] | 0 | 0 |
| all/high | markov_w05_dist_vs_markov_w0_dist | 15 | -11.26 [-14.49, -8.20] | 6.55 [1.18, 10.32] | 0 | 0 |
| all/high | markov_w05_dist_int_vs_markov_w0_dist | 15 | -9.43 [-12.13, -6.66] | 7.80 [3.04, 11.20] | 0 | 0 |
| all/high | markov_w0_dist_vs_markov_w05_dist | 15 | 12.69 [8.94, 16.94] | -7.01 [-11.51, -1.19] | 0 | 0 |
| all/high | markov_w0_dist_int_vs_markov_w05_dist | 15 | 12.86 [9.41, 16.87] | -8.25 [-13.15, -1.51] | 0 | 0 |
| all/high | markov_w05_dist_int_vs_markov_w05_dist | 15 | 2.07 [-0.10, 4.76] | 1.33 [0.06, 2.96] | 0 | 0 |
| all/dynamic | markov_w0_dist_int_vs_markov_w0_dist | 15 | 4.27 [2.29, 6.49] | -2.64 [-4.73, 0.46] | 2 | 0 |
| all/dynamic | markov_w05_dist_vs_markov_w0_dist | 15 | -3.39 [-8.14, 0.55] | 6.82 [2.88, 9.73] | 1 | 0 |
| all/dynamic | markov_w05_dist_int_vs_markov_w0_dist | 15 | -0.55 [-3.80, 1.75] | 6.51 [3.53, 8.39] | 1 | 0 |
| all/dynamic | markov_w0_dist_vs_markov_w05_dist | 15 | 3.51 [-0.55, 8.86] | -7.31 [-10.78, -2.96] | 1 | 0 |
| all/dynamic | markov_w0_dist_int_vs_markov_w05_dist | 15 | 7.93 [4.57, 12.57] | -10.14 [-14.39, -3.50] | 2 | 0 |
| all/dynamic | markov_w05_dist_int_vs_markov_w05_dist | 15 | 2.95 [0.28, 6.19] | -0.33 [-2.50, 1.13] | 2 | 0 |
| all/pooled | markov_w0_dist_int_vs_markov_w0_dist | 15 | 1.90 [0.99, 2.82] | -1.82 [-3.95, 0.47] | 2 | 0 |
| all/pooled | markov_w05_dist_vs_markov_w0_dist | 15 | -7.96 [-11.15, -5.57] | 6.67 [2.28, 9.87] | 1 | 0 |
| all/pooled | markov_w05_dist_int_vs_markov_w0_dist | 15 | -5.75 [-7.76, -4.09] | 7.22 [3.46, 9.67] | 1 | 0 |
| all/pooled | markov_w0_dist_vs_markov_w05_dist | 15 | 8.65 [5.90, 12.54] | -7.14 [-10.95, -2.33] | 1 | 0 |
| all/pooled | markov_w0_dist_int_vs_markov_w05_dist | 15 | 10.71 [7.78, 14.62] | -9.09 [-13.56, -2.79] | 2 | 0 |
| all/pooled | markov_w05_dist_int_vs_markov_w05_dist | 15 | 2.40 [1.06, 4.32] | 0.59 [-0.68, 1.90] | 2 | 0 |
| humaneval/high | markov_w0_dist_int_vs_markov_w0_dist | 5 | 0.09 [-2.87, 2.93] | -0.02 [-3.48, 2.34] | 0 | 0 |
| humaneval/high | markov_w05_dist_vs_markov_w0_dist | 5 | -6.89 [-10.14, -4.27] | -4.20 [-7.04, -2.28] | 0 | 0 |
| humaneval/high | markov_w05_dist_int_vs_markov_w0_dist | 5 | -4.64 [-8.96, -1.42] | -2.25 [-5.53, -0.02] | 0 | 0 |
| humaneval/high | markov_w0_dist_vs_markov_w05_dist | 5 | 7.40 [4.46, 11.28] | 4.03 [2.22, 6.57] | 0 | 0 |
| humaneval/high | markov_w0_dist_int_vs_markov_w05_dist | 5 | 7.50 [5.27, 10.33] | 4.01 [2.73, 6.39] | 0 | 0 |
| humaneval/high | markov_w05_dist_int_vs_markov_w05_dist | 5 | 2.42 [0.30, 4.46] | 1.87 [-0.01, 3.76] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_markov_w0_dist | 5 | 2.53 [-0.92, 7.35] | 3.82 [0.95, 7.16] | 0 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_markov_w0_dist | 5 | -13.50 [-24.68, -3.36] | -5.12 [-9.94, -1.06] | 0 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_markov_w0_dist | 5 | -5.05 [-11.91, 1.61] | -2.41 [-6.96, 1.74] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_markov_w05_dist | 5 | 15.60 [3.47, 32.77] | 4.87 [1.05, 9.04] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_markov_w05_dist | 5 | 18.52 [5.01, 36.48] | 8.51 [4.41, 14.95] | 0 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_markov_w05_dist | 5 | 9.77 [3.52, 17.83] | 2.58 [1.16, 4.08] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_markov_w0_dist | 5 | 1.22 [-1.94, 3.42] | 1.86 [-0.37, 4.05] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_vs_markov_w0_dist | 5 | -10.13 [-16.52, -4.25] | -4.65 [-7.91, -2.51] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_markov_w0_dist | 5 | -4.83 [-10.29, -0.91] | -2.33 [-5.85, 0.62] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_vs_markov_w05_dist | 5 | 11.27 [4.44, 19.79] | 4.45 [2.45, 7.33] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_markov_w05_dist | 5 | 12.63 [7.32, 18.80] | 6.22 [3.77, 9.30] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_markov_w05_dist | 5 | 5.89 [3.13, 8.64] | 2.22 [1.72, 3.21] | 0 | 0 |
| gsm8k/high | markov_w0_dist_int_vs_markov_w0_dist | 5 | 1.14 [-1.23, 2.38] | -0.09 [-1.17, 0.77] | 0 | 0 |
| gsm8k/high | markov_w05_dist_vs_markov_w0_dist | 5 | -16.54 [-20.54, -12.86] | -1.29 [-6.00, 1.35] | 0 | 0 |
| gsm8k/high | markov_w05_dist_int_vs_markov_w0_dist | 5 | -14.18 [-17.64, -10.76] | 0.79 [-1.70, 2.62] | 0 | 0 |
| gsm8k/high | markov_w0_dist_vs_markov_w05_dist | 5 | 19.82 [14.75, 25.85] | 1.28 [-1.37, 5.66] | 0 | 0 |
| gsm8k/high | markov_w0_dist_int_vs_markov_w05_dist | 5 | 21.18 [16.92, 26.54] | 1.19 [-0.86, 4.79] | 0 | 0 |
| gsm8k/high | markov_w05_dist_int_vs_markov_w05_dist | 5 | 2.83 [-2.35, 10.61] | 2.05 [-1.33, 6.17] | 0 | 0 |
| gsm8k/dynamic | markov_w0_dist_int_vs_markov_w0_dist | 5 | 3.66 [1.51, 7.71] | -1.54 [-3.97, 3.68] | 0 | 0 |
| gsm8k/dynamic | markov_w05_dist_vs_markov_w0_dist | 5 | -8.50 [-12.15, -4.35] | 4.06 [2.96, 4.80] | 0 | 0 |
| gsm8k/dynamic | markov_w05_dist_int_vs_markov_w0_dist | 5 | -2.95 [-8.77, 2.11] | 4.61 [2.27, 6.00] | 0 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_markov_w05_dist | 5 | 9.30 [4.55, 13.82] | -4.24 [-5.05, -3.05] | 0 | 0 |
| gsm8k/dynamic | markov_w0_dist_int_vs_markov_w05_dist | 5 | 13.29 [10.38, 16.41] | -5.84 [-9.22, 0.40] | 0 | 0 |
| gsm8k/dynamic | markov_w05_dist_int_vs_markov_w05_dist | 5 | 6.08 [2.55, 9.03] | 0.57 [-0.84, 1.52] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_int_vs_markov_w0_dist | 5 | 2.26 [1.34, 3.82] | -0.74 [-1.63, 1.51] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_markov_w0_dist | 5 | -13.09 [-16.38, -10.02] | 1.12 [-1.17, 2.56] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_int_vs_markov_w0_dist | 5 | -9.45 [-11.17, -7.94] | 2.50 [0.71, 3.51] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_markov_w05_dist | 5 | 15.07 [11.13, 19.59] | -1.13 [-2.63, 1.15] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_int_vs_markov_w05_dist | 5 | 17.67 [14.09, 21.67] | -1.88 [-4.03, 1.92] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_int_vs_markov_w05_dist | 5 | 4.20 [1.67, 7.37] | 1.40 [-0.68, 3.64] | 0 | 0 |
| mtbench/high | markov_w0_dist_int_vs_markov_w0_dist | 5 | -0.33 [-2.48, 3.16] | -1.89 [-5.32, 1.23] | 0 | 0 |
| mtbench/high | markov_w05_dist_vs_markov_w0_dist | 5 | -9.14 [-12.35, -4.54] | 12.37 [9.22, 15.64] | 0 | 0 |
| mtbench/high | markov_w05_dist_int_vs_markov_w0_dist | 5 | -7.68 [-10.32, -3.32] | 13.07 [10.29, 15.93] | 0 | 0 |
| mtbench/high | markov_w0_dist_vs_markov_w05_dist | 5 | 10.06 [4.75, 14.09] | -14.11 [-18.55, -10.16] | 0 | 0 |
| mtbench/high | markov_w0_dist_int_vs_markov_w05_dist | 5 | 9.71 [5.91, 11.82] | -16.26 [-18.52, -12.92] | 0 | 0 |
| mtbench/high | markov_w05_dist_int_vs_markov_w05_dist | 5 | 1.61 [0.52, 2.52] | 0.80 [0.16, 1.58] | 0 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_markov_w0_dist | 5 | 4.67 [0.51, 7.86] | -5.05 [-7.38, -1.65] | 2 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_markov_w0_dist | 5 | 1.99 [-1.46, 6.33] | 11.19 [8.47, 14.34] | 1 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_markov_w0_dist | 5 | 1.48 [-1.03, 3.19] | 9.48 [7.36, 10.62] | 1 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_markov_w05_dist | 5 | -1.95 [-5.96, 1.48] | -12.61 [-16.74, -9.25] | 1 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_markov_w05_dist | 5 | 2.62 [-0.03, 4.95] | -18.29 [-19.05, -15.81] | 2 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_markov_w05_dist | 5 | -0.51 [-3.28, 1.63] | -1.93 [-5.51, 0.50] | 2 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_markov_w0_dist | 5 | 1.68 [-0.08, 3.13] | -3.26 [-6.13, -0.07] | 2 | 0 |
| mtbench/pooled | markov_w05_dist_vs_markov_w0_dist | 5 | -4.68 [-6.51, -2.37] | 11.88 [9.29, 14.57] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_markov_w0_dist | 5 | -4.04 [-5.28, -1.79] | 11.53 [10.10, 12.88] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_vs_markov_w05_dist | 5 | 4.91 [2.43, 6.96] | -13.49 [-17.05, -10.24] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_markov_w05_dist | 5 | 6.67 [3.34, 8.70] | -17.19 [-18.81, -14.54] | 2 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_markov_w05_dist | 5 | 0.67 [-0.67, 1.80] | -0.40 [-2.17, 0.97] | 2 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
