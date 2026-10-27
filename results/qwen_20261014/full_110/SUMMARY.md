# Progress probe: full_110

State: complete; 1540/1540 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high; pooled = low+high.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | sync_g4 | 110 | 30458 | 15.001 | 0.4181 | 6 | 0.00 |
| all/low | fixed_g2 | 110 | 30461 | 16.819 | 0.4180 | 6 | 40.40 |
| all/low | fixed_fast | 110 | 30458 | 21.394 | 0.4170 | 6 | 35.65 |
| all/low | fixed_g8 | 110 | 30103 | 21.032 | 0.5238 | 5 | 24.30 |
| all/low | adaedl | 110 | 30442 | 13.966 | 0.4715 | 6 | 0.00 |
| all/low | markov_w0 | 110 | 30446 | 23.003 | 0.4330 | 6 | 38.90 |
| all/low | markov_w05 | 110 | 30050 | 21.453 | 0.3916 | 5 | 44.87 |
| all/high | sync_g4 | 110 | 30458 | 10.478 | 0.5475 | 6 | 0.00 |
| all/high | fixed_g2 | 110 | 30461 | 9.855 | 0.6074 | 6 | 40.39 |
| all/high | fixed_fast | 110 | 30458 | 12.873 | 0.5518 | 6 | 35.69 |
| all/high | fixed_g8 | 110 | 30103 | 14.897 | 0.6150 | 5 | 24.23 |
| all/high | adaedl | 110 | 30444 | 10.132 | 0.5927 | 6 | 0.00 |
| all/high | markov_w0 | 110 | 29993 | 14.870 | 0.5757 | 5 | 34.05 |
| all/high | markov_w05 | 110 | 30011 | 13.339 | 0.5294 | 5 | 41.73 |
| all/pooled | sync_g4 | 220 | 60916 | 12.338 | 0.4828 | 12 | 0.00 |
| all/pooled | fixed_g2 | 220 | 60922 | 12.428 | 0.5127 | 12 | 40.39 |
| all/pooled | fixed_fast | 220 | 60916 | 16.074 | 0.4844 | 12 | 35.67 |
| all/pooled | fixed_g8 | 220 | 60206 | 17.440 | 0.5694 | 10 | 24.27 |
| all/pooled | adaedl | 220 | 60886 | 11.744 | 0.5321 | 12 | 0.00 |
| all/pooled | markov_w0 | 220 | 60439 | 18.092 | 0.5038 | 11 | 36.39 |
| all/pooled | markov_w05 | 220 | 60061 | 16.452 | 0.4605 | 10 | 43.43 |
| gsm8k/low | sync_g4 | 50 | 12874 | 17.602 | 0.3580 | 0 | 0.00 |
| gsm8k/low | fixed_g2 | 50 | 12874 | 20.492 | 0.3483 | 0 | 50.33 |
| gsm8k/low | fixed_fast | 50 | 12874 | 28.351 | 0.3195 | 0 | 50.26 |
| gsm8k/low | fixed_g8 | 50 | 12853 | 30.838 | 0.3619 | 0 | 40.29 |
| gsm8k/low | adaedl | 50 | 12872 | 17.249 | 0.3857 | 0 | 0.00 |
| gsm8k/low | markov_w0 | 50 | 12875 | 31.150 | 0.3217 | 0 | 52.74 |
| gsm8k/low | markov_w05 | 50 | 12875 | 29.800 | 0.3124 | 0 | 54.23 |
| gsm8k/high | sync_g4 | 50 | 12874 | 12.291 | 0.4708 | 0 | 0.00 |
| gsm8k/high | fixed_g2 | 50 | 12874 | 11.386 | 0.5255 | 0 | 50.20 |
| gsm8k/high | fixed_fast | 50 | 12874 | 16.319 | 0.4335 | 0 | 50.37 |
| gsm8k/high | fixed_g8 | 50 | 12853 | 21.129 | 0.4307 | 0 | 40.18 |
| gsm8k/high | adaedl | 50 | 12874 | 12.881 | 0.4736 | 0 | 0.00 |
| gsm8k/high | markov_w0 | 50 | 12855 | 20.093 | 0.4280 | 0 | 48.02 |
| gsm8k/high | markov_w05 | 50 | 12873 | 18.074 | 0.4191 | 0 | 51.49 |
| gsm8k/pooled | sync_g4 | 100 | 25748 | 14.475 | 0.4144 | 0 | 0.00 |
| gsm8k/pooled | fixed_g2 | 100 | 25748 | 14.639 | 0.4369 | 0 | 50.26 |
| gsm8k/pooled | fixed_fast | 100 | 25748 | 20.715 | 0.3765 | 0 | 50.31 |
| gsm8k/pooled | fixed_g8 | 100 | 25706 | 25.076 | 0.3963 | 0 | 40.24 |
| gsm8k/pooled | adaedl | 100 | 25746 | 14.748 | 0.4296 | 0 | 0.00 |
| gsm8k/pooled | markov_w0 | 100 | 25730 | 24.432 | 0.3748 | 0 | 50.28 |
| gsm8k/pooled | markov_w05 | 100 | 25748 | 22.502 | 0.3657 | 0 | 52.97 |
| humaneval/low | sync_g4 | 30 | 10241 | 15.179 | 0.4051 | 1 | 0.00 |
| humaneval/low | fixed_g2 | 30 | 10244 | 16.411 | 0.4129 | 1 | 45.33 |
| humaneval/low | fixed_fast | 30 | 10241 | 22.270 | 0.3822 | 1 | 42.77 |
| humaneval/low | fixed_g8 | 30 | 10278 | 23.692 | 0.4519 | 1 | 30.89 |
| humaneval/low | adaedl | 30 | 10244 | 14.514 | 0.4455 | 1 | 0.00 |
| humaneval/low | markov_w0 | 30 | 10241 | 24.522 | 0.4026 | 1 | 45.10 |
| humaneval/low | markov_w05 | 30 | 10279 | 22.676 | 0.3893 | 1 | 46.89 |
| humaneval/high | sync_g4 | 30 | 10241 | 10.781 | 0.5237 | 1 | 0.00 |
| humaneval/high | fixed_g2 | 30 | 10244 | 9.930 | 0.5905 | 1 | 45.43 |
| humaneval/high | fixed_fast | 30 | 10241 | 13.615 | 0.5045 | 1 | 42.71 |
| humaneval/high | fixed_g8 | 30 | 10278 | 16.753 | 0.5306 | 1 | 31.00 |
| humaneval/high | adaedl | 30 | 10244 | 10.948 | 0.5467 | 1 | 0.00 |
| humaneval/high | markov_w0 | 30 | 10241 | 16.103 | 0.5173 | 1 | 40.37 |
| humaneval/high | markov_w05 | 30 | 10241 | 14.341 | 0.5081 | 1 | 44.05 |
| humaneval/pooled | sync_g4 | 60 | 20482 | 12.607 | 0.4644 | 2 | 0.00 |
| humaneval/pooled | fixed_g2 | 60 | 20488 | 12.374 | 0.5017 | 2 | 45.38 |
| humaneval/pooled | fixed_fast | 60 | 20482 | 16.899 | 0.4434 | 2 | 42.74 |
| humaneval/pooled | fixed_g8 | 60 | 20556 | 19.627 | 0.4913 | 2 | 30.94 |
| humaneval/pooled | adaedl | 60 | 20488 | 12.482 | 0.4961 | 2 | 0.00 |
| humaneval/pooled | markov_w0 | 60 | 20482 | 19.440 | 0.4599 | 2 | 42.71 |
| humaneval/pooled | markov_w05 | 60 | 20520 | 17.578 | 0.4486 | 2 | 45.59 |
| mtbench/low | sync_g4 | 30 | 7343 | 11.761 | 0.5415 | 5 | 0.00 |
| mtbench/low | fixed_g2 | 30 | 7343 | 13.145 | 0.5475 | 5 | 21.29 |
| mtbench/low | fixed_fast | 30 | 7343 | 14.407 | 0.6364 | 5 | 12.46 |
| mtbench/low | fixed_g8 | 30 | 6972 | 12.006 | 0.9281 | 4 | 4.71 |
| mtbench/low | adaedl | 30 | 7326 | 10.068 | 0.6587 | 5 | 0.00 |
| mtbench/low | markov_w0 | 30 | 7330 | 14.880 | 0.6708 | 5 | 20.18 |
| mtbench/low | markov_w05 | 30 | 6896 | 13.380 | 0.5431 | 4 | 23.35 |
| mtbench/high | sync_g4 | 30 | 7343 | 8.073 | 0.7152 | 5 | 0.00 |
| mtbench/high | fixed_g2 | 30 | 7343 | 7.906 | 0.7746 | 5 | 21.26 |
| mtbench/high | fixed_fast | 30 | 7343 | 8.901 | 0.8252 | 5 | 12.51 |
| mtbench/high | fixed_g8 | 30 | 6972 | 8.727 | 1.0794 | 4 | 4.64 |
| mtbench/high | adaedl | 30 | 7326 | 6.849 | 0.8665 | 5 | 0.00 |
| mtbench/high | markov_w0 | 30 | 6897 | 9.304 | 0.9376 | 4 | 16.02 |
| mtbench/high | markov_w05 | 30 | 6897 | 8.375 | 0.7669 | 4 | 18.85 |
| mtbench/pooled | sync_g4 | 60 | 14686 | 9.574 | 0.6283 | 10 | 0.00 |
| mtbench/pooled | fixed_g2 | 60 | 14686 | 9.874 | 0.6611 | 10 | 21.28 |
| mtbench/pooled | fixed_fast | 60 | 14686 | 11.004 | 0.7308 | 10 | 12.48 |
| mtbench/pooled | fixed_g8 | 60 | 13944 | 10.107 | 1.0037 | 8 | 4.67 |
| mtbench/pooled | adaedl | 60 | 14652 | 8.152 | 0.7626 | 10 | 0.00 |
| mtbench/pooled | markov_w0 | 60 | 14227 | 11.530 | 0.8001 | 9 | 17.98 |
| mtbench/pooled | markov_w05 | 60 | 13793 | 10.301 | 0.6550 | 8 | 21.29 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | sync_g4 | 110 | -29.89 [-32.33, -27.38] | -0.26 [-3.91, 3.22] | 0 | 0 |
| all/low | fixed_g2 | 110 | -21.38 [-24.46, -18.44] | -0.25 [-4.14, 3.32] | 3 | 0 |
| all/low | fixed_g8 | 110 | -1.70 [-5.62, 2.57] | -25.61 [-30.20, -20.98] | 15 | 0 |
| all/low | adaedl | 110 | -34.72 [-36.10, -33.32] | -13.07 [-15.42, -10.60] | 6 | 0 |
| all/low | markov_w0 | 110 | 7.52 [5.48, 9.54] | -3.84 [-5.52, -1.93] | 6 | 0 |
| all/low | markov_w05 | 110 | 0.27 [-2.91, 4.03] | 6.08 [3.30, 9.00] | 8 | 0 |
| all/low | fixed_g2_vs_sync_g4 | 110 | 12.13 [9.77, 14.70] | 0.01 [-1.44, 1.63] | 3 | 0 |
| all/low | fixed_fast_vs_sync_g4 | 110 | 42.62 [37.70, 47.77] | 0.26 [-3.33, 3.77] | 0 | 0 |
| all/low | fixed_g8_vs_sync_g4 | 110 | 40.21 [31.46, 49.37] | -25.28 [-33.80, -17.38] | 15 | 0 |
| all/low | adaedl_vs_sync_g4 | 110 | -6.90 [-9.28, -4.22] | -12.78 [-15.29, -10.12] | 6 | 0 |
| all/low | markov_w0_vs_sync_g4 | 110 | 53.35 [46.82, 60.22] | -3.57 [-8.23, 0.90] | 6 | 0 |
| all/low | markov_w05_vs_sync_g4 | 110 | 43.01 [35.56, 50.59] | 6.32 [4.23, 8.61] | 8 | 0 |
| all/high | sync_g4 | 110 | -18.61 [-20.36, -16.84] | 0.78 [-1.93, 3.44] | 0 | 0 |
| all/high | fixed_g2 | 110 | -23.45 [-25.57, -21.18] | -10.08 [-13.47, -6.72] | 3 | 0 |
| all/high | fixed_g8 | 110 | 15.72 [11.39, 20.35] | -11.46 [-15.59, -7.28] | 15 | 0 |
| all/high | adaedl | 110 | -21.29 [-22.40, -20.20] | -7.42 [-8.76, -6.09] | 5 | 0 |
| all/high | markov_w0 | 110 | 15.51 [12.60, 18.70] | -4.33 [-6.71, -1.84] | 9 | 0 |
| all/high | markov_w05 | 110 | 3.62 [0.99, 6.60] | 4.06 [2.32, 5.86] | 8 | 0 |
| all/high | fixed_g2_vs_sync_g4 | 110 | -5.95 [-7.17, -4.69] | -10.95 [-12.11, -9.77] | 3 | 0 |
| all/high | fixed_fast_vs_sync_g4 | 110 | 22.86 [20.26, 25.57] | -0.79 [-3.56, 1.90] | 0 | 0 |
| all/high | fixed_g8_vs_sync_g4 | 110 | 42.18 [34.39, 50.05] | -12.34 [-19.49, -6.05] | 15 | 0 |
| all/high | adaedl_vs_sync_g4 | 110 | -3.30 [-5.97, -0.57] | -8.27 [-10.98, -5.60] | 5 | 0 |
| all/high | markov_w0_vs_sync_g4 | 110 | 41.92 [36.24, 47.90] | -5.15 [-9.90, -0.74] | 9 | 0 |
| all/high | markov_w05_vs_sync_g4 | 110 | 27.31 [22.24, 32.54] | 3.30 [1.15, 5.60] | 8 | 0 |
| all/pooled | sync_g4 | 110 | -23.25 [-25.24, -21.19] | 0.33 [-2.62, 3.34] | 0 | 0 |
| all/pooled | fixed_g2 | 110 | -22.69 [-24.96, -20.29] | -5.85 [-9.31, -2.46] | 6 | 0 |
| all/pooled | fixed_g8 | 110 | 8.50 [4.37, 12.84] | -17.55 [-21.80, -13.21] | 30 | 0 |
| all/pooled | adaedl | 110 | -26.94 [-27.94, -25.92] | -9.86 [-11.47, -8.16] | 11 | 0 |
| all/pooled | markov_w0 | 110 | 12.55 [10.19, 15.09] | -4.01 [-5.81, -2.09] | 15 | 0 |
| all/pooled | markov_w05 | 110 | 2.35 [-0.23, 5.42] | 4.94 [2.93, 7.06] | 16 | 0 |
| all/pooled | fixed_g2_vs_sync_g4 | 110 | 0.73 [-0.50, 2.07] | -6.21 [-7.20, -5.13] | 6 | 0 |
| all/pooled | fixed_fast_vs_sync_g4 | 110 | 30.29 [26.89, 33.76] | -0.34 [-3.46, 2.56] | 0 | 0 |
| all/pooled | fixed_g8_vs_sync_g4 | 110 | 41.36 [33.40, 49.43] | -17.94 [-25.40, -10.97] | 30 | 0 |
| all/pooled | adaedl_vs_sync_g4 | 110 | -4.81 [-7.29, -2.17] | -10.22 [-12.71, -7.69] | 11 | 0 |
| all/pooled | markov_w0_vs_sync_g4 | 110 | 46.64 [40.74, 52.59] | -4.35 [-8.82, -0.21] | 15 | 0 |
| all/pooled | markov_w05_vs_sync_g4 | 110 | 33.35 [27.54, 39.31] | 4.62 [2.67, 6.81] | 16 | 0 |
| gsm8k/low | sync_g4 | 50 | -37.91 [-39.94, -35.97] | -12.04 [-15.31, -8.95] | 0 | 0 |
| gsm8k/low | fixed_g2 | 50 | -27.72 [-30.49, -25.24] | -9.01 [-12.78, -5.57] | 0 | 0 |
| gsm8k/low | fixed_g8 | 50 | 8.77 [4.17, 13.06] | -13.28 [-16.93, -9.82] | 2 | 0 |
| gsm8k/low | adaedl | 50 | -39.16 [-41.16, -37.20] | -20.72 [-23.33, -18.32] | 1 | 0 |
| gsm8k/low | markov_w0 | 50 | 9.87 [5.83, 13.52] | -0.71 [-3.01, 1.44] | 1 | 0 |
| gsm8k/low | markov_w05 | 50 | 5.11 [1.59, 8.70] | 2.22 [0.16, 4.56] | 1 | 0 |
| gsm8k/low | fixed_g2_vs_sync_g4 | 50 | 16.42 [12.44, 20.54] | 2.71 [0.13, 5.13] | 0 | 0 |
| gsm8k/low | fixed_fast_vs_sync_g4 | 50 | 61.07 [56.17, 66.50] | 10.75 [8.22, 13.28] | 0 | 0 |
| gsm8k/low | fixed_g8_vs_sync_g4 | 50 | 75.19 [66.57, 84.09] | -1.10 [-6.41, 3.93] | 2 | 0 |
| gsm8k/low | adaedl_vs_sync_g4 | 50 | -2.01 [-4.37, 0.34] | -7.75 [-9.95, -5.64] | 1 | 0 |
| gsm8k/low | markov_w0_vs_sync_g4 | 50 | 76.97 [69.95, 84.29] | 10.12 [6.78, 13.51] | 1 | 0 |
| gsm8k/low | markov_w05_vs_sync_g4 | 50 | 69.30 [62.13, 77.13] | 12.73 [9.92, 15.54] | 1 | 0 |
| gsm8k/high | sync_g4 | 50 | -24.69 [-26.01, -23.37] | -8.60 [-10.88, -6.40] | 0 | 0 |
| gsm8k/high | fixed_g2 | 50 | -30.23 [-32.06, -28.57] | -21.24 [-24.23, -18.36] | 0 | 0 |
| gsm8k/high | fixed_g8 | 50 | 29.47 [25.99, 32.96] | 0.65 [-2.09, 3.37] | 2 | 0 |
| gsm8k/high | adaedl | 50 | -21.07 [-22.62, -19.69] | -9.26 [-10.94, -7.77] | 0 | 0 |
| gsm8k/high | markov_w0 | 50 | 23.12 [19.58, 26.65] | 1.26 [-1.23, 3.79] | 3 | 0 |
| gsm8k/high | markov_w05 | 50 | 10.75 [7.44, 14.25] | 3.32 [1.79, 4.90] | 3 | 0 |
| gsm8k/high | fixed_g2_vs_sync_g4 | 50 | -7.36 [-9.29, -5.65] | -11.64 [-13.68, -9.86] | 0 | 0 |
| gsm8k/high | fixed_fast_vs_sync_g4 | 50 | 32.78 [30.50, 35.14] | 7.92 [6.02, 9.82] | 0 | 0 |
| gsm8k/high | fixed_g8_vs_sync_g4 | 50 | 71.91 [65.22, 78.88] | 8.52 [4.22, 12.58] | 2 | 0 |
| gsm8k/high | adaedl_vs_sync_g4 | 50 | 4.80 [2.36, 7.11] | -0.61 [-2.84, 1.56] | 0 | 0 |
| gsm8k/high | markov_w0_vs_sync_g4 | 50 | 63.48 [57.32, 70.30] | 9.08 [5.35, 12.83] | 3 | 0 |
| gsm8k/high | markov_w05_vs_sync_g4 | 50 | 47.06 [41.03, 53.50] | 10.97 [8.32, 13.74] | 3 | 0 |
| gsm8k/pooled | sync_g4 | 50 | -30.13 [-31.66, -28.69] | -10.06 [-12.66, -7.59] | 0 | 0 |
| gsm8k/pooled | fixed_g2 | 50 | -29.33 [-31.03, -27.63] | -16.05 [-18.88, -13.33] | 0 | 0 |
| gsm8k/pooled | fixed_g8 | 50 | 21.05 [17.50, 24.46] | -5.26 [-8.30, -2.41] | 4 | 0 |
| gsm8k/pooled | adaedl | 50 | -28.80 [-30.29, -27.42] | -14.12 [-15.96, -12.45] | 1 | 0 |
| gsm8k/pooled | markov_w0 | 50 | 17.95 [14.85, 20.92] | 0.43 [-1.53, 2.46] | 4 | 0 |
| gsm8k/pooled | markov_w05 | 50 | 8.63 [5.47, 11.88] | 2.85 [1.38, 4.40] | 4 | 0 |
| gsm8k/pooled | fixed_g2_vs_sync_g4 | 50 | 1.13 [-0.78, 3.04] | -5.44 [-7.16, -3.82] | 0 | 0 |
| gsm8k/pooled | fixed_fast_vs_sync_g4 | 50 | 43.11 [40.23, 46.33] | 9.14 [7.06, 11.24] | 0 | 0 |
| gsm8k/pooled | fixed_g8_vs_sync_g4 | 50 | 73.24 [65.86, 80.76] | 4.36 [-0.36, 8.76] | 4 | 0 |
| gsm8k/pooled | adaedl_vs_sync_g4 | 50 | 1.89 [-0.28, 4.04] | -3.69 [-5.80, -1.66] | 1 | 0 |
| gsm8k/pooled | markov_w0_vs_sync_g4 | 50 | 68.80 [62.96, 75.09] | 9.54 [6.18, 13.00] | 4 | 0 |
| gsm8k/pooled | markov_w05_vs_sync_g4 | 50 | 55.46 [49.29, 62.12] | 11.73 [9.09, 14.42] | 4 | 0 |
| humaneval/low | sync_g4 | 30 | -31.84 [-34.26, -29.73] | -5.99 [-10.00, -2.63] | 0 | 0 |
| humaneval/low | fixed_g2 | 30 | -26.31 [-30.74, -22.42] | -8.03 [-13.98, -3.16] | 1 | 0 |
| humaneval/low | fixed_g8 | 30 | 6.39 [2.71, 10.24] | -18.22 [-21.70, -14.80] | 4 | 0 |
| humaneval/low | adaedl | 30 | -34.83 [-36.74, -33.02] | -16.54 [-18.81, -14.34] | 1 | 0 |
| humaneval/low | markov_w0 | 30 | 10.11 [6.87, 13.35] | -5.33 [-7.71, -2.89] | 2 | 0 |
| humaneval/low | markov_w05 | 30 | 1.82 [-2.51, 5.61] | -1.86 [-4.59, 0.63] | 3 | 0 |
| humaneval/low | fixed_g2_vs_sync_g4 | 30 | 8.12 [4.60, 11.96] | -1.93 [-4.15, 0.53] | 1 | 0 |
| humaneval/low | fixed_fast_vs_sync_g4 | 30 | 46.72 [42.31, 52.12] | 5.65 [2.56, 9.09] | 0 | 0 |
| humaneval/low | fixed_g8_vs_sync_g4 | 30 | 56.09 [49.05, 63.68] | -11.54 [-17.61, -5.31] | 4 | 0 |
| humaneval/low | adaedl_vs_sync_g4 | 30 | -4.38 [-7.86, 0.38] | -9.96 [-13.85, -5.14] | 1 | 0 |
| humaneval/low | markov_w0_vs_sync_g4 | 30 | 61.55 [54.17, 70.76] | 0.62 [-4.25, 6.21] | 2 | 0 |
| humaneval/low | markov_w05_vs_sync_g4 | 30 | 49.39 [45.26, 54.64] | 3.90 [1.73, 6.15] | 3 | 0 |
| humaneval/high | sync_g4 | 30 | -20.82 [-22.09, -19.66] | -3.81 [-5.84, -1.98] | 0 | 0 |
| humaneval/high | fixed_g2 | 30 | -27.06 [-28.80, -25.12] | -17.05 [-20.32, -13.84] | 1 | 0 |
| humaneval/high | fixed_g8 | 30 | 23.04 [19.49, 27.02] | -5.19 [-8.10, -2.18] | 4 | 0 |
| humaneval/high | adaedl | 30 | -19.59 [-21.29, -17.80] | -8.37 [-10.20, -6.50] | 1 | 0 |
| humaneval/high | markov_w0 | 30 | 18.27 [15.89, 21.09] | -2.53 [-4.53, -0.29] | 2 | 0 |
| humaneval/high | markov_w05 | 30 | 5.33 [1.94, 9.17] | -0.72 [-2.53, 1.18] | 2 | 0 |
| humaneval/high | fixed_g2_vs_sync_g4 | 30 | -7.89 [-9.62, -6.01] | -12.76 [-14.61, -10.77] | 1 | 0 |
| humaneval/high | fixed_fast_vs_sync_g4 | 30 | 26.29 [24.47, 28.36] | 3.67 [1.94, 5.52] | 0 | 0 |
| humaneval/high | fixed_g8_vs_sync_g4 | 30 | 55.39 [49.63, 62.27] | -1.33 [-5.65, 3.33] | 4 | 0 |
| humaneval/high | adaedl_vs_sync_g4 | 30 | 1.55 [-0.81, 4.23] | -4.40 [-6.79, -2.07] | 1 | 0 |
| humaneval/high | markov_w0_vs_sync_g4 | 30 | 49.36 [45.10, 54.56] | 1.23 [-2.08, 5.04] | 2 | 0 |
| humaneval/high | markov_w05_vs_sync_g4 | 30 | 33.03 [28.24, 38.89] | 2.97 [0.40, 5.90] | 2 | 0 |
| humaneval/pooled | sync_g4 | 30 | -25.40 [-26.91, -24.05] | -4.75 [-7.34, -2.51] | 0 | 0 |
| humaneval/pooled | fixed_g2 | 30 | -26.78 [-29.14, -24.51] | -13.16 [-17.06, -9.54] | 2 | 0 |
| humaneval/pooled | fixed_g8 | 30 | 16.14 [12.72, 19.74] | -10.81 [-13.88, -7.71] | 8 | 0 |
| humaneval/pooled | adaedl | 30 | -26.14 [-27.77, -24.56] | -11.89 [-13.62, -10.10] | 2 | 0 |
| humaneval/pooled | markov_w0 | 30 | 15.04 [12.57, 17.82] | -3.74 [-5.84, -1.53] | 4 | 0 |
| humaneval/pooled | markov_w05 | 30 | 4.02 [1.82, 6.56] | -1.19 [-2.46, 0.13] | 5 | 0 |
| humaneval/pooled | fixed_g2_vs_sync_g4 | 30 | -1.85 [-3.81, 0.27] | -8.03 [-9.76, -6.30] | 2 | 0 |
| humaneval/pooled | fixed_fast_vs_sync_g4 | 30 | 34.04 [31.66, 36.81] | 4.53 [2.45, 6.84] | 0 | 0 |
| humaneval/pooled | fixed_g8_vs_sync_g4 | 30 | 55.68 [49.68, 62.69] | -5.78 [-10.58, -0.69] | 8 | 0 |
| humaneval/pooled | adaedl_vs_sync_g4 | 30 | -1.00 [-3.65, 2.18] | -6.82 [-9.65, -3.73] | 2 | 0 |
| humaneval/pooled | markov_w0_vs_sync_g4 | 30 | 54.20 [49.07, 60.27] | 0.96 [-2.92, 5.27] | 4 | 0 |
| humaneval/pooled | markov_w05_vs_sync_g4 | 30 | 39.42 [35.28, 44.73] | 3.40 [1.24, 5.94] | 5 | 0 |
| mtbench/low | sync_g4 | 30 | -18.37 [-22.34, -14.97] | 14.91 [10.02, 18.61] | 0 | 0 |
| mtbench/low | fixed_g2 | 30 | -8.76 [-13.56, -4.10] | 13.96 [8.90, 18.39] | 2 | 0 |
| mtbench/low | fixed_g8 | 30 | -16.66 [-21.74, -11.47] | -45.84 [-52.30, -38.43] | 9 | 0 |
| mtbench/low | adaedl | 30 | -30.12 [-32.52, -28.01] | -3.50 [-7.71, 0.65] | 4 | 0 |
| mtbench/low | markov_w0 | 30 | 3.28 [0.28, 6.26] | -5.41 [-8.64, -1.47] | 3 | 0 |
| mtbench/low | markov_w05 | 30 | -7.13 [-12.23, -1.73] | 14.66 [10.64, 18.77] | 4 | 0 |
| mtbench/low | fixed_g2_vs_sync_g4 | 30 | 11.77 [8.09, 17.18] | -1.12 [-3.26, 1.82] | 2 | 0 |
| mtbench/low | fixed_fast_vs_sync_g4 | 30 | 22.50 [17.61, 28.77] | -17.53 [-22.87, -11.13] | 0 | 0 |
| mtbench/low | fixed_g8_vs_sync_g4 | 30 | 2.09 [-4.89, 11.00] | -71.40 [-85.23, -55.52] | 9 | 0 |
| mtbench/low | adaedl_vs_sync_g4 | 30 | -14.39 [-17.56, -10.58] | -21.64 [-25.56, -17.12] | 4 | 0 |
| mtbench/low | markov_w0_vs_sync_g4 | 30 | 26.52 [22.15, 32.16] | -23.88 [-29.12, -17.22] | 3 | 0 |
| mtbench/low | markov_w05_vs_sync_g4 | 30 | 13.77 [6.59, 22.58] | -0.29 [-3.98, 3.83] | 4 | 0 |
| mtbench/high | sync_g4 | 30 | -9.30 [-11.44, -7.41] | 13.33 [10.60, 15.54] | 0 | 0 |
| mtbench/high | fixed_g2 | 30 | -11.18 [-14.28, -8.20] | 6.13 [2.19, 9.59] | 2 | 0 |
| mtbench/high | fixed_g8 | 30 | -1.96 [-5.07, 2.54] | -30.80 [-34.76, -25.78] | 9 | 0 |
| mtbench/high | adaedl | 30 | -23.05 [-25.01, -21.24] | -5.01 [-8.10, -1.96] | 4 | 0 |
| mtbench/high | markov_w0 | 30 | 4.53 [2.14, 7.74] | -13.62 [-16.10, -10.77] | 4 | 0 |
| mtbench/high | markov_w05 | 30 | -5.92 [-7.85, -3.52] | 7.07 [5.25, 8.98] | 3 | 0 |
| mtbench/high | fixed_g2_vs_sync_g4 | 30 | -2.07 [-4.18, 0.41] | -8.31 [-10.22, -6.20] | 2 | 0 |
| mtbench/high | fixed_fast_vs_sync_g4 | 30 | 10.25 [8.00, 12.91] | -15.39 [-18.41, -11.86] | 0 | 0 |
| mtbench/high | fixed_g8_vs_sync_g4 | 30 | 8.09 [3.11, 14.88] | -50.92 [-59.31, -41.11] | 9 | 0 |
| mtbench/high | adaedl_vs_sync_g4 | 30 | -15.16 [-17.51, -12.48] | -21.16 [-24.41, -17.90] | 4 | 0 |
| mtbench/high | markov_w0_vs_sync_g4 | 30 | 15.25 [11.31, 20.47] | -31.10 [-36.19, -25.12] | 4 | 0 |
| mtbench/high | markov_w05_vs_sync_g4 | 30 | 3.73 [0.56, 7.92] | -7.23 [-9.65, -5.07] | 3 | 0 |
| mtbench/pooled | sync_g4 | 30 | -12.99 [-15.59, -10.81] | 14.02 [10.62, 16.54] | 0 | 0 |
| mtbench/pooled | fixed_g2 | 30 | -10.27 [-13.95, -6.82] | 9.54 [5.20, 13.34] | 4 | 0 |
| mtbench/pooled | fixed_g8 | 30 | -8.15 [-11.83, -3.55] | -37.35 [-42.20, -31.42] | 18 | 0 |
| mtbench/pooled | adaedl | 30 | -25.91 [-27.89, -24.10] | -4.35 [-7.80, -0.95] | 8 | 0 |
| mtbench/pooled | markov_w0 | 30 | 4.78 [1.95, 8.09] | -9.49 [-11.78, -6.82] | 7 | 0 |
| mtbench/pooled | markov_w05 | 30 | -6.39 [-9.21, -3.18] | 10.38 [7.91, 12.85] | 7 | 0 |
| mtbench/pooled | fixed_g2_vs_sync_g4 | 30 | 3.13 [0.67, 6.16] | -5.21 [-6.95, -3.19] | 4 | 0 |
| mtbench/pooled | fixed_fast_vs_sync_g4 | 30 | 14.93 [12.12, 18.48] | -16.31 [-19.82, -11.89] | 0 | 0 |
| mtbench/pooled | fixed_g8_vs_sync_g4 | 30 | 5.56 [-0.14, 13.25] | -59.75 [-69.81, -47.94] | 18 | 0 |
| mtbench/pooled | adaedl_vs_sync_g4 | 30 | -14.85 [-17.32, -12.06] | -21.37 [-24.58, -18.14] | 8 | 0 |
| mtbench/pooled | markov_w0_vs_sync_g4 | 30 | 20.43 [16.60, 25.71] | -27.34 [-31.93, -21.69] | 7 | 0 |
| mtbench/pooled | markov_w05_vs_sync_g4 | 30 | 7.59 [3.25, 13.18] | -4.24 [-6.52, -1.77] | 7 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
