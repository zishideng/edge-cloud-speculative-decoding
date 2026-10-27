# Progress probe: qwen_full_dist_110

State: complete; 1980/1980 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | sync_g4 | 110 | 30625 | 26.456 | 0.2806 | 7 | 0.00 |
| all/low | fixed_g2 | 110 | 30594 | 37.459 | 0.2934 | 7 | 40.72 |
| all/low | fixed_fast | 110 | 30624 | 36.108 | 0.3549 | 7 | 36.23 |
| all/low | fixed_g8 | 110 | 30780 | 27.219 | 0.5085 | 7 | 24.49 |
| all/low | markov_w0_dist | 110 | 30652 | 36.295 | 0.3082 | 7 | 42.20 |
| all/low | markov_w05_dist | 110 | 30675 | 36.160 | 0.2856 | 7 | 42.07 |
| all/high | sync_g4 | 110 | 30950 | 13.350 | 0.4480 | 7 | 0.00 |
| all/high | fixed_g2 | 110 | 30942 | 14.383 | 0.4591 | 7 | 40.68 |
| all/high | fixed_fast | 110 | 30950 | 18.363 | 0.4564 | 7 | 35.97 |
| all/high | fixed_g8 | 110 | 30932 | 20.318 | 0.5836 | 7 | 24.31 |
| all/high | markov_w0_dist | 110 | 30988 | 20.738 | 0.5144 | 7 | 36.27 |
| all/high | markov_w05_dist | 110 | 31015 | 18.545 | 0.4414 | 7 | 42.52 |
| all/dynamic | sync_g4 | 110 | 30710 | 19.203 | 0.3456 | 7 | 0.00 |
| all/dynamic | fixed_g2 | 110 | 30750 | 24.347 | 0.3422 | 7 | 40.65 |
| all/dynamic | fixed_fast | 110 | 30710 | 26.283 | 0.3989 | 7 | 35.81 |
| all/dynamic | fixed_g8 | 110 | 30836 | 23.468 | 0.5462 | 7 | 24.38 |
| all/dynamic | markov_w0_dist | 110 | 30842 | 27.674 | 0.3898 | 7 | 39.12 |
| all/dynamic | markov_w05_dist | 110 | 30846 | 26.039 | 0.3459 | 8 | 41.42 |
| all/pooled | sync_g4 | 330 | 92285 | 18.184 | 0.3584 | 21 | 0.00 |
| all/pooled | fixed_g2 | 330 | 92286 | 21.812 | 0.3652 | 21 | 40.68 |
| all/pooled | fixed_fast | 330 | 92284 | 24.928 | 0.4036 | 21 | 36.00 |
| all/pooled | fixed_g8 | 330 | 92548 | 23.328 | 0.5462 | 21 | 24.39 |
| all/pooled | markov_w0_dist | 330 | 92482 | 26.781 | 0.4045 | 21 | 38.67 |
| all/pooled | markov_w05_dist | 330 | 92536 | 24.974 | 0.3579 | 22 | 42.03 |
| humaneval/low | sync_g4 | 30 | 10249 | 28.088 | 0.2606 | 2 | 0.00 |
| humaneval/low | fixed_g2 | 30 | 10227 | 40.187 | 0.2716 | 2 | 45.47 |
| humaneval/low | fixed_fast | 30 | 10249 | 41.117 | 0.3104 | 2 | 43.14 |
| humaneval/low | fixed_g8 | 30 | 10305 | 32.372 | 0.4278 | 2 | 30.88 |
| humaneval/low | markov_w0_dist | 30 | 10249 | 38.992 | 0.3003 | 2 | 46.84 |
| humaneval/low | markov_w05_dist | 30 | 10227 | 38.720 | 0.2820 | 2 | 45.31 |
| humaneval/high | sync_g4 | 30 | 10410 | 14.253 | 0.4185 | 2 | 0.00 |
| humaneval/high | fixed_g2 | 30 | 10420 | 15.269 | 0.4304 | 2 | 45.49 |
| humaneval/high | fixed_fast | 30 | 10410 | 20.540 | 0.4038 | 2 | 42.84 |
| humaneval/high | fixed_g8 | 30 | 10500 | 24.168 | 0.4922 | 2 | 31.08 |
| humaneval/high | markov_w0_dist | 30 | 10445 | 22.758 | 0.4710 | 2 | 42.24 |
| humaneval/high | markov_w05_dist | 30 | 10444 | 21.622 | 0.4172 | 2 | 45.21 |
| humaneval/dynamic | sync_g4 | 30 | 10291 | 20.524 | 0.3206 | 2 | 0.00 |
| humaneval/dynamic | fixed_g2 | 30 | 10390 | 26.655 | 0.3137 | 2 | 45.78 |
| humaneval/dynamic | fixed_fast | 30 | 10291 | 30.037 | 0.3478 | 2 | 43.16 |
| humaneval/dynamic | fixed_g8 | 30 | 10383 | 28.252 | 0.4521 | 2 | 31.52 |
| humaneval/dynamic | markov_w0_dist | 30 | 10330 | 30.814 | 0.3651 | 2 | 44.33 |
| humaneval/dynamic | markov_w05_dist | 30 | 10359 | 28.999 | 0.3325 | 2 | 44.36 |
| humaneval/pooled | sync_g4 | 90 | 30950 | 19.384 | 0.3336 | 6 | 0.00 |
| humaneval/pooled | fixed_g2 | 90 | 31037 | 23.394 | 0.3390 | 6 | 45.58 |
| humaneval/pooled | fixed_fast | 90 | 30950 | 28.170 | 0.3543 | 6 | 43.05 |
| humaneval/pooled | fixed_g8 | 90 | 31188 | 27.839 | 0.4576 | 6 | 31.16 |
| humaneval/pooled | markov_w0_dist | 90 | 31024 | 29.350 | 0.3793 | 6 | 44.11 |
| humaneval/pooled | markov_w05_dist | 90 | 31030 | 28.097 | 0.3444 | 6 | 44.98 |
| gsm8k/low | sync_g4 | 50 | 13004 | 29.315 | 0.2519 | 0 | 0.00 |
| gsm8k/low | fixed_g2 | 50 | 12968 | 43.641 | 0.2531 | 0 | 50.26 |
| gsm8k/low | fixed_fast | 50 | 13004 | 45.615 | 0.2793 | 0 | 50.38 |
| gsm8k/low | fixed_g8 | 50 | 13056 | 38.318 | 0.3584 | 0 | 40.60 |
| gsm8k/low | markov_w0_dist | 50 | 13005 | 42.889 | 0.2677 | 0 | 51.40 |
| gsm8k/low | markov_w05_dist | 50 | 13005 | 42.005 | 0.2560 | 0 | 50.97 |
| gsm8k/high | sync_g4 | 50 | 13012 | 15.067 | 0.3964 | 0 | 0.00 |
| gsm8k/high | fixed_g2 | 50 | 13013 | 16.194 | 0.4049 | 0 | 50.43 |
| gsm8k/high | fixed_fast | 50 | 13012 | 22.782 | 0.3612 | 0 | 50.48 |
| gsm8k/high | fixed_g8 | 50 | 12993 | 28.470 | 0.4091 | 0 | 40.67 |
| gsm8k/high | markov_w0_dist | 50 | 13043 | 28.044 | 0.3898 | 0 | 49.41 |
| gsm8k/high | markov_w05_dist | 50 | 13080 | 24.444 | 0.3649 | 0 | 52.29 |
| gsm8k/dynamic | sync_g4 | 50 | 12977 | 21.567 | 0.3069 | 0 | 0.00 |
| gsm8k/dynamic | fixed_g2 | 50 | 12961 | 27.618 | 0.2984 | 0 | 50.14 |
| gsm8k/dynamic | fixed_fast | 50 | 12977 | 33.211 | 0.3118 | 0 | 50.17 |
| gsm8k/dynamic | fixed_g8 | 50 | 13000 | 33.344 | 0.3805 | 0 | 40.77 |
| gsm8k/dynamic | markov_w0_dist | 50 | 13074 | 34.568 | 0.3237 | 0 | 49.42 |
| gsm8k/dynamic | markov_w05_dist | 50 | 12997 | 31.117 | 0.3062 | 0 | 50.98 |
| gsm8k/pooled | sync_g4 | 150 | 38993 | 20.427 | 0.3184 | 0 | 0.00 |
| gsm8k/pooled | fixed_g2 | 150 | 38942 | 24.804 | 0.3189 | 0 | 50.27 |
| gsm8k/pooled | fixed_fast | 150 | 38993 | 31.270 | 0.3174 | 0 | 50.34 |
| gsm8k/pooled | fixed_g8 | 150 | 39049 | 32.898 | 0.3826 | 0 | 40.68 |
| gsm8k/pooled | markov_w0_dist | 150 | 39122 | 34.122 | 0.3271 | 0 | 49.95 |
| gsm8k/pooled | markov_w05_dist | 150 | 39082 | 30.959 | 0.3092 | 0 | 51.45 |
| mtbench/low | sync_g4 | 30 | 7372 | 21.118 | 0.3591 | 5 | 0.00 |
| mtbench/low | fixed_g2 | 30 | 7399 | 27.911 | 0.3941 | 5 | 22.14 |
| mtbench/low | fixed_fast | 30 | 7371 | 23.491 | 0.5503 | 5 | 13.51 |
| mtbench/low | fixed_g8 | 30 | 7419 | 15.725 | 0.8847 | 5 | 5.13 |
| mtbench/low | markov_w0_dist | 30 | 7398 | 26.569 | 0.3905 | 5 | 23.14 |
| mtbench/low | markov_w05_dist | 30 | 7443 | 27.105 | 0.3421 | 5 | 23.49 |
| mtbench/high | sync_g4 | 30 | 7528 | 10.393 | 0.5780 | 5 | 0.00 |
| mtbench/high | fixed_g2 | 30 | 7509 | 11.285 | 0.5931 | 5 | 21.85 |
| mtbench/high | fixed_fast | 30 | 7528 | 12.393 | 0.6936 | 5 | 13.22 |
| mtbench/high | fixed_g8 | 30 | 7439 | 11.778 | 1.0173 | 5 | 4.77 |
| mtbench/high | markov_w0_dist | 30 | 7500 | 13.153 | 0.7916 | 5 | 17.46 |
| mtbench/high | markov_w05_dist | 30 | 7491 | 11.450 | 0.6086 | 5 | 16.62 |
| mtbench/dynamic | sync_g4 | 30 | 7442 | 15.001 | 0.4476 | 5 | 0.00 |
| mtbench/dynamic | fixed_g2 | 30 | 7399 | 18.319 | 0.4593 | 5 | 21.81 |
| mtbench/dynamic | fixed_fast | 30 | 7442 | 17.106 | 0.6217 | 5 | 12.99 |
| mtbench/dynamic | fixed_g8 | 30 | 7453 | 13.391 | 0.9665 | 5 | 5.03 |
| mtbench/dynamic | markov_w0_dist | 30 | 7438 | 18.547 | 0.5403 | 5 | 19.40 |
| mtbench/dynamic | markov_w05_dist | 30 | 7490 | 18.282 | 0.4334 | 6 | 21.40 |
| mtbench/pooled | sync_g4 | 90 | 22342 | 14.235 | 0.4623 | 15 | 0.00 |
| mtbench/pooled | fixed_g2 | 90 | 22307 | 16.717 | 0.4827 | 15 | 21.93 |
| mtbench/pooled | fixed_fast | 90 | 22341 | 16.472 | 0.6223 | 15 | 13.24 |
| mtbench/pooled | fixed_g8 | 90 | 22311 | 13.441 | 0.9563 | 15 | 4.98 |
| mtbench/pooled | markov_w0_dist | 90 | 22336 | 17.873 | 0.5751 | 15 | 19.31 |
| mtbench/pooled | markov_w05_dist | 90 | 22424 | 16.753 | 0.4616 | 16 | 20.67 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | sync_g4 | 110 | -26.73 [-29.39, -23.94] | 20.94 [17.97, 23.81] | 1 | 0 |
| all/low | fixed_g2 | 110 | 3.74 [1.14, 6.38] | 17.33 [14.99, 19.61] | 16 | 0 |
| all/low | fixed_g8 | 110 | -24.62 [-26.80, -22.25] | -43.27 [-47.45, -39.10] | 28 | 0 |
| all/low | markov_w0_dist | 110 | 0.52 [-1.86, 2.89] | 13.15 [9.62, 16.56] | 9 | 0 |
| all/low | markov_w05_dist | 110 | 0.14 [-2.57, 2.98] | 19.54 [15.49, 23.39] | 16 | 0 |
| all/low | sync_g4_vs_fixed_g2 | 110 | -29.37 [-30.60, -28.19] | 4.36 [3.14, 5.52] | 16 | 0 |
| all/low | fixed_fast_vs_fixed_g2 | 110 | -3.61 [-6.00, -1.13] | -20.97 [-24.39, -17.64] | 16 | 0 |
| all/low | fixed_g8_vs_fixed_g2 | 110 | -27.34 [-31.06, -23.30] | -73.31 [-83.15, -63.96] | 33 | 0 |
| all/low | markov_w0_dist_vs_fixed_g2 | 110 | -3.11 [-4.27, -1.91] | -5.06 [-6.88, -3.29] | 14 | 0 |
| all/low | markov_w05_dist_vs_fixed_g2 | 110 | -3.47 [-4.65, -2.28] | 2.67 [0.43, 4.83] | 8 | 0 |
| all/low | sync_g4_vs_fixed_g8 | 110 | -2.80 [-8.99, 3.84] | 44.82 [41.09, 48.25] | 28 | 0 |
| all/low | fixed_g2_vs_fixed_g8 | 110 | 37.62 [30.37, 45.06] | 42.30 [39.01, 45.40] | 33 | 0 |
| all/low | fixed_fast_vs_fixed_g8 | 110 | 32.66 [28.61, 36.61] | 30.20 [28.11, 32.18] | 28 | 0 |
| all/low | markov_w0_dist_vs_fixed_g8 | 110 | 33.35 [26.68, 40.30] | 39.38 [35.11, 43.28] | 33 | 0 |
| all/low | markov_w05_dist_vs_fixed_g8 | 110 | 32.85 [25.45, 40.26] | 43.84 [39.34, 47.94] | 32 | 0 |
| all/low | fixed_g2_vs_sync_g4 | 110 | 41.59 [39.27, 44.08] | -4.56 [-5.85, -3.24] | 16 | 0 |
| all/low | fixed_fast_vs_sync_g4 | 110 | 36.48 [31.47, 41.62] | -26.48 [-31.25, -21.91] | 1 | 0 |
| all/low | fixed_g8_vs_sync_g4 | 110 | 2.88 [-3.70, 9.88] | -81.22 [-93.23, -69.76] | 28 | 0 |
| all/low | markov_w0_dist_vs_sync_g4 | 110 | 37.19 [34.41, 40.10] | -9.85 [-11.62, -8.08] | 9 | 0 |
| all/low | markov_w05_dist_vs_sync_g4 | 110 | 36.68 [34.16, 39.09] | -1.77 [-3.57, 0.07] | 16 | 0 |
| all/high | sync_g4 | 110 | -27.30 [-29.22, -25.28] | 1.84 [-1.32, 4.90] | 0 | 0 |
| all/high | fixed_g2 | 110 | -21.68 [-23.82, -19.46] | -0.60 [-3.82, 2.43] | 15 | 0 |
| all/high | fixed_g8 | 110 | 10.64 [7.23, 14.37] | -27.87 [-31.80, -23.81] | 23 | 0 |
| all/high | markov_w0_dist | 110 | 12.93 [8.45, 16.60] | -12.71 [-15.09, -10.46] | 25 | 0 |
| all/high | markov_w05_dist | 110 | 0.99 [-1.32, 3.41] | 3.28 [1.26, 5.35] | 17 | 0 |
| all/high | sync_g4_vs_fixed_g2 | 110 | -7.18 [-7.87, -6.53] | 2.43 [1.73, 3.08] | 15 | 0 |
| all/high | fixed_fast_vs_fixed_g2 | 110 | 27.68 [24.16, 31.26] | 0.60 [-2.49, 3.68] | 15 | 0 |
| all/high | fixed_g8_vs_fixed_g2 | 110 | 41.27 [33.29, 50.43] | -27.11 [-35.00, -19.40] | 27 | 0 |
| all/high | markov_w0_dist_vs_fixed_g2 | 110 | 44.19 [36.32, 51.86] | -12.04 [-16.47, -7.82] | 19 | 0 |
| all/high | markov_w05_dist_vs_fixed_g2 | 110 | 28.94 [22.84, 35.00] | 3.86 [2.45, 5.38] | 14 | 0 |
| all/high | sync_g4_vs_fixed_g8 | 110 | -34.29 [-38.16, -30.40] | 23.24 [18.16, 27.78] | 23 | 0 |
| all/high | fixed_g2_vs_fixed_g8 | 110 | -29.21 [-33.52, -24.97] | 21.33 [16.25, 25.92] | 27 | 0 |
| all/high | fixed_fast_vs_fixed_g8 | 110 | -9.62 [-12.57, -6.74] | 21.80 [19.23, 24.13] | 23 | 0 |
| all/high | markov_w0_dist_vs_fixed_g8 | 110 | 2.07 [-2.27, 5.33] | 11.86 [8.64, 14.74] | 25 | 0 |
| all/high | markov_w05_dist_vs_fixed_g8 | 110 | -8.72 [-10.59, -6.94] | 24.36 [20.33, 27.92] | 27 | 0 |
| all/high | fixed_g2_vs_sync_g4 | 110 | 7.73 [6.98, 8.54] | -2.49 [-3.18, -1.76] | 15 | 0 |
| all/high | fixed_fast_vs_sync_g4 | 110 | 37.55 [33.84, 41.29] | -1.88 [-5.16, 1.30] | 0 | 0 |
| all/high | fixed_g8_vs_sync_g4 | 110 | 52.19 [43.67, 61.71] | -30.27 [-38.47, -22.19] | 23 | 0 |
| all/high | markov_w0_dist_vs_sync_g4 | 110 | 55.34 [47.21, 63.69] | -14.82 [-19.57, -10.35] | 25 | 0 |
| all/high | markov_w05_dist_vs_sync_g4 | 110 | 38.91 [32.51, 45.45] | 1.47 [-0.23, 3.19] | 17 | 0 |
| all/dynamic | sync_g4 | 110 | -26.94 [-29.57, -24.31] | 13.38 [10.20, 16.38] | 0 | 0 |
| all/dynamic | fixed_g2 | 110 | -7.37 [-10.22, -4.50] | 14.21 [11.51, 16.72] | 15 | 0 |
| all/dynamic | fixed_g8 | 110 | -10.71 [-13.74, -7.49] | -36.92 [-41.21, -32.54] | 25 | 0 |
| all/dynamic | markov_w0_dist | 110 | 5.29 [3.59, 7.21] | 2.29 [-0.52, 5.14] | 19 | 0 |
| all/dynamic | markov_w05_dist | 110 | -0.93 [-3.04, 1.06] | 13.29 [9.57, 16.94] | 18 | 1 |
| all/dynamic | sync_g4_vs_fixed_g2 | 110 | -21.13 [-22.63, -19.64] | -0.97 [-2.11, 0.06] | 15 | 0 |
| all/dynamic | fixed_fast_vs_fixed_g2 | 110 | 7.95 [4.71, 11.38] | -16.57 [-20.07, -13.01] | 15 | 0 |
| all/dynamic | fixed_g8_vs_fixed_g2 | 110 | -3.61 [-9.36, 2.60] | -59.60 [-69.34, -50.05] | 34 | 0 |
| all/dynamic | markov_w0_dist_vs_fixed_g2 | 110 | 13.66 [10.53, 17.11] | -13.89 [-16.15, -11.66] | 19 | 0 |
| all/dynamic | markov_w05_dist_vs_fixed_g2 | 110 | 6.95 [4.35, 9.84] | -1.08 [-3.01, 0.76] | 18 | 1 |
| all/dynamic | sync_g4_vs_fixed_g8 | 110 | -18.17 [-23.41, -12.84] | 36.74 [32.28, 40.75] | 25 | 0 |
| all/dynamic | fixed_g2_vs_fixed_g8 | 110 | 3.75 [-2.54, 10.33] | 37.34 [33.35, 40.95] | 34 | 0 |
| all/dynamic | fixed_fast_vs_fixed_g8 | 110 | 12.00 [8.10, 15.93] | 26.97 [24.55, 29.18] | 25 | 0 |
| all/dynamic | markov_w0_dist_vs_fixed_g8 | 110 | 17.92 [13.15, 22.84] | 28.64 [24.34, 32.69] | 32 | 0 |
| all/dynamic | markov_w05_dist_vs_fixed_g8 | 110 | 10.96 [5.59, 16.45] | 36.67 [31.81, 41.14] | 34 | 1 |
| all/dynamic | fixed_g2_vs_sync_g4 | 110 | 26.79 [24.44, 29.25] | 0.96 [-0.06, 2.07] | 15 | 0 |
| all/dynamic | fixed_fast_vs_sync_g4 | 110 | 36.87 [32.11, 41.99] | -15.45 [-19.59, -11.35] | 0 | 0 |
| all/dynamic | fixed_g8_vs_sync_g4 | 110 | 22.21 [14.74, 30.56] | -58.07 [-68.77, -47.66] | 25 | 0 |
| all/dynamic | markov_w0_dist_vs_sync_g4 | 110 | 44.11 [39.33, 49.45] | -12.80 [-15.73, -9.78] | 19 | 0 |
| all/dynamic | markov_w05_dist_vs_sync_g4 | 110 | 35.60 [31.73, 39.68] | -0.11 [-1.88, 1.64] | 18 | 1 |
| all/pooled | sync_g4 | 110 | -27.06 [-29.31, -24.69] | 11.21 [8.15, 14.24] | 1 | 0 |
| all/pooled | fixed_g2 | 110 | -12.50 [-14.89, -10.07] | 9.50 [6.79, 12.10] | 46 | 0 |
| all/pooled | fixed_g8 | 110 | -6.42 [-9.20, -3.44] | -35.32 [-39.34, -31.22] | 76 | 0 |
| all/pooled | markov_w0_dist | 110 | 7.43 [5.53, 8.97] | -0.23 [-2.34, 1.85] | 53 | 0 |
| all/pooled | markov_w05_dist | 110 | 0.18 [-0.90, 1.33] | 11.32 [8.14, 14.35] | 51 | 1 |
| all/pooled | sync_g4_vs_fixed_g2 | 110 | -16.63 [-17.39, -15.91] | 1.89 [1.09, 2.63] | 46 | 0 |
| all/pooled | fixed_fast_vs_fixed_g2 | 110 | 14.29 [11.19, 17.50] | -10.50 [-13.76, -7.28] | 46 | 0 |
| all/pooled | fixed_g8_vs_fixed_g2 | 110 | 6.95 [1.14, 13.50] | -49.54 [-58.46, -40.76] | 94 | 0 |
| all/pooled | markov_w0_dist_vs_fixed_g2 | 110 | 22.78 [19.03, 26.56] | -10.75 [-12.86, -8.59] | 52 | 0 |
| all/pooled | markov_w05_dist_vs_fixed_g2 | 110 | 14.50 [11.33, 17.66] | 2.01 [0.94, 3.02] | 40 | 1 |
| all/pooled | sync_g4_vs_fixed_g8 | 110 | -22.05 [-26.81, -17.17] | 34.39 [30.07, 38.40] | 76 | 0 |
| all/pooled | fixed_g2_vs_fixed_g8 | 110 | -6.50 [-11.89, -1.13] | 33.13 [28.95, 36.89] | 94 | 0 |
| all/pooled | fixed_fast_vs_fixed_g8 | 110 | 6.86 [3.56, 10.13] | 26.10 [23.79, 28.23] | 76 | 0 |
| all/pooled | markov_w0_dist_vs_fixed_g8 | 110 | 14.80 [10.57, 18.71] | 25.94 [22.15, 29.29] | 90 | 0 |
| all/pooled | markov_w05_dist_vs_fixed_g8 | 110 | 7.05 [3.28, 10.79] | 34.47 [29.92, 38.47] | 93 | 1 |
| all/pooled | fixed_g2_vs_sync_g4 | 110 | 19.95 [18.92, 21.05] | -1.92 [-2.71, -1.10] | 46 | 0 |
| all/pooled | fixed_fast_vs_sync_g4 | 110 | 37.09 [32.78, 41.46] | -12.63 [-16.61, -8.88] | 1 | 0 |
| all/pooled | fixed_g8_vs_sync_g4 | 110 | 28.29 [20.72, 36.63] | -52.41 [-62.33, -43.01] | 76 | 0 |
| all/pooled | markov_w0_dist_vs_sync_g4 | 110 | 47.28 [42.12, 52.56] | -12.88 [-15.72, -10.08] | 53 | 0 |
| all/pooled | markov_w05_dist_vs_sync_g4 | 110 | 37.34 [33.00, 41.82] | 0.12 [-1.05, 1.37] | 51 | 1 |
| humaneval/low | sync_g4 | 30 | -31.69 [-33.61, -29.97] | 16.06 [13.52, 18.17] | 0 | 0 |
| humaneval/low | fixed_g2 | 30 | -2.26 [-4.15, -0.46] | 12.50 [10.87, 13.99] | 5 | 0 |
| humaneval/low | fixed_g8 | 30 | -21.27 [-23.26, -19.11] | -37.83 [-41.20, -34.37] | 6 | 0 |
| humaneval/low | markov_w0_dist | 30 | -5.17 [-6.67, -3.67] | 3.27 [1.42, 5.03] | 1 | 0 |
| humaneval/low | markov_w05_dist | 30 | -5.83 [-7.62, -3.84] | 9.15 [6.58, 11.80] | 5 | 0 |
| humaneval/low | sync_g4_vs_fixed_g2 | 30 | -30.11 [-31.49, -28.85] | 4.06 [2.41, 5.49] | 5 | 0 |
| humaneval/low | fixed_fast_vs_fixed_g2 | 30 | 2.32 [0.46, 4.33] | -14.28 [-16.26, -12.19] | 5 | 0 |
| humaneval/low | fixed_g8_vs_fixed_g2 | 30 | -19.45 [-22.15, -16.27] | -57.51 [-63.02, -51.64] | 7 | 0 |
| humaneval/low | markov_w0_dist_vs_fixed_g2 | 30 | -2.97 [-4.76, -1.06] | -10.55 [-12.13, -8.91] | 5 | 0 |
| humaneval/low | markov_w05_dist_vs_fixed_g2 | 30 | -3.65 [-5.96, -1.15] | -3.82 [-5.52, -1.91] | 0 | 0 |
| humaneval/low | sync_g4_vs_fixed_g8 | 30 | -13.23 [-17.48, -9.41] | 39.09 [36.00, 41.72] | 6 | 0 |
| humaneval/low | fixed_g2_vs_fixed_g8 | 30 | 24.14 [19.44, 28.45] | 36.51 [34.05, 38.66] | 7 | 0 |
| humaneval/low | fixed_fast_vs_fixed_g8 | 30 | 27.01 [23.63, 30.32] | 27.44 [25.58, 29.18] | 6 | 0 |
| humaneval/low | markov_w0_dist_vs_fixed_g8 | 30 | 20.45 [16.53, 24.37] | 29.82 [26.99, 32.35] | 7 | 0 |
| humaneval/low | markov_w05_dist_vs_fixed_g8 | 30 | 19.61 [15.51, 23.82] | 34.09 [30.87, 36.91] | 7 | 0 |
| humaneval/low | fixed_g2_vs_sync_g4 | 30 | 43.08 [40.54, 45.97] | -4.24 [-5.81, -2.47] | 5 | 0 |
| humaneval/low | fixed_fast_vs_sync_g4 | 30 | 46.39 [42.79, 50.62] | -19.13 [-22.20, -15.64] | 0 | 0 |
| humaneval/low | fixed_g8_vs_sync_g4 | 30 | 15.25 [10.39, 21.18] | -64.19 [-71.57, -56.24] | 6 | 0 |
| humaneval/low | markov_w0_dist_vs_sync_g4 | 30 | 38.82 [35.47, 42.67] | -15.23 [-17.74, -12.41] | 1 | 0 |
| humaneval/low | markov_w05_dist_vs_sync_g4 | 30 | 37.85 [34.17, 42.40] | -8.22 [-10.05, -6.42] | 5 | 0 |
| humaneval/high | sync_g4 | 30 | -30.61 [-32.25, -29.14] | -3.63 [-6.43, -1.26] | 0 | 0 |
| humaneval/high | fixed_g2 | 30 | -25.66 [-27.21, -24.18] | -6.57 [-9.09, -4.24] | 4 | 0 |
| humaneval/high | fixed_g8 | 30 | 17.66 [14.36, 21.27] | -21.89 [-25.24, -18.51] | 5 | 0 |
| humaneval/high | markov_w0_dist | 30 | 10.80 [-0.68, 19.46] | -16.62 [-22.14, -12.00] | 5 | 0 |
| humaneval/high | markov_w05_dist | 30 | 5.27 [2.30, 9.09] | -3.32 [-4.95, -1.85] | 4 | 0 |
| humaneval/high | sync_g4_vs_fixed_g2 | 30 | -6.66 [-7.66, -5.66] | 2.76 [1.85, 3.71] | 4 | 0 |
| humaneval/high | fixed_fast_vs_fixed_g2 | 30 | 34.52 [31.89, 37.39] | 6.17 [4.07, 8.33] | 4 | 0 |
| humaneval/high | fixed_g8_vs_fixed_g2 | 30 | 58.28 [51.46, 66.28] | -14.38 [-19.33, -8.81] | 5 | 0 |
| humaneval/high | markov_w0_dist_vs_fixed_g2 | 30 | 49.04 [32.71, 63.24] | -9.43 [-15.77, -3.65] | 4 | 0 |
| humaneval/high | markov_w05_dist_vs_fixed_g2 | 30 | 41.60 [35.54, 49.18] | 3.05 [1.11, 5.34] | 2 | 0 |
| humaneval/high | sync_g4_vs_fixed_g8 | 30 | -41.03 [-44.00, -38.21] | 14.98 [10.45, 18.82] | 5 | 0 |
| humaneval/high | fixed_g2_vs_fixed_g8 | 30 | -36.82 [-39.86, -33.98] | 12.57 [8.09, 16.20] | 5 | 0 |
| humaneval/high | fixed_fast_vs_fixed_g8 | 30 | -15.01 [-17.54, -12.56] | 17.96 [15.62, 20.15] | 5 | 0 |
| humaneval/high | markov_w0_dist_vs_fixed_g8 | 30 | -5.83 [-15.63, 0.65] | 4.32 [-0.36, 7.65] | 5 | 0 |
| humaneval/high | markov_w05_dist_vs_fixed_g8 | 30 | -10.54 [-12.64, -8.09] | 15.24 [12.33, 17.82] | 5 | 0 |
| humaneval/high | fixed_g2_vs_sync_g4 | 30 | 7.13 [6.00, 8.29] | -2.84 [-3.85, -1.88] | 4 | 0 |
| humaneval/high | fixed_fast_vs_sync_g4 | 30 | 44.11 [41.12, 47.60] | 3.50 [1.25, 6.04] | 0 | 0 |
| humaneval/high | fixed_g8_vs_sync_g4 | 30 | 69.56 [61.85, 78.57] | -17.62 [-23.19, -11.67] | 5 | 0 |
| humaneval/high | markov_w0_dist_vs_sync_g4 | 30 | 59.67 [42.49, 75.47] | -12.54 [-18.86, -6.24] | 5 | 0 |
| humaneval/high | markov_w05_dist_vs_sync_g4 | 30 | 51.70 [44.70, 60.57] | 0.30 [-2.07, 2.97] | 4 | 0 |
| humaneval/dynamic | sync_g4 | 30 | -31.67 [-34.08, -29.48] | 7.82 [5.51, 9.88] | 0 | 0 |
| humaneval/dynamic | fixed_g2 | 30 | -11.26 [-12.85, -9.75] | 9.81 [8.00, 11.42] | 4 | 0 |
| humaneval/dynamic | fixed_g8 | 30 | -5.95 [-9.56, -2.41] | -29.99 [-33.71, -26.31] | 7 | 0 |
| humaneval/dynamic | markov_w0_dist | 30 | 2.58 [0.03, 5.06] | -4.98 [-7.41, -2.58] | 5 | 0 |
| humaneval/dynamic | markov_w05_dist | 30 | -3.46 [-5.31, -1.57] | 4.39 [2.01, 6.68] | 6 | 0 |
| humaneval/dynamic | sync_g4_vs_fixed_g2 | 30 | -23.00 [-25.41, -20.76] | -2.20 [-3.91, -0.53] | 4 | 0 |
| humaneval/dynamic | fixed_fast_vs_fixed_g2 | 30 | 12.69 [10.80, 14.74] | -10.87 [-12.90, -8.69] | 4 | 0 |
| humaneval/dynamic | fixed_g8_vs_fixed_g2 | 30 | 5.99 [1.22, 10.92] | -44.13 [-49.62, -38.43] | 10 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_fixed_g2 | 30 | 15.60 [12.49, 18.81] | -16.40 [-19.08, -13.66] | 6 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_fixed_g2 | 30 | 8.79 [6.20, 11.85] | -6.01 [-7.96, -4.07] | 4 | 0 |
| humaneval/dynamic | sync_g4_vs_fixed_g8 | 30 | -27.35 [-30.63, -24.31] | 29.09 [25.71, 31.98] | 7 | 0 |
| humaneval/dynamic | fixed_g2_vs_fixed_g8 | 30 | -5.65 [-9.84, -1.21] | 30.62 [27.76, 33.17] | 10 | 0 |
| humaneval/dynamic | fixed_fast_vs_fixed_g8 | 30 | 6.32 [2.47, 10.56] | 23.07 [20.83, 25.21] | 7 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_fixed_g8 | 30 | 9.07 [5.67, 12.62] | 19.24 [16.05, 22.34] | 8 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_fixed_g8 | 30 | 2.65 [-0.81, 6.39] | 26.45 [23.15, 29.57] | 9 | 0 |
| humaneval/dynamic | fixed_g2_vs_sync_g4 | 30 | 29.87 [26.19, 34.07] | 2.15 [0.52, 3.77] | 4 | 0 |
| humaneval/dynamic | fixed_fast_vs_sync_g4 | 30 | 46.35 [41.80, 51.70] | -8.49 [-10.97, -5.83] | 0 | 0 |
| humaneval/dynamic | fixed_g8_vs_sync_g4 | 30 | 37.65 [32.12, 44.16] | -41.03 [-47.02, -34.61] | 7 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_sync_g4 | 30 | 50.13 [45.05, 55.74] | -13.90 [-17.49, -10.17] | 5 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_sync_g4 | 30 | 41.29 [36.55, 46.88] | -3.73 [-6.32, -1.04] | 6 | 0 |
| humaneval/pooled | sync_g4 | 30 | -31.19 [-32.98, -29.69] | 5.82 [3.47, 7.83] | 0 | 0 |
| humaneval/pooled | fixed_g2 | 30 | -16.95 [-18.39, -15.59] | 4.31 [2.44, 5.98] | 13 | 0 |
| humaneval/pooled | fixed_g8 | 30 | -1.18 [-3.78, 1.50] | -29.17 [-32.35, -26.03] | 18 | 0 |
| humaneval/pooled | markov_w0_dist | 30 | 4.19 [-0.51, 7.80] | -7.08 [-9.02, -5.29] | 11 | 0 |
| humaneval/pooled | markov_w05_dist | 30 | -0.26 [-1.88, 1.80] | 2.79 [1.27, 4.39] | 15 | 0 |
| humaneval/pooled | sync_g4_vs_fixed_g2 | 30 | -17.14 [-18.26, -16.14] | 1.58 [0.55, 2.57] | 13 | 0 |
| humaneval/pooled | fixed_fast_vs_fixed_g2 | 30 | 20.41 [18.48, 22.54] | -4.50 [-6.36, -2.50] | 13 | 0 |
| humaneval/pooled | fixed_g8_vs_fixed_g2 | 30 | 19.00 [14.83, 23.74] | -34.99 [-39.91, -29.63] | 22 | 0 |
| humaneval/pooled | markov_w0_dist_vs_fixed_g2 | 30 | 25.46 [18.85, 31.09] | -11.90 [-14.82, -8.94] | 15 | 0 |
| humaneval/pooled | markov_w05_dist_vs_fixed_g2 | 30 | 20.10 [16.93, 24.04] | -1.59 [-2.63, -0.37] | 6 | 0 |
| humaneval/pooled | sync_g4_vs_fixed_g8 | 30 | -30.37 [-33.64, -27.38] | 27.09 [23.45, 30.13] | 18 | 0 |
| humaneval/pooled | fixed_g2_vs_fixed_g8 | 30 | -15.96 [-19.19, -12.91] | 25.92 [22.86, 28.53] | 22 | 0 |
| humaneval/pooled | fixed_fast_vs_fixed_g8 | 30 | 1.19 [-1.47, 3.93] | 22.58 [20.65, 24.44] | 18 | 0 |
| humaneval/pooled | markov_w0_dist_vs_fixed_g8 | 30 | 5.43 [0.28, 9.34] | 17.10 [14.64, 19.31] | 20 | 0 |
| humaneval/pooled | markov_w05_dist_vs_fixed_g8 | 30 | 0.93 [-1.17, 3.46] | 24.74 [21.93, 27.31] | 21 | 0 |
| humaneval/pooled | fixed_g2_vs_sync_g4 | 30 | 20.69 [19.25, 22.33] | -1.61 [-2.64, -0.55] | 13 | 0 |
| humaneval/pooled | fixed_fast_vs_sync_g4 | 30 | 45.33 [42.23, 49.20] | -6.18 [-8.50, -3.60] | 0 | 0 |
| humaneval/pooled | fixed_g8_vs_sync_g4 | 30 | 43.62 [37.70, 50.70] | -37.15 [-43.12, -30.63] | 18 | 0 |
| humaneval/pooled | markov_w0_dist_vs_sync_g4 | 30 | 51.41 [43.91, 58.93] | -13.70 [-16.87, -10.07] | 11 | 0 |
| humaneval/pooled | markov_w05_dist_vs_sync_g4 | 30 | 44.95 [40.21, 50.99] | -3.22 [-4.83, -1.33] | 15 | 0 |
| gsm8k/low | sync_g4 | 50 | -35.73 [-37.37, -34.09] | 9.81 [7.56, 11.86] | 0 | 0 |
| gsm8k/low | fixed_g2 | 50 | -4.33 [-6.28, -2.30] | 9.35 [7.58, 10.96] | 3 | 0 |
| gsm8k/low | fixed_g8 | 50 | -16.00 [-18.38, -13.27] | -28.33 [-31.61, -24.78] | 8 | 0 |
| gsm8k/low | markov_w0_dist | 50 | -5.98 [-7.57, -4.52] | 4.13 [1.74, 6.33] | 2 | 0 |
| gsm8k/low | markov_w05_dist | 50 | -7.91 [-9.61, -6.29] | 8.32 [6.11, 10.44] | 2 | 0 |
| gsm8k/low | sync_g4_vs_fixed_g2 | 50 | -32.83 [-34.07, -31.63] | 0.50 [-0.87, 1.80] | 3 | 0 |
| gsm8k/low | fixed_fast_vs_fixed_g2 | 50 | 4.52 [2.36, 6.70] | -10.32 [-12.31, -8.20] | 3 | 0 |
| gsm8k/low | fixed_g8_vs_fixed_g2 | 50 | -12.20 [-15.98, -7.93] | -41.57 [-47.21, -35.54] | 10 | 0 |
| gsm8k/low | markov_w0_dist_vs_fixed_g2 | 50 | -1.72 [-4.02, 0.62] | -5.76 [-7.87, -3.66] | 1 | 0 |
| gsm8k/low | markov_w05_dist_vs_fixed_g2 | 50 | -3.75 [-5.81, -1.83] | -1.14 [-2.80, 0.65] | 1 | 0 |
| gsm8k/low | sync_g4_vs_fixed_g8 | 50 | -23.49 [-27.38, -19.72] | 29.72 [26.14, 32.92] | 8 | 0 |
| gsm8k/low | fixed_g2_vs_fixed_g8 | 50 | 13.89 [8.62, 19.03] | 29.36 [26.22, 32.07] | 10 | 0 |
| gsm8k/low | fixed_fast_vs_fixed_g8 | 50 | 19.04 [15.30, 22.51] | 22.08 [19.86, 24.02] | 8 | 0 |
| gsm8k/low | markov_w0_dist_vs_fixed_g8 | 50 | 11.93 [7.58, 15.96] | 25.30 [21.74, 28.47] | 9 | 0 |
| gsm8k/low | markov_w05_dist_vs_fixed_g8 | 50 | 9.62 [5.14, 14.06] | 28.56 [25.25, 31.66] | 9 | 0 |
| gsm8k/low | fixed_g2_vs_sync_g4 | 50 | 48.87 [46.26, 51.68] | -0.51 [-1.83, 0.87] | 3 | 0 |
| gsm8k/low | fixed_fast_vs_sync_g4 | 50 | 55.60 [51.73, 59.67] | -10.87 [-13.46, -8.18] | 0 | 0 |
| gsm8k/low | fixed_g8_vs_sync_g4 | 50 | 30.71 [24.57, 37.69] | -42.28 [-49.08, -35.40] | 8 | 0 |
| gsm8k/low | markov_w0_dist_vs_sync_g4 | 50 | 46.30 [42.58, 50.04] | -6.29 [-8.73, -3.93] | 2 | 0 |
| gsm8k/low | markov_w05_dist_vs_sync_g4 | 50 | 43.29 [40.33, 46.03] | -1.65 [-3.61, 0.41] | 2 | 0 |
| gsm8k/high | sync_g4 | 50 | -33.86 [-35.11, -32.66] | -9.74 [-12.18, -7.38] | 0 | 0 |
| gsm8k/high | fixed_g2 | 50 | -28.92 [-30.19, -27.59] | -12.09 [-14.42, -9.71] | 2 | 0 |
| gsm8k/high | fixed_g8 | 50 | 24.97 [22.20, 27.92] | -13.24 [-15.88, -10.50] | 8 | 0 |
| gsm8k/high | markov_w0_dist | 50 | 23.10 [20.84, 25.34] | -7.90 [-10.01, -5.80] | 9 | 0 |
| gsm8k/high | markov_w05_dist | 50 | 7.30 [4.08, 10.73] | -1.02 [-2.51, 0.49] | 7 | 0 |
| gsm8k/high | sync_g4_vs_fixed_g2 | 50 | -6.96 [-7.80, -6.05] | 2.10 [1.20, 3.04] | 2 | 0 |
| gsm8k/high | fixed_fast_vs_fixed_g2 | 50 | 40.68 [38.10, 43.24] | 10.78 [8.85, 12.60] | 2 | 0 |
| gsm8k/high | fixed_g8_vs_fixed_g2 | 50 | 75.81 [69.31, 82.79] | -1.03 [-5.20, 3.22] | 9 | 0 |
| gsm8k/high | markov_w0_dist_vs_fixed_g2 | 50 | 73.17 [67.79, 78.76] | 3.74 [0.62, 6.96] | 9 | 0 |
| gsm8k/high | markov_w05_dist_vs_fixed_g2 | 50 | 50.94 [44.45, 58.04] | 9.87 [8.00, 11.87] | 7 | 0 |
| gsm8k/high | sync_g4_vs_fixed_g8 | 50 | -47.08 [-49.15, -44.98] | 3.10 [-1.34, 7.10] | 8 | 0 |
| gsm8k/high | fixed_g2_vs_fixed_g8 | 50 | -43.12 [-45.29, -40.94] | 1.02 [-3.33, 4.94] | 9 | 0 |
| gsm8k/high | fixed_fast_vs_fixed_g8 | 50 | -19.98 [-21.82, -18.17] | 11.70 [9.50, 13.70] | 8 | 0 |
| gsm8k/high | markov_w0_dist_vs_fixed_g8 | 50 | -1.50 [-3.14, 0.26] | 4.72 [2.79, 6.73] | 9 | 0 |
| gsm8k/high | markov_w05_dist_vs_fixed_g8 | 50 | -14.14 [-16.11, -12.13] | 10.79 [8.22, 13.28] | 11 | 0 |
| gsm8k/high | fixed_g2_vs_sync_g4 | 50 | 7.48 [6.44, 8.46] | -2.14 [-3.14, -1.21] | 2 | 0 |
| gsm8k/high | fixed_fast_vs_sync_g4 | 50 | 51.21 [48.51, 54.11] | 8.87 [6.87, 10.86] | 0 | 0 |
| gsm8k/high | fixed_g8_vs_sync_g4 | 50 | 88.96 [81.74, 96.66] | -3.20 [-7.64, 1.32] | 8 | 0 |
| gsm8k/high | markov_w0_dist_vs_sync_g4 | 50 | 86.13 [80.56, 91.97] | 1.67 [-1.63, 5.05] | 9 | 0 |
| gsm8k/high | markov_w05_dist_vs_sync_g4 | 50 | 62.24 [55.51, 69.87] | 7.94 [5.84, 10.10] | 7 | 0 |
| gsm8k/dynamic | sync_g4 | 50 | -35.06 [-37.22, -32.91] | 1.58 [-1.57, 4.40] | 0 | 0 |
| gsm8k/dynamic | fixed_g2 | 50 | -16.84 [-19.60, -14.23] | 4.31 [1.52, 6.70] | 3 | 0 |
| gsm8k/dynamic | fixed_g8 | 50 | 0.40 [-3.03, 4.00] | -22.03 [-25.22, -18.62] | 7 | 0 |
| gsm8k/dynamic | markov_w0_dist | 50 | 4.09 [1.73, 6.39] | -3.82 [-6.16, -1.51] | 5 | 0 |
| gsm8k/dynamic | markov_w05_dist | 50 | -6.31 [-9.72, -3.46] | 1.78 [-0.45, 4.03] | 5 | 0 |
| gsm8k/dynamic | sync_g4_vs_fixed_g2 | 50 | -21.91 [-24.35, -19.57] | -2.85 [-4.54, -1.23] | 3 | 0 |
| gsm8k/dynamic | fixed_fast_vs_fixed_g2 | 50 | 20.25 [16.59, 24.37] | -4.50 [-7.18, -1.54] | 3 | 0 |
| gsm8k/dynamic | fixed_g8_vs_fixed_g2 | 50 | 20.73 [14.06, 28.28] | -27.53 [-33.36, -21.25] | 9 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_fixed_g2 | 50 | 25.17 [20.13, 30.89] | -8.50 [-11.78, -4.98] | 4 | 0 |
| gsm8k/dynamic | markov_w05_dist_vs_fixed_g2 | 50 | 12.67 [6.85, 18.54] | -2.64 [-5.20, 0.04] | 4 | 0 |
| gsm8k/dynamic | sync_g4_vs_fixed_g8 | 50 | -35.32 [-38.75, -31.89] | 19.35 [14.99, 23.35] | 7 | 0 |
| gsm8k/dynamic | fixed_g2_vs_fixed_g8 | 50 | -17.17 [-22.05, -12.33] | 21.58 [17.52, 25.02] | 9 | 0 |
| gsm8k/dynamic | fixed_fast_vs_fixed_g8 | 50 | -0.40 [-3.85, 3.12] | 18.05 [15.70, 20.14] | 7 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_fixed_g8 | 50 | 3.67 [0.57, 6.57] | 14.92 [11.76, 17.81] | 10 | 0 |
| gsm8k/dynamic | markov_w05_dist_vs_fixed_g8 | 50 | -6.68 [-10.22, -3.44] | 19.52 [16.02, 22.79] | 10 | 0 |
| gsm8k/dynamic | fixed_g2_vs_sync_g4 | 50 | 28.06 [24.33, 32.20] | 2.77 [1.22, 4.35] | 3 | 0 |
| gsm8k/dynamic | fixed_fast_vs_sync_g4 | 50 | 53.99 [49.06, 59.28] | -1.60 [-4.60, 1.54] | 0 | 0 |
| gsm8k/dynamic | fixed_g8_vs_sync_g4 | 50 | 54.61 [46.81, 63.25] | -23.99 [-30.47, -17.63] | 7 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_sync_g4 | 50 | 60.29 [54.53, 66.81] | -5.49 [-9.49, -1.36] | 5 | 0 |
| gsm8k/dynamic | markov_w05_dist_vs_sync_g4 | 50 | 44.28 [37.99, 51.11] | 0.21 [-2.47, 3.11] | 5 | 0 |
| gsm8k/pooled | sync_g4 | 50 | -34.68 [-36.17, -33.17] | -0.30 [-2.78, 2.03] | 0 | 0 |
| gsm8k/pooled | fixed_g2 | 50 | -20.68 [-22.30, -19.11] | -0.46 [-2.58, 1.58] | 8 | 0 |
| gsm8k/pooled | fixed_g8 | 50 | 5.21 [2.72, 7.99] | -20.53 [-23.33, -17.55] | 23 | 0 |
| gsm8k/pooled | markov_w0_dist | 50 | 9.12 [7.73, 10.47] | -3.05 [-4.51, -1.57] | 16 | 0 |
| gsm8k/pooled | markov_w05_dist | 50 | -0.99 [-2.84, 0.82] | 2.60 [1.04, 4.19] | 14 | 0 |
| gsm8k/pooled | sync_g4_vs_fixed_g2 | 50 | -17.65 [-18.68, -16.63] | 0.16 [-0.82, 1.21] | 8 | 0 |
| gsm8k/pooled | fixed_fast_vs_fixed_g2 | 50 | 26.07 [23.62, 28.70] | 0.46 [-1.61, 2.51] | 8 | 0 |
| gsm8k/pooled | fixed_g8_vs_fixed_g2 | 50 | 32.63 [27.37, 38.53] | -19.98 [-24.98, -14.73] | 28 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_fixed_g2 | 50 | 37.57 [34.19, 41.33] | -2.58 [-4.93, -0.17] | 14 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_fixed_g2 | 50 | 24.82 [20.95, 29.09] | 3.05 [1.56, 4.75] | 12 | 0 |
| gsm8k/pooled | sync_g4_vs_fixed_g8 | 50 | -37.91 [-40.72, -35.19] | 16.78 [12.67, 20.41] | 23 | 0 |
| gsm8k/pooled | fixed_g2_vs_fixed_g8 | 50 | -24.60 [-27.81, -21.49] | 16.65 [12.84, 19.98] | 28 | 0 |
| gsm8k/pooled | fixed_fast_vs_fixed_g8 | 50 | -4.95 [-7.40, -2.64] | 17.03 [14.93, 18.92] | 23 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_fixed_g8 | 50 | 3.72 [1.24, 6.15] | 14.50 [11.87, 16.90] | 28 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_fixed_g8 | 50 | -5.89 [-7.97, -3.72] | 19.19 [16.25, 21.93] | 30 | 0 |
| gsm8k/pooled | fixed_g2_vs_sync_g4 | 50 | 21.43 [19.95, 22.97] | -0.16 [-1.22, 0.81] | 8 | 0 |
| gsm8k/pooled | fixed_fast_vs_sync_g4 | 50 | 53.08 [49.64, 56.67] | 0.30 [-2.08, 2.71] | 0 | 0 |
| gsm8k/pooled | fixed_g8_vs_sync_g4 | 50 | 61.05 [54.29, 68.70] | -20.16 [-25.64, -14.50] | 23 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_sync_g4 | 50 | 67.05 [62.55, 71.99] | -2.74 [-5.54, 0.15] | 16 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_sync_g4 | 50 | 51.56 [46.66, 56.93] | 2.90 [0.92, 4.96] | 14 | 0 |
| mtbench/low | sync_g4 | 30 | -10.10 [-13.35, -6.93] | 34.74 [32.22, 36.72] | 1 | 0 |
| mtbench/low | fixed_g2 | 30 | 18.81 [15.25, 22.70] | 28.39 [26.18, 30.37] | 8 | 0 |
| mtbench/low | fixed_g8 | 30 | -33.06 [-34.80, -30.74] | -60.78 [-64.44, -56.09] | 14 | 0 |
| mtbench/low | markov_w0_dist | 30 | 13.10 [9.55, 17.16] | 29.03 [24.86, 32.79] | 6 | 0 |
| mtbench/low | markov_w05_dist | 30 | 15.39 [10.87, 20.15] | 37.84 [33.62, 41.17] | 9 | 0 |
| mtbench/low | sync_g4_vs_fixed_g2 | 30 | -24.34 [-26.14, -22.61] | 8.87 [7.03, 10.54] | 8 | 0 |
| mtbench/low | fixed_fast_vs_fixed_g2 | 30 | -15.84 [-18.50, -13.23] | -39.64 [-43.62, -35.46] | 8 | 0 |
| mtbench/low | fixed_g8_vs_fixed_g2 | 30 | -43.66 [-46.27, -40.44] | -124.51 [-135.06, -112.39] | 16 | 0 |
| mtbench/low | markov_w0_dist_vs_fixed_g2 | 30 | -4.81 [-6.66, -3.04] | 0.90 [-2.36, 4.11] | 8 | 0 |
| mtbench/low | markov_w05_dist_vs_fixed_g2 | 30 | -2.89 [-4.64, -1.07] | 13.20 [9.86, 16.01] | 7 | 0 |
| mtbench/low | sync_g4_vs_fixed_g8 | 30 | 34.29 [25.42, 41.92] | 59.41 [56.64, 61.36] | 14 | 0 |
| mtbench/low | fixed_g2_vs_fixed_g8 | 30 | 77.49 [67.91, 86.13] | 55.46 [52.92, 57.46] | 16 | 0 |
| mtbench/low | fixed_fast_vs_fixed_g8 | 30 | 49.38 [44.38, 53.36] | 37.80 [35.93, 39.19] | 14 | 0 |
| mtbench/low | markov_w0_dist_vs_fixed_g8 | 30 | 68.96 [59.64, 78.08] | 55.86 [52.08, 58.91] | 17 | 0 |
| mtbench/low | markov_w05_dist_vs_fixed_g8 | 30 | 72.37 [61.44, 82.74] | 61.34 [57.61, 64.10] | 16 | 0 |
| mtbench/low | fixed_g2_vs_sync_g4 | 30 | 32.16 [29.21, 35.38] | -9.73 [-11.78, -7.56] | 8 | 0 |
| mtbench/low | fixed_fast_vs_sync_g4 | 30 | 11.24 [7.44, 15.41] | -53.23 [-58.03, -47.54] | 1 | 0 |
| mtbench/low | fixed_g8_vs_sync_g4 | 30 | -25.54 [-29.54, -20.27] | -146.36 [-158.77, -130.63] | 14 | 0 |
| mtbench/low | markov_w0_dist_vs_sync_g4 | 30 | 25.81 [22.85, 28.93] | -8.74 [-12.08, -5.30] | 6 | 0 |
| mtbench/low | markov_w05_dist_vs_sync_g4 | 30 | 28.35 [25.33, 31.62] | 4.75 [1.56, 7.83] | 9 | 0 |
| mtbench/high | sync_g4 | 30 | -16.14 [-18.49, -13.99] | 16.67 [13.93, 18.91] | 0 | 0 |
| mtbench/high | fixed_g2 | 30 | -8.94 [-12.01, -5.81] | 14.49 [11.53, 17.19] | 9 | 0 |
| mtbench/high | fixed_g8 | 30 | -4.96 [-7.88, -1.49] | -46.68 [-51.43, -41.61] | 10 | 0 |
| mtbench/high | markov_w0_dist | 30 | 6.13 [4.14, 8.50] | -14.14 [-17.55, -10.42] | 11 | 0 |
| mtbench/high | markov_w05_dist | 30 | -7.61 [-9.35, -5.46] | 12.25 [9.58, 14.84] | 6 | 0 |
| mtbench/high | sync_g4_vs_fixed_g2 | 30 | -7.91 [-9.37, -6.56] | 2.55 [1.05, 3.94] | 9 | 0 |
| mtbench/high | fixed_fast_vs_fixed_g2 | 30 | 9.81 [6.17, 13.65] | -16.95 [-20.76, -13.03] | 9 | 0 |
| mtbench/high | fixed_g8_vs_fixed_g2 | 30 | 4.37 [-1.51, 11.37] | -71.54 [-81.11, -60.93] | 13 | 0 |
| mtbench/high | markov_w0_dist_vs_fixed_g2 | 30 | 16.55 [12.39, 21.78] | -33.48 [-37.37, -28.80] | 6 | 0 |
| mtbench/high | markov_w05_dist_vs_fixed_g2 | 30 | 1.46 [-2.03, 5.92] | -2.63 [-4.11, -1.04] | 5 | 0 |
| mtbench/high | sync_g4_vs_fixed_g8 | 30 | -11.76 [-17.02, -7.03] | 43.19 [39.49, 46.08] | 10 | 0 |
| mtbench/high | fixed_g2_vs_fixed_g8 | 30 | -4.18 [-10.21, 1.53] | 41.70 [37.86, 44.79] | 13 | 0 |
| mtbench/high | fixed_fast_vs_fixed_g8 | 30 | 5.22 [1.52, 8.56] | 31.82 [29.38, 33.96] | 10 | 0 |
| mtbench/high | markov_w0_dist_vs_fixed_g8 | 30 | 11.67 [8.12, 15.71] | 22.18 [18.23, 26.07] | 11 | 0 |
| mtbench/high | markov_w05_dist_vs_fixed_g8 | 30 | -2.79 [-5.80, 0.75] | 40.17 [36.51, 43.23] | 11 | 0 |
| mtbench/high | fixed_g2_vs_sync_g4 | 30 | 8.58 [7.02, 10.34] | -2.61 [-4.10, -1.06] | 9 | 0 |
| mtbench/high | fixed_fast_vs_sync_g4 | 30 | 19.24 [16.26, 22.68] | -20.00 [-23.32, -16.18] | 0 | 0 |
| mtbench/high | fixed_g8_vs_sync_g4 | 30 | 13.33 [7.57, 20.51] | -76.02 [-85.47, -65.26] | 10 | 0 |
| mtbench/high | markov_w0_dist_vs_sync_g4 | 30 | 26.55 [22.32, 32.03] | -36.97 [-41.85, -31.44] | 11 | 0 |
| mtbench/high | markov_w05_dist_vs_sync_g4 | 30 | 10.17 [6.61, 14.88] | -5.31 [-7.00, -3.34] | 6 | 0 |
| mtbench/dynamic | sync_g4 | 30 | -12.30 [-15.23, -9.74] | 28.00 [25.60, 29.98] | 0 | 0 |
| mtbench/dynamic | fixed_g2 | 30 | 7.09 [2.94, 11.57] | 26.12 [23.83, 28.35] | 8 | 0 |
| mtbench/dynamic | fixed_g8 | 30 | -21.71 [-24.72, -18.51] | -55.47 [-59.49, -51.00] | 11 | 0 |
| mtbench/dynamic | markov_w0_dist | 30 | 8.43 [5.23, 12.35] | 13.10 [8.32, 17.57] | 9 | 0 |
| mtbench/dynamic | markov_w05_dist | 30 | 6.88 [2.98, 11.34] | 30.29 [26.06, 33.95] | 7 | 1 |
| mtbench/dynamic | sync_g4_vs_fixed_g2 | 30 | -18.11 [-20.97, -15.57] | 2.54 [1.02, 3.86] | 8 | 0 |
| mtbench/dynamic | fixed_fast_vs_fixed_g2 | 30 | -6.62 [-10.37, -2.86] | -35.36 [-39.57, -31.28] | 8 | 0 |
| mtbench/dynamic | fixed_g8_vs_fixed_g2 | 30 | -26.90 [-32.03, -21.30] | -110.45 [-121.78, -98.89] | 15 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_fixed_g2 | 30 | 1.24 [-1.95, 4.25] | -17.63 [-21.44, -14.00] | 9 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_fixed_g2 | 30 | -0.20 [-3.24, 2.92] | 5.64 [2.50, 8.27] | 10 | 1 |
| mtbench/dynamic | sync_g4_vs_fixed_g8 | 30 | 12.02 [5.52, 18.17] | 53.69 [50.85, 55.96] | 11 | 0 |
| mtbench/dynamic | fixed_g2_vs_fixed_g8 | 30 | 36.80 [27.07, 47.12] | 52.48 [49.72, 54.91] | 15 | 0 |
| mtbench/dynamic | fixed_fast_vs_fixed_g8 | 30 | 27.74 [22.72, 32.83] | 35.68 [33.78, 37.30] | 11 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_fixed_g8 | 30 | 38.50 [30.93, 47.10] | 44.10 [39.57, 48.09] | 14 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_fixed_g8 | 30 | 36.52 [27.62, 46.11] | 55.16 [51.22, 58.43] | 15 | 1 |
| mtbench/dynamic | fixed_g2_vs_sync_g4 | 30 | 22.12 [18.44, 26.54] | -2.61 [-4.01, -1.03] | 8 | 0 |
| mtbench/dynamic | fixed_fast_vs_sync_g4 | 30 | 14.03 [10.79, 17.97] | -38.89 [-42.82, -34.41] | 0 | 0 |
| mtbench/dynamic | fixed_g8_vs_sync_g4 | 30 | -10.73 [-15.38, -5.23] | -115.94 [-127.07, -103.45] | 11 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_sync_g4 | 30 | 23.64 [19.69, 28.76] | -20.70 [-25.58, -15.73] | 9 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_sync_g4 | 30 | 21.87 [17.02, 27.12] | 3.17 [-0.02, 6.46] | 7 | 1 |
| mtbench/pooled | sync_g4 | 30 | -13.58 [-16.28, -11.24] | 25.71 [23.24, 27.66] | 1 | 0 |
| mtbench/pooled | fixed_g2 | 30 | 1.49 [-1.76, 4.79] | 22.44 [20.03, 24.62] | 25 | 0 |
| mtbench/pooled | fixed_g8 | 30 | -18.40 [-20.45, -15.87] | -53.66 [-57.26, -49.18] | 35 | 0 |
| mtbench/pooled | markov_w0_dist | 30 | 8.51 [6.52, 10.99] | 7.60 [4.20, 10.89] | 26 | 0 |
| mtbench/pooled | markov_w05_dist | 30 | 1.70 [-0.21, 3.93] | 25.83 [22.35, 28.77] | 22 | 1 |
| mtbench/pooled | sync_g4_vs_fixed_g2 | 30 | -14.85 [-16.23, -13.60] | 4.22 [2.87, 5.37] | 25 | 0 |
| mtbench/pooled | fixed_fast_vs_fixed_g2 | 30 | -1.47 [-4.57, 1.80] | -28.94 [-32.65, -25.04] | 25 | 0 |
| mtbench/pooled | fixed_g8_vs_fixed_g2 | 30 | -19.60 [-23.81, -14.63] | -98.12 [-107.97, -87.06] | 44 | 0 |
| mtbench/pooled | markov_w0_dist_vs_fixed_g2 | 30 | 6.91 [4.61, 9.83] | -19.14 [-21.33, -16.68] | 23 | 0 |
| mtbench/pooled | markov_w05_dist_vs_fixed_g2 | 30 | 0.21 [-1.87, 2.76] | 4.36 [2.66, 5.88] | 22 | 1 |
| mtbench/pooled | sync_g4_vs_fixed_g8 | 30 | 5.91 [-0.13, 11.23] | 51.65 [48.59, 53.92] | 35 | 0 |
| mtbench/pooled | fixed_g2_vs_fixed_g8 | 30 | 24.38 [17.14, 31.24] | 49.52 [46.54, 51.92] | 44 | 0 |
| mtbench/pooled | fixed_fast_vs_fixed_g8 | 30 | 22.55 [18.87, 25.70] | 34.92 [32.97, 36.41] | 35 | 0 |
| mtbench/pooled | markov_w0_dist_vs_fixed_g8 | 30 | 32.98 [28.00, 38.02] | 39.86 [36.08, 43.00] | 42 | 0 |
| mtbench/pooled | markov_w05_dist_vs_fixed_g8 | 30 | 24.64 [19.34, 29.71] | 51.73 [48.17, 54.54] | 42 | 1 |
| mtbench/pooled | fixed_g2_vs_sync_g4 | 30 | 17.44 [15.74, 19.38] | -4.40 [-5.67, -2.95] | 25 | 0 |
| mtbench/pooled | fixed_fast_vs_sync_g4 | 30 | 15.71 [12.67, 19.45] | -34.61 [-38.23, -30.28] | 1 | 0 |
| mtbench/pooled | fixed_g8_vs_sync_g4 | 30 | -5.58 [-10.09, 0.13] | -106.84 [-117.03, -94.50] | 35 | 0 |
| mtbench/pooled | markov_w0_dist_vs_sync_g4 | 30 | 25.56 [22.40, 29.63] | -24.39 [-27.71, -20.68] | 26 | 0 |
| mtbench/pooled | markov_w05_dist_vs_sync_g4 | 30 | 17.69 [14.71, 21.30] | 0.15 [-1.70, 2.14] | 22 | 1 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
