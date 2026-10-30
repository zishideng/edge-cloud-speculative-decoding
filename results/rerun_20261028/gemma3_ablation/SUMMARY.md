# Progress probe: gemma3_ablation

State: complete; 360/360 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | picospec | 30 | 8213 | 29.290 | 0.3324 | 6 | 32.94 |
| all/low | markov_w0_fresh4_int | 30 | 8213 | 28.945 | 0.3408 | 6 | 34.62 |
| all/low | markov_w0_dist_int | 30 | 8192 | 28.357 | 0.2850 | 6 | 44.10 |
| all/low | markov_w0_int | 30 | 8230 | 28.034 | 0.2766 | 6 | 41.78 |
| all/high | picospec | 30 | 8296 | 14.008 | 0.4759 | 6 | 26.42 |
| all/high | markov_w0_fresh4_int | 30 | 8296 | 15.933 | 0.4949 | 6 | 23.06 |
| all/high | markov_w0_dist_int | 30 | 8252 | 15.881 | 0.4891 | 6 | 28.48 |
| all/high | markov_w0_int | 30 | 8237 | 16.032 | 0.4951 | 6 | 28.51 |
| all/dynamic | picospec | 30 | 8326 | 19.566 | 0.3869 | 7 | 31.42 |
| all/dynamic | markov_w0_fresh4_int | 30 | 8326 | 20.863 | 0.4018 | 7 | 30.15 |
| all/dynamic | markov_w0_dist_int | 30 | 8127 | 21.132 | 0.3705 | 5 | 37.83 |
| all/dynamic | markov_w0_int | 30 | 8141 | 21.127 | 0.3645 | 5 | 36.16 |
| all/pooled | picospec | 90 | 24835 | 19.131 | 0.3986 | 19 | 30.00 |
| all/pooled | markov_w0_fresh4_int | 90 | 24835 | 20.636 | 0.4127 | 19 | 28.09 |
| all/pooled | markov_w0_dist_int | 90 | 24571 | 20.594 | 0.3818 | 17 | 35.01 |
| all/pooled | markov_w0_int | 90 | 24608 | 20.632 | 0.3788 | 17 | 33.95 |
| mtbench/low | picospec | 10 | 3222 | 20.432 | 0.4866 | 3 | 11.81 |
| mtbench/low | markov_w0_fresh4_int | 10 | 3222 | 19.857 | 0.4949 | 3 | 12.51 |
| mtbench/low | markov_w0_dist_int | 10 | 3220 | 19.913 | 0.3730 | 3 | 24.39 |
| mtbench/low | markov_w0_int | 10 | 3239 | 20.437 | 0.3691 | 3 | 24.32 |
| mtbench/high | picospec | 10 | 3239 | 9.813 | 0.6858 | 3 | 8.86 |
| mtbench/high | markov_w0_fresh4_int | 10 | 3239 | 10.460 | 0.7535 | 3 | 8.81 |
| mtbench/high | markov_w0_dist_int | 10 | 3195 | 10.512 | 0.7289 | 3 | 14.27 |
| mtbench/high | markov_w0_int | 10 | 3180 | 10.651 | 0.7452 | 3 | 15.72 |
| mtbench/dynamic | picospec | 10 | 3246 | 13.414 | 0.5639 | 3 | 11.13 |
| mtbench/dynamic | markov_w0_fresh4_int | 10 | 3246 | 13.677 | 0.6047 | 3 | 11.19 |
| mtbench/dynamic | markov_w0_dist_int | 10 | 3188 | 14.404 | 0.5225 | 3 | 20.21 |
| mtbench/dynamic | markov_w0_int | 10 | 3199 | 14.791 | 0.5173 | 3 | 20.08 |
| mtbench/pooled | picospec | 30 | 9707 | 13.302 | 0.5789 | 9 | 10.44 |
| mtbench/pooled | markov_w0_fresh4_int | 30 | 9707 | 13.686 | 0.6179 | 9 | 10.34 |
| mtbench/pooled | markov_w0_dist_int | 30 | 9603 | 13.979 | 0.5410 | 9 | 18.08 |
| mtbench/pooled | markov_w0_int | 30 | 9618 | 14.284 | 0.5427 | 9 | 18.79 |
| gsm8k/low | picospec | 10 | 3273 | 36.069 | 0.2677 | 3 | 43.63 |
| gsm8k/low | markov_w0_fresh4_int | 10 | 3273 | 35.234 | 0.2812 | 3 | 44.38 |
| gsm8k/low | markov_w0_dist_int | 10 | 3254 | 33.919 | 0.2604 | 3 | 51.25 |
| gsm8k/low | markov_w0_int | 10 | 3273 | 31.974 | 0.2423 | 3 | 49.27 |
| gsm8k/high | picospec | 10 | 3339 | 17.018 | 0.3885 | 3 | 35.78 |
| gsm8k/high | markov_w0_fresh4_int | 10 | 3339 | 20.034 | 0.3968 | 3 | 32.64 |
| gsm8k/high | markov_w0_dist_int | 10 | 3339 | 19.684 | 0.4043 | 3 | 37.95 |
| gsm8k/high | markov_w0_int | 10 | 3339 | 19.713 | 0.4062 | 3 | 37.76 |
| gsm8k/dynamic | picospec | 10 | 3362 | 24.671 | 0.3116 | 4 | 41.65 |
| gsm8k/dynamic | markov_w0_fresh4_int | 10 | 3362 | 27.489 | 0.3176 | 4 | 40.78 |
| gsm8k/dynamic | markov_w0_dist_int | 10 | 3221 | 26.110 | 0.3175 | 2 | 46.81 |
| gsm8k/dynamic | markov_w0_int | 10 | 3224 | 25.008 | 0.3069 | 2 | 45.36 |
| gsm8k/pooled | picospec | 30 | 9974 | 23.567 | 0.3230 | 10 | 40.08 |
| gsm8k/pooled | markov_w0_fresh4_int | 30 | 9974 | 26.119 | 0.3322 | 10 | 38.20 |
| gsm8k/pooled | markov_w0_dist_int | 30 | 9814 | 25.233 | 0.3281 | 8 | 44.03 |
| gsm8k/pooled | markov_w0_int | 30 | 9836 | 24.549 | 0.3191 | 8 | 42.95 |
| humaneval/low | picospec | 10 | 1718 | 53.754 | 0.1662 | 0 | 72.38 |
| humaneval/low | markov_w0_fresh4_int | 10 | 1718 | 60.082 | 0.1651 | 0 | 74.37 |
| humaneval/low | markov_w0_dist_int | 10 | 1718 | 54.973 | 0.1666 | 0 | 75.52 |
| humaneval/low | markov_w0_int | 10 | 1718 | 52.502 | 0.1674 | 0 | 73.60 |
| humaneval/high | picospec | 10 | 1718 | 26.046 | 0.2500 | 0 | 69.43 |
| humaneval/high | markov_w0_fresh4_int | 10 | 1718 | 38.747 | 0.1982 | 0 | 70.73 |
| humaneval/high | markov_w0_dist_int | 10 | 1718 | 37.311 | 0.2079 | 0 | 71.94 |
| humaneval/high | markov_w0_int | 10 | 1718 | 37.476 | 0.2051 | 0 | 71.76 |
| humaneval/dynamic | picospec | 10 | 1718 | 36.342 | 0.1995 | 0 | 71.92 |
| humaneval/dynamic | markov_w0_fresh4_int | 10 | 1718 | 43.546 | 0.1832 | 0 | 73.96 |
| humaneval/dynamic | markov_w0_dist_int | 10 | 1718 | 43.048 | 0.1879 | 0 | 75.02 |
| humaneval/dynamic | markov_w0_int | 10 | 1718 | 42.805 | 0.1880 | 0 | 74.33 |
| humaneval/pooled | picospec | 30 | 5154 | 35.498 | 0.2052 | 0 | 71.22 |
| humaneval/pooled | markov_w0_fresh4_int | 30 | 5154 | 45.860 | 0.1822 | 0 | 72.97 |
| humaneval/pooled | markov_w0_dist_int | 30 | 5154 | 43.974 | 0.1875 | 0 | 74.09 |
| humaneval/pooled | markov_w0_int | 30 | 5154 | 43.420 | 0.1868 | 0 | 73.18 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | markov_w0_fresh4_int_vs_picospec | 30 | -1.18 [-3.01, 1.11] | -2.53 [-3.85, -1.37] | 0 | 0 |
| all/low | markov_w0_dist_int_vs_picospec | 30 | -3.19 [-5.63, -0.06] | 14.25 [8.34, 18.49] | 5 | 0 |
| all/low | markov_w0_int_vs_picospec | 30 | -4.29 [-7.61, -1.46] | 16.79 [11.74, 20.23] | 5 | 0 |
| all/low | picospec_vs_markov_w0_dist_int | 30 | 3.29 [0.06, 5.96] | -16.62 [-22.68, -9.09] | 5 | 0 |
| all/low | markov_w0_fresh4_int_vs_markov_w0_dist_int | 30 | 2.07 [-1.59, 5.51] | -19.57 [-25.59, -12.39] | 5 | 0 |
| all/low | markov_w0_int_vs_markov_w0_dist_int | 30 | -1.14 [-4.52, 1.72] | 2.95 [0.82, 4.87] | 4 | 0 |
| all/high | markov_w0_fresh4_int_vs_picospec | 30 | 13.75 [10.65, 18.77] | -4.00 [-6.85, 0.42] | 2 | 0 |
| all/high | markov_w0_dist_int_vs_picospec | 30 | 13.37 [10.43, 17.86] | -2.77 [-5.09, 0.48] | 7 | 0 |
| all/high | markov_w0_int_vs_picospec | 30 | 14.45 [11.58, 19.14] | -4.04 [-6.47, -0.16] | 6 | 0 |
| all/high | picospec_vs_markov_w0_dist_int | 30 | -11.79 [-15.16, -9.44] | 2.70 [-0.48, 4.85] | 7 | 0 |
| all/high | markov_w0_fresh4_int_vs_markov_w0_dist_int | 30 | 0.33 [-1.65, 2.30] | -1.19 [-3.41, 1.65] | 8 | 0 |
| all/high | markov_w0_int_vs_markov_w0_dist_int | 30 | 0.95 [-0.46, 2.51] | -1.23 [-2.68, 0.61] | 1 | 0 |
| all/dynamic | markov_w0_fresh4_int_vs_picospec | 30 | 6.63 [2.80, 11.09] | -3.87 [-6.48, -0.77] | 3 | 0 |
| all/dynamic | markov_w0_dist_int_vs_picospec | 30 | 8.00 [4.53, 12.07] | 4.22 [0.56, 8.09] | 8 | 0 |
| all/dynamic | markov_w0_int_vs_picospec | 30 | 7.98 [3.96, 11.81] | 5.78 [2.67, 8.56] | 8 | 0 |
| all/dynamic | picospec_vs_markov_w0_dist_int | 30 | -7.41 [-10.77, -4.34] | -4.41 [-8.80, -0.56] | 8 | 2 |
| all/dynamic | markov_w0_fresh4_int_vs_markov_w0_dist_int | 30 | -1.27 [-5.36, 2.80] | -8.44 [-13.92, -2.57] | 9 | 2 |
| all/dynamic | markov_w0_int_vs_markov_w0_dist_int | 30 | -0.02 [-2.96, 2.27] | 1.63 [-0.55, 3.61] | 3 | 0 |
| all/pooled | markov_w0_fresh4_int_vs_picospec | 30 | 7.87 [5.27, 11.46] | -3.55 [-5.32, -1.01] | 5 | 0 |
| all/pooled | markov_w0_dist_int_vs_picospec | 30 | 7.65 [5.52, 10.92] | 4.20 [1.32, 6.95] | 20 | 0 |
| all/pooled | markov_w0_int_vs_picospec | 30 | 7.85 [5.63, 10.49] | 4.96 [3.05, 6.90] | 19 | 0 |
| all/pooled | picospec_vs_markov_w0_dist_int | 30 | -7.11 [-9.85, -5.23] | -4.39 [-7.46, -1.34] | 20 | 2 |
| all/pooled | markov_w0_fresh4_int_vs_markov_w0_dist_int | 30 | 0.20 [-2.54, 2.85] | -8.09 [-12.12, -3.51] | 22 | 2 |
| all/pooled | markov_w0_int_vs_markov_w0_dist_int | 30 | 0.18 [-1.59, 1.66] | 0.79 [-0.51, 2.25] | 8 | 0 |
| mtbench/low | markov_w0_fresh4_int_vs_picospec | 10 | -2.81 [-4.42, -0.30] | -1.70 [-2.76, -0.60] | 0 | 0 |
| mtbench/low | markov_w0_dist_int_vs_picospec | 10 | -2.54 [-5.94, 2.80] | 23.34 [19.19, 26.16] | 4 | 0 |
| mtbench/low | markov_w0_int_vs_picospec | 10 | 0.03 [-2.07, 2.34] | 24.15 [20.76, 26.41] | 4 | 0 |
| mtbench/low | picospec_vs_markov_w0_dist_int | 10 | 2.60 [-2.72, 6.31] | -30.45 [-35.43, -23.74] | 4 | 0 |
| mtbench/low | markov_w0_fresh4_int_vs_markov_w0_dist_int | 10 | -0.28 [-6.32, 5.02] | -32.67 [-38.86, -24.71] | 4 | 0 |
| mtbench/low | markov_w0_int_vs_markov_w0_dist_int | 10 | 2.63 [-1.33, 5.31] | 1.05 [-1.92, 3.62] | 2 | 0 |
| mtbench/high | markov_w0_fresh4_int_vs_picospec | 10 | 6.59 [4.32, 8.82] | -9.86 [-11.76, -7.63] | 1 | 0 |
| mtbench/high | markov_w0_dist_int_vs_picospec | 10 | 7.12 [4.50, 9.57] | -6.28 [-8.89, -4.21] | 6 | 0 |
| mtbench/high | markov_w0_int_vs_picospec | 10 | 8.54 [6.29, 11.14] | -8.65 [-10.47, -6.57] | 5 | 0 |
| mtbench/high | picospec_vs_markov_w0_dist_int | 10 | -6.65 [-8.73, -4.30] | 5.91 [4.04, 8.16] | 6 | 0 |
| mtbench/high | markov_w0_fresh4_int_vs_markov_w0_dist_int | 10 | -0.49 [-2.76, 1.95] | -3.37 [-5.65, -0.11] | 6 | 0 |
| mtbench/high | markov_w0_int_vs_markov_w0_dist_int | 10 | 1.33 [-1.05, 4.19] | -2.23 [-4.35, 0.77] | 1 | 0 |
| mtbench/dynamic | markov_w0_fresh4_int_vs_picospec | 10 | 1.96 [-2.98, 6.99] | -7.22 [-11.20, -3.37] | 2 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_picospec | 10 | 7.38 [4.02, 11.02] | 7.35 [3.31, 11.39] | 5 | 0 |
| mtbench/dynamic | markov_w0_int_vs_picospec | 10 | 10.26 [5.81, 14.20] | 8.27 [5.32, 10.65] | 5 | 0 |
| mtbench/dynamic | picospec_vs_markov_w0_dist_int | 10 | -6.88 [-9.93, -3.87] | -7.93 [-12.85, -3.42] | 5 | 0 |
| mtbench/dynamic | markov_w0_fresh4_int_vs_markov_w0_dist_int | 10 | -5.05 [-9.15, -0.43] | -15.73 [-22.12, -8.33] | 5 | 0 |
| mtbench/dynamic | markov_w0_int_vs_markov_w0_dist_int | 10 | 2.68 [-1.00, 5.50] | 0.99 [-2.44, 4.33] | 2 | 0 |
| mtbench/pooled | markov_w0_fresh4_int_vs_picospec | 10 | 2.89 [0.15, 5.76] | -6.73 [-8.53, -4.62] | 3 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec | 10 | 5.09 [3.23, 7.42] | 6.55 [3.19, 9.03] | 15 | 0 |
| mtbench/pooled | markov_w0_int_vs_picospec | 10 | 7.39 [5.40, 9.47] | 6.25 [4.43, 7.94] | 14 | 0 |
| mtbench/pooled | picospec_vs_markov_w0_dist_int | 10 | -4.84 [-6.91, -3.13] | -7.01 [-9.93, -3.29] | 15 | 0 |
| mtbench/pooled | markov_w0_fresh4_int_vs_markov_w0_dist_int | 10 | -2.09 [-5.64, 1.15] | -14.20 [-18.17, -8.71] | 15 | 0 |
| mtbench/pooled | markov_w0_int_vs_markov_w0_dist_int | 10 | 2.19 [0.24, 3.94] | -0.31 [-2.08, 2.14] | 5 | 0 |
| gsm8k/low | markov_w0_fresh4_int_vs_picospec | 10 | -2.32 [-5.59, 0.26] | -5.03 [-7.49, -3.26] | 0 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_picospec | 10 | -5.96 [-9.42, -1.85] | 2.75 [-1.56, 6.04] | 1 | 0 |
| gsm8k/low | markov_w0_int_vs_picospec | 10 | -11.35 [-14.70, -7.17] | 9.51 [5.71, 12.47] | 1 | 0 |
| gsm8k/low | picospec_vs_markov_w0_dist_int | 10 | 6.34 [1.89, 10.40] | -2.83 [-6.43, 1.53] | 1 | 0 |
| gsm8k/low | markov_w0_fresh4_int_vs_markov_w0_dist_int | 10 | 3.88 [0.52, 7.32] | -8.00 [-11.15, -4.17] | 1 | 0 |
| gsm8k/low | markov_w0_int_vs_markov_w0_dist_int | 10 | -5.73 [-8.34, -3.00] | 6.95 [5.47, 8.15] | 2 | 0 |
| gsm8k/high | markov_w0_fresh4_int_vs_picospec | 10 | 17.72 [14.08, 22.76] | -2.13 [-4.98, 2.18] | 1 | 0 |
| gsm8k/high | markov_w0_dist_int_vs_picospec | 10 | 15.66 [13.03, 19.89] | -4.07 [-6.33, -0.12] | 1 | 0 |
| gsm8k/high | markov_w0_int_vs_picospec | 10 | 15.83 [13.56, 20.11] | -4.55 [-6.75, -0.95] | 1 | 0 |
| gsm8k/high | picospec_vs_markov_w0_dist_int | 10 | -13.54 [-16.59, -11.52] | 3.91 [0.12, 5.96] | 1 | 0 |
| gsm8k/high | markov_w0_fresh4_int_vs_markov_w0_dist_int | 10 | 1.78 [0.06, 4.04] | 1.86 [-0.35, 4.27] | 2 | 0 |
| gsm8k/high | markov_w0_int_vs_markov_w0_dist_int | 10 | 0.15 [-1.05, 1.64] | -0.46 [-2.03, 0.88] | 0 | 0 |
| gsm8k/dynamic | markov_w0_fresh4_int_vs_picospec | 10 | 11.42 [6.74, 16.67] | -1.93 [-3.68, 0.22] | 1 | 0 |
| gsm8k/dynamic | markov_w0_dist_int_vs_picospec | 10 | 5.83 [0.93, 12.12] | -1.89 [-6.36, 2.24] | 3 | 0 |
| gsm8k/dynamic | markov_w0_int_vs_picospec | 10 | 1.36 [-3.68, 7.16] | 1.52 [-3.61, 6.08] | 3 | 0 |
| gsm8k/dynamic | picospec_vs_markov_w0_dist_int | 10 | -5.51 [-10.81, -0.93] | 1.85 [-2.29, 5.98] | 3 | 2 |
| gsm8k/dynamic | markov_w0_fresh4_int_vs_markov_w0_dist_int | 10 | 5.28 [0.60, 9.68] | -0.04 [-4.66, 4.64] | 4 | 2 |
| gsm8k/dynamic | markov_w0_int_vs_markov_w0_dist_int | 10 | -4.22 [-7.32, -1.79] | 3.34 [0.37, 5.53] | 1 | 0 |
| gsm8k/pooled | markov_w0_fresh4_int_vs_picospec | 10 | 10.83 [8.01, 14.27] | -2.86 [-4.10, -0.85] | 2 | 0 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec | 10 | 7.07 [4.48, 11.17] | -1.59 [-4.17, 1.25] | 5 | 0 |
| gsm8k/pooled | markov_w0_int_vs_picospec | 10 | 4.17 [1.42, 8.00] | 1.20 [-1.66, 3.95] | 5 | 0 |
| gsm8k/pooled | picospec_vs_markov_w0_dist_int | 10 | -6.60 [-10.05, -4.28] | 1.57 [-1.27, 4.01] | 5 | 2 |
| gsm8k/pooled | markov_w0_fresh4_int_vs_markov_w0_dist_int | 10 | 3.51 [1.19, 5.90] | -1.24 [-4.06, 1.86] | 7 | 2 |
| gsm8k/pooled | markov_w0_int_vs_markov_w0_dist_int | 10 | -2.71 [-3.98, -1.65] | 2.74 [1.41, 3.69] | 3 | 0 |
| humaneval/low | markov_w0_fresh4_int_vs_picospec | 10 | 11.77 [5.55, 17.84] | 0.61 [-3.96, 5.26] | 0 | 0 |
| humaneval/low | markov_w0_dist_int_vs_picospec | 10 | 2.27 [-3.38, 8.25] | -0.28 [-3.60, 3.47] | 0 | 0 |
| humaneval/low | markov_w0_int_vs_picospec | 10 | -2.33 [-10.14, 5.33] | -0.77 [-4.60, 3.25] | 0 | 0 |
| humaneval/low | picospec_vs_markov_w0_dist_int | 10 | -2.22 [-7.62, 3.50] | 0.28 [-3.60, 3.48] | 0 | 0 |
| humaneval/low | markov_w0_fresh4_int_vs_markov_w0_dist_int | 10 | 9.29 [0.23, 19.75] | 0.89 [-2.87, 4.89] | 0 | 0 |
| humaneval/low | markov_w0_int_vs_markov_w0_dist_int | 10 | -4.50 [-14.47, 6.16] | -0.49 [-6.14, 4.15] | 0 | 0 |
| humaneval/high | markov_w0_fresh4_int_vs_picospec | 10 | 48.76 [42.65, 55.35] | 20.72 [17.79, 23.85] | 0 | 0 |
| humaneval/high | markov_w0_dist_int_vs_picospec | 10 | 43.25 [37.73, 48.77] | 16.83 [12.87, 21.30] | 0 | 0 |
| humaneval/high | markov_w0_int_vs_picospec | 10 | 43.88 [36.87, 51.60] | 17.95 [13.53, 23.04] | 0 | 0 |
| humaneval/high | picospec_vs_markov_w0_dist_int | 10 | -30.19 [-32.78, -27.39] | -20.24 [-27.06, -14.77] | 0 | 0 |
| humaneval/high | markov_w0_fresh4_int_vs_markov_w0_dist_int | 10 | 3.85 [-0.45, 8.43] | 4.68 [1.07, 7.94] | 0 | 0 |
| humaneval/high | markov_w0_int_vs_markov_w0_dist_int | 10 | 0.44 [-1.12, 2.27] | 1.35 [-1.13, 3.58] | 0 | 0 |
| humaneval/dynamic | markov_w0_fresh4_int_vs_picospec | 10 | 19.82 [5.57, 30.55] | 8.15 [1.61, 13.05] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_picospec | 10 | 18.45 [10.22, 25.72] | 5.80 [1.11, 10.69] | 0 | 0 |
| humaneval/dynamic | markov_w0_int_vs_picospec | 10 | 17.78 [8.25, 27.19] | 5.79 [0.60, 11.17] | 0 | 0 |
| humaneval/dynamic | picospec_vs_markov_w0_dist_int | 10 | -15.58 [-20.46, -9.27] | -6.15 [-11.97, -1.12] | 0 | 0 |
| humaneval/dynamic | markov_w0_fresh4_int_vs_markov_w0_dist_int | 10 | 1.16 [-6.42, 6.94] | 2.50 [-2.89, 5.77] | 0 | 0 |
| humaneval/dynamic | markov_w0_int_vs_markov_w0_dist_int | 10 | -0.57 [-5.17, 5.25] | -0.01 [-2.43, 2.66] | 0 | 0 |
| humaneval/pooled | markov_w0_fresh4_int_vs_picospec | 10 | 29.19 [21.79, 35.50] | 11.22 [7.62, 14.93] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec | 10 | 23.88 [20.26, 27.28] | 8.64 [4.90, 12.58] | 0 | 0 |
| humaneval/pooled | markov_w0_int_vs_picospec | 10 | 22.32 [16.50, 28.62] | 8.96 [5.70, 13.06] | 0 | 0 |
| humaneval/pooled | picospec_vs_markov_w0_dist_int | 10 | -19.28 [-21.44, -16.84] | -9.45 [-14.39, -5.16] | 0 | 0 |
| humaneval/pooled | markov_w0_fresh4_int_vs_markov_w0_dist_int | 10 | 4.29 [-0.57, 7.94] | 2.83 [-0.57, 5.63] | 0 | 0 |
| humaneval/pooled | markov_w0_int_vs_markov_w0_dist_int | 10 | -1.26 [-4.67, 2.36] | 0.35 [-1.58, 2.15] | 0 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
