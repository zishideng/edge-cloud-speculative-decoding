# Progress probe: full_110

State: complete; 1540/1540 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high; pooled = low+high.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | sync_g4 | 110 | 27463 | 13.864 | 0.5843 | 11 | 0.00 |
| all/low | fixed_g2 | 110 | 27493 | 15.937 | 0.6195 | 12 | 43.08 |
| all/low | fixed_fast | 110 | 27473 | 18.073 | 0.6946 | 11 | 39.15 |
| all/low | fixed_g8 | 110 | 27023 | 14.539 | 0.9659 | 8 | 25.90 |
| all/low | adaedl | 110 | 27175 | 13.297 | 0.6695 | 9 | 0.00 |
| all/low | markov_w0 | 110 | 27500 | 19.193 | 0.6609 | 12 | 44.34 |
| all/low | markov_w05 | 110 | 27527 | 18.418 | 0.6219 | 12 | 45.66 |
| all/high | sync_g4 | 110 | 27647 | 9.737 | 0.7161 | 12 | 0.00 |
| all/high | fixed_g2 | 110 | 27602 | 9.778 | 0.7959 | 12 | 43.17 |
| all/high | fixed_fast | 110 | 27647 | 12.711 | 0.8016 | 12 | 39.14 |
| all/high | fixed_g8 | 110 | 27186 | 13.414 | 0.9925 | 9 | 26.22 |
| all/high | adaedl | 110 | 27356 | 9.832 | 0.7927 | 10 | 0.00 |
| all/high | markov_w0 | 110 | 27340 | 14.301 | 0.8847 | 11 | 40.16 |
| all/high | markov_w05 | 110 | 27461 | 12.679 | 0.7836 | 12 | 44.70 |
| all/pooled | sync_g4 | 220 | 55110 | 11.433 | 0.6504 | 23 | 0.00 |
| all/pooled | fixed_g2 | 220 | 55095 | 12.114 | 0.7079 | 24 | 43.12 |
| all/pooled | fixed_fast | 220 | 55120 | 14.917 | 0.7483 | 23 | 39.14 |
| all/pooled | fixed_g8 | 220 | 54209 | 13.952 | 0.9792 | 17 | 26.06 |
| all/pooled | adaedl | 220 | 54531 | 11.300 | 0.7313 | 19 | 0.00 |
| all/pooled | markov_w0 | 220 | 54840 | 16.397 | 0.7725 | 23 | 41.97 |
| all/pooled | markov_w05 | 220 | 54988 | 15.023 | 0.7027 | 24 | 45.18 |
| gsm8k/low | sync_g4 | 50 | 10164 | 15.126 | 0.5497 | 5 | 0.00 |
| gsm8k/low | fixed_g2 | 50 | 10185 | 17.228 | 0.5838 | 5 | 45.73 |
| gsm8k/low | fixed_fast | 50 | 10164 | 19.892 | 0.6453 | 5 | 42.83 |
| gsm8k/low | fixed_g8 | 50 | 9838 | 15.871 | 0.8817 | 3 | 29.84 |
| gsm8k/low | adaedl | 50 | 9892 | 13.893 | 0.6426 | 4 | 0.00 |
| gsm8k/low | markov_w0 | 50 | 10182 | 20.364 | 0.6135 | 5 | 47.26 |
| gsm8k/low | markov_w05 | 50 | 10182 | 20.058 | 0.5864 | 5 | 47.30 |
| gsm8k/high | sync_g4 | 50 | 10217 | 10.398 | 0.6819 | 5 | 0.00 |
| gsm8k/high | fixed_g2 | 50 | 10238 | 10.489 | 0.7562 | 5 | 45.78 |
| gsm8k/high | fixed_fast | 50 | 10217 | 13.787 | 0.7492 | 5 | 42.81 |
| gsm8k/high | fixed_g8 | 50 | 9888 | 14.974 | 0.8973 | 3 | 29.92 |
| gsm8k/high | adaedl | 50 | 9942 | 10.519 | 0.7520 | 4 | 0.00 |
| gsm8k/high | markov_w0 | 50 | 9942 | 15.647 | 0.8067 | 4 | 43.15 |
| gsm8k/high | markov_w05 | 50 | 9974 | 13.580 | 0.7497 | 5 | 45.47 |
| gsm8k/pooled | sync_g4 | 100 | 20381 | 12.318 | 0.6160 | 10 | 0.00 |
| gsm8k/pooled | fixed_g2 | 100 | 20423 | 13.031 | 0.6702 | 10 | 45.76 |
| gsm8k/pooled | fixed_fast | 100 | 20381 | 16.279 | 0.6974 | 10 | 42.82 |
| gsm8k/pooled | fixed_g8 | 100 | 19726 | 15.409 | 0.8895 | 6 | 29.88 |
| gsm8k/pooled | adaedl | 100 | 19834 | 11.969 | 0.6974 | 8 | 0.00 |
| gsm8k/pooled | markov_w0 | 100 | 20124 | 17.724 | 0.7089 | 9 | 44.97 |
| gsm8k/pooled | markov_w05 | 100 | 20156 | 16.228 | 0.6672 | 10 | 46.40 |
| humaneval/low | sync_g4 | 30 | 9025 | 14.819 | 0.5321 | 1 | 0.00 |
| humaneval/low | fixed_g2 | 30 | 9020 | 17.240 | 0.5513 | 1 | 52.45 |
| humaneval/low | fixed_fast | 30 | 9035 | 21.210 | 0.5629 | 1 | 54.31 |
| humaneval/low | fixed_g8 | 30 | 9015 | 20.220 | 0.6800 | 0 | 44.91 |
| humaneval/low | adaedl | 30 | 9014 | 15.616 | 0.5559 | 0 | 0.00 |
| humaneval/low | markov_w0 | 30 | 9030 | 23.295 | 0.5475 | 1 | 56.58 |
| humaneval/low | markov_w05 | 30 | 9016 | 22.383 | 0.5474 | 1 | 56.10 |
| humaneval/high | sync_g4 | 30 | 9132 | 10.506 | 0.6517 | 1 | 0.00 |
| humaneval/high | fixed_g2 | 30 | 9127 | 10.432 | 0.7192 | 1 | 52.39 |
| humaneval/high | fixed_fast | 30 | 9132 | 14.834 | 0.6576 | 1 | 53.94 |
| humaneval/high | fixed_g8 | 30 | 9122 | 18.428 | 0.7054 | 0 | 45.13 |
| humaneval/high | adaedl | 30 | 9121 | 11.802 | 0.6567 | 0 | 0.00 |
| humaneval/high | markov_w0 | 30 | 9123 | 18.398 | 0.6772 | 1 | 54.41 |
| humaneval/high | markov_w05 | 30 | 9128 | 17.224 | 0.6660 | 1 | 55.48 |
| humaneval/pooled | sync_g4 | 60 | 18157 | 12.283 | 0.5923 | 2 | 0.00 |
| humaneval/pooled | fixed_g2 | 60 | 18147 | 12.980 | 0.6358 | 2 | 52.42 |
| humaneval/pooled | fixed_fast | 60 | 18167 | 17.442 | 0.6105 | 2 | 54.12 |
| humaneval/pooled | fixed_g8 | 60 | 18137 | 19.277 | 0.6928 | 0 | 45.02 |
| humaneval/pooled | adaedl | 60 | 18135 | 13.433 | 0.6066 | 0 | 0.00 |
| humaneval/pooled | markov_w0 | 60 | 18153 | 20.547 | 0.6127 | 2 | 55.39 |
| humaneval/pooled | markov_w05 | 60 | 18144 | 19.452 | 0.6070 | 2 | 55.77 |
| mtbench/low | sync_g4 | 30 | 8274 | 11.820 | 0.6838 | 5 | 0.00 |
| mtbench/low | fixed_g2 | 30 | 8288 | 13.572 | 0.7377 | 6 | 31.47 |
| mtbench/low | fixed_fast | 30 | 8274 | 14.188 | 0.8988 | 5 | 23.10 |
| mtbench/low | fixed_g8 | 30 | 8170 | 10.304 | 1.3827 | 5 | 10.07 |
| mtbench/low | adaedl | 30 | 8269 | 10.961 | 0.8255 | 5 | 0.00 |
| mtbench/low | markov_w0 | 30 | 8288 | 15.202 | 0.8426 | 6 | 31.45 |
| mtbench/low | markov_w05 | 30 | 8329 | 14.260 | 0.7461 | 6 | 32.27 |
| mtbench/high | sync_g4 | 30 | 8298 | 8.402 | 0.8292 | 6 | 0.00 |
| mtbench/high | fixed_g2 | 30 | 8237 | 8.476 | 0.9303 | 6 | 31.55 |
| mtbench/high | fixed_fast | 30 | 8298 | 10.140 | 1.0247 | 6 | 23.17 |
| mtbench/high | fixed_g8 | 30 | 8176 | 9.383 | 1.4280 | 6 | 10.53 |
| mtbench/high | adaedl | 30 | 8293 | 7.792 | 0.9910 | 6 | 0.00 |
| mtbench/high | markov_w0 | 30 | 8275 | 10.603 | 1.2072 | 6 | 27.75 |
| mtbench/high | markov_w05 | 30 | 8359 | 9.273 | 0.9524 | 6 | 28.50 |
| mtbench/pooled | sync_g4 | 60 | 16572 | 9.819 | 0.7566 | 11 | 0.00 |
| mtbench/pooled | fixed_g2 | 60 | 16525 | 10.442 | 0.8337 | 12 | 31.51 |
| mtbench/pooled | fixed_fast | 60 | 16572 | 11.825 | 0.9618 | 11 | 23.13 |
| mtbench/pooled | fixed_g8 | 60 | 16346 | 9.822 | 1.4054 | 11 | 10.30 |
| mtbench/pooled | adaedl | 60 | 16562 | 9.107 | 0.9084 | 11 | 0.00 |
| mtbench/pooled | markov_w0 | 60 | 16563 | 12.494 | 1.0247 | 12 | 29.26 |
| mtbench/pooled | markov_w05 | 60 | 16688 | 11.234 | 0.8494 | 12 | 30.51 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | sync_g4 | 110 | -23.29 [-25.57, -20.98] | 15.87 [13.65, 17.96] | 1 | 0 |
| all/low | fixed_g2 | 110 | -11.82 [-15.16, -8.00] | 10.80 [8.45, 13.06] | 10 | 1 |
| all/low | fixed_g8 | 110 | -19.55 [-22.40, -16.66] | -39.06 [-42.68, -35.41] | 13 | 0 |
| all/low | adaedl | 110 | -26.42 [-28.04, -24.57] | 3.61 [2.01, 5.17] | 8 | 0 |
| all/low | markov_w0 | 110 | 6.20 [3.62, 8.88] | 4.85 [2.86, 7.00] | 7 | 1 |
| all/low | markov_w05 | 110 | 1.91 [-0.40, 4.88] | 10.46 [8.45, 12.49] | 9 | 1 |
| all/low | fixed_g2_vs_sync_g4 | 110 | 14.96 [10.92, 18.76] | -6.03 [-7.86, -4.44] | 9 | 1 |
| all/low | fixed_fast_vs_sync_g4 | 110 | 30.36 [26.55, 34.35] | -18.87 [-21.90, -15.81] | 1 | 0 |
| all/low | fixed_g8_vs_sync_g4 | 110 | 4.87 [-0.49, 10.62] | -65.30 [-73.37, -57.14] | 12 | 0 |
| all/low | adaedl_vs_sync_g4 | 110 | -4.08 [-6.39, -1.47] | -14.57 [-16.79, -12.23] | 7 | 0 |
| all/low | markov_w0_vs_sync_g4 | 110 | 38.44 [33.28, 43.63] | -13.10 [-16.52, -9.45] | 8 | 1 |
| all/low | markov_w05_vs_sync_g4 | 110 | 32.85 [28.68, 37.47] | -6.44 [-8.11, -4.63] | 8 | 1 |
| all/high | sync_g4 | 110 | -23.40 [-24.77, -22.09] | 10.67 [8.74, 12.55] | 0 | 0 |
| all/high | fixed_g2 | 110 | -23.08 [-24.67, -21.50] | 0.71 [-1.37, 2.76] | 10 | 0 |
| all/high | fixed_g8 | 110 | 5.53 [2.26, 9.11] | -23.82 [-27.08, -20.26] | 13 | 0 |
| all/high | adaedl | 110 | -22.65 [-23.49, -21.86] | 1.11 [0.24, 1.96] | 6 | 0 |
| all/high | markov_w0 | 110 | 12.51 [10.21, 14.93] | -10.36 [-12.31, -8.31] | 12 | 0 |
| all/high | markov_w05 | 110 | -0.25 [-2.67, 2.49] | 2.25 [0.86, 3.65] | 10 | 1 |
| all/high | fixed_g2_vs_sync_g4 | 110 | 0.43 [-0.64, 1.53] | -11.14 [-11.93, -10.33] | 10 | 0 |
| all/high | fixed_fast_vs_sync_g4 | 110 | 30.55 [28.35, 32.92] | -11.94 [-14.35, -9.58] | 0 | 0 |
| all/high | fixed_g8_vs_sync_g4 | 110 | 37.77 [31.65, 44.51] | -38.60 [-45.07, -32.04] | 13 | 0 |
| all/high | adaedl_vs_sync_g4 | 110 | 0.98 [-1.16, 3.26] | -10.69 [-12.78, -8.54] | 6 | 0 |
| all/high | markov_w0_vs_sync_g4 | 110 | 46.88 [41.82, 52.31] | -23.54 [-28.09, -19.00] | 12 | 0 |
| all/high | markov_w05_vs_sync_g4 | 110 | 30.22 [25.17, 35.76] | -9.42 [-11.29, -7.53] | 10 | 1 |
| all/pooled | sync_g4 | 110 | -23.36 [-24.94, -21.86] | 13.07 [11.11, 14.99] | 1 | 0 |
| all/pooled | fixed_g2 | 110 | -18.79 [-20.73, -16.78] | 5.39 [3.36, 7.37] | 20 | 1 |
| all/pooled | fixed_g8 | 110 | -6.47 [-9.36, -3.36] | -30.87 [-34.21, -27.40] | 26 | 0 |
| all/pooled | adaedl | 110 | -24.25 [-25.18, -23.29] | 2.27 [1.19, 3.31] | 14 | 0 |
| all/pooled | markov_w0 | 110 | 9.92 [8.02, 11.97] | -3.23 [-4.76, -1.58] | 19 | 1 |
| all/pooled | markov_w05 | 110 | 0.71 [-1.32, 3.07] | 6.10 [4.53, 7.68] | 19 | 2 |
| all/pooled | fixed_g2_vs_sync_g4 | 110 | 5.96 [4.32, 7.69] | -8.83 [-9.84, -7.84] | 19 | 1 |
| all/pooled | fixed_fast_vs_sync_g4 | 110 | 30.48 [27.97, 33.23] | -15.04 [-17.63, -12.50] | 1 | 0 |
| all/pooled | fixed_g8_vs_sync_g4 | 110 | 22.04 [16.43, 28.14] | -50.55 [-57.67, -43.38] | 25 | 0 |
| all/pooled | adaedl_vs_sync_g4 | 110 | -1.16 [-3.18, 0.94] | -12.43 [-14.48, -10.36] | 13 | 0 |
| all/pooled | markov_w0_vs_sync_g4 | 110 | 43.42 [38.93, 48.24] | -18.76 [-22.51, -15.03] | 20 | 1 |
| all/pooled | markov_w05_vs_sync_g4 | 110 | 31.40 [26.95, 36.26] | -8.03 [-9.67, -6.30] | 18 | 2 |
| gsm8k/low | sync_g4 | 50 | -23.96 [-25.99, -21.75] | 14.82 [12.75, 16.96] | 0 | 0 |
| gsm8k/low | fixed_g2 | 50 | -13.39 [-19.05, -7.42] | 9.52 [5.71, 12.90] | 3 | 0 |
| gsm8k/low | fixed_g8 | 50 | -20.21 [-23.33, -17.22] | -36.63 [-39.05, -34.16] | 4 | 0 |
| gsm8k/low | adaedl | 50 | -30.16 [-32.07, -28.41] | 0.42 [-2.27, 3.35] | 4 | 0 |
| gsm8k/low | markov_w0 | 50 | 2.37 [-2.62, 6.35] | 4.93 [1.51, 8.08] | 2 | 0 |
| gsm8k/low | markov_w05 | 50 | 0.83 [-1.46, 3.11] | 9.12 [7.07, 11.25] | 2 | 0 |
| gsm8k/low | fixed_g2_vs_sync_g4 | 50 | 13.89 [4.80, 22.64] | -6.21 [-10.42, -3.05] | 3 | 0 |
| gsm8k/low | fixed_fast_vs_sync_g4 | 50 | 31.51 [27.80, 35.12] | -17.39 [-20.42, -14.61] | 0 | 0 |
| gsm8k/low | fixed_g8_vs_sync_g4 | 50 | 4.93 [-0.26, 10.06] | -60.40 [-66.32, -54.75] | 4 | 0 |
| gsm8k/low | adaedl_vs_sync_g4 | 50 | -8.15 [-12.02, -4.97] | -16.89 [-19.67, -14.49] | 4 | 0 |
| gsm8k/low | markov_w0_vs_sync_g4 | 50 | 34.63 [24.92, 42.01] | -11.61 [-16.14, -7.23] | 2 | 0 |
| gsm8k/low | markov_w05_vs_sync_g4 | 50 | 32.60 [26.29, 38.58] | -6.68 [-9.65, -3.57] | 2 | 0 |
| gsm8k/high | sync_g4 | 50 | -24.59 [-25.87, -23.48] | 8.98 [7.41, 10.34] | 0 | 0 |
| gsm8k/high | fixed_g2 | 50 | -23.92 [-25.25, -22.72] | -0.93 [-2.68, 0.68] | 3 | 0 |
| gsm8k/high | fixed_g8 | 50 | 8.61 [6.33, 11.04] | -19.78 [-21.97, -17.40] | 3 | 0 |
| gsm8k/high | adaedl | 50 | -23.71 [-24.82, -22.61] | -0.37 [-1.42, 0.86] | 3 | 0 |
| gsm8k/high | markov_w0 | 50 | 13.49 [9.88, 16.96] | -7.68 [-9.94, -5.23] | 3 | 0 |
| gsm8k/high | markov_w05 | 50 | -1.50 [-4.10, 1.45] | -0.07 [-1.87, 2.07] | 4 | 1 |
| gsm8k/high | fixed_g2_vs_sync_g4 | 50 | 0.88 [-0.15, 2.11] | -10.89 [-11.88, -9.79] | 3 | 0 |
| gsm8k/high | fixed_fast_vs_sync_g4 | 50 | 32.60 [30.69, 34.90] | -9.87 [-11.53, -8.00] | 0 | 0 |
| gsm8k/high | fixed_g8_vs_sync_g4 | 50 | 44.02 [40.21, 48.64] | -31.60 [-35.40, -27.19] | 3 | 0 |
| gsm8k/high | adaedl_vs_sync_g4 | 50 | 1.17 [-0.52, 3.28] | -10.28 [-12.00, -8.29] | 3 | 0 |
| gsm8k/high | markov_w0_vs_sync_g4 | 50 | 50.49 [44.69, 56.46] | -18.30 [-22.02, -14.23] | 3 | 0 |
| gsm8k/high | markov_w05_vs_sync_g4 | 50 | 30.61 [26.13, 36.12] | -9.94 [-12.44, -6.95] | 4 | 1 |
| gsm8k/pooled | sync_g4 | 50 | -24.33 [-25.65, -23.19] | 11.67 [10.08, 13.16] | 0 | 0 |
| gsm8k/pooled | fixed_g2 | 50 | -19.95 [-22.39, -17.75] | 3.89 [1.56, 6.03] | 6 | 0 |
| gsm8k/pooled | fixed_g8 | 50 | -5.34 [-7.96, -2.86] | -27.56 [-29.70, -25.26] | 7 | 0 |
| gsm8k/pooled | adaedl | 50 | -26.48 [-27.79, -25.31] | -0.01 [-1.59, 1.67] | 7 | 0 |
| gsm8k/pooled | markov_w0 | 50 | 8.88 [5.63, 12.07] | -1.66 [-3.87, 0.67] | 5 | 0 |
| gsm8k/pooled | markov_w05 | 50 | -0.31 [-2.56, 2.37] | 4.33 [2.61, 6.21] | 6 | 1 |
| gsm8k/pooled | fixed_g2_vs_sync_g4 | 50 | 5.79 [2.23, 9.17] | -8.81 [-10.92, -6.99] | 6 | 0 |
| gsm8k/pooled | fixed_fast_vs_sync_g4 | 50 | 32.15 [30.19, 34.50] | -13.22 [-15.15, -11.21] | 0 | 0 |
| gsm8k/pooled | fixed_g8_vs_sync_g4 | 50 | 25.09 [20.72, 29.82] | -44.41 [-49.06, -39.61] | 7 | 0 |
| gsm8k/pooled | adaedl_vs_sync_g4 | 50 | -2.84 [-4.91, -0.59] | -13.22 [-15.06, -11.31] | 7 | 0 |
| gsm8k/pooled | markov_w0_vs_sync_g4 | 50 | 43.89 [38.40, 49.65] | -15.10 [-18.58, -11.23] | 5 | 0 |
| gsm8k/pooled | markov_w05_vs_sync_g4 | 50 | 31.74 [27.34, 37.22] | -8.32 [-10.80, -5.46] | 6 | 1 |
| humaneval/low | sync_g4 | 30 | -30.13 [-34.03, -24.41] | 5.47 [2.58, 8.68] | 1 | 0 |
| humaneval/low | fixed_g2 | 30 | -18.71 [-23.62, -11.47] | 2.06 [-0.95, 5.40] | 2 | 0 |
| humaneval/low | fixed_g8 | 30 | -4.66 [-9.42, 0.20] | -20.81 [-24.55, -17.39] | 4 | 0 |
| humaneval/low | adaedl | 30 | -26.37 [-30.37, -20.80] | 1.24 [-1.38, 4.13] | 3 | 0 |
| humaneval/low | markov_w0 | 30 | 9.83 [4.57, 16.25] | 2.73 [0.46, 5.25] | 1 | 0 |
| humaneval/low | markov_w05 | 30 | 5.53 [-0.47, 14.20] | 2.76 [0.36, 5.84] | 3 | 0 |
| humaneval/low | fixed_g2_vs_sync_g4 | 30 | 16.34 [11.71, 22.28] | -3.60 [-5.57, -1.20] | 1 | 0 |
| humaneval/low | fixed_fast_vs_sync_g4 | 30 | 43.12 [32.30, 51.58] | -5.78 [-9.51, -2.64] | 1 | 0 |
| humaneval/low | fixed_g8_vs_sync_g4 | 30 | 36.45 [27.88, 44.87] | -27.79 [-33.38, -22.33] | 3 | 0 |
| humaneval/low | adaedl_vs_sync_g4 | 30 | 5.37 [1.23, 10.12] | -4.47 [-7.22, -1.63] | 2 | 0 |
| humaneval/low | markov_w0_vs_sync_g4 | 30 | 57.20 [47.37, 66.83] | -2.89 [-7.15, 1.14] | 2 | 0 |
| humaneval/low | markov_w05_vs_sync_g4 | 30 | 51.04 [45.30, 57.12] | -2.86 [-5.55, -0.23] | 2 | 0 |
| humaneval/high | sync_g4 | 30 | -29.18 [-30.52, -27.92] | 0.90 [-1.16, 2.82] | 0 | 0 |
| humaneval/high | fixed_g2 | 30 | -29.68 [-32.46, -27.63] | -9.37 [-12.61, -6.68] | 1 | 0 |
| humaneval/high | fixed_g8 | 30 | 24.23 [20.20, 28.08] | -7.26 [-9.89, -4.80] | 3 | 0 |
| humaneval/high | adaedl | 30 | -20.44 [-21.76, -19.05] | 0.14 [-1.18, 1.46] | 2 | 0 |
| humaneval/high | markov_w0 | 30 | 24.02 [20.83, 27.00] | -2.97 [-5.20, -0.99] | 3 | 0 |
| humaneval/high | markov_w05 | 30 | 16.11 [12.52, 19.85] | -1.27 [-2.72, 0.23] | 2 | 0 |
| humaneval/high | fixed_g2_vs_sync_g4 | 30 | -0.70 [-3.29, 1.46] | -10.36 [-12.16, -8.86] | 1 | 0 |
| humaneval/high | fixed_fast_vs_sync_g4 | 30 | 41.20 [38.73, 43.92] | -0.91 [-2.90, 1.15] | 0 | 0 |
| humaneval/high | fixed_g8_vs_sync_g4 | 30 | 75.40 [67.81, 82.77] | -8.24 [-12.89, -3.87] | 3 | 0 |
| humaneval/high | adaedl_vs_sync_g4 | 30 | 12.34 [9.82, 14.77] | -0.77 [-2.70, 1.10] | 2 | 0 |
| humaneval/high | markov_w0_vs_sync_g4 | 30 | 75.12 [68.40, 81.39] | -3.91 [-7.83, -0.18] | 3 | 0 |
| humaneval/high | markov_w05_vs_sync_g4 | 30 | 63.94 [56.84, 71.33] | -2.20 [-5.13, 0.79] | 2 | 0 |
| humaneval/pooled | sync_g4 | 30 | -29.58 [-31.54, -27.18] | 2.99 [1.02, 5.05] | 1 | 0 |
| humaneval/pooled | fixed_g2 | 30 | -25.58 [-28.35, -22.57] | -4.13 [-6.76, -1.76] | 3 | 0 |
| humaneval/pooled | fixed_g8 | 30 | 10.52 [6.97, 14.13] | -13.47 [-16.15, -10.83] | 7 | 0 |
| humaneval/pooled | adaedl | 30 | -22.98 [-25.11, -20.39] | 0.64 [-0.94, 2.23] | 5 | 0 |
| humaneval/pooled | markov_w0 | 30 | 17.80 [14.68, 21.35] | -0.35 [-2.40, 1.56] | 4 | 0 |
| humaneval/pooled | markov_w05 | 30 | 11.53 [7.79, 16.13] | 0.57 [-1.14, 2.51] | 5 | 0 |
| humaneval/pooled | fixed_g2_vs_sync_g4 | 30 | 5.67 [2.87, 8.52] | -7.34 [-8.85, -5.80] | 2 | 0 |
| humaneval/pooled | fixed_fast_vs_sync_g4 | 30 | 42.00 [37.33, 46.07] | -3.08 [-5.31, -1.03] | 1 | 0 |
| humaneval/pooled | fixed_g8_vs_sync_g4 | 30 | 56.94 [49.77, 63.87] | -16.97 [-21.87, -12.53] | 6 | 0 |
| humaneval/pooled | adaedl_vs_sync_g4 | 30 | 9.36 [6.55, 12.33] | -2.42 [-4.46, -0.43] | 4 | 0 |
| humaneval/pooled | markov_w0_vs_sync_g4 | 30 | 67.28 [60.24, 73.88] | -3.45 [-7.16, -0.01] | 5 | 0 |
| humaneval/pooled | markov_w05_vs_sync_g4 | 30 | 58.36 [52.16, 64.53] | -2.49 [-5.18, 0.16] | 4 | 0 |
| mtbench/low | sync_g4 | 30 | -16.69 [-19.96, -13.50] | 23.93 [21.27, 26.39] | 0 | 0 |
| mtbench/low | fixed_g2 | 30 | -4.34 [-8.67, 1.74] | 17.93 [15.32, 20.82] | 5 | 1 |
| mtbench/low | fixed_g8 | 30 | -27.38 [-31.28, -23.90] | -53.83 [-58.34, -50.02] | 5 | 0 |
| mtbench/low | adaedl | 30 | -22.74 [-24.49, -20.42] | 8.16 [6.01, 10.57] | 1 | 0 |
| mtbench/low | markov_w0 | 30 | 7.15 [4.64, 10.28] | 6.26 [2.49, 10.98] | 4 | 1 |
| mtbench/low | markov_w05 | 30 | 0.50 [-2.37, 4.28] | 17.00 [13.77, 20.72] | 4 | 1 |
| mtbench/low | fixed_g2_vs_sync_g4 | 30 | 14.82 [11.73, 19.03] | -7.88 [-9.50, -5.88] | 5 | 1 |
| mtbench/low | fixed_fast_vs_sync_g4 | 30 | 20.04 [15.60, 24.93] | -31.45 [-35.85, -27.02] | 0 | 0 |
| mtbench/low | fixed_g8_vs_sync_g4 | 30 | -12.83 [-19.70, -6.01] | -102.21 [-114.23, -91.39] | 5 | 0 |
| mtbench/low | adaedl_vs_sync_g4 | 30 | -7.26 [-9.77, -4.29] | -20.72 [-23.41, -17.85] | 1 | 0 |
| mtbench/low | markov_w0_vs_sync_g4 | 30 | 28.62 [24.54, 34.10] | -23.22 [-27.67, -18.14] | 4 | 1 |
| mtbench/low | markov_w05_vs_sync_g4 | 30 | 20.64 [17.24, 25.75] | -9.11 [-11.23, -6.57] | 4 | 1 |
| mtbench/high | sync_g4 | 30 | -17.15 [-18.48, -15.85] | 19.08 [17.30, 20.82] | 0 | 0 |
| mtbench/high | fixed_g2 | 30 | -16.42 [-18.49, -14.10] | 9.21 [6.72, 11.78] | 6 | 0 |
| mtbench/high | fixed_g8 | 30 | -7.47 [-11.14, -4.05] | -39.36 [-42.86, -36.15] | 7 | 0 |
| mtbench/high | adaedl | 30 | -23.16 [-24.62, -21.71] | 3.28 [1.83, 4.90] | 1 | 0 |
| mtbench/high | markov_w0 | 30 | 4.56 [3.02, 6.20] | -17.81 [-19.13, -16.19] | 6 | 0 |
| mtbench/high | markov_w05 | 30 | -8.55 [-10.02, -6.93] | 7.05 [4.79, 9.42] | 4 | 0 |
| mtbench/high | fixed_g2_vs_sync_g4 | 30 | 0.88 [-0.91, 3.09] | -12.19 [-13.31, -10.74] | 6 | 0 |
| mtbench/high | fixed_fast_vs_sync_g4 | 30 | 20.69 [18.84, 22.68] | -23.58 [-26.29, -20.92] | 0 | 0 |
| mtbench/high | fixed_g8_vs_sync_g4 | 30 | 11.68 [6.59, 16.55] | -72.22 [-80.07, -64.88] | 7 | 0 |
| mtbench/high | adaedl_vs_sync_g4 | 30 | -7.25 [-9.34, -5.16] | -19.52 [-21.93, -17.26] | 1 | 0 |
| mtbench/high | markov_w0_vs_sync_g4 | 30 | 26.20 [23.27, 29.20] | -45.59 [-49.08, -41.95] | 6 | 0 |
| mtbench/high | markov_w05_vs_sync_g4 | 30 | 10.37 [7.79, 13.22] | -14.86 [-16.23, -13.42] | 4 | 0 |
| mtbench/pooled | sync_g4 | 30 | -16.96 [-18.98, -15.05] | 21.34 [19.18, 23.34] | 0 | 0 |
| mtbench/pooled | fixed_g2 | 30 | -11.69 [-14.48, -8.17] | 13.33 [10.86, 15.93] | 11 | 1 |
| mtbench/pooled | fixed_g8 | 30 | -16.94 [-20.71, -13.53] | -46.11 [-49.96, -42.69] | 12 | 0 |
| mtbench/pooled | adaedl | 30 | -22.99 [-24.06, -21.74] | 5.56 [3.95, 7.43] | 2 | 0 |
| mtbench/pooled | markov_w0 | 30 | 5.66 [4.16, 7.58] | -6.54 [-8.89, -3.80] | 10 | 1 |
| mtbench/pooled | markov_w05 | 30 | -5.00 [-6.36, -3.20] | 11.69 [9.06, 14.57] | 8 | 1 |
| mtbench/pooled | fixed_g2_vs_sync_g4 | 30 | 6.34 [4.39, 9.00] | -10.19 [-11.32, -8.85] | 11 | 1 |
| mtbench/pooled | fixed_fast_vs_sync_g4 | 30 | 20.42 [17.72, 23.43] | -27.13 [-30.44, -23.73] | 0 | 0 |
| mtbench/pooled | fixed_g8_vs_sync_g4 | 30 | 0.02 [-6.01, 5.87] | -85.75 [-95.08, -77.03] | 12 | 0 |
| mtbench/pooled | adaedl_vs_sync_g4 | 30 | -7.26 [-9.16, -5.10] | -20.06 [-22.20, -17.82] | 2 | 0 |
| mtbench/pooled | markov_w0_vs_sync_g4 | 30 | 27.24 [23.98, 31.00] | -35.44 [-38.70, -31.75] | 10 | 1 |
| mtbench/pooled | markov_w05_vs_sync_g4 | 30 | 14.40 [11.75, 17.68] | -12.27 [-13.83, -10.50] | 8 | 1 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
