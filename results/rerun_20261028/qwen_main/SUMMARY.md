# Progress probe: qwen_main

State: complete; 2970/2970 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | picospec_g2 | 110 | 30840 | 36.567 | 0.2984 | 7 | 46.28 |
| all/low | picospec | 110 | 30874 | 36.082 | 0.3593 | 7 | 47.33 |
| all/low | picospec_g8 | 110 | 30827 | 30.967 | 0.4470 | 6 | 41.84 |
| all/low | sync_g4 | 110 | 30874 | 25.774 | 0.2909 | 7 | 0.00 |
| all/low | hf_default | 110 | 30791 | 24.242 | 0.3664 | 6 | 0.00 |
| all/low | pipesd | 110 | 30754 | 32.985 | 0.3611 | 6 | 0.00 |
| all/low | pearl | 110 | 30788 | 32.249 | 0.2584 | 6 | 0.00 |
| all/low | markov_w0_dist_int | 110 | 30844 | 37.439 | 0.3289 | 6 | 53.10 |
| all/low | markov_w05_dist_int | 110 | 30731 | 37.006 | 0.3012 | 6 | 52.56 |
| all/high | picospec_g2 | 110 | 30692 | 14.158 | 0.4700 | 5 | 40.49 |
| all/high | picospec | 110 | 30805 | 17.957 | 0.4667 | 5 | 35.72 |
| all/high | picospec_g8 | 110 | 31038 | 19.972 | 0.5957 | 6 | 24.01 |
| all/high | sync_g4 | 110 | 30790 | 13.219 | 0.4591 | 5 | 0.00 |
| all/high | hf_default | 110 | 30830 | 12.958 | 0.5106 | 6 | 0.00 |
| all/high | pipesd | 110 | 30874 | 18.743 | 0.6255 | 5 | 0.00 |
| all/high | pearl | 110 | 30910 | 18.041 | 0.4805 | 5 | 0.00 |
| all/high | markov_w0_dist_int | 110 | 31012 | 20.909 | 0.5282 | 6 | 35.47 |
| all/high | markov_w05_dist_int | 110 | 30999 | 18.229 | 0.4520 | 5 | 43.19 |
| all/dynamic | picospec_g2 | 110 | 30607 | 24.299 | 0.3466 | 5 | 44.70 |
| all/dynamic | picospec | 110 | 30599 | 26.770 | 0.3968 | 5 | 43.00 |
| all/dynamic | picospec_g8 | 110 | 30616 | 25.300 | 0.5078 | 6 | 32.14 |
| all/dynamic | sync_g4 | 110 | 30627 | 19.137 | 0.3525 | 5 | 0.00 |
| all/dynamic | hf_default | 110 | 30635 | 17.701 | 0.4175 | 6 | 0.00 |
| all/dynamic | pipesd | 110 | 30643 | 24.446 | 0.4811 | 5 | 0.00 |
| all/dynamic | pearl | 110 | 30633 | 25.464 | 0.3594 | 5 | 0.00 |
| all/dynamic | markov_w0_dist_int | 110 | 30750 | 28.645 | 0.4042 | 5 | 45.56 |
| all/dynamic | markov_w05_dist_int | 110 | 30576 | 26.922 | 0.3572 | 6 | 48.75 |
| all/pooled | picospec_g2 | 330 | 92139 | 21.574 | 0.3716 | 17 | 43.68 |
| all/pooled | picospec | 330 | 92278 | 24.845 | 0.4076 | 17 | 41.45 |
| all/pooled | picospec_g8 | 330 | 92481 | 24.598 | 0.5170 | 18 | 31.04 |
| all/pooled | sync_g4 | 330 | 92291 | 18.000 | 0.3674 | 17 | 0.00 |
| all/pooled | hf_default | 330 | 92256 | 17.148 | 0.4316 | 18 | 0.00 |
| all/pooled | pipesd | 330 | 92271 | 24.072 | 0.4894 | 16 | 0.00 |
| all/pooled | pearl | 330 | 92331 | 23.852 | 0.3663 | 16 | 0.00 |
| all/pooled | markov_w0_dist_int | 330 | 92606 | 27.394 | 0.4206 | 17 | 42.95 |
| all/pooled | markov_w05_dist_int | 330 | 92306 | 25.174 | 0.3704 | 17 | 47.85 |
| mtbench/low | picospec_g2 | 30 | 7499 | 27.407 | 0.4006 | 6 | 27.77 |
| mtbench/low | picospec | 30 | 7516 | 23.991 | 0.5482 | 6 | 21.47 |
| mtbench/low | picospec_g8 | 30 | 7442 | 18.403 | 0.7580 | 5 | 12.08 |
| mtbench/low | sync_g4 | 30 | 7516 | 20.829 | 0.3696 | 6 | 0.00 |
| mtbench/low | hf_default | 30 | 7521 | 17.420 | 0.5129 | 5 | 0.00 |
| mtbench/low | pipesd | 30 | 7393 | 23.024 | 0.5263 | 5 | 0.00 |
| mtbench/low | pearl | 30 | 7514 | 27.278 | 0.3048 | 5 | 0.00 |
| mtbench/low | markov_w0_dist_int | 30 | 7481 | 26.874 | 0.4337 | 5 | 30.37 |
| mtbench/low | markov_w05_dist_int | 30 | 7397 | 26.912 | 0.3678 | 5 | 29.82 |
| mtbench/high | picospec_g2 | 30 | 7362 | 11.130 | 0.6064 | 4 | 21.97 |
| mtbench/high | picospec | 30 | 7398 | 11.994 | 0.7126 | 4 | 13.13 |
| mtbench/high | picospec_g8 | 30 | 7497 | 11.679 | 1.0327 | 5 | 4.98 |
| mtbench/high | sync_g4 | 30 | 7398 | 10.226 | 0.5967 | 4 | 0.00 |
| mtbench/high | hf_default | 30 | 7468 | 8.749 | 0.7452 | 5 | 0.00 |
| mtbench/high | pipesd | 30 | 7500 | 11.587 | 1.0342 | 4 | 0.00 |
| mtbench/high | pearl | 30 | 7511 | 11.750 | 0.7386 | 4 | 0.00 |
| mtbench/high | markov_w0_dist_int | 30 | 7462 | 13.052 | 0.8379 | 5 | 17.95 |
| mtbench/high | markov_w05_dist_int | 30 | 7429 | 11.291 | 0.6218 | 4 | 20.67 |
| mtbench/dynamic | picospec_g2 | 30 | 7439 | 18.345 | 0.4631 | 4 | 25.74 |
| mtbench/dynamic | picospec | 30 | 7416 | 17.722 | 0.6092 | 4 | 17.12 |
| mtbench/dynamic | picospec_g8 | 30 | 7446 | 14.601 | 0.8899 | 5 | 6.63 |
| mtbench/dynamic | sync_g4 | 30 | 7416 | 15.013 | 0.4547 | 4 | 0.00 |
| mtbench/dynamic | hf_default | 30 | 7506 | 12.037 | 0.5977 | 5 | 0.00 |
| mtbench/dynamic | pipesd | 30 | 7495 | 16.311 | 0.7340 | 4 | 0.00 |
| mtbench/dynamic | pearl | 30 | 7491 | 17.984 | 0.5073 | 4 | 0.00 |
| mtbench/dynamic | markov_w0_dist_int | 30 | 7424 | 18.898 | 0.5817 | 4 | 23.32 |
| mtbench/dynamic | markov_w05_dist_int | 30 | 7436 | 17.920 | 0.4586 | 4 | 25.38 |
| mtbench/pooled | picospec_g2 | 90 | 22300 | 16.634 | 0.4894 | 14 | 24.92 |
| mtbench/pooled | picospec | 90 | 22330 | 16.559 | 0.6230 | 14 | 16.60 |
| mtbench/pooled | picospec_g8 | 90 | 22385 | 14.384 | 0.8939 | 15 | 7.01 |
| mtbench/pooled | sync_g4 | 90 | 22330 | 14.148 | 0.4731 | 14 | 0.00 |
| mtbench/pooled | hf_default | 90 | 22495 | 11.784 | 0.6183 | 15 | 0.00 |
| mtbench/pooled | pipesd | 90 | 22388 | 15.679 | 0.7660 | 13 | 0.00 |
| mtbench/pooled | pearl | 90 | 22516 | 16.913 | 0.5169 | 13 | 0.00 |
| mtbench/pooled | markov_w0_dist_int | 90 | 22367 | 17.995 | 0.6177 | 14 | 21.91 |
| mtbench/pooled | markov_w05_dist_int | 90 | 22262 | 16.518 | 0.4829 | 13 | 25.13 |
| gsm8k/low | picospec_g2 | 50 | 13043 | 42.076 | 0.2560 | 0 | 54.40 |
| gsm8k/low | picospec | 50 | 13046 | 45.605 | 0.2810 | 0 | 59.67 |
| gsm8k/low | picospec_g8 | 50 | 13029 | 42.519 | 0.3219 | 0 | 58.50 |
| gsm8k/low | sync_g4 | 50 | 13046 | 28.824 | 0.2586 | 0 | 0.00 |
| gsm8k/low | hf_default | 50 | 13045 | 28.936 | 0.3126 | 0 | 0.00 |
| gsm8k/low | pipesd | 50 | 13064 | 40.153 | 0.2911 | 0 | 0.00 |
| gsm8k/low | pearl | 50 | 13043 | 34.857 | 0.2394 | 0 | 0.00 |
| gsm8k/low | markov_w0_dist_int | 50 | 13043 | 45.009 | 0.2800 | 0 | 63.11 |
| gsm8k/low | markov_w05_dist_int | 50 | 13081 | 43.673 | 0.2689 | 0 | 61.52 |
| gsm8k/high | picospec_g2 | 50 | 12978 | 16.009 | 0.4124 | 0 | 50.33 |
| gsm8k/high | picospec | 50 | 13017 | 22.416 | 0.3674 | 0 | 50.61 |
| gsm8k/high | picospec_g8 | 50 | 13011 | 28.318 | 0.4134 | 0 | 40.83 |
| gsm8k/high | sync_g4 | 50 | 13002 | 14.948 | 0.4052 | 0 | 0.00 |
| gsm8k/high | hf_default | 50 | 12967 | 16.254 | 0.4158 | 0 | 0.00 |
| gsm8k/high | pipesd | 50 | 13010 | 25.570 | 0.4466 | 0 | 0.00 |
| gsm8k/high | pearl | 50 | 13034 | 23.287 | 0.3721 | 0 | 0.00 |
| gsm8k/high | markov_w0_dist_int | 50 | 13090 | 27.976 | 0.3961 | 0 | 49.06 |
| gsm8k/high | markov_w05_dist_int | 50 | 13023 | 24.221 | 0.3689 | 0 | 53.25 |
| gsm8k/dynamic | picospec_g2 | 50 | 12898 | 27.154 | 0.3036 | 0 | 53.27 |
| gsm8k/dynamic | picospec | 50 | 12923 | 32.734 | 0.3135 | 0 | 56.30 |
| gsm8k/dynamic | picospec_g8 | 50 | 12973 | 35.232 | 0.3587 | 0 | 49.12 |
| gsm8k/dynamic | sync_g4 | 50 | 12951 | 21.237 | 0.3160 | 0 | 0.00 |
| gsm8k/dynamic | hf_default | 50 | 12892 | 21.635 | 0.3484 | 0 | 0.00 |
| gsm8k/dynamic | pipesd | 50 | 12905 | 30.063 | 0.3808 | 0 | 0.00 |
| gsm8k/dynamic | pearl | 50 | 12958 | 29.715 | 0.3019 | 0 | 0.00 |
| gsm8k/dynamic | markov_w0_dist_int | 50 | 13019 | 35.848 | 0.3307 | 0 | 56.75 |
| gsm8k/dynamic | markov_w05_dist_int | 50 | 12924 | 32.869 | 0.3111 | 0 | 58.13 |
| gsm8k/pooled | picospec_g2 | 150 | 38919 | 24.390 | 0.3239 | 0 | 52.61 |
| gsm8k/pooled | picospec | 150 | 38986 | 30.903 | 0.3206 | 0 | 55.26 |
| gsm8k/pooled | picospec_g8 | 150 | 39013 | 34.400 | 0.3647 | 0 | 48.40 |
| gsm8k/pooled | sync_g4 | 150 | 38999 | 20.183 | 0.3265 | 0 | 0.00 |
| gsm8k/pooled | hf_default | 150 | 38904 | 21.092 | 0.3589 | 0 | 0.00 |
| gsm8k/pooled | pipesd | 150 | 38979 | 30.852 | 0.3727 | 0 | 0.00 |
| gsm8k/pooled | pearl | 150 | 39035 | 28.493 | 0.3045 | 0 | 0.00 |
| gsm8k/pooled | markov_w0_dist_int | 150 | 39152 | 34.931 | 0.3357 | 0 | 55.45 |
| gsm8k/pooled | markov_w05_dist_int | 150 | 39028 | 31.720 | 0.3163 | 0 | 57.41 |
| humaneval/low | picospec_g2 | 30 | 10298 | 39.643 | 0.2776 | 1 | 50.38 |
| humaneval/low | picospec | 30 | 10312 | 40.231 | 0.3206 | 1 | 53.32 |
| humaneval/low | picospec_g8 | 30 | 10356 | 36.379 | 0.3807 | 1 | 49.29 |
| humaneval/low | sync_g4 | 30 | 10312 | 26.826 | 0.2743 | 1 | 0.00 |
| humaneval/low | hf_default | 30 | 10225 | 26.381 | 0.3274 | 1 | 0.00 |
| humaneval/low | pipesd | 30 | 10297 | 36.015 | 0.3311 | 1 | 0.00 |
| humaneval/low | pearl | 30 | 10231 | 33.538 | 0.2485 | 1 | 0.00 |
| humaneval/low | markov_w0_dist_int | 30 | 10320 | 40.362 | 0.3147 | 1 | 57.04 |
| humaneval/low | markov_w05_dist_int | 30 | 10253 | 40.042 | 0.2944 | 1 | 56.62 |
| humaneval/high | picospec_g2 | 30 | 10352 | 14.881 | 0.4453 | 1 | 44.70 |
| humaneval/high | picospec | 30 | 10390 | 20.061 | 0.4158 | 1 | 41.74 |
| humaneval/high | picospec_g8 | 30 | 10530 | 23.261 | 0.5097 | 1 | 29.83 |
| humaneval/high | sync_g4 | 30 | 10390 | 14.119 | 0.4284 | 1 | 0.00 |
| humaneval/high | hf_default | 30 | 10395 | 14.282 | 0.4603 | 1 | 0.00 |
| humaneval/high | pipesd | 30 | 10364 | 21.101 | 0.5542 | 1 | 0.00 |
| humaneval/high | pearl | 30 | 10365 | 20.152 | 0.4296 | 1 | 0.00 |
| humaneval/high | markov_w0_dist_int | 30 | 10460 | 23.582 | 0.4725 | 1 | 41.28 |
| humaneval/high | markov_w05_dist_int | 30 | 10547 | 20.889 | 0.4351 | 1 | 44.82 |
| humaneval/dynamic | picospec_g2 | 30 | 10270 | 27.089 | 0.3162 | 1 | 49.36 |
| humaneval/dynamic | picospec | 30 | 10260 | 31.110 | 0.3482 | 1 | 50.19 |
| humaneval/dynamic | picospec_g8 | 30 | 10197 | 30.718 | 0.4184 | 1 | 41.81 |
| humaneval/dynamic | sync_g4 | 30 | 10260 | 20.662 | 0.3248 | 1 | 0.00 |
| humaneval/dynamic | hf_default | 30 | 10237 | 20.023 | 0.3724 | 1 | 0.00 |
| humaneval/dynamic | pipesd | 30 | 10243 | 28.086 | 0.4224 | 1 | 0.00 |
| humaneval/dynamic | pearl | 30 | 10184 | 29.067 | 0.3238 | 1 | 0.00 |
| humaneval/dynamic | markov_w0_dist_int | 30 | 10307 | 32.467 | 0.3690 | 1 | 52.02 |
| humaneval/dynamic | markov_w05_dist_int | 30 | 10216 | 31.186 | 0.3419 | 2 | 52.49 |
| humaneval/pooled | picospec_g2 | 90 | 30920 | 23.169 | 0.3465 | 3 | 48.01 |
| humaneval/pooled | picospec | 90 | 30962 | 28.044 | 0.3617 | 3 | 47.92 |
| humaneval/pooled | picospec_g8 | 90 | 31083 | 29.068 | 0.4368 | 3 | 38.59 |
| humaneval/pooled | sync_g4 | 90 | 30962 | 19.150 | 0.3427 | 3 | 0.00 |
| humaneval/pooled | hf_default | 90 | 30857 | 18.969 | 0.3871 | 3 | 0.00 |
| humaneval/pooled | pipesd | 90 | 30904 | 27.067 | 0.4362 | 3 | 0.00 |
| humaneval/pooled | pearl | 90 | 30780 | 26.313 | 0.3344 | 3 | 0.00 |
| humaneval/pooled | markov_w0_dist_int | 90 | 31087 | 30.576 | 0.3858 | 3 | 48.76 |
| humaneval/pooled | markov_w05_dist_int | 90 | 31016 | 28.493 | 0.3579 | 4 | 50.70 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | picospec_vs_picospec_g2 | 110 | -1.33 [-3.71, 1.10] | -20.41 [-23.37, -17.40] | 11 | 0 |
| all/low | picospec_g8_vs_picospec_g2 | 110 | -15.32 [-19.02, -11.26] | -49.79 [-56.63, -42.79] | 31 | 0 |
| all/low | sync_g4_vs_picospec_g2 | 110 | -29.52 [-30.93, -28.08] | 2.52 [0.94, 4.14] | 11 | 0 |
| all/low | hf_default_vs_picospec_g2 | 110 | -33.71 [-35.67, -31.86] | -22.81 [-26.42, -19.76] | 23 | 0 |
| all/low | pipesd_vs_picospec_g2 | 110 | -9.80 [-11.38, -8.22] | -21.00 [-23.30, -18.79] | 13 | 0 |
| all/low | pearl_vs_picospec_g2 | 110 | -11.81 [-13.96, -9.43] | 13.40 [11.12, 15.77] | 14 | 0 |
| all/low | markov_w0_dist_int_vs_picospec_g2 | 110 | 2.39 [0.78, 4.04] | -10.22 [-11.94, -8.59] | 14 | 0 |
| all/low | markov_w05_dist_int_vs_picospec_g2 | 110 | 1.20 [-0.19, 2.63] | -0.95 [-3.47, 1.60] | 14 | 0 |
| all/low | picospec_g2_vs_picospec | 110 | 1.35 [-1.09, 3.85] | 16.95 [14.82, 18.94] | 11 | 0 |
| all/low | picospec_g8_vs_picospec | 110 | -14.18 [-16.21, -11.92] | -24.40 [-27.25, -21.37] | 27 | 0 |
| all/low | sync_g4_vs_picospec | 110 | -28.57 [-31.30, -25.58] | 19.04 [15.89, 22.14] | 0 | 0 |
| all/low | hf_default_vs_picospec | 110 | -32.81 [-34.65, -30.80] | -1.99 [-5.07, 1.23] | 18 | 0 |
| all/low | pipesd_vs_picospec | 110 | -8.58 [-10.02, -7.12] | -0.49 [-2.02, 1.05] | 16 | 0 |
| all/low | pearl_vs_picospec | 110 | -10.62 [-14.62, -6.19] | 28.08 [24.40, 31.66] | 16 | 0 |
| all/low | markov_w0_dist_int_vs_picospec | 110 | 3.76 [1.73, 5.79] | 8.46 [5.42, 11.37] | 16 | 0 |
| all/low | markov_w05_dist_int_vs_picospec | 110 | 2.56 [0.22, 4.80] | 16.16 [12.21, 20.01] | 19 | 0 |
| all/low | picospec_g2_vs_picospec_g8 | 110 | 18.09 [12.69, 23.49] | 33.24 [29.97, 36.16] | 31 | 1 |
| all/low | picospec_vs_picospec_g8 | 110 | 16.52 [13.53, 19.35] | 19.61 [17.61, 21.41] | 27 | 1 |
| all/low | sync_g4_vs_picospec_g8 | 110 | -16.77 [-21.69, -11.62] | 34.92 [30.94, 38.69] | 27 | 1 |
| all/low | hf_default_vs_picospec_g8 | 110 | -21.72 [-24.95, -18.23] | 18.01 [14.23, 21.75] | 32 | 0 |
| all/low | pipesd_vs_picospec_g8 | 110 | 6.52 [2.60, 10.28] | 19.22 [16.34, 21.86] | 38 | 0 |
| all/low | pearl_vs_picospec_g8 | 110 | 4.14 [-2.86, 11.54] | 42.19 [37.93, 46.15] | 35 | 0 |
| all/low | markov_w0_dist_int_vs_picospec_g8 | 110 | 20.90 [16.00, 25.71] | 26.41 [22.24, 30.10] | 36 | 0 |
| all/low | markov_w05_dist_int_vs_picospec_g8 | 110 | 19.50 [14.33, 24.61] | 32.60 [27.86, 36.95] | 35 | 0 |
| all/low | picospec_g2_vs_sync_g4 | 110 | 41.87 [39.05, 44.77] | -2.58 [-4.32, -0.95] | 11 | 0 |
| all/low | picospec_vs_sync_g4 | 110 | 39.99 [34.36, 45.57] | -23.52 [-28.43, -18.89] | 0 | 0 |
| all/low | picospec_g8_vs_sync_g4 | 110 | 20.15 [13.15, 27.70] | -53.66 [-63.11, -44.80] | 27 | 0 |
| all/low | hf_default_vs_sync_g4 | 110 | -5.94 [-9.58, -2.63] | -25.98 [-30.80, -21.96] | 18 | 0 |
| all/low | pipesd_vs_sync_g4 | 110 | 27.98 [24.05, 31.95] | -24.13 [-28.15, -20.25] | 16 | 0 |
| all/low | pearl_vs_sync_g4 | 110 | 25.12 [23.42, 26.90] | 11.17 [9.81, 12.50] | 16 | 0 |
| all/low | markov_w0_dist_int_vs_sync_g4 | 110 | 45.26 [41.28, 49.21] | -13.07 [-15.07, -10.96] | 16 | 0 |
| all/low | markov_w05_dist_int_vs_sync_g4 | 110 | 43.58 [40.16, 47.05] | -3.56 [-5.35, -1.73] | 19 | 0 |
| all/high | picospec_vs_picospec_g2 | 110 | 26.84 [23.01, 30.70] | 0.71 [-2.56, 3.92] | 16 | 0 |
| all/high | picospec_g8_vs_picospec_g2 | 110 | 41.06 [32.86, 49.76] | -26.74 [-34.74, -18.93] | 32 | 1 |
| all/high | sync_g4_vs_picospec_g2 | 110 | -6.63 [-7.51, -5.78] | 2.33 [1.60, 3.03] | 15 | 0 |
| all/high | hf_default_vs_picospec_g2 | 110 | -8.48 [-11.86, -5.20] | -8.64 [-12.39, -5.26] | 23 | 1 |
| all/high | pipesd_vs_picospec_g2 | 110 | 32.38 [26.15, 38.98] | -33.07 [-40.40, -26.17] | 15 | 0 |
| all/high | pearl_vs_picospec_g2 | 110 | 27.43 [22.64, 32.38] | -2.22 [-6.03, 1.50] | 22 | 0 |
| all/high | markov_w0_dist_int_vs_picospec_g2 | 110 | 47.69 [41.11, 54.39] | -12.37 [-17.31, -7.68] | 19 | 1 |
| all/high | markov_w05_dist_int_vs_picospec_g2 | 110 | 28.76 [22.88, 34.78] | 3.82 [2.34, 5.40] | 14 | 0 |
| all/high | picospec_g2_vs_picospec | 110 | -21.16 [-23.49, -18.71] | -0.71 [-4.08, 2.49] | 16 | 0 |
| all/high | picospec_g8_vs_picospec | 110 | 11.22 [7.89, 14.88] | -27.64 [-31.43, -23.68] | 24 | 1 |
| all/high | sync_g4_vs_picospec | 110 | -26.39 [-28.36, -24.44] | 1.63 [-1.51, 4.57] | 1 | 0 |
| all/high | hf_default_vs_picospec | 110 | -27.84 [-29.38, -26.30] | -9.42 [-11.88, -6.96] | 21 | 1 |
| all/high | pipesd_vs_picospec | 110 | 4.37 [2.15, 6.87] | -34.03 [-37.19, -30.75] | 18 | 0 |
| all/high | pearl_vs_picospec | 110 | 0.47 [-1.11, 2.25] | -2.95 [-4.25, -1.62] | 19 | 0 |
| all/high | markov_w0_dist_int_vs_picospec | 110 | 16.44 [14.45, 18.74] | -13.18 [-14.87, -11.26] | 17 | 1 |
| all/high | markov_w05_dist_int_vs_picospec | 110 | 1.51 [-0.72, 3.98] | 3.13 [0.75, 5.50] | 20 | 0 |
| all/high | picospec_g2_vs_picospec_g8 | 110 | -29.11 [-33.23, -24.74] | 21.10 [15.92, 25.78] | 32 | 0 |
| all/high | picospec_vs_picospec_g8 | 110 | -10.09 [-12.95, -7.32] | 21.66 [19.15, 23.91] | 24 | 0 |
| all/high | sync_g4_vs_picospec_g8 | 110 | -33.81 [-37.46, -30.08] | 22.94 [17.92, 27.36] | 24 | 0 |
| all/high | hf_default_vs_picospec_g8 | 110 | -35.12 [-37.46, -32.73] | 14.28 [10.59, 17.84] | 31 | 0 |
| all/high | pipesd_vs_picospec_g8 | 110 | -6.15 [-7.92, -4.40] | -5.00 [-6.79, -3.27] | 29 | 0 |
| all/high | pearl_vs_picospec_g8 | 110 | -9.67 [-12.01, -7.39] | 19.34 [16.99, 21.60] | 32 | 0 |
| all/high | markov_w0_dist_int_vs_picospec_g8 | 110 | 4.70 [2.43, 6.85] | 11.33 [9.01, 13.48] | 25 | 0 |
| all/high | markov_w05_dist_int_vs_picospec_g8 | 110 | -8.72 [-10.67, -6.90] | 24.11 [19.95, 27.79] | 26 | 0 |
| all/high | picospec_g2_vs_sync_g4 | 110 | 7.10 [6.14, 8.12] | -2.39 [-3.13, -1.62] | 15 | 0 |
| all/high | picospec_vs_sync_g4 | 110 | 35.84 [32.35, 39.58] | -1.66 [-4.79, 1.49] | 1 | 0 |
| all/high | picospec_g8_vs_sync_g4 | 110 | 51.08 [43.01, 59.91] | -29.76 [-37.66, -21.83] | 24 | 1 |
| all/high | hf_default_vs_sync_g4 | 110 | -1.98 [-5.38, 1.37] | -11.23 [-15.14, -7.73] | 21 | 1 |
| all/high | pipesd_vs_sync_g4 | 110 | 41.78 [35.59, 48.60] | -36.25 [-43.53, -29.15] | 18 | 0 |
| all/high | pearl_vs_sync_g4 | 110 | 36.48 [31.80, 41.41] | -4.66 [-8.46, -1.04] | 20 | 0 |
| all/high | markov_w0_dist_int_vs_sync_g4 | 110 | 58.17 [51.88, 65.10] | -15.05 [-19.87, -10.25] | 18 | 1 |
| all/high | markov_w05_dist_int_vs_sync_g4 | 110 | 37.90 [32.07, 44.18] | 1.53 [-0.08, 3.36] | 19 | 0 |
| all/dynamic | picospec_vs_picospec_g2 | 110 | 10.17 [7.16, 13.37] | -14.48 [-17.60, -11.39] | 17 | 0 |
| all/dynamic | picospec_g8_vs_picospec_g2 | 110 | 4.12 [-1.71, 10.48] | -46.50 [-54.96, -38.06] | 30 | 1 |
| all/dynamic | sync_g4_vs_picospec_g2 | 110 | -21.24 [-23.03, -19.56] | -1.72 [-3.08, -0.44] | 16 | 0 |
| all/dynamic | hf_default_vs_picospec_g2 | 110 | -27.15 [-29.46, -24.80] | -20.47 [-23.49, -17.67] | 25 | 1 |
| all/dynamic | pipesd_vs_picospec_g2 | 110 | 0.61 [-2.66, 4.08] | -38.81 [-43.08, -34.42] | 14 | 0 |
| all/dynamic | pearl_vs_picospec_g2 | 110 | 4.80 [3.04, 6.60] | -3.70 [-5.15, -2.29] | 24 | 0 |
| all/dynamic | markov_w0_dist_int_vs_picospec_g2 | 110 | 17.89 [14.40, 21.70] | -16.61 [-19.10, -14.07] | 11 | 0 |
| all/dynamic | markov_w05_dist_int_vs_picospec_g2 | 110 | 10.80 [7.53, 14.27] | -3.08 [-4.76, -1.44] | 13 | 1 |
| all/dynamic | picospec_g2_vs_picospec | 110 | -9.23 [-11.79, -6.68] | 12.65 [10.22, 14.97] | 17 | 0 |
| all/dynamic | picospec_g8_vs_picospec | 110 | -5.49 [-8.85, -1.93] | -27.97 [-32.27, -23.60] | 25 | 1 |
| all/dynamic | sync_g4_vs_picospec | 110 | -28.51 [-30.90, -25.94] | 11.15 [8.05, 14.16] | 2 | 0 |
| all/dynamic | hf_default_vs_picospec | 110 | -33.88 [-35.34, -32.32] | -5.22 [-7.77, -2.72] | 19 | 1 |
| all/dynamic | pipesd_vs_picospec | 110 | -8.68 [-10.32, -7.02] | -21.25 [-23.43, -19.00] | 17 | 0 |
| all/dynamic | pearl_vs_picospec | 110 | -4.88 [-6.49, -3.21] | 9.42 [7.71, 11.05] | 18 | 0 |
| all/dynamic | markov_w0_dist_int_vs_picospec | 110 | 7.00 [5.32, 8.75] | -1.85 [-4.26, 0.66] | 21 | 0 |
| all/dynamic | markov_w05_dist_int_vs_picospec | 110 | 0.57 [-0.92, 2.16] | 9.97 [6.71, 13.28] | 14 | 1 |
| all/dynamic | picospec_g2_vs_picospec_g8 | 110 | -3.96 [-9.49, 1.74] | 31.74 [27.57, 35.47] | 30 | 0 |
| all/dynamic | picospec_vs_picospec_g8 | 110 | 5.81 [1.97, 9.71] | 21.86 [19.09, 24.40] | 25 | 0 |
| all/dynamic | sync_g4_vs_picospec_g8 | 110 | -24.36 [-28.98, -19.50] | 30.57 [25.79, 34.89] | 25 | 0 |
| all/dynamic | hf_default_vs_picospec_g8 | 110 | -30.04 [-32.85, -27.10] | 17.77 [13.81, 21.61] | 32 | 0 |
| all/dynamic | pipesd_vs_picospec_g8 | 110 | -3.37 [-6.70, 0.14] | 5.25 [1.63, 8.67] | 32 | 0 |
| all/dynamic | pearl_vs_picospec_g8 | 110 | 0.65 [-4.00, 5.51] | 29.22 [25.58, 32.44] | 32 | 0 |
| all/dynamic | markov_w0_dist_int_vs_picospec_g8 | 110 | 13.22 [8.94, 17.53] | 20.41 [16.30, 24.13] | 29 | 0 |
| all/dynamic | markov_w05_dist_int_vs_picospec_g8 | 110 | 6.41 [2.48, 10.66] | 29.64 [24.64, 33.93] | 30 | 1 |
| all/dynamic | picospec_g2_vs_sync_g4 | 110 | 26.97 [24.31, 29.91] | 1.69 [0.43, 2.99] | 16 | 0 |
| all/dynamic | picospec_vs_sync_g4 | 110 | 39.88 [35.03, 44.72] | -12.55 [-16.49, -8.76] | 2 | 0 |
| all/dynamic | picospec_g8_vs_sync_g4 | 110 | 32.20 [24.22, 40.80] | -44.03 [-53.59, -34.74] | 25 | 1 |
| all/dynamic | hf_default_vs_sync_g4 | 110 | -7.51 [-10.83, -4.06] | -18.43 [-22.23, -15.01] | 20 | 1 |
| all/dynamic | pipesd_vs_sync_g4 | 110 | 27.74 [23.32, 32.38] | -36.47 [-41.89, -31.14] | 18 | 0 |
| all/dynamic | pearl_vs_sync_g4 | 110 | 33.06 [29.54, 36.68] | -1.95 [-4.06, 0.04] | 17 | 0 |
| all/dynamic | markov_w0_dist_int_vs_sync_g4 | 110 | 49.68 [44.36, 55.26] | -14.64 [-18.03, -11.29] | 20 | 0 |
| all/dynamic | markov_w05_dist_int_vs_sync_g4 | 110 | 40.68 [35.68, 45.98] | -1.34 [-2.99, 0.33] | 15 | 1 |
| all/pooled | picospec_vs_picospec_g2 | 110 | 15.16 [12.05, 18.29] | -9.69 [-12.83, -6.63] | 44 | 0 |
| all/pooled | picospec_g8_vs_picospec_g2 | 110 | 14.02 [8.03, 20.62] | -39.14 [-47.01, -31.47] | 93 | 2 |
| all/pooled | sync_g4_vs_picospec_g2 | 110 | -16.57 [-17.31, -15.82] | 1.11 [0.29, 1.93] | 42 | 0 |
| all/pooled | hf_default_vs_picospec_g2 | 110 | -20.52 [-22.89, -18.14] | -16.15 [-19.36, -13.32] | 71 | 2 |
| all/pooled | pipesd_vs_picospec_g2 | 110 | 11.58 [7.93, 15.36] | -31.71 [-36.47, -26.98] | 42 | 0 |
| all/pooled | pearl_vs_picospec_g2 | 110 | 10.56 [8.73, 12.45] | 1.43 [0.01, 2.88] | 60 | 0 |
| all/pooled | markov_w0_dist_int_vs_picospec_g2 | 110 | 26.98 [23.21, 30.92] | -13.20 [-15.75, -10.57] | 44 | 1 |
| all/pooled | markov_w05_dist_int_vs_picospec_g2 | 110 | 16.69 [12.92, 20.46] | 0.30 [-0.83, 1.45] | 41 | 1 |
| all/pooled | picospec_g2_vs_picospec | 110 | -13.17 [-15.46, -10.75] | 8.83 [6.22, 11.37] | 44 | 0 |
| all/pooled | picospec_g8_vs_picospec | 110 | -0.99 [-3.78, 2.07] | -26.85 [-30.27, -23.12] | 76 | 2 |
| all/pooled | sync_g4_vs_picospec | 110 | -27.55 [-29.68, -25.24] | 9.85 [6.81, 12.87] | 3 | 0 |
| all/pooled | hf_default_vs_picospec | 110 | -30.98 [-32.32, -29.59] | -5.89 [-8.36, -3.41] | 58 | 2 |
| all/pooled | pipesd_vs_picospec | 110 | -3.11 [-4.26, -1.91] | -20.07 [-21.60, -18.43] | 51 | 0 |
| all/pooled | pearl_vs_picospec | 110 | -4.00 [-5.35, -2.59] | 10.14 [8.62, 11.66] | 53 | 0 |
| all/pooled | markov_w0_dist_int_vs_picospec | 110 | 10.26 [9.24, 11.40] | -3.20 [-4.76, -1.51] | 54 | 1 |
| all/pooled | markov_w05_dist_int_vs_picospec | 110 | 1.33 [0.15, 2.61] | 9.11 [6.10, 12.10] | 53 | 1 |
| all/pooled | picospec_g2_vs_picospec_g8 | 110 | -12.29 [-17.10, -7.43] | 28.13 [23.94, 31.98] | 93 | 1 |
| all/pooled | picospec_vs_picospec_g8 | 110 | 1.00 [-2.02, 3.93] | 21.17 [18.78, 23.23] | 76 | 1 |
| all/pooled | sync_g4_vs_picospec_g8 | 110 | -26.82 [-31.07, -22.51] | 28.93 [24.35, 33.11] | 76 | 1 |
| all/pooled | hf_default_vs_picospec_g8 | 110 | -30.29 [-32.88, -27.62] | 16.52 [12.71, 20.09] | 95 | 0 |
| all/pooled | pipesd_vs_picospec_g8 | 110 | -2.14 [-4.68, 0.34] | 5.34 [2.91, 7.60] | 99 | 0 |
| all/pooled | pearl_vs_picospec_g8 | 110 | -3.03 [-7.01, 0.88] | 29.16 [25.93, 32.04] | 99 | 0 |
| all/pooled | markov_w0_dist_int_vs_picospec_g8 | 110 | 11.37 [8.05, 14.47] | 18.64 [15.27, 21.62] | 90 | 0 |
| all/pooled | markov_w05_dist_int_vs_picospec_g8 | 110 | 2.34 [-0.66, 5.23] | 28.35 [23.82, 32.33] | 91 | 1 |
| all/pooled | picospec_g2_vs_sync_g4 | 110 | 19.86 [18.79, 20.94] | -1.12 [-1.97, -0.29] | 42 | 0 |
| all/pooled | picospec_vs_sync_g4 | 110 | 38.03 [33.76, 42.21] | -10.92 [-14.77, -7.31] | 3 | 0 |
| all/pooled | picospec_g8_vs_sync_g4 | 110 | 36.66 [29.05, 45.07] | -40.70 [-49.51, -32.18] | 76 | 2 |
| all/pooled | hf_default_vs_sync_g4 | 110 | -4.73 [-8.08, -1.56] | -17.45 [-21.51, -13.91] | 59 | 2 |
| all/pooled | pipesd_vs_sync_g4 | 110 | 33.74 [28.88, 38.82] | -33.19 [-38.79, -27.60] | 52 | 0 |
| all/pooled | pearl_vs_sync_g4 | 110 | 32.51 [29.78, 35.34] | 0.33 [-1.65, 2.24] | 53 | 0 |
| all/pooled | markov_w0_dist_int_vs_sync_g4 | 110 | 52.19 [47.10, 57.61] | -14.47 [-17.75, -11.12] | 54 | 1 |
| all/pooled | markov_w05_dist_int_vs_sync_g4 | 110 | 39.86 [35.04, 44.83] | -0.81 [-2.20, 0.58] | 53 | 1 |
| mtbench/low | picospec_vs_picospec_g2 | 30 | -12.46 [-15.16, -9.90] | -36.84 [-40.61, -33.07] | 7 | 0 |
| mtbench/low | picospec_g8_vs_picospec_g2 | 30 | -32.85 [-35.83, -29.63] | -89.19 [-97.12, -80.90] | 14 | 0 |
| mtbench/low | sync_g4_vs_picospec_g2 | 30 | -24.00 [-26.22, -22.12] | 7.75 [5.22, 9.76] | 7 | 0 |
| mtbench/low | hf_default_vs_picospec_g2 | 30 | -36.44 [-40.44, -32.04] | -28.02 [-36.78, -19.45] | 13 | 0 |
| mtbench/low | pipesd_vs_picospec_g2 | 30 | -15.99 [-18.50, -13.85] | -31.37 [-35.96, -27.62] | 7 | 0 |
| mtbench/low | pearl_vs_picospec_g2 | 30 | -0.47 [-4.66, 3.28] | 23.93 [20.53, 26.63] | 10 | 0 |
| mtbench/low | markov_w0_dist_int_vs_picospec_g2 | 30 | -1.94 [-4.31, 0.34] | -8.25 [-12.08, -4.99] | 9 | 0 |
| mtbench/low | markov_w05_dist_int_vs_picospec_g2 | 30 | -1.81 [-3.95, 0.48] | 8.19 [3.19, 12.36] | 6 | 0 |
| mtbench/low | picospec_g2_vs_picospec | 30 | 14.24 [10.98, 17.87] | 26.92 [24.85, 28.88] | 7 | 0 |
| mtbench/low | picospec_g8_vs_picospec | 30 | -23.29 [-24.93, -21.52] | -38.25 [-40.86, -35.44] | 12 | 0 |
| mtbench/low | sync_g4_vs_picospec | 30 | -13.18 [-16.97, -9.82] | 32.58 [29.53, 34.83] | 0 | 0 |
| mtbench/low | hf_default_vs_picospec | 30 | -27.39 [-31.82, -22.35] | 6.45 [-0.54, 13.33] | 8 | 0 |
| mtbench/low | pipesd_vs_picospec | 30 | -4.03 [-6.80, -1.24] | 4.00 [0.87, 7.05] | 8 | 0 |
| mtbench/low | pearl_vs_picospec | 30 | 13.70 [6.61, 20.12] | 44.41 [40.62, 47.39] | 10 | 0 |
| mtbench/low | markov_w0_dist_int_vs_picospec | 30 | 12.02 [8.18, 15.74] | 20.90 [16.44, 24.66] | 9 | 0 |
| mtbench/low | markov_w05_dist_int_vs_picospec | 30 | 12.17 [8.20, 16.44] | 32.91 [27.69, 37.31] | 11 | 0 |
| mtbench/low | picospec_g2_vs_picospec_g8 | 30 | 48.93 [42.11, 55.83] | 47.14 [44.72, 49.27] | 14 | 1 |
| mtbench/low | picospec_vs_picospec_g8 | 30 | 30.36 [27.43, 33.20] | 27.67 [26.17, 29.01] | 12 | 1 |
| mtbench/low | sync_g4_vs_picospec_g8 | 30 | 13.18 [6.21, 19.33] | 51.24 [48.18, 53.48] | 12 | 1 |
| mtbench/low | hf_default_vs_picospec_g8 | 30 | -5.34 [-11.83, 2.05] | 32.33 [26.61, 37.92] | 11 | 0 |
| mtbench/low | pipesd_vs_picospec_g8 | 30 | 25.11 [19.83, 30.40] | 30.56 [27.50, 33.48] | 17 | 0 |
| mtbench/low | pearl_vs_picospec_g8 | 30 | 48.23 [36.26, 59.32] | 59.79 [56.27, 62.50] | 18 | 0 |
| mtbench/low | markov_w0_dist_int_vs_picospec_g8 | 30 | 46.03 [38.24, 53.38] | 42.78 [38.49, 46.34] | 18 | 0 |
| mtbench/low | markov_w05_dist_int_vs_picospec_g8 | 30 | 46.24 [38.35, 54.06] | 51.47 [46.64, 55.34] | 17 | 0 |
| mtbench/low | picospec_g2_vs_sync_g4 | 30 | 31.58 [28.40, 35.54] | -8.40 [-10.82, -5.50] | 7 | 0 |
| mtbench/low | picospec_vs_sync_g4 | 30 | 15.18 [10.89, 20.44] | -48.33 [-53.43, -41.90] | 0 | 0 |
| mtbench/low | picospec_g8_vs_sync_g4 | 30 | -11.65 [-16.20, -5.85] | -105.08 [-114.98, -92.96] | 12 | 0 |
| mtbench/low | hf_default_vs_sync_g4 | 30 | -16.37 [-21.99, -10.38] | -38.77 [-49.87, -28.64] | 8 | 0 |
| mtbench/low | pipesd_vs_sync_g4 | 30 | 10.54 [6.11, 15.11] | -42.41 [-49.01, -36.10] | 8 | 0 |
| mtbench/low | pearl_vs_sync_g4 | 30 | 30.96 [27.29, 34.88] | 17.55 [15.01, 20.21] | 10 | 0 |
| mtbench/low | markov_w0_dist_int_vs_sync_g4 | 30 | 29.02 [25.49, 32.59] | -17.34 [-20.63, -13.70] | 9 | 0 |
| mtbench/low | markov_w05_dist_int_vs_sync_g4 | 30 | 29.20 [25.57, 32.59] | 0.48 [-3.48, 4.53] | 11 | 0 |
| mtbench/high | picospec_vs_picospec_g2 | 30 | 7.77 [4.64, 11.39] | -17.53 [-21.35, -13.34] | 8 | 0 |
| mtbench/high | picospec_g8_vs_picospec_g2 | 30 | 4.93 [-0.67, 11.76] | -70.32 [-79.62, -59.85] | 13 | 1 |
| mtbench/high | sync_g4_vs_picospec_g2 | 30 | -8.12 [-9.79, -6.54] | 1.58 [-0.09, 3.05] | 8 | 0 |
| mtbench/high | hf_default_vs_picospec_g2 | 30 | -21.39 [-25.60, -16.81] | -22.90 [-30.15, -15.96] | 12 | 1 |
| mtbench/high | pipesd_vs_picospec_g2 | 30 | 4.11 [0.18, 9.35] | -70.56 [-77.23, -62.19] | 6 | 0 |
| mtbench/high | pearl_vs_picospec_g2 | 30 | 5.57 [1.04, 10.73] | -21.82 [-26.80, -16.60] | 11 | 0 |
| mtbench/high | markov_w0_dist_int_vs_picospec_g2 | 30 | 17.27 [12.70, 22.39] | -38.18 [-43.24, -32.42] | 8 | 1 |
| mtbench/high | markov_w05_dist_int_vs_picospec_g2 | 30 | 1.45 [-2.30, 5.91] | -2.55 [-3.88, -1.04] | 3 | 0 |
| mtbench/high | picospec_g2_vs_picospec | 30 | -7.21 [-10.23, -4.44] | 14.92 [11.77, 17.59] | 8 | 0 |
| mtbench/high | picospec_g8_vs_picospec | 30 | -2.63 [-5.59, 0.97] | -44.92 [-48.58, -40.64] | 10 | 1 |
| mtbench/high | sync_g4_vs_picospec | 30 | -14.74 [-16.73, -12.96] | 16.26 [13.70, 18.26] | 0 | 0 |
| mtbench/high | hf_default_vs_picospec | 30 | -27.05 [-30.67, -23.16] | -4.57 [-10.80, 1.39] | 9 | 1 |
| mtbench/high | pipesd_vs_picospec | 30 | -3.40 [-5.82, -0.33] | -45.12 [-48.37, -41.21] | 7 | 0 |
| mtbench/high | pearl_vs_picospec | 30 | -2.04 [-4.80, 1.19] | -3.65 [-6.07, -1.08] | 10 | 0 |
| mtbench/high | markov_w0_dist_int_vs_picospec | 30 | 8.82 [6.33, 11.48] | -17.57 [-20.30, -13.97] | 9 | 1 |
| mtbench/high | markov_w05_dist_int_vs_picospec | 30 | -5.86 [-8.16, -3.12] | 12.75 [9.48, 15.78] | 7 | 0 |
| mtbench/high | picospec_g2_vs_picospec_g8 | 30 | -4.70 [-10.52, 0.67] | 41.29 [37.44, 44.33] | 13 | 0 |
| mtbench/high | picospec_vs_picospec_g8 | 30 | 2.70 [-0.96, 5.92] | 30.99 [28.90, 32.70] | 10 | 0 |
| mtbench/high | sync_g4_vs_picospec_g8 | 30 | -12.44 [-16.96, -8.56] | 42.22 [38.85, 44.73] | 10 | 0 |
| mtbench/high | hf_default_vs_picospec_g8 | 30 | -25.08 [-29.34, -20.54] | 27.84 [22.73, 32.55] | 12 | 0 |
| mtbench/high | pipesd_vs_picospec_g8 | 30 | -0.79 [-3.66, 1.94] | -0.14 [-3.00, 2.80] | 14 | 0 |
| mtbench/high | pearl_vs_picospec_g8 | 30 | 0.61 [-1.64, 2.97] | 28.48 [26.65, 30.27] | 12 | 0 |
| mtbench/high | markov_w0_dist_int_vs_picospec_g8 | 30 | 11.76 [8.45, 14.81] | 18.87 [15.90, 21.81] | 10 | 0 |
| mtbench/high | markov_w05_dist_int_vs_picospec_g8 | 30 | -3.32 [-6.23, -0.41] | 39.79 [36.04, 42.86] | 12 | 0 |
| mtbench/high | picospec_g2_vs_sync_g4 | 30 | 8.84 [7.00, 10.86] | -1.61 [-3.15, 0.09] | 8 | 0 |
| mtbench/high | picospec_vs_sync_g4 | 30 | 17.29 [14.89, 20.09] | -19.42 [-22.34, -15.87] | 0 | 0 |
| mtbench/high | picospec_g8_vs_sync_g4 | 30 | 14.21 [9.36, 20.43] | -73.06 [-80.93, -63.52] | 10 | 1 |
| mtbench/high | hf_default_vs_sync_g4 | 30 | -14.44 [-19.17, -9.46] | -24.88 [-32.91, -17.16] | 9 | 1 |
| mtbench/high | pipesd_vs_sync_g4 | 30 | 13.31 [9.31, 18.25] | -73.30 [-80.05, -65.33] | 7 | 0 |
| mtbench/high | pearl_vs_sync_g4 | 30 | 14.90 [11.09, 19.52] | -23.78 [-27.90, -19.18] | 10 | 0 |
| mtbench/high | markov_w0_dist_int_vs_sync_g4 | 30 | 27.64 [23.62, 31.98] | -40.41 [-44.96, -35.05] | 9 | 1 |
| mtbench/high | markov_w05_dist_int_vs_sync_g4 | 30 | 10.42 [6.85, 14.52] | -4.20 [-6.18, -2.07] | 7 | 0 |
| mtbench/dynamic | picospec_vs_picospec_g2 | 30 | -3.39 [-6.52, -0.45] | -31.56 [-35.41, -27.83] | 8 | 0 |
| mtbench/dynamic | picospec_g8_vs_picospec_g2 | 30 | -20.41 [-24.87, -15.25] | -92.17 [-101.87, -81.45] | 12 | 1 |
| mtbench/dynamic | sync_g4_vs_picospec_g2 | 30 | -18.16 [-21.34, -15.39] | 1.81 [-0.35, 3.89] | 8 | 0 |
| mtbench/dynamic | hf_default_vs_picospec_g2 | 30 | -34.38 [-37.15, -31.38] | -29.07 [-34.71, -23.42] | 10 | 1 |
| mtbench/dynamic | pipesd_vs_picospec_g2 | 30 | -11.09 [-14.07, -7.70] | -58.51 [-63.94, -52.71] | 4 | 0 |
| mtbench/dynamic | pearl_vs_picospec_g2 | 30 | -1.97 [-3.91, -0.14] | -9.54 [-11.57, -7.74] | 14 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_picospec_g2 | 30 | 3.01 [0.94, 5.14] | -25.62 [-29.69, -21.50] | 3 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_picospec_g2 | 30 | -2.31 [-4.75, 0.22] | 0.97 [-1.88, 3.76] | 4 | 0 |
| mtbench/dynamic | picospec_g2_vs_picospec | 30 | 3.51 [0.46, 6.97] | 23.99 [21.77, 26.15] | 8 | 0 |
| mtbench/dynamic | picospec_g8_vs_picospec | 30 | -17.61 [-21.17, -13.65] | -46.08 [-52.35, -40.33] | 10 | 1 |
| mtbench/dynamic | sync_g4_vs_picospec | 30 | -15.29 [-18.46, -12.25] | 25.36 [22.90, 27.48] | 1 | 0 |
| mtbench/dynamic | hf_default_vs_picospec | 30 | -32.08 [-34.83, -28.64] | 1.89 [-2.81, 7.00] | 6 | 1 |
| mtbench/dynamic | pipesd_vs_picospec | 30 | -7.96 [-10.61, -5.25] | -20.49 [-24.96, -15.80] | 6 | 0 |
| mtbench/dynamic | pearl_vs_picospec | 30 | 1.48 [-0.88, 4.27] | 16.73 [14.76, 18.91] | 9 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_picospec | 30 | 6.63 [3.59, 10.08] | 4.51 [-0.57, 9.75] | 10 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_picospec | 30 | 1.12 [-2.06, 4.51] | 24.72 [20.92, 28.53] | 7 | 0 |
| mtbench/dynamic | picospec_g2_vs_picospec_g8 | 30 | 25.64 [17.99, 33.10] | 47.96 [44.89, 50.46] | 12 | 0 |
| mtbench/dynamic | picospec_vs_picospec_g8 | 30 | 21.38 [15.81, 26.85] | 31.54 [28.74, 34.36] | 10 | 0 |
| mtbench/dynamic | sync_g4_vs_picospec_g8 | 30 | 2.82 [-3.24, 8.21] | 48.90 [45.47, 51.62] | 11 | 0 |
| mtbench/dynamic | hf_default_vs_picospec_g8 | 30 | -17.56 [-22.15, -12.22] | 32.84 [28.34, 37.16] | 11 | 0 |
| mtbench/dynamic | pipesd_vs_picospec_g8 | 30 | 11.71 [7.04, 16.54] | 17.52 [13.52, 21.34] | 13 | 0 |
| mtbench/dynamic | pearl_vs_picospec_g8 | 30 | 23.17 [16.16, 30.08] | 43.00 [39.91, 45.75] | 16 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_picospec_g8 | 30 | 29.43 [21.59, 37.48] | 34.63 [29.59, 39.06] | 12 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_picospec_g8 | 30 | 22.73 [15.01, 30.05] | 48.47 [44.31, 51.88] | 13 | 0 |
| mtbench/dynamic | picospec_g2_vs_sync_g4 | 30 | 22.19 [18.18, 27.13] | -1.84 [-4.04, 0.34] | 8 | 0 |
| mtbench/dynamic | picospec_vs_sync_g4 | 30 | 18.05 [13.96, 22.64] | -33.97 [-37.90, -29.70] | 1 | 0 |
| mtbench/dynamic | picospec_g8_vs_sync_g4 | 30 | -2.74 [-7.59, 3.35] | -95.71 [-106.70, -83.40] | 11 | 1 |
| mtbench/dynamic | hf_default_vs_sync_g4 | 30 | -19.82 [-24.21, -14.74] | -31.44 [-38.68, -24.16] | 6 | 1 |
| mtbench/dynamic | pipesd_vs_sync_g4 | 30 | 8.65 [4.43, 13.62] | -61.42 [-69.24, -53.33] | 6 | 0 |
| mtbench/dynamic | pearl_vs_sync_g4 | 30 | 19.79 [15.79, 24.62] | -11.56 [-13.61, -9.26] | 9 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_sync_g4 | 30 | 25.88 [21.38, 30.79] | -27.93 [-33.62, -22.01] | 10 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_sync_g4 | 30 | 19.37 [14.25, 25.12] | -0.85 [-3.78, 2.51] | 7 | 0 |
| mtbench/pooled | picospec_vs_picospec_g2 | 30 | -0.46 [-3.21, 2.49] | -27.29 [-30.97, -23.39] | 23 | 0 |
| mtbench/pooled | picospec_g8_vs_picospec_g2 | 30 | -13.53 [-17.66, -8.52] | -82.65 [-91.26, -72.96] | 39 | 2 |
| mtbench/pooled | sync_g4_vs_picospec_g2 | 30 | -14.94 [-16.50, -13.47] | 3.32 [1.71, 4.79] | 23 | 0 |
| mtbench/pooled | hf_default_vs_picospec_g2 | 30 | -29.16 [-32.37, -25.49] | -26.34 [-32.83, -19.78] | 35 | 2 |
| mtbench/pooled | pipesd_vs_picospec_g2 | 30 | -5.74 [-8.43, -2.27] | -56.52 [-61.31, -51.04] | 17 | 0 |
| mtbench/pooled | pearl_vs_picospec_g2 | 30 | 1.68 [-0.22, 3.75] | -5.62 [-7.32, -3.80] | 35 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec_g2 | 30 | 8.18 [6.02, 10.56] | -26.21 [-28.49, -23.36] | 20 | 1 |
| mtbench/pooled | markov_w05_dist_int_vs_picospec_g2 | 30 | -0.70 [-2.92, 2.04] | 1.33 [-0.81, 3.34] | 13 | 0 |
| mtbench/pooled | picospec_g2_vs_picospec | 30 | 0.46 [-2.43, 3.32] | 21.44 [18.96, 23.65] | 23 | 0 |
| mtbench/pooled | picospec_g8_vs_picospec | 30 | -13.14 [-15.33, -10.28] | -43.49 [-46.63, -39.73] | 32 | 2 |
| mtbench/pooled | sync_g4_vs_picospec | 30 | -14.56 [-17.03, -12.24] | 24.05 [21.42, 26.11] | 1 | 0 |
| mtbench/pooled | hf_default_vs_picospec | 30 | -28.83 [-32.07, -25.41] | 0.75 [-4.86, 6.39] | 23 | 2 |
| mtbench/pooled | pipesd_vs_picospec | 30 | -5.31 [-7.22, -3.25] | -22.96 [-25.84, -19.83] | 21 | 0 |
| mtbench/pooled | pearl_vs_picospec | 30 | 2.14 [0.34, 4.27] | 17.03 [15.21, 18.90] | 29 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec | 30 | 8.68 [6.90, 11.03] | 0.85 [-2.44, 4.45] | 28 | 1 |
| mtbench/pooled | markov_w05_dist_int_vs_picospec | 30 | -0.25 [-2.29, 2.27] | 22.48 [18.63, 25.95] | 25 | 0 |
| mtbench/pooled | picospec_g2_vs_picospec_g8 | 30 | 15.65 [9.32, 21.45] | 45.25 [42.18, 47.72] | 39 | 1 |
| mtbench/pooled | picospec_vs_picospec_g8 | 30 | 15.12 [11.46, 18.11] | 30.31 [28.43, 31.80] | 32 | 1 |
| mtbench/pooled | sync_g4_vs_picospec_g8 | 30 | -1.64 [-7.16, 2.98] | 47.07 [43.88, 49.43] | 33 | 1 |
| mtbench/pooled | hf_default_vs_picospec_g8 | 30 | -18.07 [-22.74, -12.91] | 30.83 [26.09, 35.38] | 34 | 0 |
| mtbench/pooled | pipesd_vs_picospec_g8 | 30 | 9.01 [5.72, 12.26] | 14.31 [11.62, 16.96] | 44 | 0 |
| mtbench/pooled | pearl_vs_picospec_g8 | 30 | 17.59 [12.86, 22.13] | 42.18 [39.56, 44.40] | 46 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec_g8 | 30 | 25.11 [19.92, 29.92] | 30.90 [27.09, 34.41] | 40 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_picospec_g8 | 30 | 14.84 [10.24, 19.52] | 45.98 [41.93, 49.27] | 42 | 0 |
| mtbench/pooled | picospec_g2_vs_sync_g4 | 30 | 17.57 [15.57, 19.76] | -3.44 [-5.03, -1.73] | 23 | 0 |
| mtbench/pooled | picospec_vs_sync_g4 | 30 | 17.04 [13.95, 20.52] | -31.67 [-35.33, -27.27] | 1 | 0 |
| mtbench/pooled | picospec_g8_vs_sync_g4 | 30 | 1.66 [-2.90, 7.71] | -88.93 [-97.76, -78.20] | 33 | 2 |
| mtbench/pooled | hf_default_vs_sync_g4 | 30 | -16.71 [-21.29, -11.61] | -30.69 [-38.86, -22.64] | 23 | 2 |
| mtbench/pooled | pipesd_vs_sync_g4 | 30 | 10.82 [6.91, 15.36] | -61.90 [-68.36, -54.91] | 21 | 0 |
| mtbench/pooled | pearl_vs_sync_g4 | 30 | 19.54 [16.80, 22.55] | -9.25 [-11.43, -6.76] | 29 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_sync_g4 | 30 | 27.19 [23.97, 30.58] | -30.55 [-34.13, -26.56] | 28 | 1 |
| mtbench/pooled | markov_w05_dist_int_vs_sync_g4 | 30 | 16.75 [13.18, 20.84] | -2.06 [-4.50, 0.69] | 25 | 0 |
| gsm8k/low | picospec_vs_picospec_g2 | 50 | 8.39 [5.99, 10.88] | -9.77 [-11.75, -7.78] | 1 | 0 |
| gsm8k/low | picospec_g8_vs_picospec_g2 | 50 | 1.05 [-2.55, 5.00] | -25.74 [-29.87, -21.39] | 8 | 0 |
| gsm8k/low | sync_g4_vs_picospec_g2 | 50 | -31.50 [-33.07, -29.84] | -0.99 [-2.75, 0.69] | 1 | 0 |
| gsm8k/low | hf_default_vs_picospec_g2 | 50 | -31.23 [-33.35, -28.88] | -22.09 [-25.05, -19.13] | 7 | 0 |
| gsm8k/low | pipesd_vs_picospec_g2 | 50 | -4.57 [-6.70, -2.25] | -13.71 [-15.54, -11.81] | 4 | 0 |
| gsm8k/low | pearl_vs_picospec_g2 | 50 | -17.16 [-18.90, -15.35] | 6.48 [4.93, 8.00] | 2 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_picospec_g2 | 50 | 6.97 [4.31, 9.90] | -9.37 [-11.66, -7.01] | 2 | 0 |
| gsm8k/low | markov_w05_dist_int_vs_picospec_g2 | 50 | 3.80 [1.23, 6.59] | -5.04 [-6.73, -3.38] | 5 | 0 |
| gsm8k/low | picospec_g2_vs_picospec | 50 | -7.74 [-9.81, -5.65] | 8.90 [7.22, 10.51] | 1 | 0 |
| gsm8k/low | picospec_g8_vs_picospec | 50 | -6.77 [-8.72, -4.75] | -14.55 [-16.77, -12.40] | 7 | 0 |
| gsm8k/low | sync_g4_vs_picospec | 50 | -36.80 [-38.72, -34.83] | 7.99 [5.37, 10.59] | 0 | 0 |
| gsm8k/low | hf_default_vs_picospec | 50 | -36.55 [-38.26, -34.74] | -11.23 [-14.10, -8.47] | 6 | 0 |
| gsm8k/low | pipesd_vs_picospec | 50 | -11.96 [-13.47, -10.30] | -3.59 [-5.06, -2.21] | 5 | 0 |
| gsm8k/low | pearl_vs_picospec | 50 | -23.57 [-25.87, -21.04] | 14.80 [12.15, 17.34] | 3 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_picospec | 50 | -1.31 [-3.28, 0.72] | 0.36 [-2.00, 2.67] | 3 | 0 |
| gsm8k/low | markov_w05_dist_int_vs_picospec | 50 | -4.24 [-6.05, -2.51] | 4.31 [2.15, 6.42] | 4 | 0 |
| gsm8k/low | picospec_g2_vs_picospec_g8 | 50 | -1.04 [-4.76, 2.62] | 20.47 [17.62, 23.00] | 8 | 0 |
| gsm8k/low | picospec_vs_picospec_g8 | 50 | 7.26 [4.99, 9.55] | 12.70 [11.03, 14.36] | 7 | 0 |
| gsm8k/low | sync_g4_vs_picospec_g8 | 50 | -32.21 [-35.25, -29.05] | 19.68 [16.18, 23.06] | 7 | 0 |
| gsm8k/low | hf_default_vs_picospec_g8 | 50 | -31.94 [-34.23, -29.53] | 2.90 [-0.68, 6.30] | 13 | 0 |
| gsm8k/low | pipesd_vs_picospec_g8 | 50 | -5.57 [-8.10, -3.01] | 9.56 [7.23, 11.87] | 12 | 0 |
| gsm8k/low | pearl_vs_picospec_g8 | 50 | -18.02 [-21.79, -14.16] | 25.62 [22.12, 28.90] | 9 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_picospec_g8 | 50 | 5.86 [3.22, 8.58] | 13.02 [10.09, 15.87] | 8 | 0 |
| gsm8k/low | markov_w05_dist_int_vs_picospec_g8 | 50 | 2.71 [0.08, 5.37] | 16.46 [13.63, 19.21] | 9 | 0 |
| gsm8k/low | picospec_g2_vs_sync_g4 | 50 | 45.98 [42.52, 49.41] | 0.98 [-0.70, 2.68] | 1 | 0 |
| gsm8k/low | picospec_vs_sync_g4 | 50 | 58.22 [53.43, 63.18] | -8.69 [-11.84, -5.68] | 0 | 0 |
| gsm8k/low | picospec_g8_vs_sync_g4 | 50 | 47.51 [40.95, 54.45] | -24.50 [-29.98, -19.30] | 7 | 0 |
| gsm8k/low | hf_default_vs_sync_g4 | 50 | 0.39 [-2.74, 3.94] | -20.89 [-24.27, -17.58] | 6 | 0 |
| gsm8k/low | pipesd_vs_sync_g4 | 50 | 39.30 [35.19, 43.99] | -12.59 [-15.62, -9.52] | 5 | 0 |
| gsm8k/low | pearl_vs_sync_g4 | 50 | 20.93 [19.01, 22.89] | 7.40 [6.04, 8.60] | 3 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_sync_g4 | 50 | 56.15 [51.34, 61.59] | -8.29 [-11.44, -5.17] | 3 | 0 |
| gsm8k/low | markov_w05_dist_int_vs_sync_g4 | 50 | 51.52 [47.06, 56.58] | -4.00 [-6.21, -1.74] | 4 | 0 |
| gsm8k/high | picospec_vs_picospec_g2 | 50 | 40.02 [37.10, 42.89] | 10.90 [9.23, 12.66] | 4 | 0 |
| gsm8k/high | picospec_g8_vs_picospec_g2 | 50 | 76.89 [70.39, 83.95] | -0.25 [-4.36, 3.95] | 10 | 0 |
| gsm8k/high | sync_g4_vs_picospec_g2 | 50 | -6.62 [-7.70, -5.48] | 1.75 [0.80, 2.70] | 3 | 0 |
| gsm8k/high | hf_default_vs_picospec_g2 | 50 | 1.53 [-1.95, 5.15] | -0.84 [-4.00, 2.14] | 7 | 0 |
| gsm8k/high | pipesd_vs_picospec_g2 | 50 | 59.73 [53.72, 66.38] | -8.29 [-12.99, -3.28] | 6 | 0 |
| gsm8k/high | pearl_vs_picospec_g2 | 50 | 45.46 [41.78, 49.43] | 9.77 [7.51, 12.14] | 7 | 0 |
| gsm8k/high | markov_w0_dist_int_vs_picospec_g2 | 50 | 74.76 [68.95, 81.02] | 3.96 [0.80, 7.41] | 6 | 0 |
| gsm8k/high | markov_w05_dist_int_vs_picospec_g2 | 50 | 51.30 [44.84, 58.34] | 10.54 [8.48, 12.66] | 4 | 0 |
| gsm8k/high | picospec_g2_vs_picospec | 50 | -28.58 [-30.02, -27.06] | -12.24 [-14.49, -10.16] | 4 | 0 |
| gsm8k/high | picospec_g8_vs_picospec | 50 | 26.33 [22.93, 29.65] | -12.52 [-15.17, -9.79] | 7 | 0 |
| gsm8k/high | sync_g4_vs_picospec | 50 | -33.32 [-34.80, -31.83] | -10.28 [-12.82, -7.95] | 1 | 0 |
| gsm8k/high | hf_default_vs_picospec | 50 | -27.49 [-29.34, -25.66] | -13.18 [-15.61, -10.86] | 6 | 0 |
| gsm8k/high | pipesd_vs_picospec | 50 | 14.07 [11.19, 17.26] | -21.54 [-24.92, -17.93] | 7 | 0 |
| gsm8k/high | pearl_vs_picospec | 50 | 3.88 [2.15, 5.56] | -1.27 [-2.49, -0.15] | 3 | 0 |
| gsm8k/high | markov_w0_dist_int_vs_picospec | 50 | 24.81 [22.24, 27.68] | -7.79 [-9.79, -5.61] | 3 | 0 |
| gsm8k/high | markov_w05_dist_int_vs_picospec | 50 | 8.05 [4.80, 11.59] | -0.41 [-1.96, 1.17] | 4 | 0 |
| gsm8k/high | picospec_g2_vs_picospec_g8 | 50 | -43.47 [-45.64, -41.31] | 0.25 [-4.12, 4.18] | 10 | 0 |
| gsm8k/high | picospec_vs_picospec_g8 | 50 | -20.84 [-22.87, -18.65] | 11.12 [8.92, 13.17] | 7 | 0 |
| gsm8k/high | sync_g4_vs_picospec_g8 | 50 | -47.21 [-49.39, -45.07] | 1.99 [-2.59, 6.10] | 7 | 0 |
| gsm8k/high | hf_default_vs_picospec_g8 | 50 | -42.60 [-44.03, -41.11] | -0.59 [-3.37, 1.98] | 9 | 0 |
| gsm8k/high | pipesd_vs_picospec_g8 | 50 | -9.70 [-11.48, -7.90] | -8.02 [-9.66, -6.44] | 8 | 0 |
| gsm8k/high | pearl_vs_picospec_g8 | 50 | -17.77 [-19.35, -16.25] | 9.99 [8.15, 11.63] | 8 | 0 |
| gsm8k/high | markov_w0_dist_int_vs_picospec_g8 | 50 | -1.21 [-2.95, 0.66] | 4.20 [2.50, 5.78] | 6 | 0 |
| gsm8k/high | markov_w05_dist_int_vs_picospec_g8 | 50 | -14.47 [-16.62, -12.14] | 10.76 [8.28, 13.08] | 8 | 0 |
| gsm8k/high | picospec_g2_vs_sync_g4 | 50 | 7.09 [5.80, 8.34] | -1.78 [-2.78, -0.80] | 3 | 0 |
| gsm8k/high | picospec_vs_sync_g4 | 50 | 49.96 [46.68, 53.37] | 9.32 [7.37, 11.36] | 1 | 0 |
| gsm8k/high | picospec_g8_vs_sync_g4 | 50 | 89.44 [82.06, 97.59] | -2.03 [-6.49, 2.53] | 7 | 0 |
| gsm8k/high | hf_default_vs_sync_g4 | 50 | 8.73 [4.79, 13.00] | -2.63 [-6.10, 0.70] | 6 | 0 |
| gsm8k/high | pipesd_vs_sync_g4 | 50 | 71.06 [64.27, 78.71] | -10.21 [-15.38, -4.79] | 7 | 0 |
| gsm8k/high | pearl_vs_sync_g4 | 50 | 55.78 [51.41, 60.39] | 8.16 [5.56, 10.88] | 4 | 0 |
| gsm8k/high | markov_w0_dist_int_vs_sync_g4 | 50 | 87.16 [80.58, 94.48] | 2.25 [-1.30, 6.01] | 4 | 0 |
| gsm8k/high | markov_w05_dist_int_vs_sync_g4 | 50 | 62.04 [54.80, 70.35] | 8.95 [6.41, 11.42] | 3 | 0 |
| gsm8k/dynamic | picospec_vs_picospec_g2 | 50 | 20.55 [17.18, 24.05] | -3.26 [-5.75, -0.88] | 5 | 0 |
| gsm8k/dynamic | picospec_g8_vs_picospec_g2 | 50 | 29.75 [23.86, 35.53] | -18.16 [-22.54, -13.82] | 9 | 0 |
| gsm8k/dynamic | sync_g4_vs_picospec_g2 | 50 | -21.79 [-24.52, -19.14] | -4.11 [-5.74, -2.42] | 4 | 0 |
| gsm8k/dynamic | hf_default_vs_picospec_g2 | 50 | -20.33 [-23.46, -17.13] | -14.77 [-18.05, -11.70] | 9 | 0 |
| gsm8k/dynamic | pipesd_vs_picospec_g2 | 50 | 10.71 [6.38, 15.22] | -25.44 [-28.94, -21.65] | 7 | 0 |
| gsm8k/dynamic | pearl_vs_picospec_g2 | 50 | 9.43 [6.95, 12.22] | 0.55 [-1.12, 2.35] | 6 | 0 |
| gsm8k/dynamic | markov_w0_dist_int_vs_picospec_g2 | 50 | 32.02 [26.95, 37.42] | -8.95 [-11.80, -5.61] | 5 | 0 |
| gsm8k/dynamic | markov_w05_dist_int_vs_picospec_g2 | 50 | 21.04 [17.05, 25.54] | -2.47 [-4.67, -0.18] | 4 | 0 |
| gsm8k/dynamic | picospec_g2_vs_picospec | 50 | -17.05 [-19.39, -14.66] | 3.16 [0.87, 5.44] | 5 | 0 |
| gsm8k/dynamic | picospec_g8_vs_picospec | 50 | 7.63 [4.59, 10.60] | -14.43 [-16.92, -11.83] | 7 | 0 |
| gsm8k/dynamic | sync_g4_vs_picospec | 50 | -35.12 [-37.42, -32.95] | -0.82 [-3.19, 1.44] | 1 | 0 |
| gsm8k/dynamic | hf_default_vs_picospec | 50 | -33.91 [-36.12, -31.73] | -11.15 [-14.18, -8.46] | 8 | 0 |
| gsm8k/dynamic | pipesd_vs_picospec | 50 | -8.16 [-10.84, -5.60] | -21.48 [-23.90, -19.02] | 8 | 0 |
| gsm8k/dynamic | pearl_vs_picospec | 50 | -9.23 [-10.67, -7.84] | 3.69 [2.52, 4.83] | 5 | 0 |
| gsm8k/dynamic | markov_w0_dist_int_vs_picospec | 50 | 9.51 [6.82, 12.26] | -5.51 [-7.46, -3.42] | 7 | 0 |
| gsm8k/dynamic | markov_w05_dist_int_vs_picospec | 50 | 0.41 [-1.59, 2.64] | 0.77 [-1.41, 2.78] | 4 | 0 |
| gsm8k/dynamic | picospec_g2_vs_picospec_g8 | 50 | -22.93 [-26.22, -19.26] | 15.37 [12.14, 18.39] | 9 | 0 |
| gsm8k/dynamic | picospec_vs_picospec_g8 | 50 | -7.09 [-9.59, -4.39] | 12.61 [10.58, 14.47] | 7 | 0 |
| gsm8k/dynamic | sync_g4_vs_picospec_g8 | 50 | -39.72 [-41.98, -37.46] | 11.89 [8.36, 15.21] | 6 | 0 |
| gsm8k/dynamic | hf_default_vs_picospec_g8 | 50 | -38.59 [-40.57, -36.53] | 2.86 [-0.56, 5.94] | 13 | 0 |
| gsm8k/dynamic | pipesd_vs_picospec_g8 | 50 | -14.67 [-16.53, -12.88] | -6.16 [-8.86, -3.50] | 11 | 0 |
| gsm8k/dynamic | pearl_vs_picospec_g8 | 50 | -15.66 [-18.52, -12.44] | 15.83 [13.25, 18.20] | 8 | 0 |
| gsm8k/dynamic | markov_w0_dist_int_vs_picospec_g8 | 50 | 1.75 [-0.58, 4.13] | 7.79 [5.29, 10.40] | 7 | 0 |
| gsm8k/dynamic | markov_w05_dist_int_vs_picospec_g8 | 50 | -6.71 [-9.02, -4.44] | 13.28 [10.38, 16.16] | 8 | 0 |
| gsm8k/dynamic | picospec_g2_vs_sync_g4 | 50 | 27.86 [23.66, 32.49] | 3.95 [2.36, 5.43] | 4 | 0 |
| gsm8k/dynamic | picospec_vs_sync_g4 | 50 | 54.14 [49.13, 59.80] | 0.81 [-1.46, 3.09] | 1 | 0 |
| gsm8k/dynamic | picospec_g8_vs_sync_g4 | 50 | 65.90 [59.90, 72.34] | -13.49 [-17.94, -9.12] | 6 | 0 |
| gsm8k/dynamic | hf_default_vs_sync_g4 | 50 | 1.87 [-1.21, 5.10] | -10.24 [-13.18, -7.50] | 9 | 0 |
| gsm8k/dynamic | pipesd_vs_sync_g4 | 50 | 41.56 [37.64, 45.94] | -20.49 [-24.09, -16.60] | 9 | 0 |
| gsm8k/dynamic | pearl_vs_sync_g4 | 50 | 39.92 [35.56, 45.14] | 4.47 [2.58, 6.37] | 4 | 0 |
| gsm8k/dynamic | markov_w0_dist_int_vs_sync_g4 | 50 | 68.80 [63.87, 74.35] | -4.65 [-7.65, -1.44] | 6 | 0 |
| gsm8k/dynamic | markov_w05_dist_int_vs_sync_g4 | 50 | 54.77 [49.60, 60.45] | 1.57 [-1.03, 3.98] | 5 | 0 |
| gsm8k/pooled | picospec_vs_picospec_g2 | 50 | 26.70 [24.40, 29.01] | 1.02 [-0.74, 2.79] | 10 | 0 |
| gsm8k/pooled | picospec_g8_vs_picospec_g2 | 50 | 41.04 [36.37, 46.12] | -12.58 [-16.62, -8.52] | 27 | 0 |
| gsm8k/pooled | sync_g4_vs_picospec_g2 | 50 | -17.25 [-18.27, -16.27] | -0.81 [-1.76, 0.14] | 8 | 0 |
| gsm8k/pooled | hf_default_vs_picospec_g2 | 50 | -13.52 [-15.81, -11.15] | -10.79 [-13.52, -8.14] | 23 | 0 |
| gsm8k/pooled | pipesd_vs_picospec_g2 | 50 | 26.49 [23.32, 29.99] | -15.06 [-18.20, -11.67] | 17 | 0 |
| gsm8k/pooled | pearl_vs_picospec_g2 | 50 | 16.82 [15.27, 18.42] | 6.00 [4.92, 7.13] | 15 | 0 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec_g2 | 50 | 43.21 [39.84, 46.99] | -3.63 [-5.93, -1.10] | 13 | 0 |
| gsm8k/pooled | markov_w05_dist_int_vs_picospec_g2 | 50 | 30.05 [26.31, 34.15] | 2.37 [0.83, 3.96] | 13 | 0 |
| gsm8k/pooled | picospec_g2_vs_picospec | 50 | -21.07 [-22.49, -19.62] | -1.03 [-2.87, 0.73] | 10 | 0 |
| gsm8k/pooled | picospec_g8_vs_picospec | 50 | 11.31 [9.05, 13.67] | -13.73 [-15.95, -11.41] | 21 | 0 |
| gsm8k/pooled | sync_g4_vs_picospec | 50 | -34.69 [-36.13, -33.30] | -1.84 [-4.17, 0.33] | 2 | 0 |
| gsm8k/pooled | hf_default_vs_picospec | 50 | -31.75 [-33.01, -30.41] | -11.93 [-14.10, -9.81] | 20 | 0 |
| gsm8k/pooled | pipesd_vs_picospec | 50 | -0.17 [-1.63, 1.49] | -16.24 [-17.93, -14.41] | 20 | 0 |
| gsm8k/pooled | pearl_vs_picospec | 50 | -7.80 [-8.98, -6.62] | 5.04 [3.99, 6.02] | 11 | 0 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec | 50 | 13.03 [11.45, 14.68] | -4.69 [-6.22, -3.10] | 13 | 0 |
| gsm8k/pooled | markov_w05_dist_int_vs_picospec | 50 | 2.64 [0.90, 4.53] | 1.37 [-0.14, 2.85] | 12 | 0 |
| gsm8k/pooled | picospec_g2_vs_picospec_g8 | 50 | -29.10 [-31.56, -26.67] | 11.17 [7.85, 14.25] | 27 | 0 |
| gsm8k/pooled | picospec_vs_picospec_g8 | 50 | -10.16 [-12.02, -8.30] | 12.07 [10.24, 13.75] | 21 | 0 |
| gsm8k/pooled | sync_g4_vs_picospec_g8 | 50 | -41.33 [-43.59, -39.15] | 10.45 [6.66, 13.84] | 20 | 0 |
| gsm8k/pooled | hf_default_vs_picospec_g8 | 50 | -38.69 [-40.14, -37.22] | 1.59 [-1.39, 4.28] | 35 | 0 |
| gsm8k/pooled | pipesd_vs_picospec_g8 | 50 | -10.31 [-11.78, -8.91] | -2.20 [-3.82, -0.65] | 31 | 0 |
| gsm8k/pooled | pearl_vs_picospec_g8 | 50 | -17.17 [-19.31, -14.97] | 16.51 [14.18, 18.71] | 25 | 0 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec_g8 | 50 | 1.54 [-0.21, 3.29] | 7.95 [5.89, 10.00] | 21 | 0 |
| gsm8k/pooled | markov_w05_dist_int_vs_picospec_g8 | 50 | -7.79 [-9.51, -6.12] | 13.28 [10.73, 15.72] | 25 | 0 |
| gsm8k/pooled | picospec_g2_vs_sync_g4 | 50 | 20.85 [19.43, 22.36] | 0.80 [-0.14, 1.73] | 8 | 0 |
| gsm8k/pooled | picospec_vs_sync_g4 | 50 | 53.11 [49.94, 56.56] | 1.81 [-0.33, 4.00] | 2 | 0 |
| gsm8k/pooled | picospec_g8_vs_sync_g4 | 50 | 70.44 [64.34, 77.27] | -11.68 [-16.07, -7.13] | 20 | 0 |
| gsm8k/pooled | hf_default_vs_sync_g4 | 50 | 4.50 [1.42, 7.77] | -9.90 [-12.75, -6.99] | 21 | 0 |
| gsm8k/pooled | pipesd_vs_sync_g4 | 50 | 52.86 [48.52, 57.69] | -14.13 [-17.85, -10.20] | 21 | 0 |
| gsm8k/pooled | pearl_vs_sync_g4 | 50 | 41.17 [38.56, 43.95] | 6.76 [5.26, 8.30] | 11 | 0 |
| gsm8k/pooled | markov_w0_dist_int_vs_sync_g4 | 50 | 73.07 [68.14, 78.34] | -2.80 [-5.51, 0.07] | 13 | 0 |
| gsm8k/pooled | markov_w05_dist_int_vs_sync_g4 | 50 | 57.16 [52.11, 62.85] | 3.15 [1.12, 5.26] | 12 | 0 |
| humaneval/low | picospec_vs_picospec_g2 | 30 | 1.48 [-0.66, 3.81] | -15.50 [-17.63, -13.20] | 3 | 0 |
| humaneval/low | picospec_g8_vs_picospec_g2 | 30 | -8.23 [-11.18, -4.84] | -37.17 [-41.66, -32.09] | 9 | 0 |
| humaneval/low | sync_g4_vs_picospec_g2 | 30 | -32.33 [-34.40, -30.50] | 1.16 [-1.29, 3.21] | 3 | 0 |
| humaneval/low | hf_default_vs_picospec_g2 | 30 | -33.45 [-35.61, -31.12] | -17.96 [-20.68, -15.11] | 3 | 0 |
| humaneval/low | pipesd_vs_picospec_g2 | 30 | -9.15 [-10.73, -7.37] | -19.28 [-21.22, -17.17] | 2 | 0 |
| humaneval/low | pearl_vs_picospec_g2 | 30 | -15.40 [-17.55, -13.07] | 10.47 [8.16, 12.96] | 2 | 0 |
| humaneval/low | markov_w0_dist_int_vs_picospec_g2 | 30 | 1.81 [-0.05, 3.96] | -13.38 [-15.36, -11.34] | 3 | 0 |
| humaneval/low | markov_w05_dist_int_vs_picospec_g2 | 30 | 1.01 [-1.08, 3.38] | -6.06 [-8.55, -3.43] | 3 | 0 |
| humaneval/low | picospec_g2_vs_picospec | 30 | -1.46 [-3.67, 0.67] | 13.42 [11.66, 14.99] | 3 | 0 |
| humaneval/low | picospec_g8_vs_picospec | 30 | -9.57 [-12.11, -6.40] | -18.77 [-21.90, -14.91] | 8 | 0 |
| humaneval/low | sync_g4_vs_picospec | 30 | -33.32 [-36.19, -30.55] | 14.42 [11.39, 17.14] | 0 | 0 |
| humaneval/low | hf_default_vs_picospec | 30 | -34.43 [-36.72, -31.70] | -2.14 [-5.03, 1.23] | 4 | 0 |
| humaneval/low | pipesd_vs_picospec | 30 | -10.48 [-12.24, -8.59] | -3.28 [-5.00, -1.60] | 3 | 0 |
| humaneval/low | pearl_vs_picospec | 30 | -16.64 [-20.22, -12.71] | 22.48 [19.18, 25.67] | 3 | 0 |
| humaneval/low | markov_w0_dist_int_vs_picospec | 30 | 0.33 [-1.24, 2.03] | 1.84 [-0.46, 4.04] | 4 | 0 |
| humaneval/low | markov_w05_dist_int_vs_picospec | 30 | -0.47 [-3.00, 2.51] | 8.17 [5.31, 11.29] | 4 | 0 |
| humaneval/low | picospec_g2_vs_picospec_g8 | 30 | 8.97 [5.09, 12.59] | 27.10 [24.29, 29.41] | 9 | 0 |
| humaneval/low | picospec_vs_picospec_g8 | 30 | 10.59 [6.84, 13.78] | 15.80 [12.98, 17.97] | 8 | 0 |
| humaneval/low | sync_g4_vs_picospec_g8 | 30 | -26.26 [-30.06, -22.70] | 27.94 [24.40, 31.08] | 8 | 0 |
| humaneval/low | hf_default_vs_picospec_g8 | 30 | -27.48 [-29.89, -24.80] | 14.00 [10.97, 16.97] | 8 | 0 |
| humaneval/low | pipesd_vs_picospec_g8 | 30 | -1.00 [-4.15, 1.82] | 13.04 [9.91, 15.63] | 9 | 0 |
| humaneval/low | pearl_vs_picospec_g8 | 30 | -7.81 [-12.38, -3.48] | 34.73 [31.40, 37.58] | 8 | 0 |
| humaneval/low | markov_w0_dist_int_vs_picospec_g8 | 30 | 10.95 [7.76, 13.73] | 17.35 [14.21, 20.15] | 10 | 0 |
| humaneval/low | markov_w05_dist_int_vs_picospec_g8 | 30 | 10.07 [6.88, 13.08] | 22.68 [19.58, 25.42] | 9 | 0 |
| humaneval/low | picospec_g2_vs_sync_g4 | 30 | 47.78 [43.89, 52.43] | -1.17 [-3.32, 1.27] | 3 | 0 |
| humaneval/low | picospec_vs_sync_g4 | 30 | 49.97 [43.99, 56.72] | -16.85 [-20.68, -12.86] | 0 | 0 |
| humaneval/low | picospec_g8_vs_sync_g4 | 30 | 35.61 [29.37, 42.98] | -38.78 [-45.10, -32.28] | 8 | 0 |
| humaneval/low | hf_default_vs_sync_g4 | 30 | -1.66 [-6.22, 3.38] | -19.35 [-23.50, -15.31] | 4 | 0 |
| humaneval/low | pipesd_vs_sync_g4 | 30 | 34.26 [29.63, 39.81] | -20.68 [-24.38, -16.59] | 3 | 0 |
| humaneval/low | pearl_vs_sync_g4 | 30 | 25.02 [22.49, 27.75] | 9.42 [7.70, 11.21] | 3 | 0 |
| humaneval/low | markov_w0_dist_int_vs_sync_g4 | 30 | 50.46 [45.16, 56.90] | -14.71 [-17.53, -11.60] | 4 | 0 |
| humaneval/low | markov_w05_dist_int_vs_sync_g4 | 30 | 49.26 [44.19, 55.02] | -7.30 [-9.89, -4.52] | 4 | 0 |
| humaneval/high | picospec_vs_picospec_g2 | 30 | 34.81 [31.90, 38.11] | 6.61 [4.58, 8.86] | 4 | 0 |
| humaneval/high | picospec_g8_vs_picospec_g2 | 30 | 56.31 [49.60, 64.11] | -14.47 [-19.44, -9.26] | 9 | 0 |
| humaneval/high | sync_g4_vs_picospec_g2 | 30 | -5.12 [-6.61, -3.55] | 3.78 [2.63, 4.92] | 4 | 0 |
| humaneval/high | hf_default_vs_picospec_g2 | 30 | -4.03 [-6.83, -0.99] | -3.37 [-6.27, -0.47] | 4 | 0 |
| humaneval/high | pipesd_vs_picospec_g2 | 30 | 41.80 [36.13, 48.84] | -24.48 [-29.63, -18.64] | 3 | 0 |
| humaneval/high | pearl_vs_picospec_g2 | 30 | 35.42 [30.89, 40.21] | 3.52 [0.72, 6.43] | 4 | 0 |
| humaneval/high | markov_w0_dist_int_vs_picospec_g2 | 30 | 58.47 [53.13, 64.47] | -6.12 [-9.69, -2.30] | 5 | 0 |
| humaneval/high | markov_w05_dist_int_vs_picospec_g2 | 30 | 40.38 [34.34, 47.87] | 2.28 [0.01, 4.71] | 7 | 0 |
| humaneval/high | picospec_g2_vs_picospec | 30 | -25.82 [-27.59, -24.18] | -7.07 [-9.72, -4.80] | 4 | 0 |
| humaneval/high | picospec_g8_vs_picospec | 30 | 15.95 [12.74, 19.65] | -22.56 [-25.74, -19.01] | 7 | 0 |
| humaneval/high | sync_g4_vs_picospec | 30 | -29.62 [-30.82, -28.48] | -3.02 [-5.28, -1.08] | 0 | 0 |
| humaneval/high | hf_default_vs_picospec | 30 | -28.81 [-30.45, -27.06] | -10.69 [-13.16, -8.18] | 6 | 0 |
| humaneval/high | pipesd_vs_picospec | 30 | 5.19 [2.40, 8.64] | -33.28 [-36.68, -29.18] | 4 | 0 |
| humaneval/high | pearl_vs_picospec | 30 | 0.45 [-2.32, 3.66] | -3.31 [-5.80, -0.37] | 6 | 0 |
| humaneval/high | markov_w0_dist_int_vs_picospec | 30 | 17.56 [14.99, 20.28] | -13.63 [-15.91, -11.13] | 5 | 0 |
| humaneval/high | markov_w05_dist_int_vs_picospec | 30 | 4.13 [0.56, 8.53] | -4.63 [-6.85, -2.65] | 9 | 0 |
| humaneval/high | picospec_g2_vs_picospec_g8 | 30 | -36.03 [-39.07, -33.16] | 12.64 [8.48, 16.28] | 9 | 0 |
| humaneval/high | picospec_vs_picospec_g8 | 30 | -13.76 [-16.42, -11.30] | 18.41 [15.97, 20.47] | 7 | 0 |
| humaneval/high | sync_g4_vs_picospec_g8 | 30 | -39.30 [-42.01, -36.87] | 15.95 [11.78, 19.40] | 7 | 0 |
| humaneval/high | hf_default_vs_picospec_g8 | 30 | -38.60 [-40.67, -36.38] | 9.69 [6.41, 13.01] | 10 | 0 |
| humaneval/high | pipesd_vs_picospec_g8 | 30 | -9.28 [-11.27, -7.00] | -8.74 [-10.85, -6.28] | 7 | 0 |
| humaneval/high | pearl_vs_picospec_g8 | 30 | -13.37 [-16.51, -9.81] | 15.71 [12.68, 19.28] | 12 | 0 |
| humaneval/high | markov_w0_dist_int_vs_picospec_g8 | 30 | 1.38 [-1.00, 4.04] | 7.29 [5.35, 9.23] | 9 | 0 |
| humaneval/high | markov_w05_dist_int_vs_picospec_g8 | 30 | -10.20 [-12.38, -7.77] | 14.63 [11.77, 17.39] | 6 | 0 |
| humaneval/high | picospec_g2_vs_sync_g4 | 30 | 5.40 [3.68, 7.08] | -3.93 [-5.17, -2.70] | 4 | 0 |
| humaneval/high | picospec_vs_sync_g4 | 30 | 42.08 [39.82, 44.56] | 2.93 [1.07, 5.01] | 0 | 0 |
| humaneval/high | picospec_g8_vs_sync_g4 | 30 | 64.75 [58.40, 72.45] | -18.97 [-24.06, -13.35] | 7 | 0 |
| humaneval/high | hf_default_vs_sync_g4 | 30 | 1.15 [-1.50, 4.15] | -7.44 [-10.41, -4.44] | 6 | 0 |
| humaneval/high | pipesd_vs_sync_g4 | 30 | 49.45 [43.89, 56.35] | -29.37 [-34.72, -23.26] | 4 | 0 |
| humaneval/high | pearl_vs_sync_g4 | 30 | 42.73 [38.37, 47.46] | -0.28 [-2.99, 2.75] | 6 | 0 |
| humaneval/high | markov_w0_dist_int_vs_sync_g4 | 30 | 67.03 [61.60, 73.28] | -10.30 [-13.91, -6.23] | 5 | 0 |
| humaneval/high | markov_w05_dist_int_vs_sync_g4 | 30 | 47.95 [41.81, 55.91] | -1.57 [-3.61, 0.72] | 9 | 0 |
| humaneval/dynamic | picospec_vs_picospec_g2 | 30 | 14.84 [10.92, 18.63] | -10.11 [-12.78, -7.50] | 4 | 0 |
| humaneval/dynamic | picospec_g8_vs_picospec_g2 | 30 | 13.40 [7.32, 19.72] | -32.30 [-37.41, -27.03] | 9 | 0 |
| humaneval/dynamic | sync_g4_vs_picospec_g2 | 30 | -23.72 [-26.42, -21.24] | -2.70 [-4.85, -0.59] | 4 | 0 |
| humaneval/dynamic | hf_default_vs_picospec_g2 | 30 | -26.09 [-29.05, -22.89] | -17.78 [-21.25, -14.08] | 6 | 0 |
| humaneval/dynamic | pipesd_vs_picospec_g2 | 30 | 3.68 [-1.15, 9.44] | -33.57 [-38.45, -28.22] | 3 | 0 |
| humaneval/dynamic | pearl_vs_picospec_g2 | 30 | 7.30 [5.05, 9.59] | -2.40 [-4.29, -0.54] | 4 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_picospec_g2 | 30 | 19.85 [14.85, 25.41] | -16.68 [-19.87, -13.17] | 3 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_picospec_g2 | 30 | 15.12 [10.70, 20.13] | -8.12 [-10.37, -5.71] | 5 | 1 |
| humaneval/dynamic | picospec_g2_vs_picospec | 30 | -12.93 [-15.70, -9.85] | 9.18 [6.98, 11.33] | 4 | 0 |
| humaneval/dynamic | picospec_g8_vs_picospec | 30 | -1.26 [-5.12, 2.59] | -20.15 [-23.55, -16.41] | 8 | 0 |
| humaneval/dynamic | sync_g4_vs_picospec | 30 | -33.58 [-36.11, -31.06] | 6.73 [3.52, 9.73] | 0 | 0 |
| humaneval/dynamic | hf_default_vs_picospec | 30 | -35.64 [-38.10, -33.10] | -6.96 [-10.19, -3.65] | 5 | 0 |
| humaneval/dynamic | pipesd_vs_picospec | 30 | -9.72 [-13.03, -6.36] | -21.31 [-25.00, -17.54] | 3 | 0 |
| humaneval/dynamic | pearl_vs_picospec | 30 | -6.57 [-9.30, -3.38] | 7.00 [4.63, 9.68] | 4 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_picospec | 30 | 4.36 [2.18, 6.90] | -5.96 [-8.24, -3.55] | 4 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_picospec | 30 | 0.24 [-2.24, 2.83] | 1.81 [-0.55, 4.25] | 3 | 1 |
| humaneval/dynamic | picospec_g2_vs_picospec_g8 | 30 | -11.81 [-16.47, -6.82] | 24.41 [21.28, 27.23] | 9 | 0 |
| humaneval/dynamic | picospec_vs_picospec_g8 | 30 | 1.28 [-2.52, 5.39] | 16.77 [14.09, 19.06] | 8 | 0 |
| humaneval/dynamic | sync_g4_vs_picospec_g8 | 30 | -32.74 [-36.11, -29.46] | 22.38 [18.32, 25.80] | 8 | 0 |
| humaneval/dynamic | hf_default_vs_picospec_g8 | 30 | -34.82 [-37.43, -31.64] | 10.98 [7.75, 14.28] | 8 | 0 |
| humaneval/dynamic | pipesd_vs_picospec_g8 | 30 | -8.57 [-11.71, -5.01] | -0.96 [-5.22, 2.93] | 8 | 0 |
| humaneval/dynamic | pearl_vs_picospec_g8 | 30 | -5.38 [-9.78, -1.17] | 22.60 [19.90, 25.08] | 8 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_picospec_g8 | 30 | 5.69 [2.47, 9.31] | 11.81 [9.11, 14.77] | 10 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_picospec_g8 | 30 | 1.52 [-1.41, 4.62] | 18.28 [15.36, 21.06] | 9 | 1 |
| humaneval/dynamic | picospec_g2_vs_sync_g4 | 30 | 31.10 [26.97, 35.90] | 2.63 [0.58, 4.63] | 4 | 0 |
| humaneval/dynamic | picospec_vs_sync_g4 | 30 | 50.56 [45.05, 56.52] | -7.22 [-10.78, -3.65] | 0 | 0 |
| humaneval/dynamic | picospec_g8_vs_sync_g4 | 30 | 48.67 [41.76, 56.53] | -28.83 [-34.77, -22.43] | 8 | 0 |
| humaneval/dynamic | hf_default_vs_sync_g4 | 30 | -3.10 [-6.65, 0.79] | -14.68 [-18.25, -10.99] | 5 | 0 |
| humaneval/dynamic | pipesd_vs_sync_g4 | 30 | 35.93 [30.22, 42.64] | -30.07 [-36.08, -23.65] | 3 | 0 |
| humaneval/dynamic | pearl_vs_sync_g4 | 30 | 40.68 [36.55, 45.55] | 0.29 [-2.42, 2.92] | 4 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_sync_g4 | 30 | 57.13 [50.36, 65.13] | -13.61 [-17.69, -8.92] | 4 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_sync_g4 | 30 | 50.93 [45.17, 57.79] | -5.28 [-7.99, -2.49] | 3 | 1 |
| humaneval/pooled | picospec_vs_picospec_g2 | 30 | 21.04 [18.44, 24.02] | -4.37 [-6.36, -2.20] | 11 | 0 |
| humaneval/pooled | picospec_g8_vs_picospec_g2 | 30 | 25.46 [21.05, 30.49] | -26.03 [-30.16, -21.45] | 27 | 0 |
| humaneval/pooled | sync_g4_vs_picospec_g2 | 30 | -17.35 [-18.56, -16.21] | 1.10 [-0.12, 2.22] | 11 | 0 |
| humaneval/pooled | hf_default_vs_picospec_g2 | 30 | -18.13 [-20.39, -15.73] | -11.71 [-14.39, -8.91] | 13 | 0 |
| humaneval/pooled | pipesd_vs_picospec_g2 | 30 | 16.83 [13.42, 20.96] | -25.87 [-29.61, -21.60] | 8 | 0 |
| humaneval/pooled | pearl_vs_picospec_g2 | 30 | 13.57 [11.63, 15.67] | 3.50 [1.88, 5.31] | 10 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec_g2 | 30 | 31.97 [28.23, 36.34] | -11.32 [-13.63, -8.53] | 11 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_picospec_g2 | 30 | 22.98 [19.05, 27.48] | -3.27 [-4.96, -1.46] | 15 | 1 |
| humaneval/pooled | picospec_g2_vs_picospec | 30 | -17.38 [-19.37, -15.57] | 4.19 [2.15, 5.98] | 11 | 0 |
| humaneval/pooled | picospec_g8_vs_picospec | 30 | 3.65 [1.19, 6.25] | -20.75 [-23.39, -18.15] | 23 | 0 |
| humaneval/pooled | sync_g4_vs_picospec | 30 | -31.72 [-33.50, -30.01] | 5.24 [2.68, 7.55] | 0 | 0 |
| humaneval/pooled | hf_default_vs_picospec | 30 | -32.36 [-34.10, -30.42] | -7.03 [-9.50, -4.35] | 15 | 0 |
| humaneval/pooled | pipesd_vs_picospec | 30 | -3.48 [-5.51, -1.32] | -20.59 [-22.92, -18.20] | 10 | 0 |
| humaneval/pooled | pearl_vs_picospec | 30 | -6.17 [-8.20, -3.61] | 7.55 [5.58, 10.02] | 13 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec | 30 | 9.03 [7.56, 10.72] | -6.66 [-7.98, -5.25] | 13 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_picospec | 30 | 1.60 [-0.70, 4.12] | 1.05 [-1.08, 3.18] | 16 | 1 |
| humaneval/pooled | picospec_g2_vs_picospec_g8 | 30 | -20.29 [-23.36, -17.39] | 20.66 [17.66, 23.17] | 27 | 0 |
| humaneval/pooled | picospec_vs_picospec_g8 | 30 | -3.52 [-5.88, -1.18] | 17.19 [15.36, 18.95] | 23 | 0 |
| humaneval/pooled | sync_g4_vs_picospec_g8 | 30 | -34.12 [-36.92, -31.44] | 21.53 [18.11, 24.55] | 23 | 0 |
| humaneval/pooled | hf_default_vs_picospec_g8 | 30 | -34.74 [-36.66, -32.52] | 11.37 [8.57, 14.26] | 26 | 0 |
| humaneval/pooled | pipesd_vs_picospec_g8 | 30 | -6.88 [-8.93, -4.56] | 0.13 [-2.24, 2.53] | 24 | 0 |
| humaneval/pooled | pearl_vs_picospec_g8 | 30 | -9.48 [-12.61, -6.45] | 23.44 [20.78, 25.81] | 28 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec_g8 | 30 | 5.19 [3.01, 7.50] | 11.67 [9.53, 13.76] | 29 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_picospec_g8 | 30 | -1.98 [-3.62, -0.20] | 18.06 [15.42, 20.39] | 24 | 1 |
| humaneval/pooled | picospec_g2_vs_sync_g4 | 30 | 20.99 [19.34, 22.79] | -1.11 [-2.27, 0.12] | 11 | 0 |
| humaneval/pooled | picospec_vs_sync_g4 | 30 | 46.45 [42.87, 50.37] | -5.53 [-8.17, -2.75] | 0 | 0 |
| humaneval/pooled | picospec_g8_vs_sync_g4 | 30 | 51.80 [45.86, 58.53] | -27.43 [-32.54, -22.11] | 23 | 0 |
| humaneval/pooled | hf_default_vs_sync_g4 | 30 | -0.94 [-3.96, 2.28] | -12.94 [-16.22, -9.78] | 15 | 0 |
| humaneval/pooled | pipesd_vs_sync_g4 | 30 | 41.35 [36.71, 46.89] | -27.26 [-31.94, -22.12] | 10 | 0 |
| humaneval/pooled | pearl_vs_sync_g4 | 30 | 37.41 [34.98, 40.27] | 2.43 [0.70, 4.43] | 13 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_sync_g4 | 30 | 59.67 [54.58, 65.56] | -12.56 [-15.61, -9.07] | 13 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_sync_g4 | 30 | 48.79 [43.58, 54.95] | -4.42 [-6.42, -2.26] | 16 | 1 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
