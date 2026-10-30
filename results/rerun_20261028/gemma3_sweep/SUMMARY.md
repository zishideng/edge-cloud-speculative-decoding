# Progress probe: gemma3_sweep

State: complete; 600/600 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: d10, d25, d50, d200; pooled = d10+d25+d50+d200.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/d10 | picospec_g2 | 30 | 8125 | 26.296 | 0.2756 | 5 | 35.55 |
| all/d10 | picospec | 30 | 8150 | 28.446 | 0.3304 | 5 | 30.97 |
| all/d10 | picospec_g8 | 30 | 8143 | 25.120 | 0.4673 | 5 | 22.09 |
| all/d10 | markov_w0_dist_int | 30 | 8225 | 28.329 | 0.2942 | 6 | 41.38 |
| all/d10 | pearl | 30 | 8234 | 27.744 | 0.2609 | 6 | 0.00 |
| all/d25 | picospec_g2 | 30 | 8022 | 21.417 | 0.3167 | 4 | 33.48 |
| all/d25 | picospec | 30 | 8156 | 23.511 | 0.3491 | 5 | 28.62 |
| all/d25 | picospec_g8 | 30 | 8105 | 23.125 | 0.4894 | 4 | 19.16 |
| all/d25 | markov_w0_dist_int | 30 | 8131 | 24.833 | 0.3338 | 5 | 37.34 |
| all/d25 | pearl | 30 | 8155 | 22.197 | 0.3051 | 5 | 0.00 |
| all/d50 | picospec_g2 | 30 | 8044 | 17.403 | 0.3692 | 4 | 33.48 |
| all/d50 | picospec | 30 | 8102 | 19.938 | 0.3697 | 5 | 27.71 |
| all/d50 | picospec_g8 | 30 | 8047 | 20.115 | 0.5127 | 4 | 17.41 |
| all/d50 | markov_w0_dist_int | 30 | 8052 | 21.303 | 0.3890 | 4 | 34.04 |
| all/d50 | pearl | 30 | 8064 | 20.678 | 0.3527 | 4 | 0.00 |
| all/d200 | picospec_g2 | 30 | 8043 | 7.885 | 0.6893 | 5 | 33.65 |
| all/d200 | picospec | 30 | 8068 | 9.524 | 0.6311 | 5 | 27.12 |
| all/d200 | picospec_g8 | 30 | 8137 | 9.972 | 0.6904 | 5 | 16.44 |
| all/d200 | markov_w0_dist_int | 30 | 8252 | 10.297 | 0.6425 | 6 | 26.32 |
| all/d200 | pearl | 30 | 8304 | 9.605 | 0.7348 | 6 | 0.00 |
| all/pooled | picospec_g2 | 120 | 32234 | 14.883 | 0.4124 | 18 | 34.02 |
| all/pooled | picospec | 120 | 32476 | 17.212 | 0.4196 | 20 | 28.53 |
| all/pooled | picospec_g8 | 120 | 32432 | 17.154 | 0.5401 | 18 | 18.54 |
| all/pooled | markov_w0_dist_int | 120 | 32660 | 18.173 | 0.4154 | 21 | 33.59 |
| all/pooled | pearl | 120 | 32757 | 17.073 | 0.4146 | 21 | 0.00 |
| mtbench/d10 | picospec_g2 | 10 | 3188 | 20.496 | 0.3529 | 3 | 18.49 |
| mtbench/d10 | picospec | 10 | 3213 | 19.695 | 0.4819 | 3 | 11.30 |
| mtbench/d10 | picospec_g8 | 10 | 3206 | 16.125 | 0.7482 | 3 | 4.27 |
| mtbench/d10 | markov_w0_dist_int | 10 | 3188 | 19.929 | 0.3897 | 3 | 23.20 |
| mtbench/d10 | pearl | 10 | 3195 | 21.644 | 0.3308 | 3 | 0.00 |
| mtbench/d25 | picospec_g2 | 10 | 3181 | 16.493 | 0.4101 | 3 | 16.66 |
| mtbench/d25 | picospec | 10 | 3240 | 15.868 | 0.5094 | 3 | 10.09 |
| mtbench/d25 | picospec_g8 | 10 | 3266 | 14.999 | 0.7727 | 3 | 3.39 |
| mtbench/d25 | markov_w0_dist_int | 10 | 3183 | 17.028 | 0.4596 | 3 | 21.07 |
| mtbench/d25 | pearl | 10 | 3189 | 17.089 | 0.3905 | 3 | 0.00 |
| mtbench/d50 | picospec_g2 | 10 | 3212 | 13.867 | 0.4661 | 3 | 16.42 |
| mtbench/d50 | picospec | 10 | 3195 | 13.732 | 0.5381 | 3 | 9.45 |
| mtbench/d50 | picospec_g8 | 10 | 3217 | 12.840 | 0.8143 | 3 | 2.91 |
| mtbench/d50 | markov_w0_dist_int | 10 | 3212 | 14.442 | 0.5532 | 3 | 18.74 |
| mtbench/d50 | pearl | 10 | 3212 | 14.747 | 0.4938 | 3 | 0.00 |
| mtbench/d200 | picospec_g2 | 10 | 3202 | 6.495 | 0.8459 | 3 | 17.21 |
| mtbench/d200 | picospec | 10 | 3215 | 7.004 | 0.8687 | 3 | 9.62 |
| mtbench/d200 | picospec_g8 | 10 | 3208 | 6.419 | 1.0796 | 3 | 2.84 |
| mtbench/d200 | markov_w0_dist_int | 10 | 3202 | 6.993 | 0.9493 | 3 | 12.92 |
| mtbench/d200 | pearl | 10 | 3257 | 6.075 | 1.1606 | 3 | 0.00 |
| mtbench/pooled | picospec_g2 | 40 | 12783 | 11.913 | 0.5191 | 12 | 17.16 |
| mtbench/pooled | picospec | 40 | 12863 | 12.146 | 0.5995 | 12 | 10.07 |
| mtbench/pooled | picospec_g8 | 40 | 12897 | 11.052 | 0.8533 | 12 | 3.28 |
| mtbench/pooled | markov_w0_dist_int | 40 | 12785 | 12.446 | 0.5883 | 12 | 17.84 |
| mtbench/pooled | pearl | 40 | 12853 | 11.812 | 0.5966 | 12 | 0.00 |
| gsm8k/d10 | picospec_g2 | 10 | 3219 | 29.638 | 0.2447 | 2 | 43.07 |
| gsm8k/d10 | picospec | 10 | 3219 | 35.202 | 0.2681 | 2 | 40.68 |
| gsm8k/d10 | picospec_g8 | 10 | 3219 | 33.355 | 0.3516 | 2 | 31.48 |
| gsm8k/d10 | markov_w0_dist_int | 10 | 3319 | 33.242 | 0.2691 | 3 | 48.07 |
| gsm8k/d10 | pearl | 10 | 3321 | 31.041 | 0.2340 | 3 | 0.00 |
| gsm8k/d25 | picospec_g2 | 10 | 3123 | 24.389 | 0.2785 | 1 | 41.61 |
| gsm8k/d25 | picospec | 10 | 3198 | 29.975 | 0.2808 | 2 | 38.23 |
| gsm8k/d25 | picospec_g8 | 10 | 3121 | 30.464 | 0.3717 | 1 | 28.27 |
| gsm8k/d25 | markov_w0_dist_int | 10 | 3230 | 30.096 | 0.2972 | 2 | 44.26 |
| gsm8k/d25 | pearl | 10 | 3248 | 25.376 | 0.2689 | 2 | 0.00 |
| gsm8k/d50 | picospec_g2 | 10 | 3114 | 19.316 | 0.3309 | 1 | 42.04 |
| gsm8k/d50 | picospec | 10 | 3189 | 24.526 | 0.3009 | 2 | 37.94 |
| gsm8k/d50 | picospec_g8 | 10 | 3112 | 26.722 | 0.3871 | 1 | 26.66 |
| gsm8k/d50 | markov_w0_dist_int | 10 | 3122 | 26.104 | 0.3338 | 1 | 42.99 |
| gsm8k/d50 | pearl | 10 | 3134 | 24.521 | 0.2968 | 1 | 0.00 |
| gsm8k/d200 | picospec_g2 | 10 | 3123 | 8.622 | 0.6266 | 2 | 41.62 |
| gsm8k/d200 | picospec | 10 | 3135 | 11.158 | 0.5351 | 2 | 36.22 |
| gsm8k/d200 | picospec_g8 | 10 | 3211 | 12.968 | 0.5300 | 2 | 24.28 |
| gsm8k/d200 | markov_w0_dist_int | 10 | 3332 | 12.364 | 0.5361 | 3 | 34.57 |
| gsm8k/d200 | pearl | 10 | 3329 | 12.401 | 0.5715 | 3 | 0.00 |
| gsm8k/pooled | picospec_g2 | 40 | 12579 | 16.550 | 0.3692 | 6 | 42.08 |
| gsm8k/pooled | picospec | 40 | 12741 | 20.917 | 0.3452 | 8 | 38.21 |
| gsm8k/pooled | picospec_g8 | 40 | 12663 | 22.491 | 0.4105 | 6 | 27.40 |
| gsm8k/pooled | markov_w0_dist_int | 40 | 13003 | 21.808 | 0.3600 | 9 | 41.66 |
| gsm8k/pooled | pearl | 40 | 13032 | 20.645 | 0.3440 | 9 | 0.00 |
| humaneval/d10 | picospec_g2 | 10 | 1718 | 38.320 | 0.1898 | 0 | 61.41 |
| humaneval/d10 | picospec | 10 | 1718 | 53.816 | 0.1639 | 0 | 71.14 |
| humaneval/d10 | picospec_g8 | 10 | 1718 | 59.584 | 0.1597 | 0 | 75.22 |
| humaneval/d10 | markov_w0_dist_int | 10 | 1718 | 56.282 | 0.1656 | 0 | 74.31 |
| humaneval/d10 | pearl | 10 | 1718 | 40.734 | 0.1830 | 0 | 0.00 |
| humaneval/d25 | picospec_g2 | 10 | 1718 | 32.020 | 0.2135 | 0 | 61.09 |
| humaneval/d25 | picospec | 10 | 1718 | 47.688 | 0.1735 | 0 | 69.87 |
| humaneval/d25 | picospec_g8 | 10 | 1718 | 56.730 | 0.1646 | 0 | 73.98 |
| humaneval/d25 | markov_w0_dist_int | 10 | 1718 | 51.788 | 0.1696 | 0 | 72.36 |
| humaneval/d25 | pearl | 10 | 1718 | 32.541 | 0.2152 | 0 | 0.00 |
| humaneval/d50 | picospec_g2 | 10 | 1718 | 24.768 | 0.2577 | 0 | 61.01 |
| humaneval/d50 | picospec | 10 | 1718 | 39.349 | 0.1844 | 0 | 69.43 |
| humaneval/d50 | picospec_g8 | 10 | 1718 | 51.980 | 0.1754 | 0 | 70.56 |
| humaneval/d50 | markov_w0_dist_int | 10 | 1718 | 47.760 | 0.1821 | 0 | 71.69 |
| humaneval/d50 | pearl | 10 | 1718 | 38.722 | 0.1906 | 0 | 0.00 |
| humaneval/d200 | picospec_g2 | 10 | 1718 | 10.424 | 0.5114 | 0 | 61.01 |
| humaneval/d200 | picospec | 10 | 1718 | 16.036 | 0.3614 | 0 | 69.24 |
| humaneval/d200 | picospec_g8 | 10 | 1718 | 25.047 | 0.2637 | 0 | 69.67 |
| humaneval/d200 | markov_w0_dist_int | 10 | 1718 | 23.217 | 0.2770 | 0 | 71.69 |
| humaneval/d200 | pearl | 10 | 1718 | 28.634 | 0.2441 | 0 | 0.00 |
| humaneval/pooled | picospec_g2 | 40 | 6872 | 20.658 | 0.2931 | 0 | 61.13 |
| humaneval/pooled | picospec | 40 | 6872 | 31.416 | 0.2208 | 0 | 69.91 |
| humaneval/pooled | picospec_g8 | 40 | 6872 | 42.747 | 0.1909 | 0 | 72.29 |
| humaneval/pooled | markov_w0_dist_int | 40 | 6872 | 39.570 | 0.1986 | 0 | 72.48 |
| humaneval/pooled | pearl | 40 | 6872 | 34.474 | 0.2082 | 0 | 0.00 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/d10 | picospec_vs_picospec_g2 | 30 | 8.18 [2.73, 16.29] | -19.91 [-26.51, -11.14] | 4 | 0 |
| all/d10 | picospec_g8_vs_picospec_g2 | 30 | -4.47 [-12.14, 7.50] | -69.56 [-86.50, -47.60] | 7 | 0 |
| all/d10 | markov_w0_dist_int_vs_picospec_g2 | 30 | 7.73 [2.94, 14.50] | -6.77 [-9.94, -3.11] | 4 | 1 |
| all/d10 | pearl_vs_picospec_g2 | 30 | 5.51 [2.93, 8.25] | 5.32 [3.23, 7.46] | 6 | 1 |
| all/d10 | picospec_g2_vs_picospec | 30 | -7.56 [-14.01, -2.65] | 16.60 [10.02, 20.96] | 4 | 0 |
| all/d10 | picospec_g8_vs_picospec | 30 | -11.69 [-14.77, -7.11] | -41.41 [-47.93, -32.22] | 4 | 0 |
| all/d10 | markov_w0_dist_int_vs_picospec | 30 | -0.41 [-3.01, 2.07] | 10.96 [4.51, 15.70] | 7 | 1 |
| all/d10 | pearl_vs_picospec | 30 | -2.47 [-9.32, 3.19] | 21.04 [14.18, 25.81] | 9 | 1 |
| all/d10 | picospec_g2_vs_picospec_g8 | 30 | 4.68 [-6.98, 13.82] | 41.02 [32.25, 46.38] | 7 | 0 |
| all/d10 | picospec_vs_picospec_g8 | 30 | 13.24 [7.66, 17.33] | 29.28 [24.37, 32.40] | 4 | 0 |
| all/d10 | markov_w0_dist_int_vs_picospec_g8 | 30 | 12.77 [5.77, 18.58] | 37.03 [28.28, 42.87] | 9 | 1 |
| all/d10 | pearl_vs_picospec_g8 | 30 | 10.45 [-1.99, 20.65] | 44.16 [35.14, 49.64] | 10 | 1 |
| all/d25 | picospec_vs_picospec_g2 | 30 | 9.78 [2.69, 18.96] | -10.20 [-16.05, -2.68] | 5 | 1 |
| all/d25 | picospec_g8_vs_picospec_g2 | 30 | 7.98 [-0.46, 19.71] | -54.51 [-68.83, -36.37] | 8 | 0 |
| all/d25 | markov_w0_dist_int_vs_picospec_g2 | 30 | 15.95 [10.25, 23.75] | -5.39 [-8.98, -0.89] | 4 | 1 |
| all/d25 | pearl_vs_picospec_g2 | 30 | 3.64 [0.62, 6.33] | 3.67 [1.09, 5.79] | 6 | 1 |
| all/d25 | picospec_g2_vs_picospec | 30 | -8.91 [-15.94, -2.62] | 9.26 [2.61, 13.83] | 5 | 0 |
| all/d25 | picospec_g8_vs_picospec | 30 | -1.64 [-6.41, 4.28] | -40.21 [-46.78, -31.79] | 6 | 0 |
| all/d25 | markov_w0_dist_int_vs_picospec | 30 | 5.63 [0.73, 11.83] | 4.37 [-0.75, 9.12] | 6 | 1 |
| all/d25 | pearl_vs_picospec | 30 | -5.59 [-13.72, 1.62] | 12.59 [5.01, 17.59] | 9 | 1 |
| all/d25 | picospec_g2_vs_picospec_g8 | 30 | -7.39 [-16.47, 0.46] | 35.28 [26.67, 40.77] | 8 | 0 |
| all/d25 | picospec_vs_picospec_g8 | 30 | 1.67 [-4.10, 6.85] | 28.68 [24.12, 31.87] | 6 | 1 |
| all/d25 | markov_w0_dist_int_vs_picospec_g8 | 30 | 7.39 [1.43, 13.58] | 31.79 [24.56, 36.95] | 10 | 1 |
| all/d25 | pearl_vs_picospec_g8 | 30 | -4.01 [-13.90, 4.37] | 37.66 [28.54, 43.48] | 10 | 1 |
| all/d50 | picospec_vs_picospec_g2 | 30 | 14.56 [7.87, 23.76] | -0.14 [-6.07, 7.46] | 6 | 1 |
| all/d50 | picospec_g8_vs_picospec_g2 | 30 | 15.58 [3.40, 32.08] | -38.87 [-53.81, -20.81] | 9 | 0 |
| all/d50 | markov_w0_dist_int_vs_picospec_g2 | 30 | 22.41 [14.44, 33.93] | -5.35 [-10.88, 1.97] | 5 | 0 |
| all/d50 | pearl_vs_picospec_g2 | 30 | 18.82 [13.23, 26.10] | 4.48 [0.18, 9.65] | 4 | 0 |
| all/d50 | picospec_g2_vs_picospec | 30 | -12.71 [-19.20, -7.30] | 0.14 [-8.06, 5.73] | 6 | 0 |
| all/d50 | picospec_g8_vs_picospec | 30 | 0.89 [-5.33, 7.97] | -38.68 [-45.97, -28.90] | 7 | 0 |
| all/d50 | markov_w0_dist_int_vs_picospec | 30 | 6.85 [4.42, 9.61] | -5.20 [-8.63, -1.92] | 7 | 0 |
| all/d50 | pearl_vs_picospec | 30 | 3.71 [0.72, 6.04] | 4.62 [1.77, 6.85] | 8 | 0 |
| all/d50 | picospec_g2_vs_picospec_g8 | 30 | -13.48 [-24.29, -3.29] | 27.99 [17.22, 34.98] | 9 | 0 |
| all/d50 | picospec_vs_picospec_g8 | 30 | -0.88 [-7.38, 5.63] | 27.89 [22.42, 31.49] | 7 | 1 |
| all/d50 | markov_w0_dist_int_vs_picospec_g8 | 30 | 5.91 [-0.48, 13.21] | 24.14 [17.40, 29.39] | 9 | 0 |
| all/d50 | pearl_vs_picospec_g8 | 30 | 2.80 [-5.44, 10.77] | 31.22 [24.73, 35.64] | 9 | 0 |
| all/d200 | picospec_vs_picospec_g2 | 30 | 20.79 [15.29, 28.67] | 8.45 [3.98, 14.19] | 5 | 0 |
| all/d200 | picospec_g8_vs_picospec_g2 | 30 | 26.47 [14.20, 45.21] | -0.17 [-10.92, 13.02] | 9 | 0 |
| all/d200 | markov_w0_dist_int_vs_picospec_g2 | 30 | 30.59 [21.10, 45.22] | 6.79 [-0.22, 16.01] | 4 | 1 |
| all/d200 | pearl_vs_picospec_g2 | 30 | 21.81 [9.56, 41.16] | -6.61 [-18.26, 7.77] | 12 | 1 |
| all/d200 | picospec_g2_vs_picospec | 30 | -17.21 [-22.28, -13.26] | -9.23 [-16.54, -4.14] | 5 | 0 |
| all/d200 | picospec_g8_vs_picospec | 30 | 4.70 [-1.04, 13.37] | -9.41 [-15.61, -1.03] | 7 | 0 |
| all/d200 | markov_w0_dist_int_vs_picospec | 30 | 8.11 [4.86, 13.24] | -1.81 [-4.72, 2.54] | 6 | 1 |
| all/d200 | pearl_vs_picospec | 30 | 0.85 [-5.43, 10.22] | -16.45 [-23.71, -7.01] | 12 | 1 |
| all/d200 | picospec_g2_vs_picospec_g8 | 30 | -20.93 [-31.13, -12.43] | 0.17 [-14.97, 9.84] | 9 | 0 |
| all/d200 | picospec_vs_picospec_g8 | 30 | -4.49 [-11.79, 1.06] | 8.60 [1.02, 13.50] | 7 | 0 |
| all/d200 | markov_w0_dist_int_vs_picospec_g8 | 30 | 3.26 [-1.10, 6.77] | 6.94 [2.56, 10.15] | 9 | 1 |
| all/d200 | pearl_vs_picospec_g8 | 30 | -3.68 [-5.84, -1.42] | -6.43 [-8.66, -4.06] | 12 | 1 |
| all/pooled | picospec_vs_picospec_g2 | 30 | 15.64 [9.89, 23.96] | -1.74 [-7.01, 5.20] | 20 | 2 |
| all/pooled | picospec_g8_vs_picospec_g2 | 30 | 15.25 [4.76, 30.93] | -30.95 [-44.27, -14.04] | 33 | 0 |
| all/pooled | markov_w0_dist_int_vs_picospec_g2 | 30 | 22.11 [15.03, 32.95] | -0.73 [-5.33, 5.98] | 17 | 3 |
| all/pooled | pearl_vs_picospec_g2 | 30 | 14.71 [8.21, 23.84] | -0.54 [-6.21, 6.31] | 28 | 3 |
| all/pooled | picospec_g2_vs_picospec | 30 | -13.53 [-19.33, -9.00] | 1.71 [-5.49, 6.55] | 20 | 0 |
| all/pooled | picospec_g8_vs_picospec | 30 | -0.34 [-4.77, 5.77] | -28.71 [-35.02, -20.10] | 24 | 0 |
| all/pooled | markov_w0_dist_int_vs_picospec | 30 | 5.59 [3.65, 8.35] | 0.99 [-1.43, 3.31] | 26 | 3 |
| all/pooled | pearl_vs_picospec | 30 | -0.81 [-2.26, 0.77] | 1.18 [-0.08, 2.44] | 38 | 3 |
| all/pooled | picospec_g2_vs_picospec_g8 | 30 | -13.24 [-23.63, -4.55] | 23.64 [12.31, 30.68] | 33 | 0 |
| all/pooled | picospec_vs_picospec_g8 | 30 | 0.34 [-5.45, 5.01] | 22.31 [16.74, 25.94] | 24 | 2 |
| all/pooled | markov_w0_dist_int_vs_picospec_g8 | 30 | 5.94 [0.80, 10.69] | 23.08 [16.40, 27.77] | 37 | 3 |
| all/pooled | pearl_vs_picospec_g8 | 30 | -0.47 [-5.74, 3.68] | 23.22 [17.68, 26.79] | 41 | 3 |
| mtbench/d10 | picospec_vs_picospec_g2 | 10 | -3.91 [-7.06, 0.32] | -36.54 [-40.88, -30.28] | 3 | 0 |
| mtbench/d10 | picospec_g8_vs_picospec_g2 | 10 | -21.33 [-25.30, -15.09] | -111.99 [-123.33, -94.32] | 6 | 0 |
| mtbench/d10 | markov_w0_dist_int_vs_picospec_g2 | 10 | -2.77 [-5.22, 0.25] | -10.42 [-14.48, -6.81] | 2 | 0 |
| mtbench/d10 | pearl_vs_picospec_g2 | 10 | 5.60 [2.67, 8.88] | 6.28 [3.48, 8.91] | 3 | 0 |
| mtbench/d10 | picospec_g2_vs_picospec | 10 | 4.07 [-0.32, 7.59] | 26.76 [23.24, 29.02] | 3 | 0 |
| mtbench/d10 | picospec_g8_vs_picospec | 10 | -18.13 [-20.07, -15.10] | -55.26 [-59.73, -48.60] | 4 | 0 |
| mtbench/d10 | markov_w0_dist_int_vs_picospec | 10 | 1.19 [-0.99, 3.54] | 19.13 [12.76, 23.44] | 4 | 0 |
| mtbench/d10 | pearl_vs_picospec | 10 | 9.89 [4.57, 14.56] | 31.36 [27.30, 34.21] | 5 | 0 |
| mtbench/d10 | picospec_g2_vs_picospec_g8 | 10 | 27.11 [17.77, 33.86] | 52.83 [48.54, 55.22] | 6 | 0 |
| mtbench/d10 | picospec_vs_picospec_g8 | 10 | 22.14 [17.79, 25.12] | 35.59 [32.70, 37.39] | 4 | 0 |
| mtbench/d10 | markov_w0_dist_int_vs_picospec_g8 | 10 | 23.59 [17.25, 28.70] | 47.91 [41.37, 51.54] | 6 | 0 |
| mtbench/d10 | pearl_vs_picospec_g8 | 10 | 34.22 [23.29, 42.68] | 55.79 [51.31, 58.39] | 6 | 0 |
| mtbench/d25 | picospec_vs_picospec_g2 | 10 | -3.79 [-8.38, 1.92] | -24.23 [-28.25, -19.40] | 4 | 0 |
| mtbench/d25 | picospec_g8_vs_picospec_g2 | 10 | -9.06 [-16.32, -2.04] | -88.44 [-100.81, -75.37] | 7 | 0 |
| mtbench/d25 | markov_w0_dist_int_vs_picospec_g2 | 10 | 3.24 [-0.76, 7.77] | -12.07 [-16.72, -8.94] | 2 | 0 |
| mtbench/d25 | pearl_vs_picospec_g2 | 10 | 3.61 [-0.94, 6.83] | 4.78 [1.16, 6.96] | 3 | 0 |
| mtbench/d25 | picospec_g2_vs_picospec | 10 | 3.94 [-1.88, 9.15] | 19.51 [16.25, 22.03] | 4 | 0 |
| mtbench/d25 | picospec_g8_vs_picospec | 10 | -5.48 [-12.41, 3.30] | -51.68 [-58.18, -44.07] | 4 | 0 |
| mtbench/d25 | markov_w0_dist_int_vs_picospec | 10 | 7.31 [-0.11, 16.53] | 9.79 [3.34, 14.34] | 3 | 0 |
| mtbench/d25 | pearl_vs_picospec | 10 | 7.70 [-0.49, 15.50] | 23.36 [18.60, 26.39] | 5 | 0 |
| mtbench/d25 | picospec_g2_vs_picospec_g8 | 10 | 9.97 [2.09, 19.50] | 46.93 [42.98, 50.20] | 7 | 0 |
| mtbench/d25 | picospec_vs_picospec_g8 | 10 | 5.80 [-3.20, 14.17] | 34.07 [30.59, 36.78] | 4 | 0 |
| mtbench/d25 | markov_w0_dist_int_vs_picospec_g8 | 10 | 13.53 [7.09, 21.35] | 40.53 [35.05, 44.73] | 7 | 0 |
| mtbench/d25 | pearl_vs_picospec_g8 | 10 | 13.94 [5.67, 23.07] | 49.47 [45.03, 52.67] | 7 | 0 |
| mtbench/d50 | picospec_vs_picospec_g2 | 10 | -0.97 [-5.30, 5.37] | -15.46 [-19.87, -9.45] | 4 | 0 |
| mtbench/d50 | picospec_g8_vs_picospec_g2 | 10 | -7.41 [-17.28, 3.49] | -74.73 [-88.35, -58.48] | 7 | 0 |
| mtbench/d50 | markov_w0_dist_int_vs_picospec_g2 | 10 | 4.15 [-0.23, 11.05] | -18.70 [-22.67, -13.54] | 3 | 0 |
| mtbench/d50 | pearl_vs_picospec_g2 | 10 | 6.35 [2.22, 12.25] | -5.96 [-9.61, -1.32] | 3 | 0 |
| mtbench/d50 | picospec_g2_vs_picospec | 10 | 0.98 [-5.10, 5.60] | 13.39 [8.63, 16.58] | 4 | 0 |
| mtbench/d50 | picospec_g8_vs_picospec | 10 | -6.50 [-13.94, 0.47] | -51.33 [-59.47, -41.92] | 5 | 0 |
| mtbench/d50 | markov_w0_dist_int_vs_picospec | 10 | 5.17 [4.02, 6.65] | -2.80 [-6.47, 1.00] | 5 | 0 |
| mtbench/d50 | pearl_vs_picospec | 10 | 7.39 [4.90, 9.77] | 8.23 [6.00, 10.36] | 5 | 0 |
| mtbench/d50 | picospec_g2_vs_picospec_g8 | 10 | 8.00 [-3.37, 20.89] | 42.77 [36.90, 46.91] | 7 | 0 |
| mtbench/d50 | picospec_vs_picospec_g8 | 10 | 6.95 [-0.47, 16.20] | 33.92 [29.54, 37.29] | 5 | 0 |
| mtbench/d50 | markov_w0_dist_int_vs_picospec_g8 | 10 | 12.48 [4.56, 22.43] | 32.07 [26.11, 37.27] | 7 | 0 |
| mtbench/d50 | pearl_vs_picospec_g8 | 10 | 14.86 [6.51, 25.47] | 39.36 [35.11, 42.56] | 7 | 0 |
| mtbench/d200 | picospec_vs_picospec_g2 | 10 | 7.85 [4.46, 12.68] | -2.70 [-5.93, 1.81] | 3 | 0 |
| mtbench/d200 | picospec_g8_vs_picospec_g2 | 10 | -1.17 [-7.05, 7.88] | -27.63 [-35.16, -16.86] | 6 | 0 |
| mtbench/d200 | markov_w0_dist_int_vs_picospec_g2 | 10 | 7.66 [3.45, 14.57] | -12.23 [-16.07, -6.21] | 1 | 0 |
| mtbench/d200 | pearl_vs_picospec_g2 | 10 | -6.46 [-12.08, 1.91] | -37.21 [-45.69, -25.46] | 7 | 0 |
| mtbench/d200 | picospec_g2_vs_picospec | 10 | -7.27 [-11.25, -4.27] | 2.63 [-1.84, 5.60] | 3 | 0 |
| mtbench/d200 | picospec_g8_vs_picospec | 10 | -8.36 [-11.55, -3.87] | -24.27 [-28.47, -18.40] | 6 | 0 |
| mtbench/d200 | markov_w0_dist_int_vs_picospec | 10 | -0.17 [-1.56, 1.75] | -9.28 [-10.74, -7.59] | 3 | 0 |
| mtbench/d200 | pearl_vs_picospec | 10 | -13.26 [-16.50, -8.80] | -33.60 [-38.87, -26.65] | 7 | 0 |
| mtbench/d200 | picospec_g2_vs_picospec_g8 | 10 | 1.18 [-7.30, 7.59] | 21.65 [14.42, 26.02] | 6 | 0 |
| mtbench/d200 | picospec_vs_picospec_g8 | 10 | 9.12 [4.03, 13.05] | 19.53 [15.54, 22.16] | 6 | 0 |
| mtbench/d200 | markov_w0_dist_int_vs_picospec_g8 | 10 | 8.94 [5.21, 12.25] | 12.06 [8.47, 14.72] | 6 | 0 |
| mtbench/d200 | pearl_vs_picospec_g8 | 10 | -5.35 [-8.29, -2.57] | -7.51 [-10.73, -4.39] | 7 | 0 |
| mtbench/pooled | picospec_vs_picospec_g2 | 10 | 1.96 [-1.13, 6.94] | -15.50 [-18.86, -10.46] | 14 | 0 |
| mtbench/pooled | picospec_g8_vs_picospec_g2 | 10 | -7.22 [-13.06, 1.01] | -64.40 [-73.71, -50.57] | 26 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec_g2 | 10 | 4.48 [1.41, 9.54] | -13.35 [-15.40, -10.41] | 8 | 0 |
| mtbench/pooled | pearl_vs_picospec_g2 | 10 | -0.85 [-4.93, 4.53] | -14.94 [-19.63, -9.29] | 16 | 0 |
| mtbench/pooled | picospec_g2_vs_picospec | 10 | -1.92 [-6.49, 1.14] | 13.42 [9.47, 15.87] | 14 | 0 |
| mtbench/pooled | picospec_g8_vs_picospec | 10 | -9.01 [-12.89, -4.87] | -42.34 [-47.01, -36.08] | 19 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec | 10 | 2.47 [1.04, 4.12] | 1.86 [-0.94, 4.12] | 15 | 0 |
| mtbench/pooled | pearl_vs_picospec | 10 | -2.75 [-4.59, -1.24] | 0.48 [-1.50, 2.37] | 22 | 0 |
| mtbench/pooled | picospec_g2_vs_picospec_g8 | 10 | 7.78 [-1.00, 15.02] | 39.17 [33.59, 42.43] | 26 | 0 |
| mtbench/pooled | picospec_vs_picospec_g8 | 10 | 9.90 [5.12, 14.80] | 29.75 [26.52, 31.98] | 19 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec_g8 | 10 | 12.61 [7.65, 17.84] | 31.05 [26.07, 34.66] | 26 | 0 |
| mtbench/pooled | pearl_vs_picospec_g8 | 10 | 6.87 [2.56, 10.70] | 30.08 [26.90, 32.29] | 27 | 0 |
| gsm8k/d10 | picospec_vs_picospec_g2 | 10 | 18.77 [12.92, 27.77] | -9.56 [-13.32, -4.40] | 1 | 0 |
| gsm8k/d10 | picospec_g8_vs_picospec_g2 | 10 | 12.54 [5.79, 20.80] | -43.68 [-51.41, -33.67] | 1 | 0 |
| gsm8k/d10 | markov_w0_dist_int_vs_picospec_g2 | 10 | 12.16 [6.82, 17.38] | -9.95 [-13.97, -6.51] | 2 | 1 |
| gsm8k/d10 | pearl_vs_picospec_g2 | 10 | 4.73 [-0.43, 10.31] | 4.40 [0.92, 8.32] | 3 | 1 |
| gsm8k/d10 | picospec_g2_vs_picospec | 10 | -15.81 [-21.74, -11.44] | 8.73 [4.22, 11.76] | 1 | 0 |
| gsm8k/d10 | picospec_g8_vs_picospec | 10 | -5.25 [-7.67, -2.62] | -31.13 [-34.14, -26.95] | 0 | 0 |
| gsm8k/d10 | markov_w0_dist_int_vs_picospec | 10 | -5.57 [-9.44, -1.87] | -0.35 [-4.90, 3.75] | 3 | 1 |
| gsm8k/d10 | pearl_vs_picospec | 10 | -11.82 [-18.21, -5.21] | 12.74 [7.33, 17.77] | 4 | 1 |
| gsm8k/d10 | picospec_g2_vs_picospec_g8 | 10 | -11.14 [-17.22, -5.47] | 30.40 [25.19, 33.95] | 1 | 0 |
| gsm8k/d10 | picospec_vs_picospec_g8 | 10 | 5.54 [2.70, 8.31] | 23.74 [21.23, 25.45] | 0 | 0 |
| gsm8k/d10 | markov_w0_dist_int_vs_picospec_g8 | 10 | -0.34 [-3.42, 2.83] | 23.47 [18.17, 28.06] | 3 | 1 |
| gsm8k/d10 | pearl_vs_picospec_g8 | 10 | -6.94 [-13.57, 0.10] | 33.46 [27.40, 38.56] | 4 | 1 |
| gsm8k/d25 | picospec_vs_picospec_g2 | 10 | 22.90 [18.20, 26.58] | -0.84 [-3.44, 2.45] | 1 | 1 |
| gsm8k/d25 | picospec_g8_vs_picospec_g2 | 10 | 24.91 [19.57, 31.08] | -33.46 [-39.54, -24.31] | 1 | 0 |
| gsm8k/d25 | markov_w0_dist_int_vs_picospec_g2 | 10 | 23.40 [18.42, 28.42] | -6.71 [-10.65, -1.82] | 2 | 1 |
| gsm8k/d25 | pearl_vs_picospec_g2 | 10 | 4.05 [-0.68, 9.08] | 3.45 [-0.47, 7.22] | 3 | 1 |
| gsm8k/d25 | picospec_g2_vs_picospec | 10 | -18.63 [-21.00, -15.40] | 0.83 [-2.51, 3.32] | 1 | 0 |
| gsm8k/d25 | picospec_g8_vs_picospec | 10 | 1.63 [-2.05, 5.87] | -32.35 [-38.68, -26.01] | 2 | 0 |
| gsm8k/d25 | markov_w0_dist_int_vs_picospec | 10 | 0.40 [-1.91, 2.87] | -5.83 [-8.67, -2.02] | 3 | 1 |
| gsm8k/d25 | pearl_vs_picospec | 10 | -15.34 [-18.53, -12.26] | 4.25 [0.15, 7.31] | 4 | 1 |
| gsm8k/d25 | picospec_g2_vs_picospec_g8 | 10 | -19.94 [-23.71, -16.36] | 25.07 [19.56, 28.33] | 1 | 0 |
| gsm8k/d25 | picospec_vs_picospec_g8 | 10 | -1.61 [-5.55, 2.09] | 24.44 [20.64, 27.89] | 2 | 1 |
| gsm8k/d25 | markov_w0_dist_int_vs_picospec_g8 | 10 | -1.21 [-6.00, 4.23] | 20.04 [15.66, 24.41] | 3 | 1 |
| gsm8k/d25 | pearl_vs_picospec_g8 | 10 | -16.70 [-22.50, -10.72] | 27.66 [21.34, 32.68] | 3 | 1 |
| gsm8k/d50 | picospec_vs_picospec_g2 | 10 | 26.97 [21.46, 34.89] | 9.07 [5.52, 13.82] | 2 | 1 |
| gsm8k/d50 | picospec_g8_vs_picospec_g2 | 10 | 38.34 [28.07, 49.10] | -17.00 [-25.69, -8.51] | 2 | 0 |
| gsm8k/d50 | markov_w0_dist_int_vs_picospec_g2 | 10 | 35.14 [29.08, 44.09] | -0.89 [-4.70, 5.05] | 2 | 0 |
| gsm8k/d50 | pearl_vs_picospec_g2 | 10 | 26.95 [22.62, 32.76] | 10.29 [7.62, 13.88] | 1 | 0 |
| gsm8k/d50 | picospec_g2_vs_picospec | 10 | -21.24 [-25.86, -17.67] | -9.97 [-16.04, -5.84] | 2 | 0 |
| gsm8k/d50 | picospec_g8_vs_picospec | 10 | 8.95 [2.18, 14.35] | -28.67 [-33.95, -23.04] | 2 | 0 |
| gsm8k/d50 | markov_w0_dist_int_vs_picospec | 10 | 6.43 [0.09, 11.76] | -10.95 [-16.50, -5.58] | 2 | 0 |
| gsm8k/d50 | pearl_vs_picospec | 10 | -0.02 [-5.17, 4.28] | 1.34 [-3.72, 5.51] | 3 | 0 |
| gsm8k/d50 | picospec_g2_vs_picospec_g8 | 10 | -27.72 [-32.93, -21.92] | 14.53 [7.85, 20.44] | 2 | 0 |
| gsm8k/d50 | picospec_vs_picospec_g8 | 10 | -8.22 [-12.55, -2.13] | 22.28 [18.73, 25.34] | 2 | 1 |
| gsm8k/d50 | markov_w0_dist_int_vs_picospec_g8 | 10 | -2.31 [-9.22, 5.03] | 13.77 [8.42, 18.59] | 2 | 0 |
| gsm8k/d50 | pearl_vs_picospec_g8 | 10 | -8.24 [-13.99, -1.87] | 23.32 [18.51, 27.59] | 2 | 0 |
| gsm8k/d200 | picospec_vs_picospec_g2 | 10 | 29.40 [24.22, 35.77] | 14.60 [11.11, 18.46] | 2 | 0 |
| gsm8k/d200 | picospec_g8_vs_picospec_g2 | 10 | 50.40 [40.59, 62.98] | 15.42 [9.69, 22.03] | 3 | 0 |
| gsm8k/d200 | markov_w0_dist_int_vs_picospec_g2 | 10 | 43.40 [35.71, 54.85] | 14.45 [9.69, 20.63] | 3 | 1 |
| gsm8k/d200 | pearl_vs_picospec_g2 | 10 | 43.83 [35.26, 57.02] | 8.79 [3.14, 16.41] | 5 | 1 |
| gsm8k/d200 | picospec_g2_vs_picospec | 10 | -22.72 [-26.35, -19.50] | -17.09 [-22.64, -12.50] | 2 | 0 |
| gsm8k/d200 | picospec_g8_vs_picospec | 10 | 16.23 [12.63, 21.13] | 0.97 [-2.01, 5.23] | 1 | 0 |
| gsm8k/d200 | markov_w0_dist_int_vs_picospec | 10 | 10.82 [7.90, 15.53] | -0.17 [-2.69, 3.82] | 3 | 1 |
| gsm8k/d200 | pearl_vs_picospec | 10 | 11.15 [7.39, 17.83] | -6.80 [-10.29, -1.09] | 5 | 1 |
| gsm8k/d200 | picospec_g2_vs_picospec_g8 | 10 | -33.51 [-38.64, -28.87] | -18.23 [-28.25, -10.73] | 3 | 0 |
| gsm8k/d200 | picospec_vs_picospec_g8 | 10 | -13.96 [-17.45, -11.22] | -0.97 [-5.52, 1.97] | 1 | 0 |
| gsm8k/d200 | markov_w0_dist_int_vs_picospec_g8 | 10 | -4.66 [-7.27, -2.14] | -1.15 [-3.80, 1.12] | 3 | 1 |
| gsm8k/d200 | pearl_vs_picospec_g8 | 10 | -4.37 [-6.77, -1.00] | -7.84 [-10.42, -4.45] | 5 | 1 |
| gsm8k/pooled | picospec_vs_picospec_g2 | 10 | 26.39 [22.32, 31.88] | 6.51 [3.84, 9.91] | 6 | 2 |
| gsm8k/pooled | picospec_g8_vs_picospec_g2 | 10 | 35.90 [27.99, 45.10] | -11.18 [-17.97, -3.63] | 7 | 0 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec_g2 | 10 | 31.77 [27.02, 38.58] | 2.50 [-0.03, 6.88] | 9 | 3 |
| gsm8k/pooled | pearl_vs_picospec_g2 | 10 | 24.75 [21.51, 29.70] | 6.83 [4.72, 10.25] | 12 | 3 |
| gsm8k/pooled | picospec_g2_vs_picospec | 10 | -20.88 [-24.17, -18.25] | -6.96 [-11.00, -3.99] | 6 | 0 |
| gsm8k/pooled | picospec_g8_vs_picospec | 10 | 7.53 [4.17, 11.20] | -18.92 [-22.92, -14.40] | 5 | 0 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec | 10 | 4.26 [1.38, 7.79] | -4.29 [-6.71, -1.37] | 11 | 3 |
| gsm8k/pooled | pearl_vs_picospec | 10 | -1.30 [-4.13, 1.55] | 0.35 [-1.89, 2.67] | 16 | 3 |
| gsm8k/pooled | picospec_g2_vs_picospec_g8 | 10 | -26.42 [-31.08, -21.87] | 10.05 [3.50, 15.23] | 7 | 0 |
| gsm8k/pooled | picospec_vs_picospec_g8 | 10 | -7.00 [-10.07, -4.00] | 15.91 [12.58, 18.65] | 5 | 2 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec_g8 | 10 | -3.04 [-6.50, 0.03] | 12.30 [8.61, 15.78] | 11 | 3 |
| gsm8k/pooled | pearl_vs_picospec_g8 | 10 | -8.21 [-12.20, -4.41] | 16.20 [12.50, 19.63] | 14 | 3 |
| humaneval/d10 | picospec_vs_picospec_g2 | 10 | 40.44 [33.44, 48.17] | 13.66 [7.98, 19.13] | 0 | 0 |
| humaneval/d10 | picospec_g8_vs_picospec_g2 | 10 | 55.49 [43.46, 69.07] | 15.88 [7.59, 23.61] | 0 | 0 |
| humaneval/d10 | markov_w0_dist_int_vs_picospec_g2 | 10 | 46.87 [36.53, 57.44] | 12.74 [6.76, 18.03] | 0 | 0 |
| humaneval/d10 | pearl_vs_picospec_g2 | 10 | 6.30 [1.26, 12.26] | 3.56 [0.43, 7.85] | 0 | 0 |
| humaneval/d10 | picospec_g2_vs_picospec | 10 | -28.79 [-32.51, -25.06] | -15.82 [-23.66, -8.67] | 0 | 0 |
| humaneval/d10 | picospec_g8_vs_picospec | 10 | 10.72 [4.17, 18.11] | 2.58 [-1.61, 7.29] | 0 | 0 |
| humaneval/d10 | markov_w0_dist_int_vs_picospec | 10 | 4.58 [-1.20, 11.62] | -1.06 [-5.44, 3.09] | 0 | 0 |
| humaneval/d10 | pearl_vs_picospec | 10 | -24.31 [-27.05, -20.99] | -11.69 [-17.51, -6.35] | 0 | 0 |
| humaneval/d10 | picospec_g2_vs_picospec_g8 | 10 | -35.69 [-40.85, -30.29] | -18.88 [-30.91, -8.21] | 0 | 0 |
| humaneval/d10 | picospec_vs_picospec_g8 | 10 | -9.68 [-15.33, -4.01] | -2.65 [-7.86, 1.59] | 0 | 0 |
| humaneval/d10 | markov_w0_dist_int_vs_picospec_g8 | 10 | -5.54 [-9.73, -0.42] | -3.74 [-9.04, 0.94] | 0 | 0 |
| humaneval/d10 | pearl_vs_picospec_g8 | 10 | -31.64 [-35.94, -26.89] | -14.65 [-25.57, -5.17] | 0 | 0 |
| humaneval/d25 | picospec_vs_picospec_g2 | 10 | 48.93 [41.27, 56.10] | 18.70 [14.58, 22.73] | 0 | 0 |
| humaneval/d25 | picospec_g8_vs_picospec_g2 | 10 | 77.17 [68.01, 88.33] | 22.87 [15.98, 29.63] | 0 | 0 |
| humaneval/d25 | markov_w0_dist_int_vs_picospec_g2 | 10 | 61.74 [51.70, 72.78] | 20.52 [13.94, 27.05] | 0 | 0 |
| humaneval/d25 | pearl_vs_picospec_g2 | 10 | 1.63 [-2.97, 6.52] | -0.81 [-4.74, 3.10] | 0 | 0 |
| humaneval/d25 | picospec_g2_vs_picospec | 10 | -32.86 [-35.94, -29.21] | -23.00 [-29.42, -17.07] | 0 | 0 |
| humaneval/d25 | picospec_g8_vs_picospec | 10 | 18.96 [13.59, 24.42] | 5.13 [0.44, 9.84] | 0 | 0 |
| humaneval/d25 | markov_w0_dist_int_vs_picospec | 10 | 8.60 [2.26, 14.06] | 2.24 [-1.58, 6.76] | 0 | 0 |
| humaneval/d25 | pearl_vs_picospec | 10 | -31.76 [-34.40, -28.97] | -23.99 [-30.20, -19.16] | 0 | 0 |
| humaneval/d25 | picospec_g2_vs_picospec_g8 | 10 | -43.56 [-46.90, -40.48] | -29.65 [-42.11, -19.01] | 0 | 0 |
| humaneval/d25 | picospec_vs_picospec_g8 | 10 | -15.94 [-19.63, -11.97] | -5.41 [-10.91, -0.44] | 0 | 0 |
| humaneval/d25 | markov_w0_dist_int_vs_picospec_g8 | 10 | -8.71 [-13.48, -3.84] | -3.04 [-6.21, 0.17] | 0 | 0 |
| humaneval/d25 | pearl_vs_picospec_g8 | 10 | -42.64 [-45.74, -39.28] | -30.70 [-41.62, -21.20] | 0 | 0 |
| humaneval/d50 | picospec_vs_picospec_g2 | 10 | 58.87 [53.75, 64.19] | 28.45 [25.94, 31.00] | 0 | 0 |
| humaneval/d50 | picospec_g8_vs_picospec_g2 | 10 | 109.87 [91.96, 129.22] | 31.91 [24.77, 38.48] | 0 | 0 |
| humaneval/d50 | markov_w0_dist_int_vs_picospec_g2 | 10 | 92.83 [80.87, 108.08] | 29.32 [23.29, 35.08] | 0 | 0 |
| humaneval/d50 | pearl_vs_picospec_g2 | 10 | 56.34 [52.21, 61.11] | 26.04 [23.76, 28.60] | 0 | 0 |
| humaneval/d50 | picospec_g2_vs_picospec | 10 | -37.06 [-39.10, -34.96] | -39.76 [-44.94, -35.02] | 0 | 0 |
| humaneval/d50 | picospec_g8_vs_picospec | 10 | 32.10 [23.95, 40.79] | 4.84 [-1.90, 11.32] | 0 | 0 |
| humaneval/d50 | markov_w0_dist_int_vs_picospec | 10 | 21.38 [16.79, 27.50] | 1.22 [-4.19, 6.95] | 0 | 0 |
| humaneval/d50 | pearl_vs_picospec | 10 | -1.59 [-4.21, 1.25] | -3.37 [-5.86, -0.76] | 0 | 0 |
| humaneval/d50 | picospec_g2_vs_picospec_g8 | 10 | -52.35 [-56.37, -47.91] | -46.87 [-62.56, -32.93] | 0 | 0 |
| humaneval/d50 | picospec_vs_picospec_g8 | 10 | -24.30 [-28.97, -19.32] | -5.09 [-12.76, 1.86] | 0 | 0 |
| humaneval/d50 | markov_w0_dist_int_vs_picospec_g8 | 10 | -8.12 [-13.80, -1.71] | -3.80 [-7.90, 0.57] | 0 | 0 |
| humaneval/d50 | pearl_vs_picospec_g8 | 10 | -25.51 [-30.53, -19.62] | -8.63 [-18.34, -0.22] | 0 | 0 |
| humaneval/d200 | picospec_vs_picospec_g2 | 10 | 53.83 [49.93, 57.85] | 29.34 [27.44, 31.30] | 0 | 0 |
| humaneval/d200 | picospec_g8_vs_picospec_g2 | 10 | 140.27 [124.34, 158.71] | 48.43 [44.81, 52.34] | 0 | 0 |
| humaneval/d200 | markov_w0_dist_int_vs_picospec_g2 | 10 | 122.71 [108.00, 139.04] | 45.83 [42.05, 49.57] | 0 | 0 |
| humaneval/d200 | pearl_vs_picospec_g2 | 10 | 174.68 [147.49, 208.38] | 52.27 [46.94, 57.53] | 0 | 0 |
| humaneval/d200 | picospec_g2_vs_picospec | 10 | -34.99 [-36.65, -33.30] | -41.52 [-45.57, -37.82] | 0 | 0 |
| humaneval/d200 | picospec_g8_vs_picospec | 10 | 56.19 [49.10, 64.49] | 27.02 [23.47, 30.97] | 0 | 0 |
| humaneval/d200 | markov_w0_dist_int_vs_picospec | 10 | 44.78 [37.43, 52.73] | 23.34 [19.56, 27.25] | 0 | 0 |
| humaneval/d200 | pearl_vs_picospec | 10 | 78.56 [64.22, 96.71] | 32.45 [26.44, 38.87] | 0 | 0 |
| humaneval/d200 | picospec_g2_vs_picospec_g8 | 10 | -58.38 [-61.35, -55.43] | -93.92 [-109.82, -81.20] | 0 | 0 |
| humaneval/d200 | picospec_vs_picospec_g8 | 10 | -35.98 [-39.21, -32.93] | -37.03 [-44.86, -30.66] | 0 | 0 |
| humaneval/d200 | markov_w0_dist_int_vs_picospec_g8 | 10 | -7.31 [-10.21, -4.04] | -5.04 [-7.65, -2.20] | 0 | 0 |
| humaneval/d200 | pearl_vs_picospec_g8 | 10 | 14.32 [9.34, 20.66] | 7.44 [3.16, 12.31] | 0 | 0 |
| humaneval/pooled | picospec_vs_picospec_g2 | 10 | 52.08 [47.72, 56.50] | 24.67 [21.94, 27.35] | 0 | 0 |
| humaneval/pooled | picospec_g8_vs_picospec_g2 | 10 | 106.93 [94.07, 121.82] | 34.88 [29.26, 40.28] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec_g2 | 10 | 91.55 [80.09, 103.75] | 32.24 [27.36, 37.02] | 0 | 0 |
| humaneval/pooled | pearl_vs_picospec_g2 | 10 | 66.88 [59.66, 75.38] | 28.95 [25.74, 32.34] | 0 | 0 |
| humaneval/pooled | picospec_g2_vs_picospec | 10 | -34.24 [-36.10, -32.30] | -32.74 [-37.66, -28.11] | 0 | 0 |
| humaneval/pooled | picospec_g8_vs_picospec | 10 | 36.07 [30.38, 42.73] | 13.55 [9.27, 18.27] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec | 10 | 25.96 [21.06, 31.37] | 10.05 [6.46, 13.96] | 0 | 0 |
| humaneval/pooled | pearl_vs_picospec | 10 | 9.74 [7.08, 13.11] | 5.69 [3.53, 8.07] | 0 | 0 |
| humaneval/pooled | picospec_g2_vs_picospec_g8 | 10 | -51.67 [-54.92, -48.47] | -53.56 [-67.45, -41.36] | 0 | 0 |
| humaneval/pooled | picospec_vs_picospec_g8 | 10 | -26.51 [-29.94, -23.30] | -15.68 [-22.35, -10.22] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec_g8 | 10 | -7.43 [-9.47, -5.02] | -4.05 [-6.79, -1.31] | 0 | 0 |
| humaneval/pooled | pearl_vs_picospec_g8 | 10 | -19.35 [-22.17, -16.52] | -9.10 [-14.81, -4.44] | 0 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
