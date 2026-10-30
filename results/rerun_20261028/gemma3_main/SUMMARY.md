# Progress probe: gemma3_main

State: complete; 2970/2970 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | picospec_g2 | 110 | 30125 | 27.748 | 0.2634 | 21 | 40.10 |
| all/low | picospec | 110 | 30125 | 30.746 | 0.3083 | 21 | 37.62 |
| all/low | picospec_g8 | 110 | 30050 | 28.608 | 0.4064 | 23 | 29.27 |
| all/low | sync_g4 | 110 | 30125 | 21.423 | 0.2920 | 21 | 0.00 |
| all/low | hf_default | 110 | 30120 | 17.601 | 0.3757 | 21 | 0.00 |
| all/low | pipesd | 110 | 30128 | 19.220 | 0.3777 | 21 | 0.00 |
| all/low | pearl | 110 | 30135 | 26.749 | 0.2482 | 21 | 0.00 |
| all/low | markov_w0_dist_int | 110 | 30157 | 29.703 | 0.2747 | 21 | 47.26 |
| all/low | markov_w05_dist_int | 110 | 30183 | 29.660 | 0.2560 | 22 | 45.93 |
| all/high | picospec_g2 | 110 | 29483 | 12.303 | 0.4767 | 19 | 36.16 |
| all/high | picospec | 110 | 29726 | 14.742 | 0.4466 | 20 | 30.84 |
| all/high | picospec_g8 | 110 | 29543 | 15.741 | 0.5316 | 20 | 19.83 |
| all/high | sync_g4 | 110 | 29726 | 12.336 | 0.4516 | 20 | 0.00 |
| all/high | hf_default | 110 | 29495 | 12.139 | 0.4933 | 19 | 0.00 |
| all/high | pipesd | 110 | 29456 | 13.326 | 0.5364 | 19 | 0.00 |
| all/high | pearl | 110 | 29803 | 15.352 | 0.4513 | 21 | 0.00 |
| all/high | markov_w0_dist_int | 110 | 29547 | 16.583 | 0.4600 | 20 | 31.34 |
| all/high | markov_w05_dist_int | 110 | 29481 | 15.201 | 0.4181 | 19 | 40.56 |
| all/dynamic | picospec_g2 | 110 | 30101 | 18.570 | 0.3468 | 22 | 38.57 |
| all/dynamic | picospec | 110 | 30138 | 20.350 | 0.3697 | 22 | 34.77 |
| all/dynamic | picospec_g8 | 110 | 30121 | 20.847 | 0.4641 | 21 | 24.50 |
| all/dynamic | sync_g4 | 110 | 30138 | 16.460 | 0.3571 | 22 | 0.00 |
| all/dynamic | hf_default | 110 | 30398 | 14.864 | 0.4247 | 22 | 0.00 |
| all/dynamic | pipesd | 110 | 30349 | 16.544 | 0.4381 | 23 | 0.00 |
| all/dynamic | pearl | 110 | 30149 | 19.384 | 0.3451 | 22 | 0.00 |
| all/dynamic | markov_w0_dist_int | 110 | 30243 | 21.937 | 0.3558 | 23 | 39.60 |
| all/dynamic | markov_w05_dist_int | 110 | 30241 | 21.376 | 0.3225 | 23 | 43.59 |
| all/pooled | picospec_g2 | 330 | 89709 | 17.579 | 0.3615 | 62 | 38.23 |
| all/pooled | picospec | 330 | 89989 | 20.099 | 0.3745 | 63 | 34.20 |
| all/pooled | picospec_g8 | 330 | 89714 | 20.519 | 0.4670 | 64 | 23.93 |
| all/pooled | sync_g4 | 330 | 89989 | 15.936 | 0.3665 | 63 | 0.00 |
| all/pooled | hf_default | 330 | 90013 | 14.551 | 0.4308 | 62 | 0.00 |
| all/pooled | pipesd | 330 | 89933 | 16.024 | 0.4501 | 63 | 0.00 |
| all/pooled | pearl | 330 | 90087 | 19.486 | 0.3478 | 64 | 0.00 |
| all/pooled | markov_w0_dist_int | 330 | 89947 | 21.541 | 0.3628 | 64 | 37.87 |
| all/pooled | markov_w05_dist_int | 330 | 89905 | 20.565 | 0.3315 | 64 | 43.33 |
| humaneval/low | picospec_g2 | 30 | 4651 | 40.528 | 0.1823 | 0 | 62.34 |
| humaneval/low | picospec | 30 | 4651 | 54.072 | 0.1619 | 0 | 72.78 |
| humaneval/low | picospec_g8 | 30 | 4651 | 62.178 | 0.1582 | 0 | 77.07 |
| humaneval/low | sync_g4 | 30 | 4651 | 27.991 | 0.2222 | 0 | 0.00 |
| humaneval/low | hf_default | 30 | 4670 | 28.206 | 0.2319 | 0 | 0.00 |
| humaneval/low | pipesd | 30 | 4675 | 35.133 | 0.2095 | 0 | 0.00 |
| humaneval/low | pearl | 30 | 4651 | 32.574 | 0.2048 | 0 | 0.00 |
| humaneval/low | markov_w0_dist_int | 30 | 4651 | 52.100 | 0.1659 | 0 | 75.64 |
| humaneval/low | markov_w05_dist_int | 30 | 4651 | 51.770 | 0.1699 | 0 | 73.96 |
| humaneval/high | picospec_g2 | 30 | 4651 | 16.205 | 0.3546 | 0 | 61.48 |
| humaneval/high | picospec | 30 | 4651 | 25.992 | 0.2478 | 0 | 70.10 |
| humaneval/high | picospec_g8 | 30 | 4651 | 38.547 | 0.1989 | 0 | 71.36 |
| humaneval/high | sync_g4 | 30 | 4651 | 17.033 | 0.3259 | 0 | 0.00 |
| humaneval/high | hf_default | 30 | 4689 | 22.715 | 0.2716 | 0 | 0.00 |
| humaneval/high | pipesd | 30 | 4670 | 29.603 | 0.2349 | 0 | 0.00 |
| humaneval/high | pearl | 30 | 4675 | 32.616 | 0.2123 | 0 | 0.00 |
| humaneval/high | markov_w0_dist_int | 30 | 4646 | 37.054 | 0.2007 | 0 | 72.94 |
| humaneval/high | markov_w05_dist_int | 30 | 4670 | 34.616 | 0.2127 | 0 | 72.14 |
| humaneval/dynamic | picospec_g2 | 30 | 4666 | 27.619 | 0.2365 | 0 | 62.13 |
| humaneval/dynamic | picospec | 30 | 4666 | 37.634 | 0.1941 | 0 | 71.82 |
| humaneval/dynamic | picospec_g8 | 30 | 4666 | 49.721 | 0.1765 | 0 | 74.59 |
| humaneval/dynamic | sync_g4 | 30 | 4666 | 22.825 | 0.2581 | 0 | 0.00 |
| humaneval/dynamic | hf_default | 30 | 4671 | 25.807 | 0.2475 | 0 | 0.00 |
| humaneval/dynamic | pipesd | 30 | 4666 | 34.059 | 0.2164 | 0 | 0.00 |
| humaneval/dynamic | pearl | 30 | 4666 | 31.696 | 0.2127 | 0 | 0.00 |
| humaneval/dynamic | markov_w0_dist_int | 30 | 4671 | 44.390 | 0.1808 | 0 | 74.42 |
| humaneval/dynamic | markov_w05_dist_int | 30 | 4666 | 43.221 | 0.1865 | 0 | 73.39 |
| humaneval/pooled | picospec_g2 | 90 | 13968 | 24.475 | 0.2578 | 0 | 61.98 |
| humaneval/pooled | picospec | 90 | 13968 | 35.913 | 0.2012 | 0 | 71.55 |
| humaneval/pooled | picospec_g8 | 90 | 13968 | 48.282 | 0.1778 | 0 | 74.27 |
| humaneval/pooled | sync_g4 | 90 | 13968 | 21.702 | 0.2687 | 0 | 0.00 |
| humaneval/pooled | hf_default | 90 | 14030 | 25.371 | 0.2504 | 0 | 0.00 |
| humaneval/pooled | pipesd | 90 | 14011 | 32.750 | 0.2203 | 0 | 0.00 |
| humaneval/pooled | pearl | 90 | 13992 | 32.289 | 0.2100 | 0 | 0.00 |
| humaneval/pooled | markov_w0_dist_int | 90 | 13968 | 43.666 | 0.1824 | 0 | 74.29 |
| humaneval/pooled | markov_w05_dist_int | 90 | 13987 | 42.040 | 0.1897 | 0 | 73.14 |
| mtbench/low | picospec_g2 | 30 | 9054 | 20.041 | 0.3643 | 9 | 18.61 |
| mtbench/low | picospec | 30 | 9041 | 19.421 | 0.4978 | 9 | 11.20 |
| mtbench/low | picospec_g8 | 30 | 8932 | 16.398 | 0.7301 | 10 | 4.09 |
| mtbench/low | sync_g4 | 30 | 9041 | 15.901 | 0.3957 | 9 | 0.00 |
| mtbench/low | hf_default | 30 | 8996 | 12.138 | 0.5435 | 9 | 0.00 |
| mtbench/low | pipesd | 30 | 8997 | 13.360 | 0.5429 | 9 | 0.00 |
| mtbench/low | pearl | 30 | 9046 | 22.242 | 0.2994 | 9 | 0.00 |
| mtbench/low | markov_w0_dist_int | 30 | 9073 | 19.196 | 0.3870 | 9 | 23.24 |
| mtbench/low | markov_w05_dist_int | 30 | 9116 | 20.665 | 0.3341 | 10 | 20.40 |
| mtbench/high | picospec_g2 | 30 | 9038 | 9.262 | 0.6403 | 9 | 15.19 |
| mtbench/high | picospec | 30 | 9022 | 9.331 | 0.7098 | 9 | 7.98 |
| mtbench/high | picospec_g8 | 30 | 8873 | 8.703 | 0.9677 | 9 | 2.39 |
| mtbench/high | sync_g4 | 30 | 9022 | 8.852 | 0.6287 | 9 | 0.00 |
| mtbench/high | hf_default | 30 | 8951 | 7.943 | 0.7403 | 9 | 0.00 |
| mtbench/high | pipesd | 30 | 8953 | 8.058 | 0.8915 | 9 | 0.00 |
| mtbench/high | pearl | 30 | 9022 | 9.171 | 0.7507 | 10 | 0.00 |
| mtbench/high | markov_w0_dist_int | 30 | 9034 | 9.765 | 0.7654 | 9 | 14.43 |
| mtbench/high | markov_w05_dist_int | 30 | 9022 | 9.232 | 0.6377 | 9 | 14.80 |
| mtbench/dynamic | picospec_g2 | 30 | 9224 | 13.203 | 0.4857 | 11 | 17.49 |
| mtbench/dynamic | picospec | 30 | 9220 | 12.882 | 0.5911 | 11 | 10.21 |
| mtbench/dynamic | picospec_g8 | 30 | 9158 | 11.841 | 0.8260 | 10 | 3.38 |
| mtbench/dynamic | sync_g4 | 30 | 9220 | 12.017 | 0.4895 | 11 | 0.00 |
| mtbench/dynamic | hf_default | 30 | 9229 | 10.028 | 0.6230 | 10 | 0.00 |
| mtbench/dynamic | pipesd | 30 | 9225 | 10.801 | 0.6701 | 11 | 0.00 |
| mtbench/dynamic | pearl | 30 | 9156 | 13.154 | 0.5058 | 10 | 0.00 |
| mtbench/dynamic | markov_w0_dist_int | 30 | 9220 | 13.471 | 0.5391 | 11 | 18.86 |
| mtbench/dynamic | markov_w05_dist_int | 30 | 9227 | 14.181 | 0.4495 | 11 | 17.72 |
| mtbench/pooled | picospec_g2 | 90 | 27316 | 12.847 | 0.4966 | 29 | 17.00 |
| mtbench/pooled | picospec | 90 | 27283 | 12.701 | 0.5994 | 29 | 9.63 |
| mtbench/pooled | picospec_g8 | 90 | 26963 | 11.534 | 0.8409 | 29 | 3.14 |
| mtbench/pooled | sync_g4 | 90 | 27283 | 11.585 | 0.5044 | 29 | 0.00 |
| mtbench/pooled | hf_default | 90 | 27176 | 9.746 | 0.6353 | 28 | 0.00 |
| mtbench/pooled | pipesd | 90 | 27175 | 10.299 | 0.7009 | 29 | 0.00 |
| mtbench/pooled | pearl | 90 | 27224 | 13.048 | 0.5184 | 29 | 0.00 |
| mtbench/pooled | markov_w0_dist_int | 90 | 27327 | 13.124 | 0.5634 | 29 | 17.51 |
| mtbench/pooled | markov_w05_dist_int | 90 | 27365 | 13.226 | 0.4731 | 30 | 17.64 |
| gsm8k/low | picospec_g2 | 50 | 16420 | 31.629 | 0.2308 | 12 | 48.18 |
| gsm8k/low | picospec | 50 | 16433 | 38.372 | 0.2455 | 12 | 49.07 |
| gsm8k/low | picospec_g8 | 50 | 16467 | 38.216 | 0.3009 | 13 | 41.26 |
| gsm8k/low | sync_g4 | 50 | 16433 | 24.474 | 0.2546 | 12 | 0.00 |
| gsm8k/low | hf_default | 50 | 16454 | 20.453 | 0.3249 | 12 | 0.00 |
| gsm8k/low | pipesd | 50 | 16456 | 21.624 | 0.3352 | 12 | 0.00 |
| gsm8k/low | pearl | 50 | 16438 | 28.483 | 0.2324 | 12 | 0.00 |
| gsm8k/low | markov_w0_dist_int | 50 | 16433 | 36.247 | 0.2434 | 12 | 55.40 |
| gsm8k/low | markov_w05_dist_int | 50 | 16416 | 33.732 | 0.2370 | 12 | 52.86 |
| gsm8k/high | picospec_g2 | 50 | 15794 | 13.932 | 0.4190 | 10 | 45.41 |
| gsm8k/high | picospec | 50 | 16053 | 18.438 | 0.3563 | 11 | 42.79 |
| gsm8k/high | picospec_g8 | 50 | 16019 | 21.746 | 0.3867 | 11 | 30.17 |
| gsm8k/high | sync_g4 | 50 | 16053 | 14.364 | 0.3885 | 11 | 0.00 |
| gsm8k/high | hf_default | 50 | 15855 | 14.461 | 0.4195 | 10 | 0.00 |
| gsm8k/high | pipesd | 50 | 15833 | 16.816 | 0.4245 | 10 | 0.00 |
| gsm8k/high | pearl | 50 | 16106 | 19.782 | 0.3530 | 11 | 0.00 |
| gsm8k/high | markov_w0_dist_int | 50 | 15867 | 21.701 | 0.3620 | 11 | 41.89 |
| gsm8k/high | markov_w05_dist_int | 50 | 15789 | 19.087 | 0.3535 | 10 | 45.77 |
| gsm8k/dynamic | picospec_g2 | 50 | 16211 | 21.517 | 0.2996 | 11 | 47.22 |
| gsm8k/dynamic | picospec | 50 | 16252 | 25.344 | 0.2945 | 11 | 46.19 |
| gsm8k/dynamic | picospec_g8 | 50 | 16297 | 28.216 | 0.3430 | 11 | 35.36 |
| gsm8k/dynamic | sync_g4 | 50 | 16252 | 18.912 | 0.3104 | 11 | 0.00 |
| gsm8k/dynamic | hf_default | 50 | 16498 | 17.483 | 0.3640 | 12 | 0.00 |
| gsm8k/dynamic | pipesd | 50 | 16458 | 19.516 | 0.3709 | 12 | 0.00 |
| gsm8k/dynamic | pearl | 50 | 16327 | 22.929 | 0.2928 | 12 | 0.00 |
| gsm8k/dynamic | markov_w0_dist_int | 50 | 16352 | 27.762 | 0.3025 | 12 | 48.21 |
| gsm8k/dynamic | markov_w05_dist_int | 50 | 16348 | 24.918 | 0.2897 | 12 | 50.02 |
| gsm8k/pooled | picospec_g2 | 150 | 48425 | 20.126 | 0.3152 | 33 | 46.93 |
| gsm8k/pooled | picospec | 150 | 48738 | 25.121 | 0.2983 | 34 | 45.89 |
| gsm8k/pooled | picospec_g8 | 150 | 48783 | 27.954 | 0.3431 | 35 | 35.04 |
| gsm8k/pooled | sync_g4 | 150 | 48738 | 18.403 | 0.3173 | 34 | 0.00 |
| gsm8k/pooled | hf_default | 150 | 48807 | 17.158 | 0.3688 | 34 | 0.00 |
| gsm8k/pooled | pipesd | 150 | 48747 | 19.147 | 0.3762 | 34 | 0.00 |
| gsm8k/pooled | pearl | 150 | 48871 | 23.235 | 0.2923 | 35 | 0.00 |
| gsm8k/pooled | markov_w0_dist_int | 150 | 48652 | 27.432 | 0.3020 | 35 | 47.63 |
| gsm8k/pooled | markov_w05_dist_int | 150 | 48553 | 24.647 | 0.2926 | 34 | 49.50 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | picospec_vs_picospec_g2 | 110 | 10.81 [7.07, 14.88] | -17.04 [-21.23, -12.37] | 15 | 0 |
| all/low | picospec_g8_vs_picospec_g2 | 110 | 3.10 [-2.27, 9.38] | -54.27 [-64.27, -43.65] | 27 | 2 |
| all/low | sync_g4_vs_picospec_g2 | 110 | -22.79 [-24.34, -21.19] | -10.83 [-12.33, -9.34] | 14 | 0 |
| all/low | hf_default_vs_picospec_g2 | 110 | -36.57 [-40.59, -33.24] | -42.63 [-51.06, -36.44] | 23 | 0 |
| all/low | pipesd_vs_picospec_g2 | 110 | -30.73 [-32.52, -28.62] | -43.39 [-46.30, -40.16] | 22 | 0 |
| all/low | pearl_vs_picospec_g2 | 110 | -3.60 [-7.31, 0.12] | 5.77 [2.45, 8.81] | 11 | 0 |
| all/low | markov_w0_dist_int_vs_picospec_g2 | 110 | 7.05 [3.47, 10.90] | -4.27 [-6.33, -2.03] | 8 | 0 |
| all/low | markov_w05_dist_int_vs_picospec_g2 | 110 | 6.89 [4.13, 9.90] | 2.83 [0.69, 4.87] | 10 | 1 |
| all/low | picospec_g2_vs_picospec | 110 | -9.75 [-12.95, -6.60] | 14.56 [11.01, 17.51] | 15 | 0 |
| all/low | picospec_g8_vs_picospec | 110 | -6.95 [-9.62, -4.02] | -31.81 [-35.93, -27.26] | 22 | 2 |
| all/low | sync_g4_vs_picospec | 110 | -30.32 [-33.20, -27.70] | 5.30 [1.14, 8.87] | 1 | 0 |
| all/low | hf_default_vs_picospec | 110 | -42.75 [-45.95, -39.69] | -21.87 [-29.28, -15.65] | 22 | 0 |
| all/low | pipesd_vs_picospec | 110 | -37.49 [-39.71, -35.32] | -22.51 [-26.89, -18.50] | 21 | 0 |
| all/low | pearl_vs_picospec | 110 | -13.00 [-18.21, -7.61] | 19.49 [13.89, 24.41] | 21 | 0 |
| all/low | markov_w0_dist_int_vs_picospec | 110 | -3.39 [-5.26, -1.27] | 10.91 [7.61, 14.01] | 14 | 0 |
| all/low | markov_w05_dist_int_vs_picospec | 110 | -3.53 [-6.87, -0.46] | 16.98 [12.46, 20.88] | 16 | 1 |
| all/low | picospec_g2_vs_picospec_g8 | 110 | -3.01 [-8.58, 2.32] | 35.18 [30.39, 39.12] | 27 | 0 |
| all/low | picospec_vs_picospec_g8 | 110 | 7.47 [4.18, 10.64] | 24.13 [21.42, 26.43] | 22 | 0 |
| all/low | sync_g4_vs_picospec_g8 | 110 | -25.11 [-29.79, -20.76] | 28.16 [22.46, 32.73] | 22 | 0 |
| all/low | hf_default_vs_picospec_g8 | 110 | -38.47 [-42.89, -34.07] | 7.54 [-0.08, 14.05] | 26 | 0 |
| all/low | pipesd_vs_picospec_g8 | 110 | -32.82 [-36.50, -29.28] | 7.05 [0.78, 12.47] | 26 | 0 |
| all/low | pearl_vs_picospec_g8 | 110 | -6.50 [-14.31, 1.55] | 38.92 [32.49, 44.20] | 30 | 0 |
| all/low | markov_w0_dist_int_vs_picospec_g8 | 110 | 3.83 [0.12, 7.67] | 32.41 [27.76, 36.48] | 27 | 0 |
| all/low | markov_w05_dist_int_vs_picospec_g8 | 110 | 3.68 [-1.62, 9.02] | 37.01 [31.35, 41.58] | 25 | 0 |
| all/low | picospec_g2_vs_sync_g4 | 110 | 29.52 [26.89, 32.17] | 9.77 [8.54, 10.97] | 14 | 0 |
| all/low | picospec_vs_sync_g4 | 110 | 43.52 [38.30, 49.69] | -5.60 [-9.73, -1.15] | 1 | 0 |
| all/low | picospec_g8_vs_sync_g4 | 110 | 33.54 [26.20, 42.44] | -39.19 [-48.66, -28.97] | 22 | 2 |
| all/low | hf_default_vs_sync_g4 | 110 | -17.84 [-22.92, -13.89] | -28.69 [-36.37, -23.06] | 22 | 0 |
| all/low | pipesd_vs_sync_g4 | 110 | -10.28 [-12.61, -7.64] | -29.37 [-32.41, -26.04] | 20 | 0 |
| all/low | pearl_vs_sync_g4 | 110 | 24.86 [19.78, 29.57] | 14.98 [12.04, 17.63] | 20 | 0 |
| all/low | markov_w0_dist_int_vs_sync_g4 | 110 | 38.65 [33.83, 44.09] | 5.92 [3.77, 8.04] | 13 | 0 |
| all/low | markov_w05_dist_int_vs_sync_g4 | 110 | 38.45 [35.09, 42.34] | 12.33 [10.57, 14.05] | 15 | 1 |
| all/high | picospec_vs_picospec_g2 | 110 | 19.83 [15.15, 25.39] | 6.32 [2.67, 10.26] | 13 | 1 |
| all/high | picospec_g8_vs_picospec_g2 | 110 | 27.94 [19.54, 38.32] | -11.52 [-19.61, -2.71] | 26 | 1 |
| all/high | sync_g4_vs_picospec_g2 | 110 | 0.27 [-0.98, 1.70] | 5.27 [4.26, 6.36] | 13 | 1 |
| all/high | hf_default_vs_picospec_g2 | 110 | -1.33 [-5.18, 2.96] | -3.49 [-7.50, 0.32] | 26 | 0 |
| all/high | pipesd_vs_picospec_g2 | 110 | 8.32 [3.11, 14.64] | -12.52 [-18.16, -6.25] | 17 | 0 |
| all/high | pearl_vs_picospec_g2 | 110 | 24.79 [18.80, 32.18] | 5.33 [0.90, 10.22] | 24 | 2 |
| all/high | markov_w0_dist_int_vs_picospec_g2 | 110 | 34.79 [27.46, 43.53] | 3.51 [-1.17, 8.79] | 11 | 1 |
| all/high | markov_w05_dist_int_vs_picospec_g2 | 110 | 23.56 [17.95, 30.83] | 12.29 [9.79, 15.30] | 15 | 0 |
| all/high | picospec_g2_vs_picospec | 110 | -16.55 [-20.25, -13.15] | -6.75 [-11.43, -2.74] | 13 | 0 |
| all/high | picospec_g8_vs_picospec | 110 | 6.78 [2.96, 11.71] | -19.04 [-23.49, -13.86] | 22 | 0 |
| all/high | sync_g4_vs_picospec | 110 | -16.32 [-19.11, -13.70] | -1.13 [-4.77, 1.96] | 1 | 0 |
| all/high | hf_default_vs_picospec | 110 | -17.65 [-20.42, -14.93] | -10.47 [-14.57, -6.58] | 25 | 0 |
| all/high | pipesd_vs_picospec | 110 | -9.60 [-11.37, -7.45] | -20.11 [-22.29, -17.43] | 20 | 0 |
| all/high | pearl_vs_picospec | 110 | 4.14 [1.91, 6.66] | -1.06 [-2.77, 0.95] | 21 | 1 |
| all/high | markov_w0_dist_int_vs_picospec | 110 | 12.49 [9.52, 15.92] | -3.00 [-5.09, -0.67] | 14 | 1 |
| all/high | markov_w05_dist_int_vs_picospec | 110 | 3.12 [0.88, 5.47] | 6.37 [4.28, 8.41] | 18 | 0 |
| all/high | picospec_g2_vs_picospec_g8 | 110 | -21.84 [-27.70, -16.35] | 10.33 [2.64, 16.39] | 26 | 0 |
| all/high | picospec_vs_picospec_g8 | 110 | -6.35 [-10.48, -2.88] | 16.00 [12.18, 19.02] | 22 | 0 |
| all/high | sync_g4_vs_picospec_g8 | 110 | -21.63 [-26.95, -16.90] | 15.05 [8.37, 20.26] | 23 | 0 |
| all/high | hf_default_vs_picospec_g8 | 110 | -22.88 [-26.96, -18.77] | 7.20 [1.14, 12.64] | 29 | 0 |
| all/high | pipesd_vs_picospec_g8 | 110 | -15.34 [-17.87, -12.93] | -0.90 [-4.10, 1.91] | 27 | 0 |
| all/high | pearl_vs_picospec_g8 | 110 | -2.47 [-5.13, -0.03] | 15.11 [12.28, 17.45] | 21 | 1 |
| all/high | markov_w0_dist_int_vs_picospec_g8 | 110 | 5.35 [2.35, 8.14] | 13.47 [10.57, 16.14] | 23 | 1 |
| all/high | markov_w05_dist_int_vs_picospec_g8 | 110 | -3.43 [-6.58, -0.24] | 21.35 [16.97, 25.11] | 21 | 0 |
| all/high | picospec_g2_vs_sync_g4 | 110 | -0.27 [-1.68, 0.99] | -5.56 [-6.79, -4.45] | 13 | 0 |
| all/high | picospec_vs_sync_g4 | 110 | 19.51 [15.88, 23.62] | 1.11 [-2.00, 4.55] | 1 | 0 |
| all/high | picospec_g8_vs_sync_g4 | 110 | 27.60 [20.33, 36.90] | -17.72 [-25.41, -9.14] | 23 | 0 |
| all/high | hf_default_vs_sync_g4 | 110 | -1.59 [-5.09, 1.90] | -9.24 [-13.26, -5.66] | 25 | 0 |
| all/high | pipesd_vs_sync_g4 | 110 | 8.03 [3.84, 13.27] | -18.77 [-23.82, -12.81] | 20 | 0 |
| all/high | pearl_vs_sync_g4 | 110 | 24.46 [19.52, 30.63] | 0.07 [-3.90, 4.66] | 21 | 1 |
| all/high | markov_w0_dist_int_vs_sync_g4 | 110 | 34.43 [28.15, 42.12] | -1.86 [-6.31, 3.23] | 14 | 1 |
| all/high | markov_w05_dist_int_vs_sync_g4 | 110 | 23.23 [18.43, 29.37] | 7.41 [5.06, 10.21] | 18 | 0 |
| all/dynamic | picospec_vs_picospec_g2 | 110 | 9.59 [6.19, 13.63] | -6.60 [-10.20, -2.46] | 14 | 0 |
| all/dynamic | picospec_g8_vs_picospec_g2 | 110 | 12.26 [5.29, 20.30] | -33.80 [-42.95, -24.16] | 26 | 0 |
| all/dynamic | sync_g4_vs_picospec_g2 | 110 | -11.36 [-14.41, -7.85] | -2.96 [-5.62, -0.12] | 14 | 0 |
| all/dynamic | hf_default_vs_picospec_g2 | 110 | -19.96 [-24.91, -15.13] | -22.46 [-29.75, -16.72] | 20 | 1 |
| all/dynamic | pipesd_vs_picospec_g2 | 110 | -10.91 [-15.16, -6.24] | -26.32 [-31.42, -21.10] | 15 | 1 |
| all/dynamic | pearl_vs_picospec_g2 | 110 | 4.39 [0.60, 8.50] | 0.50 [-2.41, 3.50] | 14 | 1 |
| all/dynamic | markov_w0_dist_int_vs_picospec_g2 | 110 | 18.13 [12.51, 24.09] | -2.60 [-6.05, 1.16] | 14 | 1 |
| all/dynamic | markov_w05_dist_int_vs_picospec_g2 | 110 | 15.11 [10.65, 20.59] | 7.00 [4.35, 10.14] | 12 | 1 |
| all/dynamic | picospec_g2_vs_picospec | 110 | -8.75 [-11.99, -5.83] | 6.19 [2.40, 9.25] | 14 | 0 |
| all/dynamic | picospec_g8_vs_picospec | 110 | 2.44 [-2.05, 7.40] | -25.52 [-30.22, -20.64] | 19 | 0 |
| all/dynamic | sync_g4_vs_picospec | 110 | -19.12 [-23.01, -14.96] | 3.41 [-1.06, 7.40] | 0 | 0 |
| all/dynamic | hf_default_vs_picospec | 110 | -26.96 [-31.45, -22.76] | -14.88 [-21.15, -9.31] | 19 | 1 |
| all/dynamic | pipesd_vs_picospec | 110 | -18.70 [-22.16, -14.75] | -18.50 [-22.39, -14.67] | 13 | 1 |
| all/dynamic | pearl_vs_picospec | 110 | -4.75 [-8.55, -0.64] | 6.65 [3.30, 9.83] | 13 | 1 |
| all/dynamic | markov_w0_dist_int_vs_picospec | 110 | 7.80 [4.16, 11.89] | 3.75 [0.32, 7.05] | 12 | 1 |
| all/dynamic | markov_w05_dist_int_vs_picospec | 110 | 5.04 [0.90, 10.17] | 12.75 [8.59, 16.80] | 15 | 1 |
| all/dynamic | picospec_g2_vs_picospec_g8 | 110 | -10.92 [-16.88, -5.02] | 25.26 [19.46, 30.04] | 26 | 1 |
| all/dynamic | picospec_vs_picospec_g8 | 110 | -2.38 [-6.89, 2.09] | 20.33 [17.11, 23.21] | 19 | 1 |
| all/dynamic | sync_g4_vs_picospec_g8 | 110 | -21.04 [-26.14, -16.30] | 23.05 [17.24, 27.85] | 19 | 1 |
| all/dynamic | hf_default_vs_picospec_g8 | 110 | -28.70 [-33.15, -24.19] | 8.48 [1.98, 14.41] | 25 | 1 |
| all/dynamic | pipesd_vs_picospec_g8 | 110 | -20.64 [-24.08, -17.33] | 5.60 [0.81, 9.87] | 24 | 2 |
| all/dynamic | pearl_vs_picospec_g8 | 110 | -7.02 [-11.86, -2.53] | 25.63 [21.01, 29.49] | 24 | 1 |
| all/dynamic | markov_w0_dist_int_vs_picospec_g8 | 110 | 5.23 [2.01, 8.19] | 23.32 [18.92, 27.30] | 23 | 2 |
| all/dynamic | markov_w05_dist_int_vs_picospec_g8 | 110 | 2.54 [-2.60, 7.41] | 30.50 [25.24, 34.91] | 24 | 2 |
| all/dynamic | picospec_g2_vs_sync_g4 | 110 | 12.82 [8.51, 16.83] | 2.88 [0.12, 5.32] | 14 | 0 |
| all/dynamic | picospec_vs_sync_g4 | 110 | 23.64 [17.59, 29.88] | -3.53 [-7.99, 1.05] | 0 | 0 |
| all/dynamic | picospec_g8_vs_sync_g4 | 110 | 26.65 [19.47, 35.40] | -29.95 [-38.60, -20.84] | 19 | 0 |
| all/dynamic | hf_default_vs_sync_g4 | 110 | -9.69 [-13.82, -6.26] | -18.94 [-24.66, -14.80] | 19 | 1 |
| all/dynamic | pipesd_vs_sync_g4 | 110 | 0.51 [-2.30, 4.12] | -22.68 [-26.16, -18.60] | 13 | 1 |
| all/dynamic | pearl_vs_sync_g4 | 110 | 17.77 [14.49, 21.31] | 3.36 [1.21, 5.65] | 13 | 1 |
| all/dynamic | markov_w0_dist_int_vs_sync_g4 | 110 | 33.27 [27.72, 40.01] | 0.36 [-2.62, 3.74] | 12 | 1 |
| all/dynamic | markov_w05_dist_int_vs_sync_g4 | 110 | 29.87 [26.24, 34.09] | 9.68 [7.81, 11.62] | 15 | 1 |
| all/pooled | picospec_vs_picospec_g2 | 110 | 14.34 [10.62, 18.62] | -3.61 [-7.18, 0.32] | 42 | 1 |
| all/pooled | picospec_g8_vs_picospec_g2 | 110 | 16.72 [9.89, 25.00] | -29.18 [-37.99, -19.91] | 79 | 3 |
| all/pooled | sync_g4_vs_picospec_g2 | 110 | -9.35 [-10.60, -8.07] | -1.39 [-2.49, -0.31] | 41 | 1 |
| all/pooled | hf_default_vs_picospec_g2 | 110 | -17.23 [-21.15, -14.05] | -19.17 [-24.78, -15.06] | 69 | 1 |
| all/pooled | pipesd_vs_picospec_g2 | 110 | -8.85 [-11.72, -5.46] | -24.50 [-28.28, -20.16] | 54 | 1 |
| all/pooled | pearl_vs_picospec_g2 | 110 | 10.85 [8.23, 13.88] | 3.78 [1.73, 6.04] | 49 | 3 |
| all/pooled | markov_w0_dist_int_vs_picospec_g2 | 110 | 22.53 [17.58, 28.33] | -0.37 [-3.36, 2.94] | 33 | 2 |
| all/pooled | markov_w05_dist_int_vs_picospec_g2 | 110 | 16.98 [13.35, 21.17] | 8.29 [6.72, 10.00] | 37 | 2 |
| all/pooled | picospec_g2_vs_picospec | 110 | -12.54 [-15.70, -9.60] | 3.48 [-0.32, 6.70] | 42 | 0 |
| all/pooled | picospec_g8_vs_picospec | 110 | 2.09 [-1.19, 5.83] | -24.68 [-28.79, -20.05] | 63 | 2 |
| all/pooled | sync_g4_vs_picospec | 110 | -20.71 [-23.59, -18.04] | 2.14 [-1.74, 5.50] | 2 | 0 |
| all/pooled | hf_default_vs_picospec | 110 | -27.60 [-30.86, -24.79] | -15.02 [-20.44, -10.38] | 66 | 1 |
| all/pooled | pipesd_vs_picospec | 110 | -20.28 [-21.75, -18.67] | -20.16 [-22.13, -18.23] | 54 | 1 |
| all/pooled | pearl_vs_picospec | 110 | -3.05 [-5.22, -0.83] | 7.13 [4.95, 9.13] | 55 | 2 |
| all/pooled | markov_w0_dist_int_vs_picospec | 110 | 7.17 [5.34, 9.20] | 3.13 [1.41, 4.96] | 40 | 2 |
| all/pooled | markov_w05_dist_int_vs_picospec | 110 | 2.32 [0.16, 4.62] | 11.48 [8.43, 14.34] | 49 | 2 |
| all/pooled | picospec_g2_vs_picospec_g8 | 110 | -14.33 [-20.00, -9.00] | 22.59 [16.61, 27.53] | 79 | 1 |
| all/pooled | picospec_vs_picospec_g8 | 110 | -2.05 [-5.51, 1.20] | 19.80 [16.70, 22.35] | 63 | 1 |
| all/pooled | sync_g4_vs_picospec_g8 | 110 | -22.34 [-27.34, -17.74] | 21.52 [15.55, 26.37] | 64 | 1 |
| all/pooled | hf_default_vs_picospec_g8 | 110 | -29.09 [-33.17, -24.89] | 7.75 [1.25, 13.64] | 80 | 1 |
| all/pooled | pipesd_vs_picospec_g8 | 110 | -21.91 [-24.88, -19.17] | 3.63 [-0.78, 7.51] | 77 | 2 |
| all/pooled | pearl_vs_picospec_g8 | 110 | -5.04 [-9.47, -0.84] | 25.52 [21.22, 29.08] | 75 | 2 |
| all/pooled | markov_w0_dist_int_vs_picospec_g8 | 110 | 4.98 [2.30, 7.57] | 22.30 [18.67, 25.53] | 73 | 3 |
| all/pooled | markov_w05_dist_int_vs_picospec_g8 | 110 | 0.22 [-3.71, 4.15] | 29.00 [24.08, 33.20] | 70 | 2 |
| all/pooled | picospec_g2_vs_sync_g4 | 110 | 10.31 [8.77, 11.85] | 1.37 [0.31, 2.42] | 41 | 0 |
| all/pooled | picospec_vs_sync_g4 | 110 | 26.13 [22.01, 30.87] | -2.19 [-5.82, 1.71] | 2 | 0 |
| all/pooled | picospec_g8_vs_sync_g4 | 110 | 28.76 [21.56, 37.63] | -27.41 [-35.81, -18.41] | 64 | 2 |
| all/pooled | hf_default_vs_sync_g4 | 110 | -8.69 [-12.70, -5.39] | -17.55 [-22.78, -13.47] | 66 | 1 |
| all/pooled | pipesd_vs_sync_g4 | 110 | 0.55 [-2.23, 4.12] | -22.79 [-26.35, -18.52] | 53 | 1 |
| all/pooled | pearl_vs_sync_g4 | 110 | 22.28 [19.67, 25.18] | 5.10 [3.20, 7.27] | 54 | 2 |
| all/pooled | markov_w0_dist_int_vs_sync_g4 | 110 | 35.17 [29.95, 41.39] | 1.00 [-1.83, 4.26] | 39 | 2 |
| all/pooled | markov_w05_dist_int_vs_sync_g4 | 110 | 29.05 [25.33, 33.77] | 9.54 [7.97, 11.25] | 48 | 2 |
| humaneval/low | picospec_vs_picospec_g2 | 30 | 33.42 [28.60, 38.08] | 11.22 [8.96, 13.73] | 0 | 0 |
| humaneval/low | picospec_g8_vs_picospec_g2 | 30 | 53.42 [47.12, 59.50] | 13.25 [10.05, 16.52] | 0 | 0 |
| humaneval/low | sync_g4_vs_picospec_g2 | 30 | -30.93 [-34.16, -27.94] | -21.87 [-26.27, -18.50] | 0 | 0 |
| humaneval/low | hf_default_vs_picospec_g2 | 30 | -30.40 [-34.02, -26.61] | -27.18 [-32.47, -21.95] | 2 | 0 |
| humaneval/low | pipesd_vs_picospec_g2 | 30 | -13.31 [-18.22, -7.79] | -14.91 [-19.80, -10.10] | 2 | 0 |
| humaneval/low | pearl_vs_picospec_g2 | 30 | -19.63 [-23.45, -16.49] | -12.35 [-16.41, -9.27] | 1 | 0 |
| humaneval/low | markov_w0_dist_int_vs_picospec_g2 | 30 | 28.55 [23.15, 33.98] | 9.02 [6.48, 11.69] | 0 | 0 |
| humaneval/low | markov_w05_dist_int_vs_picospec_g2 | 30 | 27.74 [20.72, 34.93] | 6.84 [3.77, 10.01] | 1 | 0 |
| humaneval/low | picospec_g2_vs_picospec | 30 | -25.05 [-27.58, -22.24] | -12.64 [-15.92, -9.84] | 0 | 0 |
| humaneval/low | picospec_g8_vs_picospec | 30 | 14.99 [10.64, 19.32] | 2.28 [-0.48, 5.24] | 0 | 0 |
| humaneval/low | sync_g4_vs_picospec | 30 | -48.23 [-51.01, -45.47] | -37.28 [-43.76, -31.92] | 0 | 0 |
| humaneval/low | hf_default_vs_picospec | 30 | -47.84 [-50.46, -45.20] | -43.26 [-49.11, -38.05] | 2 | 0 |
| humaneval/low | pipesd_vs_picospec | 30 | -35.03 [-38.20, -31.69] | -29.43 [-34.53, -24.33] | 2 | 0 |
| humaneval/low | pearl_vs_picospec | 30 | -39.76 [-42.91, -37.04] | -26.55 [-32.43, -21.72] | 1 | 0 |
| humaneval/low | markov_w0_dist_int_vs_picospec | 30 | -3.65 [-8.01, 0.65] | -2.48 [-5.54, 0.46] | 0 | 0 |
| humaneval/low | markov_w05_dist_int_vs_picospec | 30 | -4.26 [-8.63, 0.12] | -4.94 [-7.88, -2.26] | 1 | 0 |
| humaneval/low | picospec_g2_vs_picospec_g8 | 30 | -34.82 [-37.30, -32.03] | -15.27 [-19.79, -11.17] | 0 | 0 |
| humaneval/low | picospec_vs_picospec_g8 | 30 | -13.04 [-16.19, -9.62] | -2.33 [-5.53, 0.48] | 0 | 0 |
| humaneval/low | sync_g4_vs_picospec_g8 | 30 | -54.98 [-57.55, -52.49] | -40.48 [-48.34, -33.51] | 0 | 0 |
| humaneval/low | hf_default_vs_picospec_g8 | 30 | -54.64 [-56.73, -52.44] | -46.60 [-54.20, -39.62] | 2 | 0 |
| humaneval/low | pipesd_vs_picospec_g8 | 30 | -43.50 [-46.39, -40.09] | -32.45 [-36.37, -28.96] | 2 | 0 |
| humaneval/low | pearl_vs_picospec_g8 | 30 | -47.61 [-49.74, -45.49] | -29.50 [-36.80, -23.16] | 1 | 0 |
| humaneval/low | markov_w0_dist_int_vs_picospec_g8 | 30 | -16.21 [-19.85, -12.85] | -4.87 [-8.00, -2.14] | 0 | 0 |
| humaneval/low | markov_w05_dist_int_vs_picospec_g8 | 30 | -16.74 [-20.57, -12.64] | -7.39 [-10.55, -4.31] | 1 | 0 |
| humaneval/low | picospec_g2_vs_sync_g4 | 30 | 44.79 [38.78, 51.89] | 17.95 [15.61, 20.80] | 0 | 0 |
| humaneval/low | picospec_vs_sync_g4 | 30 | 93.18 [83.37, 104.12] | 27.15 [24.19, 30.44] | 0 | 0 |
| humaneval/low | picospec_g8_vs_sync_g4 | 30 | 122.14 [110.49, 135.60] | 28.81 [25.10, 32.59] | 0 | 0 |
| humaneval/low | hf_default_vs_sync_g4 | 30 | 0.77 [-3.51, 6.67] | -4.36 [-8.27, 0.29] | 2 | 0 |
| humaneval/low | pipesd_vs_sync_g4 | 30 | 25.52 [16.29, 36.42] | 5.72 [0.40, 11.15] | 2 | 0 |
| humaneval/low | pearl_vs_sync_g4 | 30 | 16.37 [12.20, 20.65] | 7.81 [5.13, 10.22] | 1 | 0 |
| humaneval/low | markov_w0_dist_int_vs_sync_g4 | 30 | 86.13 [79.60, 92.76] | 25.35 [22.43, 28.43] | 0 | 0 |
| humaneval/low | markov_w05_dist_int_vs_sync_g4 | 30 | 84.95 [71.95, 99.02] | 23.56 [19.91, 27.29] | 1 | 0 |
| humaneval/high | picospec_vs_picospec_g2 | 30 | 60.39 [55.14, 67.54] | 30.14 [28.02, 32.75] | 0 | 0 |
| humaneval/high | picospec_g8_vs_picospec_g2 | 30 | 137.86 [127.42, 149.62] | 43.92 [41.46, 46.75] | 0 | 0 |
| humaneval/high | sync_g4_vs_picospec_g2 | 30 | 5.11 [2.67, 8.32] | 8.12 [6.25, 10.50] | 0 | 0 |
| humaneval/high | hf_default_vs_picospec_g2 | 30 | 40.17 [33.97, 47.14] | 23.40 [20.44, 26.50] | 3 | 0 |
| humaneval/high | pipesd_vs_picospec_g2 | 30 | 82.67 [71.35, 97.21] | 33.78 [30.08, 38.06] | 2 | 0 |
| humaneval/high | pearl_vs_picospec_g2 | 30 | 101.26 [93.94, 110.25] | 40.14 [37.99, 42.56] | 1 | 0 |
| humaneval/high | markov_w0_dist_int_vs_picospec_g2 | 30 | 128.65 [120.04, 138.88] | 43.42 [40.97, 46.13] | 1 | 0 |
| humaneval/high | markov_w05_dist_int_vs_picospec_g2 | 30 | 113.60 [105.32, 123.39] | 40.04 [37.65, 42.81] | 2 | 0 |
| humaneval/high | picospec_g2_vs_picospec | 30 | -37.65 [-40.31, -35.54] | -43.14 [-48.70, -38.94] | 0 | 0 |
| humaneval/high | picospec_g8_vs_picospec | 30 | 48.30 [38.69, 57.03] | 19.73 [15.68, 23.69] | 0 | 0 |
| humaneval/high | sync_g4_vs_picospec | 30 | -34.47 [-35.83, -33.21] | -31.51 [-33.96, -29.27] | 0 | 0 |
| humaneval/high | hf_default_vs_picospec | 30 | -12.61 [-16.10, -8.96] | -9.63 [-13.54, -5.75] | 3 | 0 |
| humaneval/high | pipesd_vs_picospec | 30 | 13.89 [8.35, 20.57] | 5.21 [0.97, 9.83] | 2 | 0 |
| humaneval/high | pearl_vs_picospec | 30 | 25.48 [21.04, 30.08] | 14.31 [11.65, 17.01] | 1 | 0 |
| humaneval/high | markov_w0_dist_int_vs_picospec | 30 | 42.56 [38.32, 47.48] | 19.01 [16.30, 21.95] | 1 | 0 |
| humaneval/high | markov_w05_dist_int_vs_picospec | 30 | 33.18 [26.37, 39.46] | 14.17 [10.62, 17.57] | 2 | 0 |
| humaneval/high | picospec_g2_vs_picospec_g8 | 30 | -57.96 [-59.94, -56.03] | -78.31 [-87.79, -70.81] | 0 | 0 |
| humaneval/high | picospec_vs_picospec_g8 | 30 | -32.57 [-36.32, -27.90] | -24.57 [-31.04, -18.59] | 0 | 0 |
| humaneval/high | sync_g4_vs_picospec_g8 | 30 | -55.81 [-58.25, -53.09] | -63.83 [-72.73, -55.94] | 0 | 0 |
| humaneval/high | hf_default_vs_picospec_g8 | 30 | -41.07 [-43.89, -37.93] | -36.58 [-41.83, -31.85] | 3 | 0 |
| humaneval/high | pipesd_vs_picospec_g8 | 30 | -23.20 [-27.04, -18.16] | -18.08 [-21.67, -14.20] | 2 | 0 |
| humaneval/high | pearl_vs_picospec_g8 | 30 | -15.39 [-18.70, -11.51] | -6.74 [-10.16, -3.38] | 1 | 0 |
| humaneval/high | markov_w0_dist_int_vs_picospec_g8 | 30 | -3.87 [-7.93, 1.62] | -0.89 [-3.91, 2.35] | 1 | 0 |
| humaneval/high | markov_w05_dist_int_vs_picospec_g8 | 30 | -10.20 [-12.79, -7.70] | -6.92 [-9.63, -4.57] | 2 | 0 |
| humaneval/high | picospec_g2_vs_sync_g4 | 30 | -4.86 [-7.68, -2.60] | -8.84 [-11.73, -6.67] | 0 | 0 |
| humaneval/high | picospec_vs_sync_g4 | 30 | 52.60 [49.71, 55.83] | 23.96 [22.64, 25.35] | 0 | 0 |
| humaneval/high | picospec_g8_vs_sync_g4 | 30 | 126.30 [113.17, 139.52] | 38.96 [35.87, 42.11] | 0 | 0 |
| humaneval/high | hf_default_vs_sync_g4 | 30 | 33.36 [28.22, 38.90] | 16.64 [13.65, 19.62] | 3 | 0 |
| humaneval/high | pipesd_vs_sync_g4 | 30 | 73.79 [64.71, 84.70] | 27.92 [24.28, 31.86] | 2 | 0 |
| humaneval/high | pearl_vs_sync_g4 | 30 | 91.48 [85.27, 98.48] | 34.85 [32.74, 37.11] | 1 | 0 |
| humaneval/high | markov_w0_dist_int_vs_sync_g4 | 30 | 117.54 [110.36, 125.61] | 38.42 [36.03, 40.97] | 1 | 0 |
| humaneval/high | markov_w05_dist_int_vs_sync_g4 | 30 | 103.22 [93.65, 112.64] | 34.74 [32.08, 37.58] | 2 | 0 |
| humaneval/dynamic | picospec_vs_picospec_g2 | 30 | 36.26 [31.16, 42.03] | 17.91 [15.11, 20.91] | 0 | 0 |
| humaneval/dynamic | picospec_g8_vs_picospec_g2 | 30 | 80.02 [68.57, 92.78] | 25.37 [20.17, 30.74] | 0 | 0 |
| humaneval/dynamic | sync_g4_vs_picospec_g2 | 30 | -17.36 [-20.93, -13.60] | -9.17 [-12.39, -5.88] | 0 | 0 |
| humaneval/dynamic | hf_default_vs_picospec_g2 | 30 | -6.56 [-13.47, 1.08] | -4.68 [-10.99, 1.47] | 1 | 0 |
| humaneval/dynamic | pipesd_vs_picospec_g2 | 30 | 23.32 [14.51, 34.04] | 8.48 [2.99, 14.09] | 0 | 0 |
| humaneval/dynamic | pearl_vs_picospec_g2 | 30 | 14.76 [11.70, 18.43] | 10.04 [7.98, 12.41] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_picospec_g2 | 30 | 60.72 [50.59, 71.54] | 23.54 [18.83, 28.34] | 1 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_picospec_g2 | 30 | 56.49 [47.23, 67.20] | 21.13 [16.75, 25.70] | 0 | 0 |
| humaneval/dynamic | picospec_g2_vs_picospec | 30 | -26.61 [-29.59, -23.76] | -21.82 [-26.45, -17.80] | 0 | 0 |
| humaneval/dynamic | picospec_g8_vs_picospec | 30 | 32.12 [26.15, 38.29] | 9.09 [5.19, 13.43] | 0 | 0 |
| humaneval/dynamic | sync_g4_vs_picospec | 30 | -39.35 [-41.67, -37.09] | -32.99 [-36.66, -29.83] | 0 | 0 |
| humaneval/dynamic | hf_default_vs_picospec | 30 | -31.43 [-35.90, -26.59] | -27.53 [-33.20, -22.12] | 1 | 0 |
| humaneval/dynamic | pipesd_vs_picospec | 30 | -9.50 [-15.11, -3.14] | -11.49 [-15.91, -6.94] | 0 | 0 |
| humaneval/dynamic | pearl_vs_picospec | 30 | -15.78 [-19.55, -12.27] | -9.59 [-14.06, -5.96] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_picospec | 30 | 17.95 [11.89, 24.19] | 6.86 [2.98, 10.71] | 1 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_picospec | 30 | 14.85 [10.44, 19.63] | 3.92 [1.12, 6.68] | 0 | 0 |
| humaneval/dynamic | picospec_g2_vs_picospec_g8 | 30 | -44.45 [-48.13, -40.68] | -34.00 [-44.38, -25.26] | 0 | 0 |
| humaneval/dynamic | picospec_vs_picospec_g8 | 30 | -24.31 [-27.69, -20.73] | -10.00 [-15.52, -5.48] | 0 | 0 |
| humaneval/dynamic | sync_g4_vs_picospec_g8 | 30 | -54.09 [-56.40, -51.82] | -46.28 [-55.53, -38.43] | 0 | 0 |
| humaneval/dynamic | hf_default_vs_picospec_g8 | 30 | -48.10 [-51.04, -44.98] | -40.28 [-47.91, -33.69] | 1 | 0 |
| humaneval/dynamic | pipesd_vs_picospec_g8 | 30 | -31.50 [-35.32, -27.12] | -22.64 [-27.08, -18.60] | 0 | 0 |
| humaneval/dynamic | pearl_vs_picospec_g8 | 30 | -36.25 [-40.22, -32.42] | -20.55 [-29.42, -12.81] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_picospec_g8 | 30 | -10.72 [-13.83, -7.77] | -2.46 [-5.20, 0.03] | 1 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_picospec_g8 | 30 | -13.07 [-16.05, -10.06] | -5.69 [-8.87, -2.92] | 0 | 0 |
| humaneval/dynamic | picospec_g2_vs_sync_g4 | 30 | 21.00 [15.74, 26.47] | 8.40 [5.56, 11.02] | 0 | 0 |
| humaneval/dynamic | picospec_vs_sync_g4 | 30 | 64.88 [58.96, 71.45] | 24.80 [22.98, 26.83] | 0 | 0 |
| humaneval/dynamic | picospec_g8_vs_sync_g4 | 30 | 117.83 [107.57, 129.34] | 31.64 [27.76, 35.70] | 0 | 0 |
| humaneval/dynamic | hf_default_vs_sync_g4 | 30 | 13.06 [7.88, 18.87] | 4.11 [0.18, 8.00] | 1 | 0 |
| humaneval/dynamic | pipesd_vs_sync_g4 | 30 | 49.21 [41.72, 58.30] | 16.16 [12.43, 20.06] | 0 | 0 |
| humaneval/dynamic | pearl_vs_sync_g4 | 30 | 38.86 [32.50, 45.50] | 17.59 [14.31, 20.65] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_sync_g4 | 30 | 94.48 [84.34, 105.24] | 29.96 [26.20, 33.84] | 1 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_sync_g4 | 30 | 89.36 [81.71, 97.66] | 27.75 [24.75, 30.86] | 0 | 0 |
| humaneval/pooled | picospec_vs_picospec_g2 | 30 | 46.73 [43.44, 50.45] | 21.94 [20.33, 23.62] | 0 | 0 |
| humaneval/pooled | picospec_g8_vs_picospec_g2 | 30 | 97.27 [89.70, 105.63] | 31.01 [27.96, 34.30] | 0 | 0 |
| humaneval/pooled | sync_g4_vs_picospec_g2 | 30 | -11.33 [-13.25, -9.33] | -4.24 [-5.94, -2.48] | 0 | 0 |
| humaneval/pooled | hf_default_vs_picospec_g2 | 30 | 3.66 [-0.19, 7.91] | 2.87 [-0.25, 6.11] | 6 | 0 |
| humaneval/pooled | pipesd_vs_picospec_g2 | 30 | 33.81 [27.15, 41.62] | 14.56 [10.59, 18.64] | 4 | 0 |
| humaneval/pooled | pearl_vs_picospec_g2 | 30 | 31.93 [28.53, 35.55] | 18.55 [16.85, 20.29] | 2 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec_g2 | 30 | 78.41 [72.35, 85.10] | 29.23 [26.40, 32.12] | 2 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_picospec_g2 | 30 | 71.77 [65.43, 78.56] | 26.41 [23.83, 29.23] | 3 | 0 |
| humaneval/pooled | picospec_g2_vs_picospec | 30 | -31.85 [-33.53, -30.28] | -28.10 [-30.92, -25.52] | 0 | 0 |
| humaneval/pooled | picospec_g8_vs_picospec | 30 | 34.44 [29.64, 39.55] | 11.63 [8.58, 15.03] | 0 | 0 |
| humaneval/pooled | sync_g4_vs_picospec | 30 | -39.57 [-40.92, -38.27] | -33.53 [-36.43, -30.95] | 0 | 0 |
| humaneval/pooled | hf_default_vs_picospec | 30 | -29.35 [-31.80, -26.78] | -24.42 [-27.98, -20.91] | 6 | 0 |
| humaneval/pooled | pipesd_vs_picospec | 30 | -8.81 [-12.55, -4.18] | -9.45 [-13.14, -5.38] | 4 | 0 |
| humaneval/pooled | pearl_vs_picospec | 30 | -10.09 [-12.70, -7.56] | -4.33 [-6.74, -2.13] | 2 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec | 30 | 21.59 [18.46, 25.15] | 9.34 [6.73, 12.01] | 2 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_picospec | 30 | 17.06 [13.04, 21.17] | 5.73 [3.31, 8.29] | 3 | 0 |
| humaneval/pooled | picospec_g2_vs_picospec_g8 | 30 | -49.31 [-51.37, -47.29] | -44.95 [-52.22, -38.81] | 0 | 0 |
| humaneval/pooled | picospec_vs_picospec_g8 | 30 | -25.62 [-28.34, -22.86] | -13.16 [-17.69, -9.39] | 0 | 0 |
| humaneval/pooled | sync_g4_vs_picospec_g8 | 30 | -55.05 [-56.97, -53.15] | -51.10 [-59.01, -44.56] | 0 | 0 |
| humaneval/pooled | hf_default_vs_picospec_g8 | 30 | -47.45 [-49.07, -45.81] | -40.79 [-45.77, -36.23] | 6 | 0 |
| humaneval/pooled | pipesd_vs_picospec_g8 | 30 | -32.17 [-34.32, -29.61] | -23.85 [-26.57, -21.26] | 4 | 0 |
| humaneval/pooled | pearl_vs_picospec_g8 | 30 | -33.12 [-35.63, -30.66] | -18.06 [-23.58, -13.32] | 2 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec_g8 | 30 | -9.56 [-11.75, -7.03] | -2.59 [-4.71, -0.62] | 2 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_picospec_g8 | 30 | -12.93 [-14.69, -11.17] | -6.67 [-8.85, -4.79] | 3 | 0 |
| humaneval/pooled | picospec_g2_vs_sync_g4 | 30 | 12.78 [10.29, 15.28] | 4.07 [2.42, 5.61] | 0 | 0 |
| humaneval/pooled | picospec_vs_sync_g4 | 30 | 65.49 [61.98, 69.26] | 25.11 [23.63, 26.70] | 0 | 0 |
| humaneval/pooled | picospec_g8_vs_sync_g4 | 30 | 122.48 [113.46, 132.42] | 33.82 [30.82, 37.11] | 0 | 0 |
| humaneval/pooled | hf_default_vs_sync_g4 | 30 | 16.91 [12.90, 21.35] | 6.82 [3.95, 9.82] | 6 | 0 |
| humaneval/pooled | pipesd_vs_sync_g4 | 30 | 50.91 [43.64, 59.21] | 18.03 [14.35, 21.93] | 4 | 0 |
| humaneval/pooled | pearl_vs_sync_g4 | 30 | 48.79 [44.90, 52.72] | 21.87 [20.09, 23.63] | 2 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_sync_g4 | 30 | 101.21 [94.68, 108.19] | 32.11 [29.33, 34.85] | 2 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_sync_g4 | 30 | 93.72 [86.17, 101.76] | 29.41 [26.96, 32.20] | 3 | 0 |
| mtbench/low | picospec_vs_picospec_g2 | 30 | -3.09 [-5.83, -0.19] | -36.63 [-39.54, -33.53] | 11 | 0 |
| mtbench/low | picospec_g8_vs_picospec_g2 | 30 | -18.18 [-20.99, -15.46] | -100.42 [-107.33, -92.88] | 18 | 1 |
| mtbench/low | sync_g4_vs_picospec_g2 | 30 | -20.66 [-22.41, -18.67] | -8.62 [-10.41, -6.68] | 10 | 0 |
| mtbench/low | hf_default_vs_picospec_g2 | 30 | -39.44 [-46.90, -33.11] | -49.17 [-68.00, -36.13] | 13 | 0 |
| mtbench/low | pipesd_vs_picospec_g2 | 30 | -33.34 [-35.18, -31.45] | -49.03 [-52.10, -45.94] | 10 | 0 |
| mtbench/low | pearl_vs_picospec_g2 | 30 | 10.98 [2.25, 18.72] | 17.82 [12.44, 21.99] | 9 | 0 |
| mtbench/low | markov_w0_dist_int_vs_picospec_g2 | 30 | -4.22 [-7.98, -0.75] | -6.24 [-10.22, -2.88] | 4 | 0 |
| mtbench/low | markov_w05_dist_int_vs_picospec_g2 | 30 | 3.11 [-0.10, 6.71] | 8.31 [5.65, 11.03] | 5 | 1 |
| mtbench/low | picospec_g2_vs_picospec | 30 | 3.19 [0.19, 6.19] | 26.81 [25.11, 28.34] | 11 | 0 |
| mtbench/low | picospec_g8_vs_picospec | 30 | -15.57 [-18.22, -12.68] | -46.69 [-50.38, -42.64] | 13 | 1 |
| mtbench/low | sync_g4_vs_picospec | 30 | -18.12 [-19.91, -16.19] | 20.50 [18.72, 22.06] | 1 | 0 |
| mtbench/low | hf_default_vs_picospec | 30 | -37.50 [-44.35, -31.39] | -9.18 [-22.96, 0.41] | 13 | 0 |
| mtbench/low | pipesd_vs_picospec | 30 | -31.21 [-33.45, -28.74] | -9.07 [-12.43, -5.94] | 11 | 0 |
| mtbench/low | pearl_vs_picospec | 30 | 14.52 [6.75, 21.34] | 39.85 [35.82, 42.96] | 15 | 0 |
| mtbench/low | markov_w0_dist_int_vs_picospec | 30 | -1.16 [-4.58, 2.19] | 22.24 [19.53, 24.64] | 10 | 0 |
| mtbench/low | markov_w05_dist_int_vs_picospec | 30 | 6.41 [2.92, 10.14] | 32.89 [30.42, 34.95] | 11 | 1 |
| mtbench/low | picospec_g2_vs_picospec_g8 | 30 | 22.22 [18.29, 26.57] | 50.10 [48.15, 51.77] | 18 | 0 |
| mtbench/low | picospec_vs_picospec_g8 | 30 | 18.44 [14.53, 22.27] | 31.83 [29.89, 33.50] | 13 | 0 |
| mtbench/low | sync_g4_vs_picospec_g8 | 30 | -3.03 [-6.61, 0.57] | 45.80 [43.56, 47.52] | 13 | 0 |
| mtbench/low | hf_default_vs_picospec_g8 | 30 | -25.98 [-35.43, -17.57] | 25.57 [14.89, 32.78] | 15 | 0 |
| mtbench/low | pipesd_vs_picospec_g8 | 30 | -18.53 [-22.20, -14.92] | 25.64 [21.78, 28.96] | 15 | 0 |
| mtbench/low | pearl_vs_picospec_g8 | 30 | 35.64 [23.64, 46.73] | 59.00 [55.50, 61.63] | 20 | 0 |
| mtbench/low | markov_w0_dist_int_vs_picospec_g8 | 30 | 17.06 [11.81, 22.46] | 46.99 [44.19, 49.44] | 17 | 0 |
| mtbench/low | markov_w05_dist_int_vs_picospec_g8 | 30 | 26.02 [20.65, 31.30] | 54.25 [51.63, 56.50] | 17 | 0 |
| mtbench/low | picospec_g2_vs_sync_g4 | 30 | 26.03 [22.96, 28.88] | 7.94 [6.27, 9.43] | 10 | 0 |
| mtbench/low | picospec_vs_sync_g4 | 30 | 22.14 [19.32, 24.87] | -25.78 [-28.30, -23.04] | 1 | 0 |
| mtbench/low | picospec_g8_vs_sync_g4 | 30 | 3.12 [-0.57, 7.07] | -84.51 [-90.54, -77.19] | 13 | 1 |
| mtbench/low | hf_default_vs_sync_g4 | 30 | -23.67 [-33.09, -15.83] | -37.33 [-55.00, -25.05] | 13 | 0 |
| mtbench/low | pipesd_vs_sync_g4 | 30 | -15.98 [-18.60, -13.01] | -37.19 [-40.66, -33.48] | 10 | 0 |
| mtbench/low | pearl_vs_sync_g4 | 30 | 39.87 [28.92, 48.44] | 24.35 [19.32, 27.92] | 14 | 0 |
| mtbench/low | markov_w0_dist_int_vs_sync_g4 | 30 | 20.72 [16.32, 24.06] | 2.20 [-1.32, 4.84] | 9 | 0 |
| mtbench/low | markov_w05_dist_int_vs_sync_g4 | 30 | 29.96 [26.23, 34.56] | 15.59 [13.32, 18.02] | 10 | 1 |
| mtbench/high | picospec_vs_picospec_g2 | 30 | 0.75 [-2.88, 4.87] | -10.84 [-14.38, -6.95] | 9 | 0 |
| mtbench/high | picospec_g8_vs_picospec_g2 | 30 | -6.04 [-9.58, -1.84] | -51.12 [-57.32, -44.17] | 16 | 0 |
| mtbench/high | sync_g4_vs_picospec_g2 | 30 | -4.42 [-6.02, -2.61] | 1.82 [0.27, 3.48] | 9 | 0 |
| mtbench/high | hf_default_vs_picospec_g2 | 30 | -14.24 [-18.99, -10.23] | -15.61 [-23.15, -9.87] | 16 | 0 |
| mtbench/high | pipesd_vs_picospec_g2 | 30 | -13.00 [-15.57, -9.95] | -39.22 [-43.15, -34.68] | 9 | 0 |
| mtbench/high | pearl_vs_picospec_g2 | 30 | -0.98 [-3.79, 1.99] | -17.24 [-20.05, -14.20] | 14 | 1 |
| mtbench/high | markov_w0_dist_int_vs_picospec_g2 | 30 | 5.43 [1.10, 9.60] | -19.53 [-22.14, -16.75] | 4 | 0 |
| mtbench/high | markov_w05_dist_int_vs_picospec_g2 | 30 | -0.32 [-2.40, 2.20] | 0.41 [-1.08, 2.08] | 6 | 0 |
| mtbench/high | picospec_g2_vs_picospec | 30 | -0.74 [-4.65, 2.97] | 9.78 [6.50, 12.58] | 9 | 0 |
| mtbench/high | picospec_g8_vs_picospec | 30 | -6.73 [-9.74, -3.15] | -36.34 [-40.09, -31.66] | 12 | 0 |
| mtbench/high | sync_g4_vs_picospec | 30 | -5.13 [-7.78, -2.41] | 11.42 [9.12, 13.43] | 1 | 0 |
| mtbench/high | hf_default_vs_picospec | 30 | -14.87 [-20.48, -9.79] | -4.31 [-12.22, 1.95] | 13 | 0 |
| mtbench/high | pipesd_vs_picospec | 30 | -13.65 [-15.60, -11.20] | -25.61 [-28.09, -22.62] | 10 | 0 |
| mtbench/high | pearl_vs_picospec | 30 | -1.71 [-4.80, 1.32] | -5.77 [-8.44, -3.22] | 13 | 1 |
| mtbench/high | markov_w0_dist_int_vs_picospec | 30 | 4.65 [0.58, 8.85] | -7.84 [-11.07, -4.71] | 6 | 0 |
| mtbench/high | markov_w05_dist_int_vs_picospec | 30 | -1.06 [-4.11, 1.76] | 10.15 [6.85, 12.68] | 10 | 0 |
| mtbench/high | picospec_g2_vs_picospec_g8 | 30 | 6.42 [1.87, 10.60] | 33.83 [30.64, 36.43] | 16 | 0 |
| mtbench/high | picospec_vs_picospec_g8 | 30 | 7.22 [3.26, 10.79] | 26.65 [24.05, 28.62] | 12 | 0 |
| mtbench/high | sync_g4_vs_picospec_g8 | 30 | 1.72 [-1.64, 4.77] | 35.03 [32.35, 37.24] | 13 | 0 |
| mtbench/high | hf_default_vs_picospec_g8 | 30 | -8.73 [-14.79, -3.57] | 23.50 [17.26, 28.22] | 15 | 0 |
| mtbench/high | pipesd_vs_picospec_g8 | 30 | -7.41 [-9.86, -4.83] | 7.87 [5.36, 10.09] | 15 | 0 |
| mtbench/high | pearl_vs_picospec_g8 | 30 | 5.38 [2.35, 8.07] | 22.42 [19.89, 24.50] | 13 | 1 |
| mtbench/high | markov_w0_dist_int_vs_picospec_g8 | 30 | 12.20 [7.94, 16.06] | 20.90 [17.55, 23.66] | 15 | 0 |
| mtbench/high | markov_w05_dist_int_vs_picospec_g8 | 30 | 6.08 [2.03, 10.06] | 34.10 [30.76, 36.66] | 14 | 0 |
| mtbench/high | picospec_g2_vs_sync_g4 | 30 | 4.62 [2.68, 6.41] | -1.85 [-3.60, -0.27] | 9 | 0 |
| mtbench/high | picospec_vs_sync_g4 | 30 | 5.41 [2.47, 8.44] | -12.89 [-15.52, -10.04] | 1 | 0 |
| mtbench/high | picospec_g8_vs_sync_g4 | 30 | -1.69 [-4.55, 1.66] | -53.92 [-59.34, -47.82] | 13 | 0 |
| mtbench/high | hf_default_vs_sync_g4 | 30 | -10.27 [-15.35, -6.05] | -17.75 [-25.83, -11.85] | 13 | 0 |
| mtbench/high | pipesd_vs_sync_g4 | 30 | -8.98 [-10.85, -6.77] | -41.80 [-44.87, -38.12] | 10 | 0 |
| mtbench/high | pearl_vs_sync_g4 | 30 | 3.60 [1.08, 6.20] | -19.41 [-21.98, -16.72] | 13 | 1 |
| mtbench/high | markov_w0_dist_int_vs_sync_g4 | 30 | 10.31 [6.38, 14.11] | -21.74 [-24.21, -18.92] | 6 | 0 |
| mtbench/high | markov_w05_dist_int_vs_sync_g4 | 30 | 4.29 [1.97, 7.17] | -1.43 [-3.73, 1.07] | 10 | 0 |
| mtbench/dynamic | picospec_vs_picospec_g2 | 30 | -2.43 [-5.89, 2.40] | -21.72 [-26.12, -16.21] | 8 | 0 |
| mtbench/dynamic | picospec_g8_vs_picospec_g2 | 30 | -10.32 [-16.42, -3.37] | -70.09 [-81.90, -57.53] | 15 | 0 |
| mtbench/dynamic | sync_g4_vs_picospec_g2 | 30 | -8.98 [-15.22, -1.45] | -0.78 [-6.24, 4.90] | 8 | 0 |
| mtbench/dynamic | hf_default_vs_picospec_g2 | 30 | -24.05 [-33.16, -14.13] | -28.28 [-43.72, -15.80] | 9 | 0 |
| mtbench/dynamic | pipesd_vs_picospec_g2 | 30 | -18.19 [-25.08, -9.69] | -37.99 [-47.45, -28.12] | 5 | 0 |
| mtbench/dynamic | pearl_vs_picospec_g2 | 30 | -0.37 [-7.61, 7.03] | -4.15 [-10.24, 1.20] | 9 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_picospec_g2 | 30 | 2.03 [-4.48, 9.20] | -11.00 [-17.49, -4.59] | 4 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_picospec_g2 | 30 | 7.41 [-0.37, 16.28] | 7.45 [1.86, 13.09] | 6 | 0 |
| mtbench/dynamic | picospec_g2_vs_picospec | 30 | 2.49 [-2.34, 6.26] | 17.84 [13.95, 20.71] | 8 | 0 |
| mtbench/dynamic | picospec_g8_vs_picospec | 30 | -8.09 [-13.79, -1.69] | -39.74 [-45.35, -33.32] | 11 | 0 |
| mtbench/dynamic | sync_g4_vs_picospec | 30 | -6.71 [-13.17, 0.84] | 17.20 [12.48, 21.28] | 0 | 0 |
| mtbench/dynamic | hf_default_vs_picospec | 30 | -22.16 [-31.25, -13.08] | -5.39 [-17.21, 3.47] | 9 | 0 |
| mtbench/dynamic | pipesd_vs_picospec | 30 | -16.16 [-22.71, -8.16] | -13.36 [-20.68, -6.91] | 6 | 0 |
| mtbench/dynamic | pearl_vs_picospec | 30 | 2.11 [-5.60, 10.56] | 14.44 [9.13, 19.13] | 8 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_picospec | 30 | 4.57 [-2.27, 11.81] | 8.81 [2.63, 14.20] | 6 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_picospec | 30 | 10.08 [1.35, 20.23] | 23.96 [17.92, 29.11] | 10 | 0 |
| mtbench/dynamic | picospec_g2_vs_picospec_g8 | 30 | 11.51 [3.48, 19.65] | 41.21 [36.52, 45.02] | 15 | 1 |
| mtbench/dynamic | picospec_vs_picospec_g8 | 30 | 8.80 [1.72, 16.00] | 28.44 [24.99, 31.20] | 11 | 1 |
| mtbench/dynamic | sync_g4_vs_picospec_g8 | 30 | 1.49 [-2.09, 4.98] | 40.75 [37.23, 43.61] | 11 | 1 |
| mtbench/dynamic | hf_default_vs_picospec_g8 | 30 | -15.31 [-23.57, -8.32] | 24.58 [16.33, 30.77] | 14 | 0 |
| mtbench/dynamic | pipesd_vs_picospec_g8 | 30 | -8.78 [-12.23, -5.18] | 18.88 [14.09, 22.77] | 12 | 1 |
| mtbench/dynamic | pearl_vs_picospec_g8 | 30 | 11.09 [6.30, 16.78] | 38.77 [34.61, 42.36] | 13 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_picospec_g8 | 30 | 13.77 [9.27, 18.41] | 34.74 [29.63, 39.11] | 14 | 1 |
| mtbench/dynamic | markov_w05_dist_int_vs_picospec_g8 | 30 | 19.76 [13.51, 26.14] | 45.59 [41.02, 49.24] | 14 | 1 |
| mtbench/dynamic | picospec_g2_vs_sync_g4 | 30 | 9.87 [1.47, 17.95] | 0.78 [-5.16, 5.87] | 8 | 0 |
| mtbench/dynamic | picospec_vs_sync_g4 | 30 | 7.20 [-0.83, 15.17] | -20.77 [-27.04, -14.27] | 0 | 0 |
| mtbench/dynamic | picospec_g8_vs_sync_g4 | 30 | -1.47 [-4.75, 2.14] | -68.77 [-77.34, -59.31] | 11 | 0 |
| mtbench/dynamic | hf_default_vs_sync_g4 | 30 | -16.56 [-23.91, -10.69] | -27.29 [-39.75, -18.91] | 9 | 0 |
| mtbench/dynamic | pipesd_vs_sync_g4 | 30 | -10.12 [-12.12, -7.53] | -36.91 [-39.76, -33.60] | 6 | 0 |
| mtbench/dynamic | pearl_vs_sync_g4 | 30 | 9.46 [5.19, 14.12] | -3.34 [-6.23, -0.42] | 8 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_sync_g4 | 30 | 12.10 [7.87, 16.85] | -10.14 [-14.31, -6.00] | 6 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_sync_g4 | 30 | 18.00 [14.47, 21.59] | 8.17 [4.97, 10.91] | 10 | 0 |
| mtbench/pooled | picospec_vs_picospec_g2 | 30 | -1.14 [-3.45, 2.00] | -20.70 [-23.38, -17.22] | 28 | 0 |
| mtbench/pooled | picospec_g8_vs_picospec_g2 | 30 | -10.22 [-13.70, -6.18] | -69.32 [-76.45, -61.56] | 49 | 1 |
| mtbench/pooled | sync_g4_vs_picospec_g2 | 30 | -9.82 [-12.23, -7.19] | -1.58 [-3.78, 0.61] | 27 | 0 |
| mtbench/pooled | hf_default_vs_picospec_g2 | 30 | -24.14 [-30.84, -18.81] | -27.93 [-40.10, -19.71] | 38 | 0 |
| mtbench/pooled | pipesd_vs_picospec_g2 | 30 | -19.84 [-22.22, -16.84] | -41.14 [-44.59, -37.09] | 24 | 0 |
| mtbench/pooled | pearl_vs_picospec_g2 | 30 | 1.56 [-1.67, 4.78] | -4.38 [-7.10, -1.87] | 32 | 1 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec_g2 | 30 | 2.15 [-1.12, 5.48] | -13.45 [-15.97, -10.80] | 12 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_picospec_g2 | 30 | 2.95 [0.07, 6.11] | 4.74 [2.42, 7.18] | 17 | 1 |
| mtbench/pooled | picospec_g2_vs_picospec | 30 | 1.15 [-1.96, 3.58] | 17.15 [14.69, 18.95] | 28 | 0 |
| mtbench/pooled | picospec_g8_vs_picospec | 30 | -9.19 [-11.89, -6.26] | -40.28 [-43.74, -36.34] | 36 | 1 |
| mtbench/pooled | sync_g4_vs_picospec | 30 | -8.78 [-11.32, -6.02] | 15.84 [13.54, 17.76] | 2 | 0 |
| mtbench/pooled | hf_default_vs_picospec | 30 | -23.26 [-30.01, -17.79] | -5.99 [-16.48, 1.07] | 35 | 0 |
| mtbench/pooled | pipesd_vs_picospec | 30 | -18.91 [-21.03, -16.45] | -16.94 [-19.53, -14.45] | 27 | 0 |
| mtbench/pooled | pearl_vs_picospec | 30 | 2.73 [-0.75, 6.26] | 13.52 [10.95, 15.81] | 36 | 1 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec | 30 | 3.33 [0.21, 6.43] | 6.01 [3.18, 8.60] | 22 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_picospec | 30 | 4.13 [0.35, 7.77] | 21.08 [17.60, 23.75] | 31 | 1 |
| mtbench/pooled | picospec_g2_vs_picospec_g8 | 30 | 11.39 [6.59, 15.88] | 40.94 [38.10, 43.33] | 49 | 1 |
| mtbench/pooled | picospec_vs_picospec_g8 | 30 | 10.12 [6.68, 13.49] | 28.72 [26.65, 30.43] | 36 | 1 |
| mtbench/pooled | sync_g4_vs_picospec_g8 | 30 | 0.45 [-2.63, 3.21] | 40.01 [37.38, 42.11] | 37 | 1 |
| mtbench/pooled | hf_default_vs_picospec_g8 | 30 | -15.50 [-23.02, -9.24] | 24.45 [16.61, 30.06] | 44 | 0 |
| mtbench/pooled | pipesd_vs_picospec_g8 | 30 | -10.71 [-13.12, -8.46] | 16.64 [13.63, 19.15] | 42 | 1 |
| mtbench/pooled | pearl_vs_picospec_g8 | 30 | 13.12 [9.29, 16.85] | 38.35 [35.75, 40.57] | 46 | 1 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec_g8 | 30 | 13.79 [11.01, 16.34] | 33.00 [30.07, 35.47] | 46 | 1 |
| mtbench/pooled | markov_w05_dist_int_vs_picospec_g8 | 30 | 14.67 [10.27, 18.67] | 43.74 [40.58, 46.24] | 45 | 1 |
| mtbench/pooled | picospec_g2_vs_sync_g4 | 30 | 10.89 [7.74, 13.93] | 1.55 [-0.62, 3.65] | 27 | 0 |
| mtbench/pooled | picospec_vs_sync_g4 | 30 | 9.63 [6.41, 12.76] | -18.83 [-21.59, -15.66] | 2 | 0 |
| mtbench/pooled | picospec_g8_vs_sync_g4 | 30 | -0.44 [-3.11, 2.70] | -66.70 [-72.75, -59.70] | 37 | 1 |
| mtbench/pooled | hf_default_vs_sync_g4 | 30 | -15.88 [-23.01, -10.41] | -25.94 [-37.68, -17.99] | 35 | 0 |
| mtbench/pooled | pipesd_vs_sync_g4 | 30 | -11.11 [-12.40, -9.55] | -38.95 [-40.81, -36.74] | 26 | 0 |
| mtbench/pooled | pearl_vs_sync_g4 | 30 | 12.62 [10.07, 15.27] | -2.76 [-4.79, -0.72] | 35 | 1 |
| mtbench/pooled | markov_w0_dist_int_vs_sync_g4 | 30 | 13.28 [10.82, 15.80] | -11.69 [-13.51, -9.87] | 21 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_sync_g4 | 30 | 14.16 [12.04, 16.31] | 6.22 [4.14, 8.08] | 30 | 1 |
| gsm8k/low | picospec_vs_picospec_g2 | 50 | 21.32 [18.22, 25.19] | -6.40 [-9.26, -3.25] | 4 | 0 |
| gsm8k/low | picospec_g8_vs_picospec_g2 | 50 | 20.82 [16.10, 25.65] | -30.38 [-36.79, -24.00] | 9 | 1 |
| gsm8k/low | sync_g4_vs_picospec_g2 | 50 | -22.62 [-24.88, -19.82] | -10.34 [-12.47, -8.01] | 4 | 0 |
| gsm8k/low | hf_default_vs_picospec_g2 | 50 | -35.34 [-38.11, -32.02] | -40.78 [-45.52, -35.95] | 8 | 0 |
| gsm8k/low | pipesd_vs_picospec_g2 | 50 | -31.63 [-34.78, -27.74] | -45.25 [-50.28, -39.88] | 10 | 0 |
| gsm8k/low | pearl_vs_picospec_g2 | 50 | -9.95 [-11.90, -7.78] | -0.69 [-2.88, 1.44] | 1 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_picospec_g2 | 50 | 14.60 [10.78, 18.95] | -5.49 [-7.97, -2.40] | 4 | 0 |
| gsm8k/low | markov_w05_dist_int_vs_picospec_g2 | 50 | 6.65 [2.11, 11.75] | -2.71 [-5.53, -0.01] | 4 | 0 |
| gsm8k/low | picospec_g2_vs_picospec | 50 | -17.57 [-20.12, -15.41] | 6.01 [3.15, 8.48] | 4 | 0 |
| gsm8k/low | picospec_g8_vs_picospec | 50 | -0.41 [-3.22, 2.73] | -22.54 [-25.82, -19.30] | 9 | 1 |
| gsm8k/low | sync_g4_vs_picospec | 50 | -36.22 [-38.05, -34.01] | -3.70 [-6.20, -1.33] | 0 | 0 |
| gsm8k/low | hf_default_vs_picospec | 50 | -46.70 [-48.65, -44.43] | -32.31 [-35.87, -29.02] | 7 | 0 |
| gsm8k/low | pipesd_vs_picospec | 50 | -43.65 [-45.67, -41.14] | -36.51 [-39.41, -33.79] | 8 | 0 |
| gsm8k/low | pearl_vs_picospec | 50 | -25.77 [-28.45, -23.09] | 5.37 [1.07, 9.25] | 5 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_picospec | 50 | -5.54 [-7.61, -3.18] | 0.86 [-0.62, 2.27] | 4 | 0 |
| gsm8k/low | markov_w05_dist_int_vs_picospec | 50 | -12.09 [-15.36, -8.73] | 3.47 [0.88, 5.57] | 4 | 0 |
| gsm8k/low | picospec_g2_vs_picospec_g8 | 50 | -17.23 [-20.41, -13.87] | 23.30 [19.36, 26.89] | 9 | 0 |
| gsm8k/low | picospec_vs_picospec_g8 | 50 | 0.41 [-2.66, 3.33] | 18.39 [16.18, 20.52] | 9 | 0 |
| gsm8k/low | sync_g4_vs_picospec_g8 | 50 | -35.96 [-38.18, -33.71] | 15.37 [11.39, 19.04] | 9 | 0 |
| gsm8k/low | hf_default_vs_picospec_g8 | 50 | -46.48 [-48.49, -44.45] | -7.98 [-12.49, -3.86] | 9 | 0 |
| gsm8k/low | pipesd_vs_picospec_g8 | 50 | -43.42 [-45.16, -41.58] | -11.41 [-14.81, -7.96] | 9 | 0 |
| gsm8k/low | pearl_vs_picospec_g8 | 50 | -25.47 [-29.20, -21.32] | 22.77 [17.68, 27.44] | 9 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_picospec_g8 | 50 | -5.15 [-6.99, -3.31] | 19.09 [16.47, 21.62] | 10 | 0 |
| gsm8k/low | markov_w05_dist_int_vs_picospec_g8 | 50 | -11.73 [-14.54, -9.36] | 21.22 [18.06, 24.17] | 7 | 0 |
| gsm8k/low | picospec_g2_vs_sync_g4 | 50 | 29.24 [24.72, 33.12] | 9.37 [7.41, 11.09] | 4 | 0 |
| gsm8k/low | picospec_vs_sync_g4 | 50 | 56.79 [51.54, 61.42] | 3.57 [1.31, 5.84] | 0 | 0 |
| gsm8k/low | picospec_g8_vs_sync_g4 | 50 | 56.15 [50.84, 61.75] | -18.16 [-23.52, -12.86] | 9 | 1 |
| gsm8k/low | hf_default_vs_sync_g4 | 50 | -16.43 [-18.88, -14.13] | -27.59 [-31.11, -24.41] | 7 | 0 |
| gsm8k/low | pipesd_vs_sync_g4 | 50 | -11.64 [-14.60, -8.44] | -31.64 [-35.76, -27.50] | 8 | 0 |
| gsm8k/low | pearl_vs_sync_g4 | 50 | 16.38 [11.31, 20.61] | 8.75 [5.72, 11.09] | 5 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_sync_g4 | 50 | 48.11 [43.75, 52.76] | 4.40 [2.09, 6.77] | 4 | 0 |
| gsm8k/low | markov_w05_dist_int_vs_sync_g4 | 50 | 37.83 [33.72, 42.71] | 6.91 [5.06, 8.60] | 4 | 0 |
| gsm8k/high | picospec_vs_picospec_g2 | 50 | 32.34 [28.38, 36.11] | 14.98 [12.74, 17.07] | 4 | 1 |
| gsm8k/high | picospec_g8_vs_picospec_g2 | 50 | 56.08 [50.18, 62.13] | 7.72 [4.09, 11.43] | 10 | 1 |
| gsm8k/high | sync_g4_vs_picospec_g2 | 50 | 3.10 [1.78, 4.60] | 7.28 [6.16, 8.50] | 4 | 1 |
| gsm8k/high | hf_default_vs_picospec_g2 | 50 | 3.79 [1.31, 6.60] | -0.11 [-2.40, 2.33] | 7 | 0 |
| gsm8k/high | pipesd_vs_picospec_g2 | 50 | 20.70 [16.59, 24.77] | -1.31 [-4.96, 2.13] | 6 | 0 |
| gsm8k/high | pearl_vs_picospec_g2 | 50 | 41.98 [38.15, 46.03] | 15.77 [13.53, 18.11] | 9 | 1 |
| gsm8k/high | markov_w0_dist_int_vs_picospec_g2 | 50 | 55.76 [49.92, 61.70] | 13.60 [10.62, 16.50] | 6 | 1 |
| gsm8k/high | markov_w05_dist_int_vs_picospec_g2 | 50 | 37.00 [31.53, 42.72] | 15.65 [13.11, 18.30] | 7 | 0 |
| gsm8k/high | picospec_g2_vs_picospec | 50 | -24.44 [-26.53, -22.11] | -17.61 [-20.58, -14.60] | 4 | 0 |
| gsm8k/high | picospec_g8_vs_picospec | 50 | 17.94 [14.51, 21.47] | -8.54 [-11.10, -5.77] | 10 | 0 |
| gsm8k/high | sync_g4_vs_picospec | 50 | -22.10 [-23.76, -20.23] | -9.05 [-11.40, -6.77] | 0 | 0 |
| gsm8k/high | hf_default_vs_picospec | 50 | -21.57 [-23.42, -19.38] | -17.74 [-20.39, -14.94] | 9 | 0 |
| gsm8k/high | pipesd_vs_picospec | 50 | -8.80 [-11.14, -6.25] | -19.15 [-22.11, -16.12] | 8 | 0 |
| gsm8k/high | pearl_vs_picospec | 50 | 7.28 [5.08, 9.74] | 0.93 [-0.91, 2.76] | 7 | 0 |
| gsm8k/high | markov_w0_dist_int_vs_picospec | 50 | 17.69 [15.33, 20.08] | -1.62 [-3.58, 0.38] | 7 | 1 |
| gsm8k/high | markov_w05_dist_int_vs_picospec | 50 | 3.52 [0.21, 6.83] | 0.79 [-1.46, 2.97] | 6 | 0 |
| gsm8k/high | picospec_g2_vs_picospec_g8 | 50 | -35.93 [-38.32, -33.41] | -8.36 [-12.90, -4.27] | 10 | 0 |
| gsm8k/high | picospec_vs_picospec_g8 | 50 | -15.21 [-17.68, -12.67] | 7.87 [5.46, 9.99] | 10 | 0 |
| gsm8k/high | sync_g4_vs_picospec_g8 | 50 | -33.94 [-36.26, -31.49] | -0.47 [-4.42, 3.21] | 10 | 0 |
| gsm8k/high | hf_default_vs_picospec_g8 | 50 | -33.50 [-35.46, -31.57] | -8.48 [-11.98, -5.42] | 11 | 0 |
| gsm8k/high | pipesd_vs_picospec_g8 | 50 | -22.67 [-24.65, -20.60] | -9.78 [-12.27, -7.50] | 10 | 0 |
| gsm8k/high | pearl_vs_picospec_g8 | 50 | -9.03 [-10.98, -6.73] | 8.72 [6.95, 10.35] | 7 | 0 |
| gsm8k/high | markov_w0_dist_int_vs_picospec_g8 | 50 | -0.21 [-2.67, 2.17] | 6.38 [4.92, 7.75] | 7 | 1 |
| gsm8k/high | markov_w05_dist_int_vs_picospec_g8 | 50 | -12.23 [-14.22, -10.24] | 8.59 [6.59, 10.31] | 5 | 0 |
| gsm8k/high | picospec_g2_vs_sync_g4 | 50 | -3.01 [-4.40, -1.75] | -7.85 [-9.29, -6.56] | 4 | 0 |
| gsm8k/high | picospec_vs_sync_g4 | 50 | 28.36 [25.36, 31.17] | 8.30 [6.34, 10.23] | 0 | 0 |
| gsm8k/high | picospec_g8_vs_sync_g4 | 50 | 51.39 [45.96, 56.90] | 0.47 [-3.31, 4.23] | 10 | 0 |
| gsm8k/high | hf_default_vs_sync_g4 | 50 | 0.67 [-1.59, 3.12] | -7.97 [-10.52, -5.23] | 9 | 0 |
| gsm8k/high | pipesd_vs_sync_g4 | 50 | 17.07 [13.33, 20.84] | -9.26 [-13.16, -5.52] | 8 | 0 |
| gsm8k/high | pearl_vs_sync_g4 | 50 | 37.71 [34.05, 41.45] | 9.15 [6.60, 11.73] | 7 | 0 |
| gsm8k/high | markov_w0_dist_int_vs_sync_g4 | 50 | 51.07 [46.07, 56.43] | 6.82 [3.76, 9.84] | 7 | 1 |
| gsm8k/high | markov_w05_dist_int_vs_sync_g4 | 50 | 32.88 [27.48, 38.20] | 9.02 [6.22, 11.92] | 6 | 0 |
| gsm8k/dynamic | picospec_vs_picospec_g2 | 50 | 17.78 [14.98, 21.09] | 1.70 [-0.54, 4.11] | 6 | 0 |
| gsm8k/dynamic | picospec_g8_vs_picospec_g2 | 50 | 31.13 [25.73, 36.85] | -14.49 [-19.22, -9.64] | 11 | 0 |
| gsm8k/dynamic | sync_g4_vs_picospec_g2 | 50 | -12.11 [-14.77, -9.23] | -3.61 [-5.90, -1.24] | 6 | 0 |
| gsm8k/dynamic | hf_default_vs_picospec_g2 | 50 | -18.75 [-21.77, -15.26] | -21.49 [-25.23, -17.51] | 10 | 1 |
| gsm8k/dynamic | pipesd_vs_picospec_g2 | 50 | -9.30 [-12.68, -5.68] | -23.79 [-27.63, -19.99] | 10 | 1 |
| gsm8k/dynamic | pearl_vs_picospec_g2 | 50 | 6.56 [2.68, 10.72] | 2.26 [-0.50, 5.02] | 5 | 1 |
| gsm8k/dynamic | markov_w0_dist_int_vs_picospec_g2 | 50 | 29.02 [23.99, 34.61] | -0.97 [-4.04, 2.43] | 9 | 1 |
| gsm8k/dynamic | markov_w05_dist_int_vs_picospec_g2 | 50 | 15.80 [11.68, 20.56] | 3.29 [0.99, 5.93] | 6 | 1 |
| gsm8k/dynamic | picospec_g2_vs_picospec | 50 | -15.10 [-17.41, -13.03] | -1.73 [-4.28, 0.53] | 6 | 0 |
| gsm8k/dynamic | picospec_g8_vs_picospec | 50 | 11.33 [7.90, 14.56] | -16.47 [-19.24, -13.69] | 8 | 0 |
| gsm8k/dynamic | sync_g4_vs_picospec | 50 | -25.38 [-27.43, -23.35] | -5.41 [-7.87, -3.18] | 0 | 0 |
| gsm8k/dynamic | hf_default_vs_picospec | 50 | -31.02 [-33.32, -28.68] | -23.59 [-26.99, -20.38] | 9 | 1 |
| gsm8k/dynamic | pipesd_vs_picospec | 50 | -23.00 [-25.41, -20.60] | -25.94 [-28.27, -23.63] | 7 | 1 |
| gsm8k/dynamic | pearl_vs_picospec | 50 | -9.53 [-12.27, -7.05] | 0.57 [-1.77, 2.56] | 5 | 1 |
| gsm8k/dynamic | markov_w0_dist_int_vs_picospec | 50 | 9.54 [6.36, 12.48] | -2.72 [-4.65, -0.67] | 5 | 1 |
| gsm8k/dynamic | markov_w05_dist_int_vs_picospec | 50 | -1.68 [-4.13, 0.97] | 1.61 [0.05, 3.21] | 5 | 1 |
| gsm8k/dynamic | picospec_g2_vs_picospec_g8 | 50 | -23.74 [-26.93, -20.46] | 12.65 [8.79, 16.12] | 11 | 0 |
| gsm8k/dynamic | picospec_vs_picospec_g8 | 50 | -10.18 [-12.71, -7.32] | 14.14 [12.04, 16.13] | 8 | 0 |
| gsm8k/dynamic | sync_g4_vs_picospec_g8 | 50 | -32.97 [-35.43, -30.54] | 9.50 [5.62, 12.98] | 8 | 0 |
| gsm8k/dynamic | hf_default_vs_picospec_g8 | 50 | -38.04 [-40.12, -35.93] | -6.12 [-10.29, -2.28] | 10 | 1 |
| gsm8k/dynamic | pipesd_vs_picospec_g8 | 50 | -30.83 [-32.64, -29.03] | -8.13 [-10.63, -5.80] | 12 | 1 |
| gsm8k/dynamic | pearl_vs_picospec_g8 | 50 | -18.74 [-21.52, -15.73] | 14.63 [11.74, 17.43] | 11 | 1 |
| gsm8k/dynamic | markov_w0_dist_int_vs_picospec_g8 | 50 | -1.61 [-4.00, 0.86] | 11.81 [9.65, 14.00] | 8 | 1 |
| gsm8k/dynamic | markov_w05_dist_int_vs_picospec_g8 | 50 | -11.69 [-14.15, -9.10] | 15.53 [13.10, 18.07] | 10 | 1 |
| gsm8k/dynamic | picospec_g2_vs_sync_g4 | 50 | 13.78 [10.17, 17.33] | 3.49 [1.23, 5.57] | 6 | 0 |
| gsm8k/dynamic | picospec_vs_sync_g4 | 50 | 34.01 [30.47, 37.81] | 5.13 [3.08, 7.29] | 0 | 0 |
| gsm8k/dynamic | picospec_g8_vs_sync_g4 | 50 | 49.20 [43.96, 54.88] | -10.49 [-14.92, -5.96] | 8 | 0 |
| gsm8k/dynamic | hf_default_vs_sync_g4 | 50 | -7.56 [-9.42, -5.58] | -17.25 [-19.65, -14.87] | 9 | 1 |
| gsm8k/dynamic | pipesd_vs_sync_g4 | 50 | 3.19 [0.13, 6.59] | -19.47 [-22.96, -15.82] | 7 | 1 |
| gsm8k/dynamic | pearl_vs_sync_g4 | 50 | 21.24 [16.86, 25.18] | 5.67 [2.95, 8.05] | 5 | 1 |
| gsm8k/dynamic | markov_w0_dist_int_vs_sync_g4 | 50 | 46.80 [42.08, 52.23] | 2.55 [-0.46, 5.84] | 5 | 1 |
| gsm8k/dynamic | markov_w05_dist_int_vs_sync_g4 | 50 | 31.76 [27.23, 36.90] | 6.66 [4.44, 8.96] | 5 | 1 |
| gsm8k/pooled | picospec_vs_picospec_g2 | 50 | 24.82 [22.05, 27.52] | 5.35 [3.39, 7.41] | 14 | 1 |
| gsm8k/pooled | picospec_g8_vs_picospec_g2 | 50 | 38.90 [34.33, 43.77] | -8.86 [-13.17, -4.65] | 30 | 2 |
| gsm8k/pooled | sync_g4_vs_picospec_g2 | 50 | -8.56 [-9.74, -7.33] | -0.67 [-1.68, 0.35] | 14 | 1 |
| gsm8k/pooled | hf_default_vs_picospec_g2 | 50 | -14.75 [-16.84, -12.40] | -17.01 [-19.61, -14.37] | 25 | 1 |
| gsm8k/pooled | pipesd_vs_picospec_g2 | 50 | -4.86 [-7.71, -1.87] | -19.37 [-22.76, -15.84] | 26 | 1 |
| gsm8k/pooled | pearl_vs_picospec_g2 | 50 | 15.45 [13.32, 17.78] | 7.27 [5.88, 8.74] | 15 | 2 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec_g2 | 50 | 36.31 [32.25, 40.66] | 4.20 [1.68, 6.78] | 19 | 2 |
| gsm8k/pooled | markov_w05_dist_int_vs_picospec_g2 | 50 | 22.46 [18.68, 26.70] | 7.16 [5.25, 9.15] | 17 | 1 |
| gsm8k/pooled | picospec_g2_vs_picospec | 50 | -19.89 [-21.58, -18.07] | -5.66 [-8.01, -3.51] | 14 | 0 |
| gsm8k/pooled | picospec_g8_vs_picospec | 50 | 11.28 [8.85, 13.74] | -15.01 [-17.40, -12.52] | 27 | 1 |
| gsm8k/pooled | sync_g4_vs_picospec | 50 | -26.74 [-28.17, -25.37] | -6.37 [-8.56, -4.30] | 0 | 0 |
| gsm8k/pooled | hf_default_vs_picospec | 50 | -31.70 [-33.12, -30.05] | -23.63 [-26.23, -21.06] | 25 | 1 |
| gsm8k/pooled | pipesd_vs_picospec | 50 | -23.78 [-25.39, -21.93] | -26.12 [-28.27, -23.89] | 23 | 1 |
| gsm8k/pooled | pearl_vs_picospec | 50 | -7.51 [-9.12, -5.81] | 2.02 [0.49, 3.50] | 17 | 1 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec | 50 | 9.20 [7.48, 10.96] | -1.22 [-2.44, 0.06] | 16 | 2 |
| gsm8k/pooled | markov_w05_dist_int_vs_picospec | 50 | -1.89 [-3.96, 0.37] | 1.91 [0.51, 3.22] | 15 | 1 |
| gsm8k/pooled | picospec_g2_vs_picospec_g8 | 50 | -28.00 [-30.44, -25.56] | 8.13 [4.44, 11.64] | 30 | 0 |
| gsm8k/pooled | picospec_vs_picospec_g8 | 50 | -10.13 [-12.08, -8.13] | 13.05 [11.13, 14.82] | 27 | 0 |
| gsm8k/pooled | sync_g4_vs_picospec_g8 | 50 | -34.17 [-36.28, -32.09] | 7.52 [3.73, 10.97] | 27 | 0 |
| gsm8k/pooled | hf_default_vs_picospec_g8 | 50 | -38.62 [-40.22, -37.09] | -7.49 [-11.16, -4.10] | 30 | 1 |
| gsm8k/pooled | pipesd_vs_picospec_g8 | 50 | -31.50 [-32.75, -30.27] | -9.65 [-11.84, -7.53] | 31 | 1 |
| gsm8k/pooled | pearl_vs_picospec_g8 | 50 | -16.88 [-19.02, -14.58] | 14.81 [12.19, 17.33] | 27 | 1 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec_g8 | 50 | -1.87 [-3.38, -0.37] | 12.00 [10.44, 13.66] | 25 | 2 |
| gsm8k/pooled | markov_w05_dist_int_vs_picospec_g8 | 50 | -11.83 [-13.19, -10.49] | 14.71 [12.57, 16.73] | 22 | 1 |
| gsm8k/pooled | picospec_g2_vs_sync_g4 | 50 | 9.36 [7.91, 10.79] | 0.67 [-0.35, 1.65] | 14 | 0 |
| gsm8k/pooled | picospec_vs_sync_g4 | 50 | 36.50 [34.00, 39.22] | 5.99 [4.12, 7.88] | 0 | 0 |
| gsm8k/pooled | picospec_g8_vs_sync_g4 | 50 | 51.90 [47.25, 56.94] | -8.13 [-12.32, -3.87] | 27 | 1 |
| gsm8k/pooled | hf_default_vs_sync_g4 | 50 | -6.77 [-8.66, -4.82] | -16.23 [-18.61, -13.86] | 25 | 1 |
| gsm8k/pooled | pipesd_vs_sync_g4 | 50 | 4.04 [1.13, 7.12] | -18.57 [-22.05, -14.98] | 23 | 1 |
| gsm8k/pooled | pearl_vs_sync_g4 | 50 | 26.25 [23.86, 28.55] | 7.89 [6.42, 9.31] | 17 | 1 |
| gsm8k/pooled | markov_w0_dist_int_vs_sync_g4 | 50 | 49.06 [44.97, 53.81] | 4.84 [2.36, 7.54] | 16 | 2 |
| gsm8k/pooled | markov_w05_dist_int_vs_sync_g4 | 50 | 33.93 [29.90, 38.47] | 7.78 [5.81, 9.80] | 15 | 1 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
