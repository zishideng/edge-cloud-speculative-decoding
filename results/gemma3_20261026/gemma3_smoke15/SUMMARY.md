# Progress probe: gemma3_smoke15

State: complete; 270/270 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | sync_g4 | 15 | 3681 | 23.682 | 0.2795 | 2 | 0.00 |
| all/low | fixed_g2 | 15 | 3708 | 35.660 | 0.2317 | 2 | 33.45 |
| all/low | fixed_fast | 15 | 3681 | 34.974 | 0.3074 | 2 | 27.83 |
| all/low | fixed_g8 | 15 | 3691 | 25.985 | 0.4699 | 2 | 16.62 |
| all/low | markov_w0_dist | 15 | 3708 | 33.772 | 0.2311 | 2 | 37.56 |
| all/low | markov_w05_dist | 15 | 3689 | 34.607 | 0.2230 | 2 | 37.28 |
| all/high | sync_g4 | 15 | 3700 | 13.362 | 0.4353 | 2 | 0.00 |
| all/high | fixed_g2 | 15 | 3658 | 14.121 | 0.4335 | 2 | 34.27 |
| all/high | fixed_fast | 15 | 3700 | 16.343 | 0.4257 | 2 | 27.85 |
| all/high | fixed_g8 | 15 | 3696 | 17.448 | 0.5361 | 2 | 17.07 |
| all/high | markov_w0_dist | 15 | 3643 | 18.838 | 0.4654 | 2 | 29.86 |
| all/high | markov_w05_dist | 15 | 3643 | 16.462 | 0.4019 | 2 | 38.56 |
| all/dynamic | sync_g4 | 15 | 3707 | 17.541 | 0.3518 | 2 | 0.00 |
| all/dynamic | fixed_g2 | 15 | 3677 | 21.648 | 0.3175 | 2 | 34.06 |
| all/dynamic | fixed_fast | 15 | 3707 | 22.202 | 0.3712 | 2 | 27.92 |
| all/dynamic | fixed_g8 | 15 | 3713 | 20.784 | 0.5144 | 2 | 16.90 |
| all/dynamic | markov_w0_dist | 15 | 3658 | 24.539 | 0.3325 | 2 | 35.49 |
| all/dynamic | markov_w05_dist | 15 | 3658 | 23.446 | 0.3035 | 2 | 37.74 |
| all/pooled | sync_g4 | 45 | 11088 | 17.226 | 0.3557 | 6 | 0.00 |
| all/pooled | fixed_g2 | 45 | 11043 | 20.723 | 0.3271 | 6 | 33.92 |
| all/pooled | fixed_fast | 45 | 11088 | 22.238 | 0.3682 | 6 | 27.87 |
| all/pooled | fixed_g8 | 45 | 11100 | 20.844 | 0.5068 | 6 | 16.86 |
| all/pooled | markov_w0_dist | 45 | 11009 | 24.343 | 0.3423 | 6 | 33.34 |
| all/pooled | markov_w05_dist | 45 | 10990 | 22.711 | 0.3091 | 6 | 37.86 |
| mtbench/low | sync_g4 | 5 | 1451 | 18.235 | 0.3680 | 1 | 0.00 |
| mtbench/low | fixed_g2 | 5 | 1478 | 26.956 | 0.3077 | 1 | 15.73 |
| mtbench/low | fixed_fast | 5 | 1451 | 24.138 | 0.4692 | 1 | 8.69 |
| mtbench/low | fixed_g8 | 5 | 1459 | 15.799 | 0.7873 | 1 | 2.27 |
| mtbench/low | markov_w0_dist | 5 | 1478 | 25.391 | 0.2921 | 1 | 20.05 |
| mtbench/low | markov_w05_dist | 5 | 1459 | 26.499 | 0.2834 | 1 | 19.90 |
| mtbench/high | sync_g4 | 5 | 1468 | 10.314 | 0.5733 | 1 | 0.00 |
| mtbench/high | fixed_g2 | 5 | 1426 | 11.298 | 0.5526 | 1 | 16.54 |
| mtbench/high | fixed_fast | 5 | 1468 | 11.405 | 0.6188 | 1 | 8.66 |
| mtbench/high | fixed_g8 | 5 | 1466 | 10.892 | 0.8736 | 1 | 2.35 |
| mtbench/high | markov_w0_dist | 5 | 1411 | 12.425 | 0.7225 | 1 | 14.91 |
| mtbench/high | markov_w05_dist | 5 | 1411 | 11.034 | 0.5683 | 1 | 16.22 |
| mtbench/dynamic | sync_g4 | 5 | 1454 | 13.400 | 0.4706 | 1 | 0.00 |
| mtbench/dynamic | fixed_g2 | 5 | 1424 | 16.204 | 0.4311 | 1 | 15.72 |
| mtbench/dynamic | fixed_fast | 5 | 1454 | 14.762 | 0.5738 | 1 | 8.80 |
| mtbench/dynamic | fixed_g8 | 5 | 1462 | 12.507 | 0.8690 | 1 | 2.27 |
| mtbench/dynamic | markov_w0_dist | 5 | 1405 | 16.577 | 0.4940 | 1 | 17.85 |
| mtbench/dynamic | markov_w05_dist | 5 | 1405 | 16.110 | 0.4262 | 1 | 16.94 |
| mtbench/pooled | sync_g4 | 15 | 4373 | 13.235 | 0.4710 | 3 | 0.00 |
| mtbench/pooled | fixed_g2 | 15 | 4328 | 16.093 | 0.4290 | 3 | 15.99 |
| mtbench/pooled | fixed_fast | 15 | 4373 | 15.220 | 0.5542 | 3 | 8.71 |
| mtbench/pooled | fixed_g8 | 15 | 4387 | 12.759 | 0.8434 | 3 | 2.30 |
| mtbench/pooled | markov_w0_dist | 15 | 4294 | 16.739 | 0.4996 | 3 | 16.77 |
| mtbench/pooled | markov_w05_dist | 15 | 4275 | 15.825 | 0.4244 | 3 | 17.75 |
| humaneval/low | sync_g4 | 5 | 855 | 32.119 | 0.2030 | 0 | 0.00 |
| humaneval/low | fixed_g2 | 5 | 855 | 56.744 | 0.1507 | 0 | 61.69 |
| humaneval/low | fixed_fast | 5 | 855 | 62.816 | 0.1445 | 0 | 70.67 |
| humaneval/low | fixed_g8 | 5 | 855 | 73.309 | 0.1517 | 0 | 72.43 |
| humaneval/low | markov_w0_dist | 5 | 855 | 61.720 | 0.1498 | 0 | 68.19 |
| humaneval/low | markov_w05_dist | 5 | 855 | 60.448 | 0.1477 | 0 | 66.81 |
| humaneval/high | sync_g4 | 5 | 855 | 18.965 | 0.3067 | 0 | 0.00 |
| humaneval/high | fixed_g2 | 5 | 855 | 18.728 | 0.3200 | 0 | 61.48 |
| humaneval/high | fixed_fast | 5 | 855 | 29.255 | 0.2346 | 0 | 70.59 |
| humaneval/high | fixed_g8 | 5 | 855 | 45.819 | 0.1908 | 0 | 72.43 |
| humaneval/high | markov_w0_dist | 5 | 855 | 42.980 | 0.1893 | 0 | 72.87 |
| humaneval/high | markov_w05_dist | 5 | 855 | 38.870 | 0.2015 | 0 | 72.02 |
| humaneval/dynamic | sync_g4 | 5 | 855 | 23.092 | 0.2568 | 0 | 0.00 |
| humaneval/dynamic | fixed_g2 | 5 | 855 | 28.829 | 0.2291 | 0 | 61.69 |
| humaneval/dynamic | fixed_fast | 5 | 855 | 38.978 | 0.1849 | 0 | 70.67 |
| humaneval/dynamic | fixed_g8 | 5 | 855 | 54.042 | 0.1699 | 0 | 72.43 |
| humaneval/dynamic | markov_w0_dist | 5 | 855 | 43.493 | 0.1818 | 0 | 70.00 |
| humaneval/dynamic | markov_w05_dist | 5 | 855 | 46.941 | 0.1804 | 0 | 70.47 |
| humaneval/pooled | sync_g4 | 15 | 2565 | 23.591 | 0.2555 | 0 | 0.00 |
| humaneval/pooled | fixed_g2 | 15 | 2565 | 28.380 | 0.2333 | 0 | 61.62 |
| humaneval/pooled | fixed_fast | 15 | 2565 | 39.600 | 0.1880 | 0 | 70.64 |
| humaneval/pooled | fixed_g8 | 15 | 2565 | 55.587 | 0.1708 | 0 | 72.43 |
| humaneval/pooled | markov_w0_dist | 15 | 2565 | 48.030 | 0.1736 | 0 | 70.45 |
| humaneval/pooled | markov_w05_dist | 15 | 2565 | 47.190 | 0.1765 | 0 | 69.87 |
| gsm8k/low | sync_g4 | 5 | 1375 | 27.923 | 0.2337 | 1 | 0.00 |
| gsm8k/low | fixed_g2 | 5 | 1375 | 40.343 | 0.2003 | 1 | 42.20 |
| gsm8k/low | fixed_fast | 5 | 1375 | 43.615 | 0.2379 | 1 | 39.06 |
| gsm8k/low | fixed_g8 | 5 | 1377 | 36.201 | 0.3312 | 1 | 25.65 |
| gsm8k/low | markov_w0_dist | 5 | 1375 | 36.441 | 0.2160 | 1 | 41.92 |
| gsm8k/low | markov_w05_dist | 5 | 1375 | 36.773 | 0.2057 | 1 | 40.68 |
| gsm8k/high | sync_g4 | 5 | 1377 | 15.386 | 0.3681 | 1 | 0.00 |
| gsm8k/high | fixed_g2 | 5 | 1377 | 15.797 | 0.3807 | 1 | 42.26 |
| gsm8k/high | fixed_fast | 5 | 1377 | 20.116 | 0.3386 | 1 | 38.82 |
| gsm8k/high | fixed_g8 | 5 | 1375 | 23.474 | 0.3909 | 1 | 25.90 |
| gsm8k/high | markov_w0_dist | 5 | 1377 | 22.977 | 0.3733 | 1 | 41.31 |
| gsm8k/high | markov_w05_dist | 5 | 1377 | 19.280 | 0.3559 | 1 | 40.51 |
| gsm8k/dynamic | sync_g4 | 5 | 1398 | 21.246 | 0.2863 | 1 | 0.00 |
| gsm8k/dynamic | fixed_g2 | 5 | 1398 | 26.722 | 0.2559 | 1 | 42.88 |
| gsm8k/dynamic | fixed_fast | 5 | 1398 | 30.043 | 0.2744 | 1 | 39.11 |
| gsm8k/dynamic | fixed_g8 | 5 | 1396 | 30.392 | 0.3541 | 1 | 26.46 |
| gsm8k/dynamic | markov_w0_dist | 5 | 1398 | 31.305 | 0.2624 | 1 | 44.37 |
| gsm8k/dynamic | markov_w05_dist | 5 | 1398 | 27.633 | 0.2554 | 1 | 40.75 |
| gsm8k/pooled | sync_g4 | 15 | 4150 | 20.289 | 0.2960 | 3 | 0.00 |
| gsm8k/pooled | fixed_g2 | 15 | 4150 | 23.910 | 0.2789 | 3 | 42.45 |
| gsm8k/pooled | fixed_fast | 15 | 4150 | 28.325 | 0.2836 | 3 | 39.00 |
| gsm8k/pooled | fixed_g8 | 15 | 4148 | 29.099 | 0.3587 | 3 | 26.00 |
| gsm8k/pooled | markov_w0_dist | 15 | 4150 | 29.160 | 0.2839 | 3 | 42.43 |
| gsm8k/pooled | markov_w05_dist | 15 | 4150 | 26.035 | 0.2723 | 3 | 40.64 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | sync_g4 | 15 | -32.29 [-38.35, -27.47] | 9.06 [-4.70, 17.13] | 0 | 0 |
| all/low | fixed_g2 | 15 | 1.96 [-6.45, 9.13] | 24.63 [14.67, 30.36] | 3 | 0 |
| all/low | fixed_g8 | 15 | -25.70 [-31.50, -15.26] | -52.89 [-62.74, -37.50] | 3 | 0 |
| all/low | markov_w0_dist | 15 | -3.44 [-13.39, 6.42] | 24.82 [11.29, 33.32] | 3 | 0 |
| all/low | markov_w05_dist | 15 | -1.05 [-9.71, 6.29] | 27.46 [14.32, 35.23] | 3 | 0 |
| all/low | sync_g4_vs_fixed_g2 | 15 | -33.59 [-37.06, -30.34] | -20.66 [-25.23, -16.53] | 3 | 0 |
| all/low | fixed_fast_vs_fixed_g2 | 15 | -1.92 [-8.36, 6.90] | -32.68 [-43.59, -17.19] | 3 | 0 |
| all/low | fixed_g8_vs_fixed_g2 | 15 | -27.13 [-36.25, -10.49] | -102.85 [-133.04, -61.21] | 3 | 0 |
| all/low | markov_w0_dist_vs_fixed_g2 | 15 | -5.29 [-11.64, 3.47] | 0.25 [-6.05, 5.96] | 1 | 0 |
| all/low | markov_w05_dist_vs_fixed_g2 | 15 | -2.95 [-8.24, 2.88] | 3.75 [-1.52, 7.92] | 2 | 0 |
| all/low | sync_g4_vs_fixed_g8 | 15 | -8.86 [-27.14, 5.40] | 40.52 [24.37, 48.89] | 3 | 0 |
| all/low | fixed_g2_vs_fixed_g8 | 15 | 37.24 [11.72, 56.87] | 50.70 [37.97, 57.09] | 3 | 0 |
| all/low | fixed_fast_vs_fixed_g8 | 15 | 34.60 [18.01, 45.98] | 34.59 [27.27, 38.55] | 3 | 0 |
| all/low | markov_w0_dist_vs_fixed_g8 | 15 | 29.97 [5.55, 51.15] | 50.83 [35.17, 59.00] | 4 | 0 |
| all/low | markov_w05_dist_vs_fixed_g8 | 15 | 33.18 [7.82, 53.03] | 52.55 [37.78, 59.93] | 4 | 0 |
| all/low | fixed_g2_vs_sync_g4 | 15 | 50.58 [43.56, 58.89] | 17.12 [14.18, 20.15] | 3 | 0 |
| all/low | fixed_fast_vs_sync_g4 | 15 | 47.68 [37.87, 62.22] | -9.97 [-20.68, 4.49] | 0 | 0 |
| all/low | fixed_g8_vs_sync_g4 | 15 | 9.72 [-5.12, 37.25] | -68.12 [-95.66, -32.23] | 3 | 0 |
| all/low | markov_w0_dist_vs_sync_g4 | 15 | 42.61 [33.19, 57.23] | 17.33 [12.70, 21.62] | 3 | 0 |
| all/low | markov_w05_dist_vs_sync_g4 | 15 | 46.13 [37.01, 57.93] | 20.23 [16.18, 24.15] | 3 | 0 |
| all/high | sync_g4 | 15 | -18.24 [-24.97, -13.49] | -2.26 [-11.80, 4.17] | 0 | 0 |
| all/high | fixed_g2 | 15 | -13.59 [-22.83, -6.19] | -1.83 [-14.11, 6.19] | 4 | 0 |
| all/high | fixed_g8 | 15 | 6.76 [-1.58, 20.09] | -25.92 [-37.21, -10.55] | 3 | 0 |
| all/high | markov_w0_dist | 15 | 15.27 [10.97, 22.54] | -9.31 [-14.80, -0.72] | 2 | 0 |
| all/high | markov_w05_dist | 15 | 0.73 [-3.94, 8.13] | 5.59 [0.17, 11.46] | 3 | 0 |
| all/high | sync_g4_vs_fixed_g2 | 15 | -5.38 [-8.08, -1.98] | -0.42 [-4.22, 3.31] | 4 | 0 |
| all/high | fixed_fast_vs_fixed_g2 | 15 | 15.73 [6.60, 29.58] | 1.79 [-6.60, 12.37] | 4 | 0 |
| all/high | fixed_g8_vs_fixed_g2 | 15 | 23.56 [5.36, 55.37] | -23.66 [-45.73, 2.76] | 5 | 0 |
| all/high | markov_w0_dist_vs_fixed_g2 | 15 | 33.41 [20.25, 56.50] | -7.35 [-19.60, 9.92] | 2 | 0 |
| all/high | markov_w05_dist_vs_fixed_g2 | 15 | 16.58 [5.67, 36.91] | 7.28 [1.51, 16.39] | 1 | 0 |
| all/high | sync_g4_vs_fixed_g8 | 15 | -23.42 [-37.18, -12.23] | 18.79 [-1.25, 30.00] | 3 | 0 |
| all/high | fixed_g2_vs_fixed_g8 | 15 | -19.07 [-35.64, -5.09] | 19.13 [-2.84, 31.38] | 5 | 0 |
| all/high | fixed_fast_vs_fixed_g8 | 15 | -6.33 [-16.73, 1.60] | 20.58 [9.54, 27.12] | 3 | 0 |
| all/high | markov_w0_dist_vs_fixed_g8 | 15 | 7.97 [-1.88, 16.60] | 13.18 [3.73, 20.39] | 5 | 0 |
| all/high | markov_w05_dist_vs_fixed_g8 | 15 | -5.65 [-15.28, 3.47] | 25.02 [10.89, 33.68] | 5 | 0 |
| all/high | fixed_g2_vs_sync_g4 | 15 | 5.68 [2.02, 8.79] | 0.42 [-3.43, 4.04] | 4 | 0 |
| all/high | fixed_fast_vs_sync_g4 | 15 | 22.31 [15.59, 33.28] | 2.21 [-4.35, 10.56] | 0 | 0 |
| all/high | fixed_g8_vs_sync_g4 | 15 | 30.58 [13.93, 59.19] | -23.14 [-42.85, 1.24] | 3 | 0 |
| all/high | markov_w0_dist_vs_sync_g4 | 15 | 40.99 [29.78, 61.28] | -6.90 [-17.08, 8.39] | 2 | 0 |
| all/high | markov_w05_dist_vs_sync_g4 | 15 | 23.20 [13.25, 41.42] | 7.67 [2.29, 15.88] | 3 | 0 |
| all/dynamic | sync_g4 | 15 | -20.99 [-29.65, -14.09] | 5.22 [-8.54, 13.81] | 0 | 0 |
| all/dynamic | fixed_g2 | 15 | -2.50 [-13.64, 6.35] | 14.47 [1.30, 22.37] | 3 | 0 |
| all/dynamic | fixed_g8 | 15 | -6.39 [-12.66, 5.65] | -38.59 [-46.89, -24.47] | 4 | 0 |
| all/dynamic | markov_w0_dist | 15 | 10.52 [5.02, 17.01] | 10.42 [-0.95, 18.67] | 3 | 0 |
| all/dynamic | markov_w05_dist | 15 | 5.60 [-2.67, 14.06] | 18.25 [7.50, 25.01] | 3 | 0 |
| all/dynamic | sync_g4_vs_fixed_g2 | 15 | -18.97 [-22.49, -15.60] | -10.80 [-14.58, -7.77] | 3 | 0 |
| all/dynamic | fixed_fast_vs_fixed_g2 | 15 | 2.56 [-5.97, 15.79] | -16.91 [-28.82, -1.31] | 3 | 0 |
| all/dynamic | fixed_g8_vs_fixed_g2 | 15 | -3.99 [-17.33, 21.14] | -62.03 [-87.81, -27.20] | 4 | 0 |
| all/dynamic | markov_w0_dist_vs_fixed_g2 | 15 | 13.35 [5.57, 26.45] | -4.73 [-12.86, 4.22] | 3 | 0 |
| all/dynamic | markov_w05_dist_vs_fixed_g2 | 15 | 8.31 [1.12, 20.23] | 4.42 [0.58, 9.32] | 1 | 0 |
| all/dynamic | sync_g4_vs_fixed_g8 | 15 | -15.60 [-32.76, -2.51] | 31.62 [13.04, 41.03] | 4 | 0 |
| all/dynamic | fixed_g2_vs_fixed_g8 | 15 | 4.16 [-17.45, 20.97] | 38.28 [21.38, 46.75] | 4 | 0 |
| all/dynamic | fixed_fast_vs_fixed_g8 | 15 | 6.83 [-5.34, 14.49] | 27.85 [19.66, 31.92] | 4 | 0 |
| all/dynamic | markov_w0_dist_vs_fixed_g8 | 15 | 18.07 [1.90, 28.85] | 35.36 [21.00, 43.77] | 4 | 0 |
| all/dynamic | markov_w05_dist_vs_fixed_g8 | 15 | 12.81 [-4.70, 25.96] | 41.01 [26.15, 48.49] | 4 | 0 |
| all/dynamic | fixed_g2_vs_sync_g4 | 15 | 23.41 [18.48, 29.02] | 9.75 [7.21, 12.73] | 3 | 0 |
| all/dynamic | fixed_fast_vs_sync_g4 | 15 | 26.57 [16.40, 42.15] | -5.51 [-16.02, 7.86] | 0 | 0 |
| all/dynamic | fixed_g8_vs_sync_g4 | 15 | 18.49 [2.57, 48.72] | -46.23 [-69.57, -14.99] | 4 | 0 |
| all/dynamic | markov_w0_dist_vs_sync_g4 | 15 | 39.89 [30.67, 54.01] | 5.48 [-2.47, 14.31] | 3 | 0 |
| all/dynamic | markov_w05_dist_vs_sync_g4 | 15 | 33.66 [25.24, 48.07] | 13.74 [10.03, 18.91] | 3 | 0 |
| all/pooled | sync_g4 | 15 | -22.54 [-29.51, -17.15] | 3.40 [-8.47, 10.92] | 0 | 0 |
| all/pooled | fixed_g2 | 15 | -6.81 [-16.56, 0.99] | 11.16 [-0.83, 18.67] | 10 | 0 |
| all/pooled | fixed_g8 | 15 | -6.27 [-13.05, 5.65] | -37.65 [-47.26, -23.07] | 10 | 0 |
| all/pooled | markov_w0_dist | 15 | 9.47 [5.04, 15.13] | 7.03 [0.38, 12.91] | 8 | 0 |
| all/pooled | markov_w05_dist | 15 | 2.13 [-3.30, 9.10] | 16.05 [7.16, 22.15] | 9 | 0 |
| all/pooled | sync_g4_vs_fixed_g2 | 15 | -16.88 [-18.73, -14.71] | -8.74 [-11.39, -6.23] | 10 | 0 |
| all/pooled | fixed_fast_vs_fixed_g2 | 15 | 7.31 [-0.98, 19.84] | -12.57 [-22.96, 0.82] | 10 | 0 |
| all/pooled | fixed_g8_vs_fixed_g2 | 15 | 0.58 [-13.52, 26.49] | -54.95 [-80.68, -22.55] | 12 | 0 |
| all/pooled | markov_w0_dist_vs_fixed_g2 | 15 | 17.47 [9.74, 30.60] | -4.65 [-11.76, 5.35] | 6 | 0 |
| all/pooled | markov_w05_dist_vs_fixed_g2 | 15 | 9.59 [2.16, 22.77] | 5.51 [2.08, 10.83] | 4 | 0 |
| all/pooled | sync_g4_vs_fixed_g8 | 15 | -17.36 [-33.15, -4.75] | 29.82 [11.50, 39.62] | 10 | 0 |
| all/pooled | fixed_g2_vs_fixed_g8 | 15 | -0.58 [-20.94, 15.64] | 35.46 [18.40, 44.65] | 12 | 0 |
| all/pooled | fixed_fast_vs_fixed_g8 | 15 | 6.69 [-5.35, 15.01] | 27.35 [18.75, 32.09] | 10 | 0 |
| all/pooled | markov_w0_dist_vs_fixed_g8 | 15 | 16.79 [1.87, 28.58] | 32.46 [19.80, 40.24] | 13 | 0 |
| all/pooled | markov_w05_dist_vs_fixed_g8 | 15 | 8.96 [-5.92, 21.12] | 39.02 [24.45, 47.09] | 13 | 0 |
| all/pooled | fixed_g2_vs_sync_g4 | 15 | 20.30 [17.24, 23.05] | 8.03 [5.86, 10.22] | 10 | 0 |
| all/pooled | fixed_fast_vs_sync_g4 | 15 | 29.09 [20.69, 41.86] | -3.52 [-12.26, 7.81] | 0 | 0 |
| all/pooled | fixed_g8_vs_sync_g4 | 15 | 21.00 [4.99, 49.59] | -42.50 [-65.62, -12.99] | 10 | 0 |
| all/pooled | markov_w0_dist_vs_sync_g4 | 15 | 41.31 [32.84, 56.63] | 3.76 [-2.54, 13.16] | 8 | 0 |
| all/pooled | markov_w05_dist_vs_sync_g4 | 15 | 31.84 [23.30, 46.59] | 13.10 [9.36, 18.37] | 9 | 0 |
| mtbench/low | sync_g4 | 5 | -24.46 [-27.60, -22.27] | 21.56 [14.89, 25.11] | 0 | 0 |
| mtbench/low | fixed_g2 | 5 | 11.67 [4.80, 17.00] | 34.42 [30.38, 37.17] | 2 | 0 |
| mtbench/low | fixed_g8 | 5 | -34.55 [-38.09, -29.99] | -67.80 [-74.79, -60.39] | 2 | 0 |
| mtbench/low | markov_w0_dist | 5 | 5.19 [-5.41, 14.95] | 37.74 [29.09, 43.00] | 2 | 0 |
| mtbench/low | markov_w05_dist | 5 | 9.78 [4.78, 17.84] | 39.59 [32.69, 43.49] | 2 | 0 |
| mtbench/low | sync_g4_vs_fixed_g2 | 5 | -32.35 [-35.56, -28.42] | -19.60 [-25.01, -14.94] | 2 | 0 |
| mtbench/low | fixed_fast_vs_fixed_g2 | 5 | -10.45 [-14.53, -4.58] | -52.48 [-59.16, -43.65] | 2 | 0 |
| mtbench/low | fixed_g8_vs_fixed_g2 | 5 | -41.39 [-44.12, -35.97] | -155.87 [-171.84, -131.28] | 1 | 0 |
| mtbench/low | markov_w0_dist_vs_fixed_g2 | 5 | -5.80 [-11.65, 1.19] | 5.07 [-2.71, 11.34] | 1 | 0 |
| mtbench/low | markov_w05_dist_vs_fixed_g2 | 5 | -1.70 [-6.83, 5.86] | 7.89 [2.52, 10.55] | 2 | 0 |
| mtbench/low | sync_g4_vs_fixed_g8 | 5 | 15.42 [5.03, 24.15] | 53.26 [46.93, 57.14] | 2 | 0 |
| mtbench/low | fixed_g2_vs_fixed_g8 | 5 | 70.61 [56.17, 78.96] | 60.92 [56.76, 63.21] | 1 | 0 |
| mtbench/low | fixed_fast_vs_fixed_g8 | 5 | 52.78 [42.83, 61.52] | 40.41 [37.65, 42.79] | 2 | 0 |
| mtbench/low | markov_w0_dist_vs_fixed_g8 | 5 | 60.71 [40.34, 77.55] | 62.90 [55.79, 67.52] | 2 | 0 |
| mtbench/low | markov_w05_dist_vs_fixed_g8 | 5 | 67.72 [56.42, 83.17] | 64.00 [58.24, 67.03] | 2 | 0 |
| mtbench/low | fixed_g2_vs_sync_g4 | 5 | 47.82 [39.71, 55.18] | 16.39 [13.00, 20.01] | 2 | 0 |
| mtbench/low | fixed_fast_vs_sync_g4 | 5 | 32.37 [28.65, 38.13] | -27.49 [-33.53, -17.49] | 0 | 0 |
| mtbench/low | fixed_g8_vs_sync_g4 | 5 | -13.36 [-19.46, -4.79] | -113.93 [-133.29, -88.45] | 2 | 0 |
| mtbench/low | markov_w0_dist_vs_sync_g4 | 5 | 39.24 [29.40, 50.54] | 20.63 [15.99, 24.75] | 2 | 0 |
| mtbench/low | markov_w05_dist_vs_sync_g4 | 5 | 45.31 [38.86, 55.31] | 22.99 [18.80, 26.92] | 2 | 0 |
| mtbench/high | sync_g4 | 5 | -9.56 [-11.87, -7.51] | 7.35 [1.68, 11.10] | 0 | 0 |
| mtbench/high | fixed_g2 | 5 | -0.94 [-6.29, 3.03] | 10.70 [5.01, 14.12] | 3 | 0 |
| mtbench/high | fixed_g8 | 5 | -4.49 [-9.45, 3.97] | -41.17 [-49.47, -27.28] | 2 | 0 |
| mtbench/high | markov_w0_dist | 5 | 8.95 [6.23, 10.57] | -16.76 [-21.24, -12.08] | 1 | 0 |
| mtbench/high | markov_w05_dist | 5 | -3.25 [-6.73, 0.58] | 8.16 [3.02, 13.07] | 2 | 0 |
| mtbench/high | sync_g4_vs_fixed_g2 | 5 | -8.70 [-11.42, -5.36] | -3.75 [-10.25, 1.22] | 3 | 0 |
| mtbench/high | fixed_fast_vs_fixed_g2 | 5 | 0.95 [-2.94, 6.71] | -11.98 [-16.45, -5.28] | 3 | 0 |
| mtbench/high | fixed_g8_vs_fixed_g2 | 5 | -3.59 [-10.58, 8.82] | -58.08 [-71.97, -36.72] | 3 | 0 |
| mtbench/high | markov_w0_dist_vs_fixed_g2 | 5 | 9.98 [4.64, 14.98] | -30.75 [-39.11, -22.18] | 2 | 0 |
| mtbench/high | markov_w05_dist_vs_fixed_g2 | 5 | -2.33 [-5.21, 1.45] | -2.85 [-5.72, 1.36] | 1 | 0 |
| mtbench/high | sync_g4_vs_fixed_g8 | 5 | -5.30 [-14.66, 1.53] | 34.37 [22.76, 40.52] | 2 | 0 |
| mtbench/high | fixed_g2_vs_fixed_g8 | 5 | 3.72 [-8.10, 11.83] | 36.74 [26.86, 41.85] | 3 | 0 |
| mtbench/high | fixed_fast_vs_fixed_g8 | 5 | 4.71 [-3.82, 10.43] | 29.16 [21.43, 33.09] | 2 | 0 |
| mtbench/high | markov_w0_dist_vs_fixed_g8 | 5 | 14.07 [2.17, 22.10] | 17.29 [5.26, 24.11] | 3 | 0 |
| mtbench/high | markov_w05_dist_vs_fixed_g8 | 5 | 1.30 [-9.09, 10.04] | 34.94 [24.91, 40.95] | 3 | 0 |
| mtbench/high | fixed_g2_vs_sync_g4 | 5 | 9.53 [5.67, 12.89] | 3.62 [-1.23, 9.30] | 3 | 0 |
| mtbench/high | fixed_fast_vs_sync_g4 | 5 | 10.57 [8.12, 13.47] | -7.93 [-12.49, -1.71] | 0 | 0 |
| mtbench/high | fixed_g8_vs_sync_g4 | 5 | 5.60 [-1.50, 17.17] | -52.37 [-68.14, -29.47] | 2 | 0 |
| mtbench/high | markov_w0_dist_vs_sync_g4 | 5 | 20.46 [17.79, 22.07] | -26.02 [-28.73, -21.43] | 1 | 0 |
| mtbench/high | markov_w05_dist_vs_sync_g4 | 5 | 6.98 [5.33, 9.63] | 0.87 [-2.97, 4.87] | 2 | 0 |
| mtbench/dynamic | sync_g4 | 5 | -9.22 [-13.85, -3.66] | 17.99 [10.19, 21.97] | 0 | 0 |
| mtbench/dynamic | fixed_g2 | 5 | 9.77 [0.98, 16.59] | 24.87 [16.40, 29.06] | 3 | 0 |
| mtbench/dynamic | fixed_g8 | 5 | -15.28 [-18.32, -10.88] | -51.46 [-55.89, -46.71] | 2 | 0 |
| mtbench/dynamic | markov_w0_dist | 5 | 12.30 [6.53, 18.12] | 13.91 [-3.95, 23.71] | 2 | 0 |
| mtbench/dynamic | markov_w05_dist | 5 | 9.13 [-0.60, 17.61] | 25.72 [15.14, 30.80] | 3 | 0 |
| mtbench/dynamic | sync_g4_vs_fixed_g2 | 5 | -17.30 [-19.47, -12.92] | -9.17 [-12.13, -5.91] | 3 | 0 |
| mtbench/dynamic | fixed_fast_vs_fixed_g2 | 5 | -8.90 [-14.23, -0.97] | -33.11 [-40.96, -19.61] | 3 | 0 |
| mtbench/dynamic | fixed_g8_vs_fixed_g2 | 5 | -22.81 [-28.21, -12.27] | -101.60 [-115.16, -76.99] | 2 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_fixed_g2 | 5 | 2.30 [-0.94, 8.75] | -14.59 [-26.22, -4.61] | 2 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_fixed_g2 | 5 | -0.58 [-3.21, 2.98] | 1.13 [-1.54, 5.20] | 1 | 0 |
| mtbench/dynamic | sync_g4_vs_fixed_g8 | 5 | 7.14 [-2.39, 13.51] | 45.85 [39.18, 49.05] | 2 | 0 |
| mtbench/dynamic | fixed_g2_vs_fixed_g8 | 5 | 29.56 [13.99, 39.30] | 50.40 [43.50, 53.52] | 2 | 0 |
| mtbench/dynamic | fixed_fast_vs_fixed_g8 | 5 | 18.03 [12.21, 22.44] | 33.97 [31.84, 35.85] | 2 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_fixed_g8 | 5 | 32.54 [21.44, 39.13] | 43.16 [29.79, 50.23] | 3 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_fixed_g8 | 5 | 28.81 [14.29, 38.01] | 50.96 [42.37, 54.89] | 2 | 0 |
| mtbench/dynamic | fixed_g2_vs_sync_g4 | 5 | 20.92 [14.84, 24.18] | 8.40 [5.58, 10.82] | 3 | 0 |
| mtbench/dynamic | fixed_fast_vs_sync_g4 | 5 | 10.16 [3.80, 16.08] | -21.93 [-28.16, -11.34] | 0 | 0 |
| mtbench/dynamic | fixed_g8_vs_sync_g4 | 5 | -6.67 [-11.90, 2.45] | -84.67 [-96.26, -64.42] | 2 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_sync_g4 | 5 | 23.71 [22.32, 25.57] | -4.97 [-15.73, 2.88] | 2 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_sync_g4 | 5 | 20.22 [14.77, 23.19] | 9.43 [5.06, 12.70] | 3 | 0 |
| mtbench/pooled | sync_g4 | 5 | -13.04 [-16.14, -9.72] | 15.00 [8.71, 18.62] | 0 | 0 |
| mtbench/pooled | fixed_g2 | 5 | 5.74 [-0.95, 11.36] | 22.59 [16.02, 26.00] | 8 | 0 |
| mtbench/pooled | fixed_g8 | 5 | -16.17 [-19.34, -10.92] | -52.18 [-58.19, -43.71] | 6 | 0 |
| mtbench/pooled | markov_w0_dist | 5 | 9.98 [4.40, 15.01] | 9.85 [-0.59, 16.15] | 5 | 0 |
| mtbench/pooled | markov_w05_dist | 5 | 3.98 [-1.64, 10.92] | 23.42 [15.45, 28.01] | 7 | 0 |
| mtbench/pooled | sync_g4_vs_fixed_g2 | 5 | -17.76 [-20.50, -14.49] | -9.81 [-14.82, -6.44] | 8 | 0 |
| mtbench/pooled | fixed_fast_vs_fixed_g2 | 5 | -5.43 [-10.20, 0.96] | -29.19 [-35.13, -19.08] | 8 | 0 |
| mtbench/pooled | fixed_g8_vs_fixed_g2 | 5 | -20.72 [-26.42, -10.58] | -96.60 [-111.65, -71.86] | 6 | 0 |
| mtbench/pooled | markov_w0_dist_vs_fixed_g2 | 5 | 4.01 [2.24, 7.33] | -16.46 [-22.58, -10.10] | 5 | 0 |
| mtbench/pooled | markov_w05_dist_vs_fixed_g2 | 5 | -1.67 [-4.16, 2.45] | 1.07 [-0.86, 4.23] | 4 | 0 |
| mtbench/pooled | sync_g4_vs_fixed_g8 | 5 | 3.73 [-5.44, 10.54] | 44.15 [36.69, 48.23] | 6 | 0 |
| mtbench/pooled | fixed_g2_vs_fixed_g8 | 5 | 26.13 [11.84, 35.91] | 49.14 [41.81, 52.75] | 6 | 0 |
| mtbench/pooled | fixed_fast_vs_fixed_g8 | 5 | 19.28 [12.26, 23.98] | 34.29 [30.41, 36.79] | 6 | 0 |
| mtbench/pooled | markov_w0_dist_vs_fixed_g8 | 5 | 31.19 [18.49, 40.59] | 40.76 [30.30, 46.73] | 8 | 0 |
| mtbench/pooled | markov_w05_dist_vs_fixed_g8 | 5 | 24.03 [11.93, 34.86] | 49.68 [41.41, 54.33] | 7 | 0 |
| mtbench/pooled | fixed_g2_vs_sync_g4 | 5 | 21.59 [16.94, 25.79] | 8.93 [6.05, 12.91] | 8 | 0 |
| mtbench/pooled | fixed_fast_vs_sync_g4 | 5 | 14.99 [10.77, 19.25] | -17.65 [-22.88, -9.54] | 0 | 0 |
| mtbench/pooled | fixed_g8_vs_sync_g4 | 5 | -3.60 [-9.53, 5.75] | -79.04 [-93.15, -57.95] | 6 | 0 |
| mtbench/pooled | markov_w0_dist_vs_sync_g4 | 5 | 26.47 [24.38, 28.74] | -6.06 [-10.92, -1.77] | 5 | 0 |
| mtbench/pooled | markov_w05_dist_vs_sync_g4 | 5 | 19.56 [16.16, 23.45] | 9.90 [5.95, 13.67] | 7 | 0 |
| humaneval/low | sync_g4 | 5 | -48.87 [-53.59, -42.62] | -40.45 [-54.32, -27.36] | 0 | 0 |
| humaneval/low | fixed_g2 | 5 | -9.67 [-10.80, -7.81] | -4.25 [-9.48, 0.58] | 0 | 0 |
| humaneval/low | fixed_g8 | 5 | 16.71 [4.83, 32.34] | -4.98 [-11.07, 0.17] | 0 | 0 |
| humaneval/low | markov_w0_dist | 5 | -1.74 [-13.68, 15.29] | -3.62 [-8.37, 0.95] | 0 | 0 |
| humaneval/low | markov_w05_dist | 5 | -3.77 [-7.69, 0.51] | -2.19 [-4.73, 1.14] | 0 | 0 |
| humaneval/low | sync_g4_vs_fixed_g2 | 5 | -43.40 [-47.92, -36.72] | -34.71 [-41.93, -28.04] | 0 | 0 |
| humaneval/low | fixed_fast_vs_fixed_g2 | 5 | 10.70 [8.48, 12.11] | 4.08 [-0.59, 8.66] | 0 | 0 |
| humaneval/low | fixed_g8_vs_fixed_g2 | 5 | 29.19 [16.24, 47.12] | -0.70 [-10.62, 8.12] | 0 | 0 |
| humaneval/low | markov_w0_dist_vs_fixed_g2 | 5 | 8.77 [-5.45, 29.06] | 0.61 [-1.74, 2.66] | 0 | 0 |
| humaneval/low | markov_w05_dist_vs_fixed_g2 | 5 | 6.53 [1.17, 11.79] | 1.98 [-2.51, 5.81] | 0 | 0 |
| humaneval/low | sync_g4_vs_fixed_g8 | 5 | -56.19 [-63.02, -48.22] | -33.78 [-54.55, -15.76] | 0 | 0 |
| humaneval/low | fixed_g2_vs_fixed_g8 | 5 | -22.60 [-32.03, -13.97] | 0.69 [-8.84, 9.60] | 0 | 0 |
| humaneval/low | fixed_fast_vs_fixed_g8 | 5 | -14.31 [-24.44, -4.61] | 4.74 [-0.17, 9.97] | 0 | 0 |
| humaneval/low | markov_w0_dist_vs_fixed_g8 | 5 | -15.81 [-22.23, -8.61] | 1.29 [-7.80, 10.22] | 0 | 0 |
| humaneval/low | markov_w05_dist_vs_fixed_g8 | 5 | -17.54 [-29.24, -4.72] | 2.65 [-4.26, 7.64] | 0 | 0 |
| humaneval/low | fixed_g2_vs_sync_g4 | 5 | 76.67 [58.03, 92.01] | 25.77 [21.90, 29.54] | 0 | 0 |
| humaneval/low | fixed_fast_vs_sync_g4 | 5 | 95.58 [74.26, 115.46] | 28.80 [21.48, 35.20] | 0 | 0 |
| humaneval/low | fixed_g8_vs_sync_g4 | 5 | 128.25 [93.13, 170.39] | 25.25 [13.61, 35.30] | 0 | 0 |
| humaneval/low | markov_w0_dist_vs_sync_g4 | 5 | 92.16 [62.63, 134.33] | 26.22 [22.23, 30.35] | 0 | 0 |
| humaneval/low | markov_w05_dist_vs_sync_g4 | 5 | 88.20 [69.21, 105.73] | 27.24 [20.21, 32.68] | 0 | 0 |
| humaneval/high | sync_g4 | 5 | -35.17 [-36.46, -34.08] | -30.75 [-35.55, -25.32] | 0 | 0 |
| humaneval/high | fixed_g2 | 5 | -35.98 [-38.07, -33.76] | -36.41 [-44.22, -28.79] | 0 | 0 |
| humaneval/high | fixed_g8 | 5 | 56.62 [45.94, 68.36] | 18.66 [11.91, 24.75] | 0 | 0 |
| humaneval/high | markov_w0_dist | 5 | 46.91 [37.74, 57.66] | 19.29 [12.35, 26.22] | 0 | 0 |
| humaneval/high | markov_w05_dist | 5 | 32.87 [27.11, 43.74] | 14.11 [8.46, 20.58] | 0 | 0 |
| humaneval/high | sync_g4_vs_fixed_g2 | 5 | 1.27 [-1.67, 4.29] | 4.15 [-0.57, 7.81] | 0 | 0 |
| humaneval/high | fixed_fast_vs_fixed_g2 | 5 | 56.21 [50.97, 61.46] | 26.69 [22.36, 30.66] | 0 | 0 |
| humaneval/high | fixed_g8_vs_fixed_g2 | 5 | 144.66 [121.05, 171.62] | 40.37 [34.65, 45.78] | 0 | 0 |
| humaneval/high | markov_w0_dist_vs_fixed_g2 | 5 | 129.50 [109.75, 150.54] | 40.83 [35.17, 45.88] | 0 | 0 |
| humaneval/high | markov_w05_dist_vs_fixed_g2 | 5 | 107.55 [94.11, 125.21] | 37.04 [32.52, 41.03] | 0 | 0 |
| humaneval/high | sync_g4_vs_fixed_g8 | 5 | -58.61 [-61.93, -54.97] | -60.73 [-75.68, -45.36] | 0 | 0 |
| humaneval/high | fixed_g2_vs_fixed_g8 | 5 | -59.13 [-63.18, -54.76] | -67.70 [-84.44, -53.01] | 0 | 0 |
| humaneval/high | fixed_fast_vs_fixed_g8 | 5 | -36.15 [-40.60, -31.48] | -22.93 [-32.89, -13.52] | 0 | 0 |
| humaneval/high | markov_w0_dist_vs_fixed_g8 | 5 | -6.20 [-10.85, -2.89] | 0.77 [-2.93, 4.15] | 0 | 0 |
| humaneval/high | markov_w05_dist_vs_fixed_g8 | 5 | -15.17 [-22.61, -8.21] | -5.59 [-12.08, -1.26] | 0 | 0 |
| humaneval/high | fixed_g2_vs_sync_g4 | 5 | -1.25 [-4.11, 1.70] | -4.33 [-8.47, 0.57] | 0 | 0 |
| humaneval/high | fixed_fast_vs_sync_g4 | 5 | 54.26 [51.69, 57.39] | 23.52 [20.21, 26.23] | 0 | 0 |
| humaneval/high | fixed_g8_vs_sync_g4 | 5 | 141.60 [122.09, 162.67] | 37.78 [31.21, 43.08] | 0 | 0 |
| humaneval/high | markov_w0_dist_vs_sync_g4 | 5 | 126.63 [109.58, 145.37] | 38.27 [31.94, 44.60] | 0 | 0 |
| humaneval/high | markov_w05_dist_vs_sync_g4 | 5 | 104.96 [93.45, 125.46] | 34.31 [28.65, 40.10] | 0 | 0 |
| humaneval/dynamic | sync_g4 | 5 | -40.76 [-47.88, -35.88] | -38.87 [-52.58, -31.78] | 0 | 0 |
| humaneval/dynamic | fixed_g2 | 5 | -26.04 [-29.14, -22.62] | -23.89 [-29.56, -19.17] | 0 | 0 |
| humaneval/dynamic | fixed_g8 | 5 | 38.64 [24.41, 54.16] | 8.15 [1.32, 14.94] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist | 5 | 11.58 [-3.20, 28.40] | 1.68 [-7.41, 10.53] | 0 | 0 |
| humaneval/dynamic | markov_w05_dist | 5 | 20.43 [11.80, 28.61] | 2.48 [-5.38, 9.66] | 0 | 0 |
| humaneval/dynamic | sync_g4_vs_fixed_g2 | 5 | -19.90 [-32.28, -11.81] | -12.09 [-26.26, -4.59] | 0 | 0 |
| humaneval/dynamic | fixed_fast_vs_fixed_g2 | 5 | 35.21 [29.24, 41.13] | 19.28 [16.09, 22.82] | 0 | 0 |
| humaneval/dynamic | fixed_g8_vs_fixed_g2 | 5 | 87.46 [69.80, 105.92] | 25.86 [18.90, 32.55] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_fixed_g2 | 5 | 50.86 [29.49, 74.10] | 20.64 [11.67, 29.33] | 0 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_fixed_g2 | 5 | 62.83 [46.48, 74.85] | 21.28 [12.51, 29.03] | 0 | 0 |
| humaneval/dynamic | sync_g4_vs_fixed_g8 | 5 | -57.27 [-61.80, -52.91] | -51.20 [-65.88, -37.86] | 0 | 0 |
| humaneval/dynamic | fixed_g2_vs_fixed_g8 | 5 | -46.65 [-51.44, -41.11] | -34.89 [-48.25, -23.31] | 0 | 0 |
| humaneval/dynamic | fixed_fast_vs_fixed_g8 | 5 | -27.87 [-35.13, -19.62] | -8.87 [-17.56, -1.33] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_fixed_g8 | 5 | -19.52 [-25.01, -13.41] | -7.04 [-9.35, -4.77] | 0 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_fixed_g8 | 5 | -13.14 [-18.73, -8.35] | -6.18 [-13.08, -1.74] | 0 | 0 |
| humaneval/dynamic | fixed_g2_vs_sync_g4 | 5 | 24.85 [13.40, 47.67] | 10.79 [4.39, 20.80] | 0 | 0 |
| humaneval/dynamic | fixed_fast_vs_sync_g4 | 5 | 68.80 [55.96, 91.86] | 27.99 [24.11, 34.46] | 0 | 0 |
| humaneval/dynamic | fixed_g8_vs_sync_g4 | 5 | 134.03 [112.35, 161.78] | 33.86 [27.46, 39.71] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_sync_g4 | 5 | 88.35 [74.07, 104.07] | 29.21 [21.12, 35.77] | 0 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_sync_g4 | 5 | 103.28 [92.15, 117.76] | 29.78 [26.08, 32.82] | 0 | 0 |
| humaneval/pooled | sync_g4 | 5 | -40.43 [-44.53, -37.31] | -35.90 [-44.87, -29.26] | 0 | 0 |
| humaneval/pooled | fixed_g2 | 5 | -28.33 [-28.86, -27.78] | -24.07 [-27.81, -20.34] | 0 | 0 |
| humaneval/pooled | fixed_g8 | 5 | 40.37 [29.01, 53.25] | 9.15 [2.84, 14.57] | 0 | 0 |
| humaneval/pooled | markov_w0_dist | 5 | 21.29 [11.77, 33.42] | 7.64 [3.34, 11.07] | 0 | 0 |
| humaneval/pooled | markov_w05_dist | 5 | 19.16 [17.28, 20.80] | 6.12 [2.90, 9.34] | 0 | 0 |
| humaneval/pooled | sync_g4_vs_fixed_g2 | 5 | -16.88 [-23.16, -12.06] | -9.54 [-16.69, -5.56] | 0 | 0 |
| humaneval/pooled | fixed_fast_vs_fixed_g2 | 5 | 39.54 [38.47, 40.56] | 19.40 [16.90, 21.76] | 0 | 0 |
| humaneval/pooled | fixed_g8_vs_fixed_g2 | 5 | 95.86 [78.91, 115.09] | 26.78 [19.84, 32.81] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_vs_fixed_g2 | 5 | 69.24 [55.46, 87.54] | 25.56 [20.39, 30.16] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_vs_fixed_g2 | 5 | 66.28 [63.03, 69.03] | 24.33 [20.10, 28.47] | 0 | 0 |
| humaneval/pooled | sync_g4_vs_fixed_g8 | 5 | -57.56 [-61.78, -52.80] | -49.59 [-65.86, -33.94] | 0 | 0 |
| humaneval/pooled | fixed_g2_vs_fixed_g8 | 5 | -48.94 [-53.51, -44.11] | -36.57 [-48.84, -24.76] | 0 | 0 |
| humaneval/pooled | fixed_fast_vs_fixed_g8 | 5 | -28.76 [-34.75, -22.49] | -10.08 [-17.06, -2.92] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_vs_fixed_g8 | 5 | -13.59 [-17.41, -9.78] | -1.66 [-3.95, 0.62] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_vs_fixed_g8 | 5 | -15.11 [-21.77, -8.22] | -3.34 [-7.70, 0.60] | 0 | 0 |
| humaneval/pooled | fixed_g2_vs_sync_g4 | 5 | 20.30 [13.71, 30.15] | 8.71 [5.27, 14.30] | 0 | 0 |
| humaneval/pooled | fixed_fast_vs_sync_g4 | 5 | 67.86 [59.50, 80.28] | 26.41 [22.63, 30.97] | 0 | 0 |
| humaneval/pooled | fixed_g8_vs_sync_g4 | 5 | 135.63 [111.87, 161.68] | 33.15 [25.34, 39.71] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_vs_sync_g4 | 5 | 103.60 [84.64, 126.31] | 32.04 [25.61, 38.15] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_vs_sync_g4 | 5 | 100.04 [87.90, 117.20] | 30.92 [25.85, 35.91] | 0 | 0 |
| gsm8k/low | sync_g4 | 5 | -35.98 [-39.67, -29.91] | 1.75 [-2.54, 5.93] | 0 | 0 |
| gsm8k/low | fixed_g2 | 5 | -7.50 [-14.81, 7.36] | 15.80 [8.45, 20.86] | 1 | 0 |
| gsm8k/low | fixed_g8 | 5 | -17.00 [-19.08, -13.49] | -39.25 [-42.43, -36.61] | 1 | 0 |
| gsm8k/low | markov_w0_dist | 5 | -16.45 [-24.68, 4.86] | 9.17 [5.10, 12.44] | 1 | 0 |
| gsm8k/low | markov_w05_dist | 5 | -15.69 [-21.37, -8.65] | 13.54 [9.64, 17.86] | 1 | 0 |
| gsm8k/low | sync_g4_vs_fixed_g2 | 5 | -30.78 [-35.43, -24.01] | -16.69 [-22.75, -7.03] | 1 | 0 |
| gsm8k/low | fixed_fast_vs_fixed_g2 | 5 | 8.11 [-6.86, 17.39] | -18.77 [-26.36, -9.23] | 1 | 0 |
| gsm8k/low | fixed_g8_vs_fixed_g2 | 5 | -10.27 [-19.99, -3.88] | -65.38 [-75.48, -54.00] | 2 | 0 |
| gsm8k/low | markov_w0_dist_vs_fixed_g2 | 5 | -9.67 [-21.46, 12.15] | -7.88 [-17.80, 2.62] | 0 | 0 |
| gsm8k/low | markov_w05_dist_vs_fixed_g2 | 5 | -8.85 [-21.42, 1.15] | -2.69 [-10.98, 6.25] | 0 | 0 |
| gsm8k/low | sync_g4_vs_fixed_g8 | 5 | -22.87 [-26.98, -16.23] | 29.44 [25.02, 33.77] | 1 | 0 |
| gsm8k/low | fixed_g2_vs_fixed_g8 | 5 | 11.44 [4.04, 24.99] | 39.53 [35.06, 43.01] | 2 | 0 |
| gsm8k/low | fixed_fast_vs_fixed_g8 | 5 | 20.48 [15.60, 23.57] | 28.18 [26.80, 29.79] | 1 | 0 |
| gsm8k/low | markov_w0_dist_vs_fixed_g8 | 5 | 0.66 [-10.43, 26.53] | 34.77 [30.96, 38.57] | 2 | 0 |
| gsm8k/low | markov_w05_dist_vs_fixed_g8 | 5 | 1.58 [-7.19, 9.38] | 37.91 [34.21, 42.00] | 2 | 0 |
| gsm8k/low | fixed_g2_vs_sync_g4 | 5 | 44.48 [31.60, 54.88] | 14.30 [6.57, 18.54] | 1 | 0 |
| gsm8k/low | fixed_fast_vs_sync_g4 | 5 | 56.20 [42.68, 65.74] | -1.78 [-6.30, 2.48] | 0 | 0 |
| gsm8k/low | fixed_g8_vs_sync_g4 | 5 | 29.64 [19.38, 36.94] | -41.73 [-50.99, -33.37] | 1 | 0 |
| gsm8k/low | markov_w0_dist_vs_sync_g4 | 5 | 30.50 [18.48, 51.05] | 7.55 [2.61, 11.67] | 1 | 0 |
| gsm8k/low | markov_w05_dist_vs_sync_g4 | 5 | 31.69 [19.45, 46.12] | 12.00 [7.86, 15.51] | 1 | 0 |
| gsm8k/high | sync_g4 | 5 | -23.51 [-28.15, -19.65] | -8.72 [-15.94, -3.28] | 0 | 0 |
| gsm8k/high | fixed_g2 | 5 | -21.47 [-24.90, -17.36] | -12.43 [-18.20, -6.50] | 1 | 0 |
| gsm8k/high | fixed_g8 | 5 | 16.69 [9.41, 19.96] | -15.45 [-21.51, -12.54] | 1 | 0 |
| gsm8k/high | markov_w0_dist | 5 | 14.22 [11.76, 17.09] | -10.26 [-12.31, -5.32] | 1 | 0 |
| gsm8k/high | markov_w05_dist | 5 | -4.15 [-8.81, 1.40] | -5.11 [-6.50, -2.44] | 1 | 0 |
| gsm8k/high | sync_g4_vs_fixed_g2 | 5 | -2.60 [-5.88, -1.23] | 3.30 [0.29, 4.71] | 1 | 0 |
| gsm8k/high | fixed_fast_vs_fixed_g2 | 5 | 27.34 [21.01, 33.16] | 11.06 [6.10, 15.40] | 1 | 0 |
| gsm8k/high | fixed_g8_vs_fixed_g2 | 5 | 48.60 [34.66, 58.67] | -2.69 [-13.04, 3.70] | 2 | 0 |
| gsm8k/high | markov_w0_dist_vs_fixed_g2 | 5 | 45.45 [35.91, 54.25] | 1.93 [-4.81, 9.49] | 0 | 0 |
| gsm8k/high | markov_w05_dist_vs_fixed_g2 | 5 | 22.05 [10.76, 34.46] | 6.51 [2.32, 10.77] | 0 | 0 |
| gsm8k/high | sync_g4_vs_fixed_g8 | 5 | -34.45 [-38.64, -28.24] | 5.83 [-1.58, 12.81] | 1 | 0 |
| gsm8k/high | fixed_g2_vs_fixed_g8 | 5 | -32.70 [-36.97, -25.74] | 2.62 [-3.85, 11.53] | 2 | 0 |
| gsm8k/high | fixed_fast_vs_fixed_g8 | 5 | -14.30 [-16.64, -8.60] | 13.39 [11.14, 17.70] | 1 | 0 |
| gsm8k/high | markov_w0_dist_vs_fixed_g8 | 5 | -2.12 [-5.01, 5.10] | 4.50 [1.43, 11.60] | 2 | 0 |
| gsm8k/high | markov_w05_dist_vs_fixed_g8 | 5 | -17.87 [-22.12, -11.77] | 8.96 [6.21, 14.42] | 2 | 0 |
| gsm8k/high | fixed_g2_vs_sync_g4 | 5 | 2.67 [1.25, 6.25] | -3.41 [-4.94, -0.30] | 1 | 0 |
| gsm8k/high | fixed_fast_vs_sync_g4 | 5 | 30.74 [24.46, 39.17] | 8.02 [3.18, 13.75] | 0 | 0 |
| gsm8k/high | fixed_g8_vs_sync_g4 | 5 | 52.57 [39.34, 62.98] | -6.19 [-14.69, 1.56] | 1 | 0 |
| gsm8k/high | markov_w0_dist_vs_sync_g4 | 5 | 49.34 [39.43, 62.72] | -1.42 [-8.08, 9.04] | 1 | 0 |
| gsm8k/high | markov_w05_dist_vs_sync_g4 | 5 | 25.31 [13.49, 38.55] | 3.32 [-0.72, 9.77] | 1 | 0 |
| gsm8k/dynamic | sync_g4 | 5 | -29.28 [-33.09, -22.06] | -4.35 [-7.77, -0.36] | 0 | 0 |
| gsm8k/dynamic | fixed_g2 | 5 | -11.05 [-17.69, -1.55] | 6.75 [-1.39, 15.16] | 0 | 0 |
| gsm8k/dynamic | fixed_g8 | 5 | 1.16 [-8.24, 7.30] | -29.06 [-40.71, -21.91] | 2 | 0 |
| gsm8k/dynamic | markov_w0_dist | 5 | 4.20 [-0.19, 7.68] | 4.37 [1.21, 10.42] | 1 | 0 |
| gsm8k/dynamic | markov_w05_dist | 5 | -8.02 [-13.31, -3.67] | 6.92 [2.21, 9.69] | 0 | 0 |
| gsm8k/dynamic | sync_g4_vs_fixed_g2 | 5 | -20.49 [-28.19, -13.30] | -11.91 [-20.20, -5.34] | 0 | 0 |
| gsm8k/dynamic | fixed_fast_vs_fixed_g2 | 5 | 12.43 [1.57, 21.49] | -7.24 [-17.87, 1.37] | 0 | 0 |
| gsm8k/dynamic | fixed_g8_vs_fixed_g2 | 5 | 13.73 [-5.11, 29.15] | -38.41 [-63.01, -21.72] | 2 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_fixed_g2 | 5 | 17.15 [2.77, 29.46] | -2.56 [-8.74, 4.94] | 1 | 0 |
| gsm8k/dynamic | markov_w05_dist_vs_fixed_g2 | 5 | 3.41 [-7.64, 12.00] | 0.18 [-7.61, 5.00] | 0 | 0 |
| gsm8k/dynamic | sync_g4_vs_fixed_g8 | 5 | -30.09 [-34.91, -20.41] | 19.15 [12.04, 28.68] | 2 | 0 |
| gsm8k/dynamic | fixed_g2_vs_fixed_g8 | 5 | -12.07 [-22.57, 5.38] | 27.75 [17.85, 38.65] | 2 | 0 |
| gsm8k/dynamic | fixed_fast_vs_fixed_g8 | 5 | -1.15 [-6.81, 8.97] | 22.52 [17.97, 28.93] | 2 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_fixed_g8 | 5 | 3.00 [-0.67, 9.35] | 25.90 [19.01, 35.76] | 1 | 0 |
| gsm8k/dynamic | markov_w05_dist_vs_fixed_g8 | 5 | -9.08 [-13.68, -2.57] | 27.88 [21.55, 34.28] | 2 | 0 |
| gsm8k/dynamic | fixed_g2_vs_sync_g4 | 5 | 25.78 [15.34, 39.26] | 10.64 [5.07, 16.80] | 0 | 0 |
| gsm8k/dynamic | fixed_fast_vs_sync_g4 | 5 | 41.40 [28.30, 49.45] | 4.17 [0.36, 7.21] | 0 | 0 |
| gsm8k/dynamic | fixed_g8_vs_sync_g4 | 5 | 43.05 [25.65, 53.62] | -23.68 [-40.21, -13.68] | 2 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_sync_g4 | 5 | 47.34 [34.34, 52.59] | 8.36 [5.68, 12.87] | 1 | 0 |
| gsm8k/dynamic | markov_w05_dist_vs_sync_g4 | 5 | 30.06 [20.31, 34.11] | 10.80 [5.79, 13.20] | 0 | 0 |
| gsm8k/pooled | sync_g4 | 5 | -28.37 [-30.96, -23.72] | -4.39 [-9.23, 0.11] | 0 | 0 |
| gsm8k/pooled | fixed_g2 | 5 | -15.59 [-20.02, -8.71] | 1.67 [-3.71, 6.65] | 2 | 0 |
| gsm8k/pooled | fixed_g8 | 5 | 2.73 [-2.62, 6.12] | -26.49 [-32.46, -22.56] | 4 | 0 |
| gsm8k/pooled | markov_w0_dist | 5 | 2.95 [0.68, 8.76] | -0.09 [-2.08, 3.14] | 3 | 0 |
| gsm8k/pooled | markov_w05_dist | 5 | -8.09 [-12.25, -4.04] | 3.99 [2.28, 5.67] | 2 | 0 |
| gsm8k/pooled | sync_g4_vs_fixed_g2 | 5 | -15.14 [-16.94, -13.53] | -6.16 [-8.50, -4.57] | 2 | 0 |
| gsm8k/pooled | fixed_fast_vs_fixed_g2 | 5 | 18.47 [9.54, 25.02] | -1.70 [-7.13, 3.58] | 2 | 0 |
| gsm8k/pooled | fixed_g8_vs_fixed_g2 | 5 | 21.70 [8.63, 31.27] | -28.64 [-40.71, -18.29] | 6 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_fixed_g2 | 5 | 21.96 [14.55, 29.55] | -1.79 [-7.65, 5.62] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_fixed_g2 | 5 | 8.89 [-0.26, 18.45] | 2.37 [-2.06, 6.05] | 0 | 0 |
| gsm8k/pooled | sync_g4_vs_fixed_g8 | 5 | -30.27 [-34.66, -23.16] | 17.48 [11.27, 23.97] | 4 | 0 |
| gsm8k/pooled | fixed_g2_vs_fixed_g8 | 5 | -17.83 [-23.82, -7.94] | 22.26 [15.46, 28.93] | 6 | 0 |
| gsm8k/pooled | fixed_fast_vs_fixed_g8 | 5 | -2.66 [-5.77, 2.70] | 20.94 [18.41, 24.51] | 4 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_fixed_g8 | 5 | 0.21 [-4.41, 10.18] | 20.87 [17.39, 26.62] | 5 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_fixed_g8 | 5 | -10.53 [-14.08, -6.00] | 24.10 [20.54, 28.83] | 6 | 0 |
| gsm8k/pooled | fixed_g2_vs_sync_g4 | 5 | 17.84 [15.65, 20.40] | 5.80 [4.37, 7.84] | 2 | 0 |
| gsm8k/pooled | fixed_fast_vs_sync_g4 | 5 | 39.61 [31.09, 44.83] | 4.20 [-0.11, 8.45] | 0 | 0 |
| gsm8k/pooled | fixed_g8_vs_sync_g4 | 5 | 43.42 [30.15, 53.04] | -21.18 [-31.53, -12.70] | 4 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_sync_g4 | 5 | 43.72 [38.09, 51.30] | 4.11 [0.36, 9.81] | 3 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_sync_g4 | 5 | 28.32 [19.51, 37.13] | 8.03 [5.41, 10.66] | 2 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
