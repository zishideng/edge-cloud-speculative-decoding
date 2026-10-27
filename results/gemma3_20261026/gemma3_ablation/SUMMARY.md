# Progress probe: gemma3_ablation

State: complete; 360/360 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | fixed_fast | 30 | 8158 | 27.381 | 0.3367 | 5 | 26.66 |
| all/low | markov_w0_fresh4 | 30 | 8158 | 27.298 | 0.3412 | 5 | 27.16 |
| all/low | markov_w0_dist | 30 | 8183 | 27.106 | 0.2738 | 6 | 37.44 |
| all/low | markov_w0 | 30 | 8251 | 27.652 | 0.2718 | 7 | 36.58 |
| all/high | fixed_fast | 30 | 8104 | 14.282 | 0.4679 | 4 | 27.30 |
| all/high | markov_w0_fresh4 | 30 | 8104 | 15.902 | 0.4748 | 4 | 25.50 |
| all/high | markov_w0_dist | 30 | 8145 | 16.071 | 0.4649 | 5 | 30.78 |
| all/high | markov_w0 | 30 | 8060 | 16.239 | 0.4911 | 4 | 28.35 |
| all/dynamic | fixed_fast | 30 | 8267 | 20.273 | 0.3784 | 6 | 26.97 |
| all/dynamic | markov_w0_fresh4 | 30 | 8267 | 20.961 | 0.3876 | 6 | 27.22 |
| all/dynamic | markov_w0_dist | 30 | 8192 | 21.427 | 0.3420 | 6 | 34.67 |
| all/dynamic | markov_w0 | 30 | 8260 | 21.318 | 0.3575 | 7 | 31.81 |
| all/pooled | fixed_fast | 90 | 24529 | 19.266 | 0.3941 | 15 | 26.97 |
| all/pooled | markov_w0_fresh4 | 90 | 24529 | 20.392 | 0.4010 | 15 | 26.54 |
| all/pooled | markov_w0_dist | 90 | 24520 | 20.588 | 0.3601 | 17 | 33.68 |
| all/pooled | markov_w0 | 90 | 24571 | 20.784 | 0.3725 | 18 | 31.47 |
| humaneval/low | fixed_fast | 10 | 1718 | 52.914 | 0.1633 | 0 | 69.43 |
| humaneval/low | markov_w0_fresh4 | 10 | 1718 | 53.635 | 0.1686 | 0 | 70.39 |
| humaneval/low | markov_w0_dist | 10 | 1718 | 50.456 | 0.1718 | 0 | 68.88 |
| humaneval/low | markov_w0 | 10 | 1718 | 47.943 | 0.1665 | 0 | 66.47 |
| humaneval/high | fixed_fast | 10 | 1718 | 26.090 | 0.2493 | 0 | 69.43 |
| humaneval/high | markov_w0_fresh4 | 10 | 1718 | 38.299 | 0.2021 | 0 | 70.66 |
| humaneval/high | markov_w0_dist | 10 | 1718 | 37.341 | 0.2060 | 0 | 71.59 |
| humaneval/high | markov_w0 | 10 | 1718 | 37.573 | 0.2047 | 0 | 71.54 |
| humaneval/dynamic | fixed_fast | 10 | 1718 | 37.444 | 0.1945 | 0 | 69.20 |
| humaneval/dynamic | markov_w0_fresh4 | 10 | 1718 | 44.476 | 0.1843 | 0 | 70.28 |
| humaneval/dynamic | markov_w0_dist | 10 | 1718 | 42.448 | 0.1881 | 0 | 69.35 |
| humaneval/dynamic | markov_w0 | 10 | 1718 | 40.858 | 0.1837 | 0 | 69.39 |
| humaneval/pooled | fixed_fast | 30 | 5154 | 35.742 | 0.2024 | 0 | 69.35 |
| humaneval/pooled | markov_w0_fresh4 | 30 | 5154 | 44.617 | 0.1850 | 0 | 70.45 |
| humaneval/pooled | markov_w0_dist | 30 | 5154 | 42.761 | 0.1886 | 0 | 69.97 |
| humaneval/pooled | markov_w0 | 30 | 5154 | 41.697 | 0.1850 | 0 | 69.26 |
| gsm8k/low | fixed_fast | 10 | 3207 | 33.808 | 0.2751 | 2 | 36.07 |
| gsm8k/low | markov_w0_fresh4 | 10 | 3207 | 33.163 | 0.2806 | 2 | 36.03 |
| gsm8k/low | markov_w0_dist | 10 | 3289 | 29.328 | 0.2553 | 3 | 43.03 |
| gsm8k/low | markov_w0 | 10 | 3357 | 31.008 | 0.2460 | 4 | 43.49 |
| gsm8k/high | fixed_fast | 10 | 3132 | 17.358 | 0.3817 | 1 | 37.92 |
| gsm8k/high | markov_w0_fresh4 | 10 | 3132 | 20.302 | 0.3867 | 1 | 34.70 |
| gsm8k/high | markov_w0_dist | 10 | 3232 | 20.254 | 0.3882 | 2 | 39.65 |
| gsm8k/high | markov_w0 | 10 | 3132 | 20.341 | 0.3936 | 1 | 38.83 |
| gsm8k/dynamic | fixed_fast | 10 | 3309 | 24.426 | 0.3111 | 3 | 36.52 |
| gsm8k/dynamic | markov_w0_fresh4 | 10 | 3309 | 25.532 | 0.3257 | 3 | 35.52 |
| gsm8k/dynamic | markov_w0_dist | 10 | 3291 | 24.757 | 0.3081 | 3 | 40.90 |
| gsm8k/dynamic | markov_w0 | 10 | 3359 | 24.552 | 0.3115 | 4 | 39.93 |
| gsm8k/pooled | fixed_fast | 30 | 9648 | 23.488 | 0.3221 | 6 | 36.82 |
| gsm8k/pooled | markov_w0_fresh4 | 30 | 9648 | 25.351 | 0.3305 | 6 | 35.35 |
| gsm8k/pooled | markov_w0_dist | 30 | 9812 | 24.248 | 0.3168 | 8 | 40.95 |
| gsm8k/pooled | markov_w0 | 30 | 9848 | 24.679 | 0.3153 | 9 | 40.46 |
| mtbench/low | fixed_fast | 10 | 3233 | 18.949 | 0.4899 | 3 | 9.02 |
| mtbench/low | markov_w0_fresh4 | 10 | 3233 | 19.005 | 0.4931 | 3 | 9.19 |
| mtbench/low | markov_w0_dist | 10 | 3176 | 20.399 | 0.3482 | 3 | 18.47 |
| mtbench/low | markov_w0 | 10 | 3176 | 20.584 | 0.3560 | 3 | 20.46 |
| mtbench/high | fixed_fast | 10 | 3254 | 10.133 | 0.6662 | 3 | 9.35 |
| mtbench/high | markov_w0_fresh4 | 10 | 3254 | 10.480 | 0.7036 | 3 | 9.75 |
| mtbench/high | markov_w0_dist | 10 | 3195 | 10.607 | 0.6817 | 3 | 15.66 |
| mtbench/high | markov_w0 | 10 | 3210 | 10.821 | 0.7396 | 3 | 14.96 |
| mtbench/dynamic | fixed_fast | 10 | 3240 | 14.308 | 0.5448 | 3 | 9.16 |
| mtbench/dynamic | markov_w0_fresh4 | 10 | 3240 | 14.326 | 0.5587 | 3 | 9.39 |
| mtbench/dynamic | markov_w0_dist | 10 | 3183 | 15.236 | 0.4600 | 3 | 16.86 |
| mtbench/dynamic | markov_w0 | 10 | 3183 | 15.258 | 0.4998 | 3 | 16.89 |
| mtbench/pooled | fixed_fast | 30 | 9727 | 13.544 | 0.5672 | 9 | 9.18 |
| mtbench/pooled | markov_w0_fresh4 | 30 | 9727 | 13.763 | 0.5854 | 9 | 9.48 |
| mtbench/pooled | markov_w0_dist | 30 | 9554 | 14.349 | 0.4970 | 9 | 16.64 |
| mtbench/pooled | markov_w0 | 30 | 9569 | 14.509 | 0.5325 | 9 | 16.72 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | markov_w0_fresh4 | 30 | -0.30 [-2.41, 1.92] | -1.34 [-2.41, -0.50] | 0 | 0 |
| all/low | markov_w0_dist | 30 | -1.00 [-6.63, 4.18] | 18.68 [11.65, 23.87] | 8 | 1 |
| all/low | markov_w0 | 30 | 0.99 [-4.56, 5.85] | 19.28 [13.19, 23.64] | 8 | 2 |
| all/low | fixed_fast_vs_markov_w0_dist | 30 | 1.01 [-4.02, 7.10] | -22.96 [-31.35, -13.18] | 8 | 0 |
| all/low | markov_w0_fresh4_vs_markov_w0_dist | 30 | 0.71 [-3.99, 6.29] | -24.61 [-32.77, -15.39] | 8 | 0 |
| all/low | markov_w0_vs_markov_w0_dist | 30 | 2.01 [0.01, 3.88] | 0.75 [-1.30, 2.72] | 2 | 1 |
| all/high | markov_w0_fresh4 | 30 | 11.34 [7.47, 17.27] | -1.47 [-3.53, 1.78] | 1 | 0 |
| all/high | markov_w0_dist | 30 | 12.53 [8.56, 18.28] | 0.64 [-1.88, 3.37] | 6 | 1 |
| all/high | markov_w0 | 30 | 13.70 [10.21, 19.05] | -4.96 [-8.13, -0.18] | 6 | 0 |
| all/high | fixed_fast_vs_markov_w0_dist | 30 | -11.13 [-15.45, -7.88] | -0.65 [-3.49, 1.84] | 6 | 0 |
| all/high | markov_w0_fresh4_vs_markov_w0_dist | 30 | -1.05 [-3.77, 1.78] | -2.13 [-4.15, 0.11] | 6 | 0 |
| all/high | markov_w0_vs_markov_w0_dist | 30 | 1.04 [-0.91, 3.01] | -5.64 [-8.03, -2.58] | 5 | 0 |
| all/dynamic | markov_w0_fresh4 | 30 | 3.40 [1.19, 6.19] | -2.43 [-3.83, -0.78] | 2 | 0 |
| all/dynamic | markov_w0_dist | 30 | 5.69 [2.68, 8.91] | 9.64 [4.89, 13.56] | 6 | 0 |
| all/dynamic | markov_w0 | 30 | 5.15 [2.30, 8.28] | 5.54 [2.66, 8.38] | 8 | 1 |
| all/dynamic | fixed_fast_vs_markov_w0_dist | 30 | -5.39 [-8.18, -2.61] | -10.66 [-15.68, -5.14] | 6 | 0 |
| all/dynamic | markov_w0_fresh4_vs_markov_w0_dist | 30 | -2.17 [-4.59, 0.82] | -13.35 [-18.04, -7.81] | 6 | 0 |
| all/dynamic | markov_w0_vs_markov_w0_dist | 30 | -0.51 [-2.35, 1.38] | -4.54 [-7.31, -1.21] | 4 | 1 |
| all/pooled | markov_w0_fresh4 | 30 | 5.84 [3.83, 8.96] | -1.74 [-2.72, -0.21] | 3 | 0 |
| all/pooled | markov_w0_dist | 30 | 6.86 [4.47, 9.94] | 8.64 [5.06, 11.49] | 20 | 2 |
| all/pooled | markov_w0 | 30 | 7.88 [5.54, 10.67] | 5.47 [3.21, 7.85] | 22 | 3 |
| all/pooled | fixed_fast_vs_markov_w0_dist | 30 | -6.42 [-9.04, -4.28] | -9.46 [-12.98, -5.33] | 20 | 0 |
| all/pooled | markov_w0_fresh4_vs_markov_w0_dist | 30 | -0.95 [-3.75, 2.30] | -11.37 [-15.10, -6.58] | 20 | 0 |
| all/pooled | markov_w0_vs_markov_w0_dist | 30 | 0.96 [-0.13, 2.03] | -3.47 [-5.58, -1.02] | 11 | 2 |
| humaneval/low | markov_w0_fresh4 | 10 | 1.36 [-2.90, 5.88] | -3.21 [-7.13, 0.27] | 0 | 0 |
| humaneval/low | markov_w0_dist | 10 | -4.65 [-8.81, -0.92] | -5.19 [-9.08, -1.80] | 0 | 0 |
| humaneval/low | markov_w0 | 10 | -9.39 [-13.59, -5.08] | -1.91 [-5.97, 2.61] | 0 | 0 |
| humaneval/low | fixed_fast_vs_markov_w0_dist | 10 | 4.87 [0.93, 9.66] | 4.94 [1.77, 8.32] | 0 | 0 |
| humaneval/low | markov_w0_fresh4_vs_markov_w0_dist | 10 | 6.30 [1.94, 12.27] | 1.89 [-0.60, 4.75] | 0 | 0 |
| humaneval/low | markov_w0_vs_markov_w0_dist | 10 | -4.98 [-9.67, -0.41] | 3.12 [0.69, 5.62] | 0 | 0 |
| humaneval/high | markov_w0_fresh4 | 10 | 46.80 [40.03, 54.48] | 18.96 [15.43, 22.79] | 0 | 0 |
| humaneval/high | markov_w0_dist | 10 | 43.13 [37.58, 50.18] | 17.36 [13.24, 21.50] | 0 | 0 |
| humaneval/high | markov_w0 | 10 | 44.01 [37.32, 51.76] | 17.90 [13.19, 22.84] | 0 | 0 |
| humaneval/high | fixed_fast_vs_markov_w0_dist | 10 | -30.13 [-33.41, -27.31] | -21.01 [-27.39, -15.26] | 0 | 0 |
| humaneval/high | markov_w0_fresh4_vs_markov_w0_dist | 10 | 2.56 [-1.36, 6.60] | 1.93 [-1.24, 4.89] | 0 | 0 |
| humaneval/high | markov_w0_vs_markov_w0_dist | 10 | 0.62 [-2.12, 4.43] | 0.66 [-1.72, 3.35] | 0 | 0 |
| humaneval/dynamic | markov_w0_fresh4 | 10 | 18.78 [9.69, 28.15] | 5.26 [0.16, 10.60] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist | 10 | 13.36 [3.91, 22.51] | 3.32 [-0.89, 7.81] | 0 | 0 |
| humaneval/dynamic | markov_w0 | 10 | 9.12 [0.15, 19.04] | 5.55 [-0.07, 10.47] | 0 | 0 |
| humaneval/dynamic | fixed_fast_vs_markov_w0_dist | 10 | -11.79 [-18.37, -3.76] | -3.43 [-8.47, 0.89] | 0 | 0 |
| humaneval/dynamic | markov_w0_fresh4_vs_markov_w0_dist | 10 | 4.78 [0.75, 8.22] | 2.01 [-1.00, 4.71] | 0 | 0 |
| humaneval/dynamic | markov_w0_vs_markov_w0_dist | 10 | -3.75 [-10.12, 2.54] | 2.31 [-2.72, 7.02] | 0 | 0 |
| humaneval/pooled | markov_w0_fresh4 | 10 | 24.83 [18.93, 31.20] | 8.61 [5.40, 12.28] | 0 | 0 |
| humaneval/pooled | markov_w0_dist | 10 | 19.64 [15.02, 24.37] | 6.79 [4.02, 10.06] | 0 | 0 |
| humaneval/pooled | markov_w0 | 10 | 16.66 [12.05, 21.16] | 8.61 [5.79, 11.76] | 0 | 0 |
| humaneval/pooled | fixed_fast_vs_markov_w0_dist | 10 | -16.41 [-19.59, -13.06] | -7.29 [-11.18, -4.19] | 0 | 0 |
| humaneval/pooled | markov_w0_fresh4_vs_markov_w0_dist | 10 | 4.34 [1.83, 6.48] | 1.94 [-0.17, 3.85] | 0 | 0 |
| humaneval/pooled | markov_w0_vs_markov_w0_dist | 10 | -2.49 [-5.33, 0.00] | 1.95 [-0.00, 3.93] | 0 | 0 |
| gsm8k/low | markov_w0_fresh4 | 10 | -1.91 [-5.87, 1.30] | -2.00 [-4.06, -0.55] | 0 | 0 |
| gsm8k/low | markov_w0_dist | 10 | -13.25 [-16.61, -9.60] | 7.21 [3.18, 10.42] | 4 | 1 |
| gsm8k/low | markov_w0 | 10 | -8.28 [-13.14, -2.90] | 10.57 [5.82, 15.05] | 4 | 2 |
| gsm8k/low | fixed_fast_vs_markov_w0_dist | 10 | 15.28 [10.62, 19.93] | -7.77 [-11.63, -3.29] | 4 | 0 |
| gsm8k/low | markov_w0_fresh4_vs_markov_w0_dist | 10 | 13.08 [10.68, 15.27] | -9.92 [-13.03, -6.05] | 4 | 0 |
| gsm8k/low | markov_w0_vs_markov_w0_dist | 10 | 5.73 [2.98, 8.53] | 3.63 [1.30, 6.07] | 1 | 1 |
| gsm8k/high | markov_w0_fresh4 | 10 | 16.96 [14.17, 20.19] | -1.29 [-2.86, 1.15] | 0 | 0 |
| gsm8k/high | markov_w0_dist | 10 | 16.68 [12.98, 20.88] | -1.70 [-4.57, 1.81] | 1 | 1 |
| gsm8k/high | markov_w0 | 10 | 17.19 [13.97, 21.10] | -3.10 [-6.14, 0.48] | 0 | 0 |
| gsm8k/high | fixed_fast_vs_markov_w0_dist | 10 | -14.30 [-17.27, -11.49] | 1.67 [-1.85, 4.37] | 1 | 0 |
| gsm8k/high | markov_w0_fresh4_vs_markov_w0_dist | 10 | 0.24 [-2.74, 3.37] | 0.40 [-2.69, 2.87] | 1 | 0 |
| gsm8k/high | markov_w0_vs_markov_w0_dist | 10 | 0.43 [-2.39, 3.10] | -1.38 [-3.95, 1.02] | 1 | 0 |
| gsm8k/dynamic | markov_w0_fresh4 | 10 | 4.52 [2.81, 6.77] | -4.70 [-6.15, -2.35] | 0 | 0 |
| gsm8k/dynamic | markov_w0_dist | 10 | 1.35 [-2.53, 5.68] | 0.95 [-2.46, 4.10] | 3 | 0 |
| gsm8k/dynamic | markov_w0 | 10 | 0.51 [-1.82, 3.09] | -0.13 [-2.58, 1.87] | 4 | 1 |
| gsm8k/dynamic | fixed_fast_vs_markov_w0_dist | 10 | -1.33 [-5.38, 2.59] | -0.96 [-4.28, 2.40] | 3 | 0 |
| gsm8k/dynamic | markov_w0_fresh4_vs_markov_w0_dist | 10 | 3.13 [-0.12, 6.44] | -5.70 [-9.44, -1.62] | 3 | 0 |
| gsm8k/dynamic | markov_w0_vs_markov_w0_dist | 10 | -0.83 [-4.24, 2.22] | -1.09 [-3.86, 1.63] | 2 | 1 |
| gsm8k/pooled | markov_w0_fresh4 | 10 | 7.93 [6.50, 9.29] | -2.62 [-3.46, -1.19] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist | 10 | 3.23 [0.68, 5.69] | 1.64 [-0.68, 4.10] | 8 | 2 |
| gsm8k/pooled | markov_w0 | 10 | 5.07 [2.60, 7.75] | 2.11 [-0.26, 4.67] | 8 | 3 |
| gsm8k/pooled | fixed_fast_vs_markov_w0_dist | 10 | -3.13 [-5.39, -0.68] | -1.66 [-4.28, 0.67] | 8 | 0 |
| gsm8k/pooled | markov_w0_fresh4_vs_markov_w0_dist | 10 | 4.55 [2.31, 7.17] | -4.33 [-7.25, -1.42] | 8 | 0 |
| gsm8k/pooled | markov_w0_vs_markov_w0_dist | 10 | 1.78 [0.64, 3.01] | 0.48 [-0.74, 1.43] | 4 | 2 |
| mtbench/low | markov_w0_fresh4 | 10 | 0.30 [-2.91, 3.51] | -0.64 [-1.65, 0.33] | 0 | 0 |
| mtbench/low | markov_w0_dist | 10 | 7.66 [2.64, 12.40] | 28.93 [23.82, 32.32] | 4 | 0 |
| mtbench/low | markov_w0 | 10 | 8.63 [4.36, 12.38] | 27.34 [22.74, 30.18] | 4 | 0 |
| mtbench/low | fixed_fast_vs_markov_w0_dist | 10 | -7.11 [-11.03, -2.57] | -40.70 [-47.76, -31.27] | 4 | 0 |
| mtbench/low | markov_w0_fresh4_vs_markov_w0_dist | 10 | -6.84 [-11.23, -1.70] | -41.61 [-49.08, -32.24] | 4 | 0 |
| mtbench/low | markov_w0_vs_markov_w0_dist | 10 | 0.91 [-1.02, 2.58] | -2.23 [-5.10, 0.08] | 1 | 0 |
| mtbench/high | markov_w0_fresh4 | 10 | 3.43 [0.40, 6.49] | -5.61 [-7.32, -3.97] | 1 | 0 |
| mtbench/high | markov_w0_dist | 10 | 4.68 [2.07, 7.42] | -2.32 [-5.10, -0.31] | 5 | 0 |
| mtbench/high | markov_w0 | 10 | 6.79 [4.42, 9.36] | -11.01 [-13.49, -8.24] | 6 | 0 |
| mtbench/high | fixed_fast_vs_markov_w0_dist | 10 | -4.47 [-6.91, -2.03] | 2.26 [0.31, 4.85] | 5 | 0 |
| mtbench/high | markov_w0_fresh4_vs_markov_w0_dist | 10 | -1.20 [-3.77, 2.28] | -3.22 [-5.44, -0.85] | 5 | 0 |
| mtbench/high | markov_w0_vs_markov_w0_dist | 10 | 2.02 [-0.71, 5.10] | -8.49 [-11.15, -4.86] | 4 | 0 |
| mtbench/dynamic | markov_w0_fresh4 | 10 | 0.12 [-2.74, 2.34] | -2.56 [-4.06, -0.88] | 2 | 0 |
| mtbench/dynamic | markov_w0_dist | 10 | 6.48 [2.94, 9.25] | 15.55 [10.28, 19.01] | 3 | 0 |
| mtbench/dynamic | markov_w0 | 10 | 6.64 [2.88, 10.88] | 8.25 [4.67, 11.66] | 4 | 0 |
| mtbench/dynamic | fixed_fast_vs_markov_w0_dist | 10 | -6.08 [-8.47, -2.85] | -18.42 [-23.47, -11.45] | 3 | 0 |
| mtbench/dynamic | markov_w0_fresh4_vs_markov_w0_dist | 10 | -5.97 [-7.41, -4.01] | -21.45 [-26.02, -15.32] | 3 | 0 |
| mtbench/dynamic | markov_w0_vs_markov_w0_dist | 10 | 0.15 [-2.00, 3.14] | -8.65 [-11.68, -4.21] | 2 | 0 |
| mtbench/pooled | markov_w0_fresh4 | 10 | 1.61 [0.13, 3.01] | -3.21 [-4.11, -2.45] | 3 | 0 |
| mtbench/pooled | markov_w0_dist | 10 | 5.95 [3.30, 8.56] | 12.38 [8.32, 14.89] | 12 | 0 |
| mtbench/pooled | markov_w0 | 10 | 7.12 [4.53, 9.78] | 6.11 [3.15, 8.49] | 14 | 0 |
| mtbench/pooled | fixed_fast_vs_markov_w0_dist | 10 | -5.61 [-7.88, -3.19] | -14.12 [-17.50, -9.07] | 12 | 0 |
| mtbench/pooled | markov_w0_fresh4_vs_markov_w0_dist | 10 | -4.09 [-6.54, -0.83] | -17.79 [-20.95, -13.29] | 12 | 0 |
| mtbench/pooled | markov_w0_vs_markov_w0_dist | 10 | 1.11 [-0.32, 2.96] | -7.15 [-9.21, -4.48] | 7 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
