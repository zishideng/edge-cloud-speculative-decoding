# Progress probe: qwen_full_110

State: complete; 2310/2310 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | sync_g4 | 110 | 30779 | 25.106 | 0.2901 | 8 | 0.00 |
| all/low | fixed_g2 | 110 | 30785 | 34.103 | 0.2965 | 7 | 40.79 |
| all/low | fixed_fast | 110 | 30780 | 33.723 | 0.3651 | 8 | 36.14 |
| all/low | fixed_g8 | 110 | 30725 | 26.144 | 0.5196 | 7 | 24.32 |
| all/low | adaedl | 110 | 30837 | 21.429 | 0.3576 | 7 | 0.00 |
| all/low | markov_w0_robust | 110 | 30661 | 32.632 | 0.3184 | 6 | 40.23 |
| all/low | markov_w05_robust | 110 | 30753 | 33.377 | 0.2924 | 7 | 41.56 |
| all/high | sync_g4 | 110 | 30772 | 13.149 | 0.4543 | 5 | 0.00 |
| all/high | fixed_g2 | 110 | 30712 | 13.947 | 0.4690 | 5 | 40.97 |
| all/high | fixed_fast | 110 | 30772 | 17.959 | 0.4622 | 5 | 36.35 |
| all/high | fixed_g8 | 110 | 30781 | 20.225 | 0.5787 | 5 | 24.99 |
| all/high | adaedl | 110 | 30749 | 12.300 | 0.5091 | 5 | 0.00 |
| all/high | markov_w0_robust | 110 | 30753 | 20.757 | 0.5299 | 5 | 35.08 |
| all/high | markov_w05_robust | 110 | 30588 | 17.956 | 0.4527 | 5 | 43.34 |
| all/dynamic | sync_g4 | 110 | 30780 | 17.786 | 0.3659 | 7 | 0.00 |
| all/dynamic | fixed_g2 | 110 | 30692 | 22.947 | 0.3495 | 6 | 40.74 |
| all/dynamic | fixed_fast | 110 | 30780 | 25.562 | 0.4065 | 7 | 36.11 |
| all/dynamic | fixed_g8 | 110 | 30799 | 23.081 | 0.5497 | 6 | 24.33 |
| all/dynamic | adaedl | 110 | 30957 | 15.780 | 0.4315 | 7 | 0.00 |
| all/dynamic | markov_w0_robust | 110 | 30633 | 25.144 | 0.4204 | 6 | 37.99 |
| all/dynamic | markov_w05_robust | 110 | 30835 | 25.258 | 0.3557 | 6 | 43.01 |
| all/pooled | sync_g4 | 330 | 92331 | 17.431 | 0.3701 | 20 | 0.00 |
| all/pooled | fixed_g2 | 330 | 92189 | 20.753 | 0.3716 | 18 | 40.83 |
| all/pooled | fixed_fast | 330 | 92332 | 24.105 | 0.4113 | 20 | 36.20 |
| all/pooled | fixed_g8 | 330 | 92305 | 22.896 | 0.5493 | 18 | 24.55 |
| all/pooled | adaedl | 330 | 92543 | 15.683 | 0.4327 | 19 | 0.00 |
| all/pooled | markov_w0_robust | 330 | 92047 | 25.291 | 0.4230 | 17 | 37.37 |
| all/pooled | markov_w05_robust | 330 | 92176 | 23.969 | 0.3667 | 18 | 42.66 |
| gsm8k/low | sync_g4 | 50 | 12969 | 27.252 | 0.2619 | 0 | 0.00 |
| gsm8k/low | fixed_g2 | 50 | 12990 | 36.933 | 0.2614 | 0 | 50.20 |
| gsm8k/low | fixed_fast | 50 | 12969 | 42.241 | 0.2866 | 0 | 50.48 |
| gsm8k/low | fixed_g8 | 50 | 12966 | 36.502 | 0.3628 | 0 | 40.93 |
| gsm8k/low | adaedl | 50 | 12955 | 23.201 | 0.3198 | 0 | 0.00 |
| gsm8k/low | markov_w0_robust | 50 | 12988 | 37.894 | 0.2711 | 0 | 50.26 |
| gsm8k/low | markov_w05_robust | 50 | 12962 | 37.431 | 0.2671 | 0 | 49.59 |
| gsm8k/high | sync_g4 | 50 | 13026 | 14.717 | 0.4056 | 0 | 0.00 |
| gsm8k/high | fixed_g2 | 50 | 12999 | 15.672 | 0.4152 | 0 | 50.31 |
| gsm8k/high | fixed_fast | 50 | 13041 | 21.922 | 0.3721 | 0 | 50.25 |
| gsm8k/high | fixed_g8 | 50 | 13055 | 28.072 | 0.4118 | 0 | 41.17 |
| gsm8k/high | adaedl | 50 | 13043 | 14.691 | 0.4286 | 0 | 0.00 |
| gsm8k/high | markov_w0_robust | 50 | 13156 | 27.105 | 0.3977 | 0 | 48.86 |
| gsm8k/high | markov_w05_robust | 50 | 13007 | 23.078 | 0.3772 | 0 | 52.68 |
| gsm8k/dynamic | sync_g4 | 50 | 12991 | 20.912 | 0.3132 | 0 | 0.00 |
| gsm8k/dynamic | fixed_g2 | 50 | 13004 | 26.769 | 0.2991 | 0 | 50.31 |
| gsm8k/dynamic | fixed_fast | 50 | 12991 | 32.695 | 0.3179 | 0 | 50.45 |
| gsm8k/dynamic | fixed_g8 | 50 | 13055 | 33.064 | 0.3821 | 0 | 40.85 |
| gsm8k/dynamic | adaedl | 50 | 13039 | 18.365 | 0.3692 | 0 | 0.00 |
| gsm8k/dynamic | markov_w0_robust | 50 | 13035 | 32.383 | 0.3253 | 0 | 50.59 |
| gsm8k/dynamic | markov_w05_robust | 50 | 13070 | 31.373 | 0.3058 | 0 | 52.12 |
| gsm8k/pooled | sync_g4 | 150 | 38986 | 19.668 | 0.3270 | 0 | 0.00 |
| gsm8k/pooled | fixed_g2 | 150 | 38993 | 23.392 | 0.3252 | 0 | 50.27 |
| gsm8k/pooled | fixed_fast | 150 | 39001 | 30.018 | 0.3256 | 0 | 50.39 |
| gsm8k/pooled | fixed_g8 | 150 | 39076 | 32.158 | 0.3856 | 0 | 40.98 |
| gsm8k/pooled | adaedl | 150 | 39037 | 18.105 | 0.3727 | 0 | 0.00 |
| gsm8k/pooled | markov_w0_robust | 150 | 39179 | 31.836 | 0.3317 | 0 | 49.82 |
| gsm8k/pooled | markov_w05_robust | 150 | 39039 | 29.430 | 0.3167 | 0 | 51.52 |
| humaneval/low | sync_g4 | 30 | 10351 | 27.559 | 0.2650 | 3 | 0.00 |
| humaneval/low | fixed_g2 | 30 | 10411 | 39.435 | 0.2682 | 2 | 45.64 |
| humaneval/low | fixed_fast | 30 | 10351 | 38.594 | 0.3207 | 3 | 42.92 |
| humaneval/low | fixed_g8 | 30 | 10305 | 31.125 | 0.4348 | 2 | 30.91 |
| humaneval/low | adaedl | 30 | 10423 | 22.346 | 0.3336 | 2 | 0.00 |
| humaneval/low | markov_w0_robust | 30 | 10267 | 36.488 | 0.2940 | 1 | 44.97 |
| humaneval/low | markov_w05_robust | 30 | 10392 | 36.828 | 0.2789 | 2 | 44.97 |
| humaneval/high | sync_g4 | 30 | 10343 | 13.946 | 0.4259 | 1 | 0.00 |
| humaneval/high | fixed_g2 | 30 | 10328 | 14.412 | 0.4481 | 1 | 45.84 |
| humaneval/high | fixed_fast | 30 | 10328 | 19.711 | 0.4130 | 1 | 43.05 |
| humaneval/high | fixed_g8 | 30 | 10350 | 23.284 | 0.4929 | 1 | 31.10 |
| humaneval/high | adaedl | 30 | 10315 | 13.291 | 0.4703 | 1 | 0.00 |
| humaneval/high | markov_w0_robust | 30 | 10266 | 22.974 | 0.4721 | 1 | 42.02 |
| humaneval/high | markov_w05_robust | 30 | 10201 | 20.580 | 0.4321 | 1 | 45.77 |
| humaneval/dynamic | sync_g4 | 30 | 10423 | 18.957 | 0.3414 | 2 | 0.00 |
| humaneval/dynamic | fixed_g2 | 30 | 10360 | 23.797 | 0.3302 | 1 | 45.35 |
| humaneval/dynamic | fixed_fast | 30 | 10423 | 27.423 | 0.3657 | 2 | 42.53 |
| humaneval/dynamic | fixed_g8 | 30 | 10326 | 27.156 | 0.4621 | 1 | 30.97 |
| humaneval/dynamic | adaedl | 30 | 10499 | 16.519 | 0.4066 | 2 | 0.00 |
| humaneval/dynamic | markov_w0_robust | 30 | 10314 | 26.850 | 0.3911 | 1 | 43.45 |
| humaneval/dynamic | markov_w05_robust | 30 | 10356 | 26.484 | 0.3548 | 1 | 45.57 |
| humaneval/pooled | sync_g4 | 90 | 31117 | 18.666 | 0.3441 | 6 | 0.00 |
| humaneval/pooled | fixed_g2 | 90 | 31099 | 21.963 | 0.3486 | 4 | 45.61 |
| humaneval/pooled | fixed_fast | 90 | 31102 | 26.532 | 0.3664 | 6 | 42.83 |
| humaneval/pooled | fixed_g8 | 90 | 30981 | 26.804 | 0.4633 | 4 | 30.99 |
| humaneval/pooled | adaedl | 90 | 31237 | 16.633 | 0.4033 | 5 | 0.00 |
| humaneval/pooled | markov_w0_robust | 90 | 30847 | 27.731 | 0.3858 | 3 | 43.29 |
| humaneval/pooled | markov_w05_robust | 90 | 30949 | 26.478 | 0.3548 | 4 | 45.46 |
| mtbench/low | sync_g4 | 30 | 7459 | 19.917 | 0.3742 | 5 | 0.00 |
| mtbench/low | fixed_g2 | 30 | 7384 | 25.729 | 0.3984 | 5 | 22.15 |
| mtbench/low | fixed_fast | 30 | 7460 | 22.103 | 0.5631 | 5 | 13.53 |
| mtbench/low | fixed_g8 | 30 | 7454 | 15.246 | 0.9094 | 5 | 4.98 |
| mtbench/low | adaedl | 30 | 7459 | 18.007 | 0.4568 | 5 | 0.00 |
| mtbench/low | markov_w0_robust | 30 | 7406 | 23.476 | 0.4353 | 5 | 21.98 |
| mtbench/low | markov_w05_robust | 30 | 7399 | 25.259 | 0.3557 | 5 | 23.72 |
| mtbench/high | sync_g4 | 30 | 7403 | 10.375 | 0.5796 | 4 | 0.00 |
| mtbench/high | fixed_g2 | 30 | 7385 | 11.258 | 0.5931 | 4 | 22.32 |
| mtbench/high | fixed_fast | 30 | 7403 | 12.451 | 0.6894 | 4 | 13.82 |
| mtbench/high | fixed_g8 | 30 | 7376 | 12.045 | 0.9945 | 4 | 5.55 |
| mtbench/high | adaedl | 30 | 7391 | 8.840 | 0.7054 | 4 | 0.00 |
| mtbench/high | markov_w0_robust | 30 | 7331 | 13.345 | 0.8481 | 4 | 16.59 |
| mtbench/high | markov_w05_robust | 30 | 7380 | 11.456 | 0.6142 | 4 | 20.33 |
| mtbench/dynamic | sync_g4 | 30 | 7366 | 13.165 | 0.4934 | 5 | 0.00 |
| mtbench/dynamic | fixed_g2 | 30 | 7328 | 17.600 | 0.4663 | 5 | 22.05 |
| mtbench/dynamic | fixed_fast | 30 | 7366 | 17.262 | 0.6206 | 5 | 13.54 |
| mtbench/dynamic | fixed_g8 | 30 | 7418 | 13.262 | 0.9665 | 5 | 4.86 |
| mtbench/dynamic | adaedl | 30 | 7419 | 12.038 | 0.5761 | 5 | 0.00 |
| mtbench/dynamic | markov_w0_robust | 30 | 7284 | 16.874 | 0.6321 | 5 | 19.31 |
| mtbench/dynamic | markov_w05_robust | 30 | 7409 | 17.932 | 0.4449 | 5 | 23.27 |
| mtbench/pooled | sync_g4 | 90 | 22228 | 13.491 | 0.4821 | 14 | 0.00 |
| mtbench/pooled | fixed_g2 | 90 | 22097 | 16.256 | 0.4860 | 14 | 22.17 |
| mtbench/pooled | fixed_fast | 90 | 22229 | 16.359 | 0.6242 | 14 | 13.63 |
| mtbench/pooled | fixed_g8 | 90 | 22248 | 13.397 | 0.9567 | 14 | 5.12 |
| mtbench/pooled | adaedl | 90 | 22269 | 11.930 | 0.5791 | 14 | 0.00 |
| mtbench/pooled | markov_w0_robust | 90 | 22021 | 16.985 | 0.6378 | 14 | 18.70 |
| mtbench/pooled | markov_w05_robust | 90 | 22188 | 16.432 | 0.4715 | 14 | 22.50 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | sync_g4 | 110 | -25.55 [-28.92, -22.05] | 20.53 [17.22, 23.46] | 1 | 0 |
| all/low | fixed_g2 | 110 | 1.13 [-4.09, 6.24] | 18.78 [15.75, 21.42] | 17 | 0 |
| all/low | fixed_g8 | 110 | -22.47 [-25.66, -18.68] | -42.31 [-47.16, -37.36] | 24 | 0 |
| all/low | adaedl | 110 | -36.46 [-39.80, -32.71] | 2.05 [-1.49, 5.62] | 17 | 0 |
| all/low | markov_w0_robust | 110 | -3.23 [-7.15, 1.09] | 12.78 [9.31, 15.83] | 17 | 0 |
| all/low | markov_w05_robust | 110 | -1.03 [-5.81, 4.07] | 19.91 [15.67, 24.01] | 18 | 0 |
| all/low | sync_g4_vs_fixed_g2 | 110 | -26.38 [-28.72, -23.49] | 2.15 [0.74, 3.59] | 17 | 1 |
| all/low | fixed_fast_vs_fixed_g2 | 110 | -1.11 [-5.88, 4.26] | -23.12 [-27.27, -18.69] | 17 | 1 |
| all/low | fixed_g8_vs_fixed_g2 | 110 | -23.34 [-28.83, -16.34] | -75.20 [-86.57, -63.76] | 30 | 1 |
| all/low | adaedl_vs_fixed_g2 | 110 | -37.16 [-40.13, -33.21] | -20.60 [-23.28, -17.67] | 19 | 0 |
| all/low | markov_w0_robust_vs_fixed_g2 | 110 | -4.31 [-7.87, 0.26] | -7.39 [-10.25, -4.67] | 14 | 0 |
| all/low | markov_w05_robust_vs_fixed_g2 | 110 | -2.13 [-5.78, 2.31] | 1.39 [-1.49, 4.28] | 13 | 0 |
| all/low | sync_g4_vs_fixed_g8 | 110 | -3.97 [-10.98, 3.00] | 44.15 [39.81, 47.92] | 24 | 1 |
| all/low | fixed_g2_vs_fixed_g8 | 110 | 30.44 [19.53, 40.52] | 42.92 [38.94, 46.40] | 30 | 1 |
| all/low | fixed_fast_vs_fixed_g8 | 110 | 28.99 [22.97, 34.52] | 29.73 [27.20, 32.05] | 24 | 1 |
| all/low | adaedl_vs_fixed_g8 | 110 | -18.04 [-23.77, -11.84] | 31.17 [26.37, 35.69] | 23 | 1 |
| all/low | markov_w0_robust_vs_fixed_g8 | 110 | 24.82 [16.60, 32.81] | 38.71 [34.46, 42.49] | 34 | 0 |
| all/low | markov_w05_robust_vs_fixed_g8 | 110 | 27.66 [17.81, 37.06] | 43.72 [38.62, 48.20] | 34 | 1 |
| all/low | fixed_g2_vs_sync_g4 | 110 | 35.84 [30.70, 40.29] | -2.20 [-3.73, -0.74] | 17 | 0 |
| all/low | fixed_fast_vs_sync_g4 | 110 | 34.32 [28.28, 40.68] | -25.83 [-30.65, -20.80] | 1 | 0 |
| all/low | fixed_g8_vs_sync_g4 | 110 | 4.14 [-2.92, 12.34] | -79.06 [-92.01, -66.13] | 24 | 0 |
| all/low | adaedl_vs_sync_g4 | 110 | -14.64 [-17.01, -11.63] | -23.25 [-25.48, -20.61] | 17 | 0 |
| all/low | markov_w0_robust_vs_sync_g4 | 110 | 29.98 [26.27, 33.58] | -9.75 [-12.47, -7.14] | 17 | 0 |
| all/low | markov_w05_robust_vs_sync_g4 | 110 | 32.94 [28.77, 36.75] | -0.78 [-2.90, 1.42] | 18 | 0 |
| all/low | sync_g4_vs_adaedl | 110 | 17.16 [13.16, 20.50] | 18.87 [17.09, 20.30] | 17 | 1 |
| all/low | fixed_g2_vs_adaedl | 110 | 59.14 [49.72, 67.04] | 17.08 [15.02, 18.89] | 19 | 0 |
| all/low | fixed_fast_vs_adaedl | 110 | 57.37 [48.61, 66.13] | -2.09 [-5.96, 1.47] | 17 | 1 |
| all/low | fixed_g8_vs_adaedl | 110 | 22.00 [13.42, 31.18] | -45.28 [-55.50, -35.82] | 23 | 1 |
| all/low | markov_w0_robust_vs_adaedl | 110 | 52.28 [44.20, 58.44] | 10.95 [7.59, 13.37] | 23 | 0 |
| all/low | markov_w05_robust_vs_adaedl | 110 | 55.75 [47.22, 62.48] | 18.23 [15.55, 20.48] | 23 | 0 |
| all/high | sync_g4 | 110 | -26.79 [-28.58, -24.89] | 1.70 [-1.23, 4.68] | 2 | 0 |
| all/high | fixed_g2 | 110 | -22.34 [-24.60, -20.02] | -1.49 [-4.83, 1.81] | 19 | 0 |
| all/high | fixed_g8 | 110 | 12.62 [9.06, 16.52] | -25.22 [-29.23, -21.11] | 22 | 0 |
| all/high | adaedl | 110 | -31.51 [-32.53, -30.40] | -10.16 [-11.95, -8.30] | 19 | 0 |
| all/high | markov_w0_robust | 110 | 15.58 [13.41, 17.93] | -14.66 [-16.98, -12.23] | 25 | 0 |
| all/high | markov_w05_robust | 110 | -0.01 [-2.80, 2.82] | 2.05 [-0.43, 4.42] | 16 | 0 |
| all/high | sync_g4_vs_fixed_g2 | 110 | -5.72 [-7.03, -4.01] | 3.15 [2.16, 4.35] | 19 | 0 |
| all/high | fixed_fast_vs_fixed_g2 | 110 | 28.77 [25.03, 32.63] | 1.47 [-1.85, 4.61] | 19 | 0 |
| all/high | fixed_g8_vs_fixed_g2 | 110 | 45.01 [36.55, 53.97] | -23.38 [-31.28, -15.67] | 33 | 0 |
| all/high | adaedl_vs_fixed_g2 | 110 | -11.81 [-14.18, -9.24] | -8.55 [-10.94, -6.20] | 21 | 0 |
| all/high | markov_w0_robust_vs_fixed_g2 | 110 | 48.83 [42.40, 55.73] | -12.98 [-18.44, -7.61] | 25 | 0 |
| all/high | markov_w05_robust_vs_fixed_g2 | 110 | 28.75 [22.65, 35.22] | 3.49 [1.47, 5.66] | 17 | 0 |
| all/high | sync_g4_vs_fixed_g8 | 110 | -34.99 [-38.52, -31.24] | 21.50 [16.59, 26.11] | 23 | 0 |
| all/high | fixed_g2_vs_fixed_g8 | 110 | -31.04 [-35.05, -26.77] | 18.95 [13.55, 23.83] | 33 | 0 |
| all/high | fixed_fast_vs_fixed_g8 | 110 | -11.20 [-14.18, -8.31] | 20.14 [17.43, 22.62] | 22 | 0 |
| all/high | adaedl_vs_fixed_g8 | 110 | -39.18 [-41.49, -36.75] | 12.02 [8.01, 15.82] | 19 | 0 |
| all/high | markov_w0_robust_vs_fixed_g8 | 110 | 2.63 [0.08, 5.09] | 8.43 [6.40, 10.37] | 30 | 0 |
| all/high | markov_w05_robust_vs_fixed_g8 | 110 | -11.22 [-14.24, -8.67] | 21.78 [17.37, 25.67] | 30 | 0 |
| all/high | fixed_g2_vs_sync_g4 | 110 | 6.07 [4.18, 7.56] | -3.25 [-4.54, -2.21] | 19 | 0 |
| all/high | fixed_fast_vs_sync_g4 | 110 | 36.59 [33.14, 40.03] | -1.73 [-4.91, 1.22] | 2 | 0 |
| all/high | fixed_g8_vs_sync_g4 | 110 | 53.82 [45.43, 62.66] | -27.39 [-35.33, -19.89] | 23 | 0 |
| all/high | adaedl_vs_sync_g4 | 110 | -6.45 [-8.49, -4.35] | -12.07 [-14.39, -9.85] | 20 | 0 |
| all/high | markov_w0_robust_vs_sync_g4 | 110 | 57.87 [51.61, 64.54] | -16.65 [-22.08, -11.32] | 25 | 0 |
| all/high | markov_w05_robust_vs_sync_g4 | 110 | 36.57 [30.39, 42.96] | 0.36 [-1.58, 2.33] | 18 | 0 |
| all/high | sync_g4_vs_adaedl | 110 | 6.90 [4.54, 9.28] | 10.77 [8.97, 12.58] | 20 | 0 |
| all/high | fixed_g2_vs_adaedl | 110 | 13.39 [10.18, 16.53] | 7.87 [5.84, 9.86] | 21 | 0 |
| all/high | fixed_fast_vs_adaedl | 110 | 46.01 [43.68, 48.22] | 9.22 [7.66, 10.67] | 19 | 0 |
| all/high | fixed_g8_vs_adaedl | 110 | 64.43 [58.11, 70.92] | -13.67 [-18.79, -8.71] | 19 | 0 |
| all/high | markov_w0_robust_vs_adaedl | 110 | 68.76 [64.39, 73.28] | -4.08 [-7.22, -0.99] | 26 | 0 |
| all/high | markov_w05_robust_vs_adaedl | 110 | 45.99 [40.97, 50.74] | 11.09 [9.45, 12.50] | 28 | 0 |
| all/dynamic | sync_g4 | 110 | -30.42 [-35.28, -26.37] | 10.01 [5.25, 13.96] | 0 | 0 |
| all/dynamic | fixed_g2 | 110 | -10.23 [-13.11, -7.39] | 14.03 [11.50, 16.56] | 13 | 0 |
| all/dynamic | fixed_g8 | 110 | -9.71 [-13.69, -4.96] | -35.21 [-40.08, -30.10] | 25 | 0 |
| all/dynamic | adaedl | 110 | -38.27 [-40.73, -35.72] | -6.13 [-9.44, -2.98] | 15 | 0 |
| all/dynamic | markov_w0_robust | 110 | -1.64 [-5.91, 2.01] | -3.42 [-6.73, -0.47] | 17 | 0 |
| all/dynamic | markov_w05_robust | 110 | -1.19 [-3.38, 0.89] | 12.52 [8.97, 15.83] | 19 | 0 |
| all/dynamic | sync_g4_vs_fixed_g2 | 110 | -22.49 [-27.71, -18.87] | -4.68 [-9.81, -1.64] | 13 | 1 |
| all/dynamic | fixed_fast_vs_fixed_g2 | 110 | 11.39 [7.98, 15.09] | -16.32 [-19.84, -12.99] | 13 | 1 |
| all/dynamic | fixed_g8_vs_fixed_g2 | 110 | 0.58 [-6.07, 7.83] | -57.28 [-67.55, -47.63] | 28 | 0 |
| all/dynamic | adaedl_vs_fixed_g2 | 110 | -31.24 [-33.62, -28.85] | -23.45 [-26.22, -21.09] | 19 | 1 |
| all/dynamic | markov_w0_robust_vs_fixed_g2 | 110 | 9.57 [4.04, 14.82] | -20.29 [-25.16, -15.98] | 13 | 0 |
| all/dynamic | markov_w05_robust_vs_fixed_g2 | 110 | 10.07 [6.73, 13.68] | -1.76 [-3.80, 0.21] | 12 | 0 |
| all/dynamic | sync_g4_vs_fixed_g8 | 110 | -22.94 [-28.94, -16.70] | 33.44 [28.45, 38.13] | 25 | 1 |
| all/dynamic | fixed_g2_vs_fixed_g8 | 110 | -0.58 [-7.27, 6.46] | 36.42 [32.26, 40.32] | 28 | 0 |
| all/dynamic | fixed_fast_vs_fixed_g8 | 110 | 10.75 [5.22, 15.86] | 26.04 [23.14, 28.61] | 25 | 1 |
| all/dynamic | adaedl_vs_fixed_g8 | 110 | -31.63 [-35.72, -27.37] | 21.50 [16.42, 26.21] | 22 | 1 |
| all/dynamic | markov_w0_robust_vs_fixed_g8 | 110 | 8.94 [2.91, 15.01] | 23.51 [19.38, 27.27] | 24 | 0 |
| all/dynamic | markov_w05_robust_vs_fixed_g8 | 110 | 9.43 [3.64, 15.28] | 35.30 [30.19, 39.83] | 33 | 0 |
| all/dynamic | fixed_g2_vs_sync_g4 | 110 | 29.02 [23.25, 38.33] | 4.47 [1.61, 8.93] | 13 | 0 |
| all/dynamic | fixed_fast_vs_sync_g4 | 110 | 43.72 [35.82, 54.51] | -11.12 [-16.23, -5.55] | 0 | 0 |
| all/dynamic | fixed_g8_vs_sync_g4 | 110 | 29.77 [20.05, 40.72] | -50.25 [-61.63, -39.77] | 25 | 0 |
| all/dynamic | adaedl_vs_sync_g4 | 110 | -11.28 [-14.21, -6.88] | -17.94 [-20.86, -13.94] | 15 | 0 |
| all/dynamic | markov_w0_robust_vs_sync_g4 | 110 | 41.37 [36.01, 47.44] | -14.92 [-19.06, -10.99] | 17 | 0 |
| all/dynamic | markov_w05_robust_vs_sync_g4 | 110 | 42.01 [35.05, 52.42] | 2.79 [-0.76, 7.99] | 19 | 0 |
| all/dynamic | sync_g4_vs_adaedl | 110 | 12.72 [7.38, 16.56] | 15.21 [12.24, 17.26] | 15 | 0 |
| all/dynamic | fixed_g2_vs_adaedl | 110 | 45.42 [40.54, 50.64] | 19.00 [17.41, 20.77] | 19 | 0 |
| all/dynamic | fixed_fast_vs_adaedl | 110 | 61.99 [55.56, 68.72] | 5.78 [2.90, 8.63] | 15 | 0 |
| all/dynamic | fixed_g8_vs_adaedl | 110 | 46.27 [37.68, 55.57] | -27.40 [-35.53, -19.65] | 22 | 0 |
| all/dynamic | markov_w0_robust_vs_adaedl | 110 | 59.34 [53.99, 65.19] | 2.56 [-0.41, 5.67] | 15 | 0 |
| all/dynamic | markov_w05_robust_vs_adaedl | 110 | 60.07 [55.20, 65.16] | 17.57 [15.57, 19.68] | 17 | 0 |
| all/pooled | sync_g4 | 110 | -27.69 [-30.04, -25.15] | 10.01 [7.01, 12.97] | 3 | 0 |
| all/pooled | fixed_g2 | 110 | -13.91 [-16.53, -11.29] | 9.63 [6.87, 12.34] | 49 | 0 |
| all/pooled | fixed_g8 | 110 | -5.02 [-8.25, -1.45] | -33.57 [-37.87, -29.01] | 71 | 0 |
| all/pooled | adaedl | 110 | -34.94 [-36.53, -33.27] | -5.21 [-7.84, -2.58] | 51 | 0 |
| all/pooled | markov_w0_robust | 110 | 4.92 [2.90, 6.82] | -2.86 [-4.36, -1.35] | 59 | 0 |
| all/pooled | markov_w05_robust | 110 | -0.57 [-2.30, 1.30] | 10.82 [7.67, 13.82] | 53 | 0 |
| all/pooled | sync_g4_vs_fixed_g2 | 110 | -16.00 [-18.12, -14.30] | 0.42 [-1.19, 1.75] | 49 | 2 |
| all/pooled | fixed_fast_vs_fixed_g2 | 110 | 16.16 [12.72, 19.80] | -10.66 [-14.07, -7.38] | 49 | 2 |
| all/pooled | fixed_g8_vs_fixed_g2 | 110 | 10.33 [3.68, 17.62] | -47.81 [-57.15, -38.67] | 91 | 1 |
| all/pooled | adaedl_vs_fixed_g2 | 110 | -24.43 [-25.96, -22.86] | -16.42 [-18.06, -14.87] | 59 | 1 |
| all/pooled | markov_w0_robust_vs_fixed_g2 | 110 | 21.87 [17.80, 26.16] | -13.83 [-17.42, -10.28] | 52 | 0 |
| all/pooled | markov_w05_robust_vs_fixed_g2 | 110 | 15.50 [12.06, 19.20] | 1.32 [-0.04, 2.73] | 42 | 0 |
| all/pooled | sync_g4_vs_fixed_g8 | 110 | -23.87 [-28.36, -18.98] | 32.63 [28.06, 36.82] | 72 | 2 |
| all/pooled | fixed_g2_vs_fixed_g8 | 110 | -9.36 [-14.98, -3.55] | 32.35 [27.88, 36.37] | 91 | 1 |
| all/pooled | fixed_fast_vs_fixed_g8 | 110 | 5.28 [1.47, 8.99] | 25.13 [22.49, 27.47] | 71 | 2 |
| all/pooled | adaedl_vs_fixed_g8 | 110 | -31.50 [-35.05, -27.80] | 21.24 [16.69, 25.45] | 64 | 2 |
| all/pooled | markov_w0_robust_vs_fixed_g8 | 110 | 10.46 [6.08, 14.76] | 22.99 [19.96, 25.82] | 88 | 0 |
| all/pooled | markov_w05_robust_vs_fixed_g8 | 110 | 4.69 [0.33, 8.80] | 33.24 [28.48, 37.43] | 97 | 1 |
| all/pooled | fixed_g2_vs_sync_g4 | 110 | 19.05 [16.69, 22.13] | -0.42 [-1.78, 1.18] | 49 | 0 |
| all/pooled | fixed_fast_vs_sync_g4 | 110 | 38.29 [33.59, 42.93] | -11.12 [-14.90, -7.54] | 3 | 0 |
| all/pooled | fixed_g8_vs_sync_g4 | 110 | 31.35 [23.43, 39.59] | -48.43 [-58.27, -39.01] | 72 | 0 |
| all/pooled | adaedl_vs_sync_g4 | 110 | -10.03 [-11.58, -8.26] | -16.91 [-18.65, -15.15] | 52 | 0 |
| all/pooled | markov_w0_robust_vs_sync_g4 | 110 | 45.09 [40.64, 49.47] | -14.31 [-18.08, -10.78] | 59 | 0 |
| all/pooled | markov_w05_robust_vs_sync_g4 | 110 | 37.50 [32.95, 42.28] | 0.90 [-0.88, 3.06] | 55 | 0 |
| all/pooled | sync_g4_vs_adaedl | 110 | 11.15 [9.01, 13.10] | 14.46 [13.15, 15.72] | 52 | 1 |
| all/pooled | fixed_g2_vs_adaedl | 110 | 32.32 [29.63, 35.05] | 14.10 [12.94, 15.30] | 59 | 0 |
| all/pooled | fixed_fast_vs_adaedl | 110 | 53.70 [49.85, 57.55] | 4.95 [2.51, 7.27] | 51 | 1 |
| all/pooled | fixed_g8_vs_adaedl | 110 | 45.99 [38.50, 53.97] | -26.96 [-34.13, -20.03] | 64 | 1 |
| all/pooled | markov_w0_robust_vs_adaedl | 110 | 61.26 [57.20, 65.50] | 2.23 [-0.23, 4.69] | 64 | 0 |
| all/pooled | markov_w05_robust_vs_adaedl | 110 | 52.83 [48.71, 56.89] | 15.24 [13.68, 16.74] | 68 | 0 |
| gsm8k/low | sync_g4 | 50 | -35.48 [-37.56, -33.25] | 8.62 [5.64, 11.27] | 0 | 0 |
| gsm8k/low | fixed_g2 | 50 | -12.57 [-19.38, -6.61] | 8.80 [3.87, 12.52] | 4 | 0 |
| gsm8k/low | fixed_g8 | 50 | -13.59 [-17.20, -8.95] | -26.57 [-30.24, -22.57] | 8 | 0 |
| gsm8k/low | adaedl | 50 | -45.07 [-47.35, -42.24] | -11.57 [-13.80, -9.60] | 8 | 0 |
| gsm8k/low | markov_w0_robust | 50 | -10.29 [-14.22, -4.94] | 5.41 [2.36, 8.17] | 3 | 0 |
| gsm8k/low | markov_w05_robust | 50 | -11.39 [-15.51, -5.69] | 6.80 [3.76, 9.68] | 2 | 0 |
| gsm8k/low | sync_g4_vs_fixed_g2 | 50 | -26.21 [-31.73, -19.22] | -0.20 [-3.11, 3.16] | 4 | 0 |
| gsm8k/low | fixed_fast_vs_fixed_g2 | 50 | 14.37 [7.08, 24.04] | -9.65 [-14.31, -4.02] | 4 | 0 |
| gsm8k/low | fixed_g8_vs_fixed_g2 | 50 | -1.17 [-10.10, 10.27] | -38.78 [-47.33, -28.52] | 11 | 0 |
| gsm8k/low | adaedl_vs_fixed_g2 | 50 | -37.18 [-42.98, -29.63] | -22.33 [-27.33, -16.45] | 9 | 0 |
| gsm8k/low | markov_w0_robust_vs_fixed_g2 | 50 | 2.60 [-6.45, 14.18] | -3.72 [-7.88, 0.91] | 3 | 0 |
| gsm8k/low | markov_w05_robust_vs_fixed_g2 | 50 | 1.35 [-6.96, 12.07] | -2.19 [-6.31, 2.73] | 4 | 0 |
| gsm8k/low | sync_g4_vs_fixed_g8 | 50 | -25.34 [-29.41, -21.27] | 27.80 [23.23, 31.64] | 8 | 0 |
| gsm8k/low | fixed_g2_vs_fixed_g8 | 50 | 1.18 [-9.31, 11.23] | 27.95 [22.19, 32.12] | 11 | 0 |
| gsm8k/low | fixed_fast_vs_fixed_g8 | 50 | 15.72 [9.83, 20.78] | 20.99 [18.41, 23.22] | 8 | 0 |
| gsm8k/low | adaedl_vs_fixed_g8 | 50 | -36.44 [-39.19, -33.61] | 11.85 [7.94, 15.22] | 6 | 0 |
| gsm8k/low | markov_w0_robust_vs_fixed_g8 | 50 | 3.81 [-0.38, 7.97] | 25.27 [21.44, 28.66] | 11 | 0 |
| gsm8k/low | markov_w05_robust_vs_fixed_g8 | 50 | 2.54 [-2.11, 7.43] | 26.37 [22.43, 30.05] | 10 | 0 |
| gsm8k/low | fixed_g2_vs_sync_g4 | 50 | 35.52 [23.79, 46.48] | 0.20 [-3.26, 3.02] | 4 | 0 |
| gsm8k/low | fixed_fast_vs_sync_g4 | 50 | 55.00 [49.82, 60.16] | -9.43 [-12.70, -5.98] | 0 | 0 |
| gsm8k/low | fixed_g8_vs_sync_g4 | 50 | 33.94 [27.01, 41.66] | -38.50 [-46.29, -30.25] | 8 | 0 |
| gsm8k/low | adaedl_vs_sync_g4 | 50 | -14.86 [-17.19, -12.16] | -22.09 [-24.76, -19.08] | 8 | 0 |
| gsm8k/low | markov_w0_robust_vs_sync_g4 | 50 | 39.05 [34.00, 45.02] | -3.51 [-6.57, -0.49] | 3 | 0 |
| gsm8k/low | markov_w05_robust_vs_sync_g4 | 50 | 37.35 [31.53, 43.78] | -1.99 [-4.76, 1.06] | 2 | 0 |
| gsm8k/low | sync_g4_vs_adaedl | 50 | 17.46 [13.84, 20.76] | 18.09 [16.02, 19.85] | 8 | 0 |
| gsm8k/low | fixed_g2_vs_adaedl | 50 | 59.18 [42.11, 75.38] | 18.26 [14.13, 21.46] | 9 | 0 |
| gsm8k/low | fixed_fast_vs_adaedl | 50 | 82.06 [73.13, 89.93] | 10.37 [8.76, 12.13] | 8 | 0 |
| gsm8k/low | fixed_g8_vs_adaedl | 50 | 57.33 [50.61, 64.45] | -13.45 [-17.95, -8.62] | 6 | 0 |
| gsm8k/low | markov_w0_robust_vs_adaedl | 50 | 63.32 [58.31, 68.22] | 15.22 [13.02, 17.23] | 9 | 0 |
| gsm8k/low | markov_w05_robust_vs_adaedl | 50 | 61.33 [54.21, 67.59] | 16.46 [14.40, 18.46] | 10 | 0 |
| gsm8k/high | sync_g4 | 50 | -32.87 [-34.25, -31.40] | -9.00 [-11.07, -7.07] | 1 | 0 |
| gsm8k/high | fixed_g2 | 50 | -28.51 [-29.66, -27.39] | -11.57 [-13.59, -9.64] | 5 | 0 |
| gsm8k/high | fixed_g8 | 50 | 28.06 [24.42, 32.05] | -10.67 [-13.90, -7.35] | 8 | 0 |
| gsm8k/high | adaedl | 50 | -32.98 [-34.47, -31.15] | -15.18 [-16.90, -13.45] | 6 | 0 |
| gsm8k/high | markov_w0_robust | 50 | 23.65 [21.11, 26.27] | -6.87 [-9.07, -4.71] | 8 | 0 |
| gsm8k/high | markov_w05_robust | 50 | 5.28 [-1.48, 10.92] | -1.37 [-4.87, 1.23] | 5 | 0 |
| gsm8k/high | sync_g4_vs_fixed_g2 | 50 | -6.10 [-7.49, -4.44] | 2.31 [1.15, 3.52] | 4 | 0 |
| gsm8k/high | fixed_fast_vs_fixed_g2 | 50 | 39.88 [37.73, 42.16] | 10.37 [8.79, 11.96] | 5 | 0 |
| gsm8k/high | fixed_g8_vs_fixed_g2 | 50 | 79.13 [72.02, 86.87] | 0.81 [-3.69, 5.35] | 10 | 0 |
| gsm8k/high | adaedl_vs_fixed_g2 | 50 | -6.26 [-8.82, -3.43] | -3.24 [-5.60, -0.90] | 6 | 0 |
| gsm8k/high | markov_w0_robust_vs_fixed_g2 | 50 | 72.96 [67.77, 78.49] | 4.21 [0.95, 7.39] | 6 | 0 |
| gsm8k/high | markov_w05_robust_vs_fixed_g2 | 50 | 47.26 [37.49, 56.41] | 9.15 [5.85, 12.00] | 6 | 0 |
| gsm8k/high | sync_g4_vs_fixed_g8 | 50 | -47.58 [-49.72, -45.44] | 1.51 [-3.22, 5.63] | 8 | 0 |
| gsm8k/high | fixed_g2_vs_fixed_g8 | 50 | -44.17 [-46.49, -41.87] | -0.81 [-5.66, 3.56] | 10 | 0 |
| gsm8k/high | fixed_fast_vs_fixed_g8 | 50 | -21.91 [-24.27, -19.63] | 9.64 [6.85, 12.20] | 8 | 0 |
| gsm8k/high | adaedl_vs_fixed_g8 | 50 | -47.67 [-49.33, -46.05] | -4.08 [-7.70, -0.86] | 4 | 0 |
| gsm8k/high | markov_w0_robust_vs_fixed_g8 | 50 | -3.44 [-5.76, -1.24] | 3.43 [1.48, 5.18] | 10 | 0 |
| gsm8k/high | markov_w05_robust_vs_fixed_g8 | 50 | -17.79 [-23.95, -13.64] | 8.41 [3.79, 11.87] | 10 | 0 |
| gsm8k/high | fixed_g2_vs_sync_g4 | 50 | 6.49 [4.65, 8.09] | -2.36 [-3.65, -1.16] | 4 | 0 |
| gsm8k/high | fixed_fast_vs_sync_g4 | 50 | 48.96 [45.76, 52.10] | 8.26 [6.60, 9.97] | 1 | 0 |
| gsm8k/high | fixed_g8_vs_sync_g4 | 50 | 90.75 [83.27, 98.90] | -1.53 [-5.97, 3.12] | 8 | 0 |
| gsm8k/high | adaedl_vs_sync_g4 | 50 | -0.17 [-2.00, 1.70] | -5.67 [-7.55, -3.87] | 6 | 0 |
| gsm8k/high | markov_w0_robust_vs_sync_g4 | 50 | 84.18 [77.77, 90.98] | 1.95 [-1.38, 5.38] | 7 | 0 |
| gsm8k/high | markov_w05_robust_vs_sync_g4 | 50 | 56.82 [45.11, 67.62] | 7.01 [3.23, 10.20] | 6 | 0 |
| gsm8k/high | sync_g4_vs_adaedl | 50 | 0.17 [-1.67, 2.04] | 5.37 [3.72, 7.02] | 6 | 0 |
| gsm8k/high | fixed_g2_vs_adaedl | 50 | 6.67 [3.55, 9.67] | 3.13 [0.89, 5.30] | 6 | 0 |
| gsm8k/high | fixed_fast_vs_adaedl | 50 | 49.22 [45.25, 52.61] | 13.18 [11.86, 14.46] | 6 | 0 |
| gsm8k/high | fixed_g8_vs_adaedl | 50 | 91.08 [85.37, 97.34] | 3.92 [0.86, 7.15] | 4 | 0 |
| gsm8k/high | markov_w0_robust_vs_adaedl | 50 | 84.50 [77.59, 90.31] | 7.22 [4.87, 9.67] | 8 | 0 |
| gsm8k/high | markov_w05_robust_vs_adaedl | 50 | 57.09 [45.52, 67.17] | 12.00 [8.59, 14.70] | 10 | 0 |
| gsm8k/dynamic | sync_g4 | 50 | -36.04 [-38.09, -33.87] | 1.49 [-1.15, 3.94] | 0 | 0 |
| gsm8k/dynamic | fixed_g2 | 50 | -18.12 [-20.46, -15.72] | 5.93 [3.36, 8.37] | 2 | 0 |
| gsm8k/dynamic | fixed_g8 | 50 | 1.13 [-4.06, 7.66] | -20.20 [-24.11, -16.09] | 7 | 0 |
| gsm8k/dynamic | adaedl | 50 | -43.83 [-46.13, -40.93] | -16.15 [-18.58, -13.73] | 3 | 0 |
| gsm8k/dynamic | markov_w0_robust | 50 | -0.96 [-5.31, 3.17] | -2.34 [-4.98, -0.12] | 3 | 0 |
| gsm8k/dynamic | markov_w05_robust | 50 | -4.04 [-7.46, -0.35] | 3.82 [1.79, 5.78] | 4 | 0 |
| gsm8k/dynamic | sync_g4_vs_fixed_g2 | 50 | -21.88 [-24.52, -19.15] | -4.72 [-6.57, -2.93] | 2 | 0 |
| gsm8k/dynamic | fixed_fast_vs_fixed_g2 | 50 | 22.14 [18.66, 25.72] | -6.30 [-9.13, -3.47] | 2 | 0 |
| gsm8k/dynamic | fixed_g8_vs_fixed_g2 | 50 | 23.51 [15.15, 33.19] | -27.77 [-34.92, -20.59] | 9 | 0 |
| gsm8k/dynamic | adaedl_vs_fixed_g2 | 50 | -31.39 [-34.88, -27.51] | -23.47 [-27.28, -19.63] | 5 | 0 |
| gsm8k/dynamic | markov_w0_robust_vs_fixed_g2 | 50 | 20.97 [14.05, 27.65] | -8.79 [-12.64, -5.32] | 3 | 0 |
| gsm8k/dynamic | markov_w05_robust_vs_fixed_g2 | 50 | 17.20 [11.35, 23.51] | -2.24 [-5.11, 0.52] | 4 | 0 |
| gsm8k/dynamic | sync_g4_vs_fixed_g8 | 50 | -36.75 [-40.31, -33.21] | 18.04 [13.42, 22.29] | 7 | 0 |
| gsm8k/dynamic | fixed_g2_vs_fixed_g8 | 50 | -19.04 [-24.92, -13.16] | 21.74 [17.07, 25.88] | 9 | 0 |
| gsm8k/dynamic | fixed_fast_vs_fixed_g8 | 50 | -1.11 [-7.12, 4.23] | 16.80 [13.86, 19.43] | 7 | 0 |
| gsm8k/dynamic | adaedl_vs_fixed_g8 | 50 | -44.45 [-46.41, -42.40] | 3.37 [-0.40, 6.98] | 6 | 0 |
| gsm8k/dynamic | markov_w0_robust_vs_fixed_g8 | 50 | -2.06 [-6.37, 1.81] | 14.86 [11.33, 18.11] | 8 | 0 |
| gsm8k/dynamic | markov_w05_robust_vs_fixed_g8 | 50 | -5.11 [-9.05, -1.37] | 19.98 [16.34, 23.33] | 11 | 0 |
| gsm8k/dynamic | fixed_g2_vs_sync_g4 | 50 | 28.01 [23.68, 32.48] | 4.51 [2.85, 6.17] | 2 | 0 |
| gsm8k/dynamic | fixed_fast_vs_sync_g4 | 50 | 56.34 [51.21, 61.53] | -1.51 [-4.11, 1.14] | 0 | 0 |
| gsm8k/dynamic | fixed_g8_vs_sync_g4 | 50 | 58.10 [49.72, 67.54] | -22.02 [-28.68, -15.50] | 7 | 0 |
| gsm8k/dynamic | adaedl_vs_sync_g4 | 50 | -12.18 [-14.86, -9.25] | -17.90 [-20.83, -14.90] | 3 | 0 |
| gsm8k/dynamic | markov_w0_robust_vs_sync_g4 | 50 | 54.85 [48.71, 60.60] | -3.89 [-7.37, -0.64] | 3 | 0 |
| gsm8k/dynamic | markov_w05_robust_vs_sync_g4 | 50 | 50.02 [44.59, 56.07] | 2.36 [0.01, 4.84] | 4 | 0 |
| gsm8k/dynamic | sync_g4_vs_adaedl | 50 | 13.87 [10.20, 17.46] | 15.19 [12.97, 17.24] | 3 | 0 |
| gsm8k/dynamic | fixed_g2_vs_adaedl | 50 | 45.76 [37.95, 53.55] | 19.01 [16.41, 21.43] | 5 | 0 |
| gsm8k/dynamic | fixed_fast_vs_adaedl | 50 | 78.03 [69.30, 85.63] | 13.90 [12.07, 15.67] | 3 | 0 |
| gsm8k/dynamic | fixed_g8_vs_adaedl | 50 | 80.03 [73.60, 86.59] | -3.49 [-7.51, 0.39] | 6 | 0 |
| gsm8k/dynamic | markov_w0_robust_vs_adaedl | 50 | 76.33 [69.63, 82.17] | 11.89 [9.60, 14.12] | 2 | 0 |
| gsm8k/dynamic | markov_w05_robust_vs_adaedl | 50 | 70.83 [65.54, 76.43] | 17.19 [15.59, 18.87] | 5 | 0 |
| gsm8k/pooled | sync_g4 | 50 | -34.48 [-35.81, -33.23] | -0.42 [-2.74, 1.67] | 1 | 0 |
| gsm8k/pooled | fixed_g2 | 50 | -22.07 [-23.99, -20.35] | 0.12 [-2.31, 2.20] | 11 | 0 |
| gsm8k/pooled | fixed_g8 | 50 | 7.13 [3.74, 11.02] | -18.43 [-21.72, -14.90] | 23 | 0 |
| gsm8k/pooled | adaedl | 50 | -39.69 [-40.89, -38.42] | -14.44 [-15.95, -13.05] | 17 | 0 |
| gsm8k/pooled | markov_w0_robust | 50 | 6.06 [3.82, 8.39] | -1.85 [-3.30, -0.43] | 14 | 0 |
| gsm8k/pooled | markov_w05_robust | 50 | -1.96 [-5.41, 1.08] | 2.73 [0.73, 4.58] | 11 | 0 |
| gsm8k/pooled | sync_g4_vs_fixed_g2 | 50 | -15.92 [-17.39, -14.16] | -0.55 [-1.70, 0.65] | 10 | 0 |
| gsm8k/pooled | fixed_fast_vs_fixed_g2 | 50 | 28.33 [25.55, 31.56] | -0.12 [-2.25, 2.26] | 11 | 0 |
| gsm8k/pooled | fixed_g8_vs_fixed_g2 | 50 | 37.48 [31.23, 44.70] | -18.57 [-24.08, -12.89] | 30 | 0 |
| gsm8k/pooled | adaedl_vs_fixed_g2 | 50 | -22.60 [-24.81, -20.07] | -14.59 [-16.98, -12.22] | 20 | 0 |
| gsm8k/pooled | markov_w0_robust_vs_fixed_g2 | 50 | 36.10 [31.81, 41.15] | -1.98 [-4.59, 0.75] | 12 | 0 |
| gsm8k/pooled | markov_w05_robust_vs_fixed_g2 | 50 | 25.81 [20.33, 31.57] | 2.61 [0.27, 5.01] | 14 | 0 |
| gsm8k/pooled | sync_g4_vs_fixed_g8 | 50 | -38.84 [-41.72, -36.00] | 15.20 [10.81, 19.08] | 23 | 0 |
| gsm8k/pooled | fixed_g2_vs_fixed_g8 | 50 | -27.26 [-30.89, -23.80] | 15.66 [11.42, 19.41] | 30 | 0 |
| gsm8k/pooled | fixed_fast_vs_fixed_g8 | 50 | -6.66 [-9.93, -3.60] | 15.56 [12.96, 17.85] | 23 | 0 |
| gsm8k/pooled | adaedl_vs_fixed_g8 | 50 | -43.70 [-45.51, -41.95] | 3.36 [-0.20, 6.54] | 16 | 0 |
| gsm8k/pooled | markov_w0_robust_vs_fixed_g8 | 50 | -1.00 [-3.80, 1.70] | 14.00 [11.34, 16.38] | 29 | 0 |
| gsm8k/pooled | markov_w05_robust_vs_fixed_g8 | 50 | -8.48 [-12.12, -5.39] | 17.86 [14.50, 21.10] | 31 | 0 |
| gsm8k/pooled | fixed_g2_vs_sync_g4 | 50 | 18.93 [16.49, 21.05] | 0.55 [-0.66, 1.68] | 10 | 0 |
| gsm8k/pooled | fixed_fast_vs_sync_g4 | 50 | 52.63 [49.76, 55.80] | 0.42 [-1.70, 2.66] | 1 | 0 |
| gsm8k/pooled | fixed_g8_vs_sync_g4 | 50 | 63.51 [56.25, 71.58] | -17.93 [-23.58, -12.11] | 23 | 0 |
| gsm8k/pooled | adaedl_vs_sync_g4 | 50 | -7.95 [-9.67, -6.04] | -13.96 [-15.91, -11.93] | 17 | 0 |
| gsm8k/pooled | markov_w0_robust_vs_sync_g4 | 50 | 61.87 [57.24, 66.91] | -1.42 [-4.05, 1.30] | 13 | 0 |
| gsm8k/pooled | markov_w05_robust_vs_sync_g4 | 50 | 49.64 [43.16, 55.96] | 3.14 [0.71, 5.45] | 12 | 0 |
| gsm8k/pooled | sync_g4_vs_adaedl | 50 | 8.63 [6.43, 10.71] | 12.25 [10.66, 13.72] | 17 | 0 |
| gsm8k/pooled | fixed_g2_vs_adaedl | 50 | 29.20 [25.10, 33.00] | 12.73 [10.89, 14.51] | 20 | 0 |
| gsm8k/pooled | fixed_fast_vs_adaedl | 50 | 65.80 [62.39, 69.18] | 12.62 [11.54, 13.75] | 17 | 0 |
| gsm8k/pooled | fixed_g8_vs_adaedl | 50 | 77.62 [72.26, 83.51] | -3.48 [-6.99, 0.20] | 16 | 0 |
| gsm8k/pooled | markov_w0_robust_vs_adaedl | 50 | 75.84 [72.08, 79.62] | 11.00 [9.51, 12.60] | 19 | 0 |
| gsm8k/pooled | markov_w05_robust_vs_adaedl | 50 | 62.55 [56.83, 67.66] | 15.01 [13.36, 16.56] | 25 | 0 |
| humaneval/low | sync_g4 | 30 | -28.59 [-33.14, -20.65] | 17.37 [14.74, 20.73] | 0 | 0 |
| humaneval/low | fixed_g2 | 30 | 2.18 [-3.94, 13.08] | 16.38 [13.85, 19.63] | 5 | 0 |
| humaneval/low | fixed_g8 | 30 | -19.35 [-22.47, -15.30] | -35.60 [-39.69, -31.50] | 7 | 0 |
| humaneval/low | adaedl | 30 | -42.10 [-45.09, -37.64] | -4.04 [-6.43, -1.66] | 4 | 0 |
| humaneval/low | markov_w0_robust | 30 | -5.46 [-11.26, 4.81] | 8.30 [5.42, 12.09] | 8 | 0 |
| humaneval/low | markov_w05_robust | 30 | -4.58 [-12.44, 6.93] | 13.03 [8.90, 17.23] | 9 | 0 |
| humaneval/low | sync_g4_vs_fixed_g2 | 30 | -30.11 [-31.31, -28.93] | 1.18 [-0.04, 2.37] | 5 | 1 |
| humaneval/low | fixed_fast_vs_fixed_g2 | 30 | -2.13 [-11.56, 4.10] | -19.59 [-24.43, -16.08] | 5 | 1 |
| humaneval/low | fixed_g8_vs_fixed_g2 | 30 | -21.07 [-26.59, -16.26] | -62.16 [-69.73, -54.31] | 8 | 1 |
| humaneval/low | adaedl_vs_fixed_g2 | 30 | -43.33 [-45.32, -41.64] | -24.42 [-27.63, -21.70] | 4 | 0 |
| humaneval/low | markov_w0_robust_vs_fixed_g2 | 30 | -7.47 [-9.39, -5.42] | -9.66 [-11.52, -7.66] | 5 | 0 |
| humaneval/low | markov_w05_robust_vs_fixed_g2 | 30 | -6.61 [-10.41, -3.64] | -4.01 [-6.79, -1.92] | 4 | 0 |
| humaneval/low | sync_g4_vs_fixed_g8 | 30 | -11.46 [-17.24, -4.43] | 39.06 [35.75, 42.04] | 7 | 1 |
| humaneval/low | fixed_g2_vs_fixed_g8 | 30 | 26.70 [19.41, 36.21] | 38.33 [35.19, 41.08] | 8 | 1 |
| humaneval/low | fixed_fast_vs_fixed_g8 | 30 | 24.00 [18.07, 28.98] | 26.25 [23.95, 28.41] | 7 | 1 |
| humaneval/low | adaedl_vs_fixed_g8 | 30 | -28.20 [-31.47, -24.88] | 23.27 [20.30, 25.74] | 6 | 1 |
| humaneval/low | markov_w0_robust_vs_fixed_g8 | 30 | 17.23 [10.97, 25.62] | 32.38 [29.20, 35.52] | 10 | 0 |
| humaneval/low | markov_w05_robust_vs_fixed_g8 | 30 | 18.32 [10.40, 27.81] | 35.86 [31.69, 39.47] | 11 | 1 |
| humaneval/low | fixed_g2_vs_sync_g4 | 30 | 43.09 [40.70, 45.58] | -1.20 [-2.43, 0.04] | 5 | 0 |
| humaneval/low | fixed_fast_vs_sync_g4 | 30 | 40.04 [26.02, 49.57] | -21.02 [-26.15, -17.29] | 0 | 0 |
| humaneval/low | fixed_g8_vs_sync_g4 | 30 | 12.94 [4.64, 20.83] | -64.10 [-72.54, -55.65] | 7 | 0 |
| humaneval/low | adaedl_vs_sync_g4 | 30 | -18.92 [-22.17, -16.36] | -25.91 [-29.56, -22.80] | 4 | 0 |
| humaneval/low | markov_w0_robust_vs_sync_g4 | 30 | 32.40 [29.27, 35.81] | -10.97 [-13.06, -8.63] | 8 | 0 |
| humaneval/low | markov_w05_robust_vs_sync_g4 | 30 | 33.63 [26.79, 39.05] | -5.25 [-8.54, -2.94] | 9 | 0 |
| humaneval/low | sync_g4_vs_adaedl | 30 | 23.33 [19.56, 28.48] | 20.58 [18.56, 22.81] | 4 | 1 |
| humaneval/low | fixed_g2_vs_adaedl | 30 | 76.47 [71.34, 82.88] | 19.63 [17.83, 21.65] | 4 | 0 |
| humaneval/low | fixed_fast_vs_adaedl | 30 | 72.71 [60.36, 82.12] | 3.89 [1.63, 6.04] | 4 | 1 |
| humaneval/low | fixed_g8_vs_adaedl | 30 | 39.28 [33.11, 45.93] | -30.33 [-34.66, -25.48] | 6 | 1 |
| humaneval/low | markov_w0_robust_vs_adaedl | 30 | 63.28 [58.07, 69.78] | 11.87 [9.78, 14.35] | 7 | 0 |
| humaneval/low | markov_w05_robust_vs_adaedl | 30 | 64.80 [56.96, 73.12] | 16.41 [13.56, 19.11] | 7 | 0 |
| humaneval/high | sync_g4 | 30 | -29.25 [-31.54, -26.94] | -3.12 [-5.83, -0.73] | 1 | 0 |
| humaneval/high | fixed_g2 | 30 | -26.88 [-29.77, -24.60] | -8.50 [-12.69, -5.31] | 5 | 0 |
| humaneval/high | fixed_g8 | 30 | 18.13 [14.85, 21.37] | -19.34 [-22.75, -15.98] | 4 | 0 |
| humaneval/high | adaedl | 30 | -32.57 [-34.18, -30.56] | -13.88 [-15.37, -12.30] | 4 | 0 |
| humaneval/high | markov_w0_robust | 30 | 16.56 [12.86, 20.56] | -14.31 [-17.95, -10.81] | 7 | 0 |
| humaneval/high | markov_w05_robust | 30 | 4.41 [0.72, 8.35] | -4.61 [-6.91, -2.36] | 5 | 0 |
| humaneval/high | sync_g4_vs_fixed_g2 | 30 | -3.23 [-6.26, 1.32] | 4.96 [2.77, 7.92] | 6 | 0 |
| humaneval/high | fixed_fast_vs_fixed_g2 | 30 | 36.76 [32.62, 42.39] | 7.84 [5.04, 11.26] | 5 | 0 |
| humaneval/high | fixed_g8_vs_fixed_g2 | 30 | 61.56 [54.41, 69.62] | -9.99 [-15.82, -4.10] | 8 | 0 |
| humaneval/high | adaedl_vs_fixed_g2 | 30 | -7.78 [-11.19, -3.15] | -4.95 [-7.90, -1.26] | 6 | 0 |
| humaneval/high | markov_w0_robust_vs_fixed_g2 | 30 | 59.41 [50.73, 69.90] | -5.35 [-10.76, 0.38] | 10 | 0 |
| humaneval/high | markov_w05_robust_vs_fixed_g2 | 30 | 42.80 [36.25, 50.37] | 3.58 [0.23, 7.77] | 3 | 0 |
| humaneval/high | sync_g4_vs_fixed_g8 | 30 | -40.10 [-43.19, -37.23] | 13.59 [9.38, 17.28] | 5 | 0 |
| humaneval/high | fixed_g2_vs_fixed_g8 | 30 | -38.10 [-41.05, -35.24] | 9.08 [3.93, 13.66] | 8 | 0 |
| humaneval/high | fixed_fast_vs_fixed_g8 | 30 | -15.35 [-17.61, -12.93] | 16.21 [13.78, 18.54] | 4 | 0 |
| humaneval/high | adaedl_vs_fixed_g8 | 30 | -42.92 [-44.94, -40.91] | 4.58 [1.75, 7.13] | 2 | 0 |
| humaneval/high | markov_w0_robust_vs_fixed_g8 | 30 | -1.33 [-4.38, 1.76] | 4.22 [1.91, 6.32] | 6 | 0 |
| humaneval/high | markov_w05_robust_vs_fixed_g8 | 30 | -11.61 [-14.25, -8.87] | 12.34 [9.37, 15.02] | 7 | 0 |
| humaneval/high | fixed_g2_vs_sync_g4 | 30 | 3.34 [-1.31, 6.67] | -5.22 [-8.60, -2.85] | 6 | 0 |
| humaneval/high | fixed_fast_vs_sync_g4 | 30 | 41.34 [36.87, 46.07] | 3.03 [0.72, 5.51] | 1 | 0 |
| humaneval/high | fixed_g8_vs_sync_g4 | 30 | 66.96 [59.31, 76.01] | -15.72 [-20.89, -10.35] | 5 | 0 |
| humaneval/high | adaedl_vs_sync_g4 | 30 | -4.69 [-6.73, -2.41] | -10.43 [-12.84, -7.83] | 5 | 0 |
| humaneval/high | markov_w0_robust_vs_sync_g4 | 30 | 64.74 [56.13, 74.14] | -10.84 [-15.86, -5.76] | 8 | 0 |
| humaneval/high | markov_w05_robust_vs_sync_g4 | 30 | 47.57 [40.59, 55.92] | -1.45 [-4.16, 1.22] | 6 | 0 |
| humaneval/high | sync_g4_vs_adaedl | 30 | 4.93 [2.47, 7.22] | 9.44 [7.26, 11.38] | 5 | 0 |
| humaneval/high | fixed_g2_vs_adaedl | 30 | 8.43 [3.25, 12.60] | 4.72 [1.24, 7.32] | 6 | 0 |
| humaneval/high | fixed_fast_vs_adaedl | 30 | 48.30 [44.01, 51.92] | 12.19 [10.95, 13.32] | 4 | 0 |
| humaneval/high | fixed_g8_vs_adaedl | 30 | 75.18 [69.25, 81.62] | -4.80 [-7.68, -1.78] | 2 | 0 |
| humaneval/high | markov_w0_robust_vs_adaedl | 30 | 72.85 [64.69, 80.05] | -0.38 [-3.37, 2.58] | 8 | 0 |
| humaneval/high | markov_w05_robust_vs_adaedl | 30 | 54.84 [49.53, 60.87] | 8.13 [6.52, 9.64] | 7 | 0 |
| humaneval/dynamic | sync_g4 | 30 | -30.87 [-34.47, -26.78] | 6.66 [3.33, 9.51] | 0 | 0 |
| humaneval/dynamic | fixed_g2 | 30 | -13.22 [-16.16, -10.52] | 9.71 [7.30, 11.84] | 5 | 0 |
| humaneval/dynamic | fixed_g8 | 30 | -0.97 [-7.43, 8.26] | -26.34 [-32.00, -19.05] | 11 | 0 |
| humaneval/dynamic | adaedl | 30 | -39.76 [-43.18, -35.75] | -11.17 [-13.90, -8.71] | 7 | 0 |
| humaneval/dynamic | markov_w0_robust | 30 | -2.09 [-7.68, 2.60] | -6.94 [-10.98, -3.26] | 8 | 0 |
| humaneval/dynamic | markov_w05_robust | 30 | -3.42 [-6.47, -0.34] | 3.00 [0.05, 5.62] | 5 | 0 |
| humaneval/dynamic | sync_g4_vs_fixed_g2 | 30 | -20.34 [-23.38, -17.15] | -3.38 [-5.68, -1.19] | 5 | 1 |
| humaneval/dynamic | fixed_fast_vs_fixed_g2 | 30 | 15.24 [11.75, 19.27] | -10.76 [-13.43, -7.88] | 5 | 1 |
| humaneval/dynamic | fixed_g8_vs_fixed_g2 | 30 | 14.12 [6.16, 23.61] | -39.93 [-48.69, -30.23] | 11 | 0 |
| humaneval/dynamic | adaedl_vs_fixed_g2 | 30 | -30.58 [-34.27, -26.89] | -23.12 [-26.45, -19.95] | 8 | 1 |
| humaneval/dynamic | markov_w0_robust_vs_fixed_g2 | 30 | 12.83 [5.97, 19.90] | -18.44 [-23.40, -13.77] | 6 | 0 |
| humaneval/dynamic | markov_w05_robust_vs_fixed_g2 | 30 | 11.29 [7.36, 15.79] | -7.43 [-9.57, -5.13] | 2 | 0 |
| humaneval/dynamic | sync_g4_vs_fixed_g8 | 30 | -30.19 [-34.61, -25.59] | 26.12 [20.42, 30.82] | 11 | 1 |
| humaneval/dynamic | fixed_g2_vs_fixed_g8 | 30 | -12.37 [-19.10, -5.80] | 28.53 [23.21, 32.74] | 11 | 0 |
| humaneval/dynamic | fixed_fast_vs_fixed_g8 | 30 | 0.98 [-7.63, 8.03] | 20.85 [16.00, 24.24] | 11 | 1 |
| humaneval/dynamic | adaedl_vs_fixed_g8 | 30 | -39.17 [-42.11, -36.26] | 12.01 [6.53, 16.40] | 6 | 1 |
| humaneval/dynamic | markov_w0_robust_vs_fixed_g8 | 30 | -1.12 [-10.05, 7.15] | 15.35 [8.56, 20.46] | 8 | 0 |
| humaneval/dynamic | markov_w05_robust_vs_fixed_g8 | 30 | -2.48 [-8.70, 2.83] | 23.22 [17.91, 27.75] | 11 | 0 |
| humaneval/dynamic | fixed_g2_vs_sync_g4 | 30 | 25.53 [20.71, 30.52] | 3.27 [1.18, 5.37] | 5 | 0 |
| humaneval/dynamic | fixed_fast_vs_sync_g4 | 30 | 44.65 [36.58, 52.60] | -7.13 [-10.51, -3.45] | 0 | 0 |
| humaneval/dynamic | fixed_g8_vs_sync_g4 | 30 | 43.25 [34.38, 52.92] | -35.35 [-44.55, -25.66] | 11 | 0 |
| humaneval/dynamic | adaedl_vs_sync_g4 | 30 | -12.86 [-15.64, -10.25] | -19.10 [-22.25, -16.13] | 7 | 0 |
| humaneval/dynamic | markov_w0_robust_vs_sync_g4 | 30 | 41.64 [32.76, 51.10] | -14.57 [-19.70, -9.35] | 8 | 0 |
| humaneval/dynamic | markov_w05_robust_vs_sync_g4 | 30 | 39.70 [33.86, 46.43] | -3.92 [-6.94, -0.74] | 5 | 0 |
| humaneval/dynamic | sync_g4_vs_adaedl | 30 | 14.76 [11.42, 18.54] | 16.03 [13.89, 18.20] | 7 | 0 |
| humaneval/dynamic | fixed_g2_vs_adaedl | 30 | 44.06 [36.78, 52.13] | 18.78 [16.63, 20.92] | 8 | 0 |
| humaneval/dynamic | fixed_fast_vs_adaedl | 30 | 66.01 [55.63, 75.98] | 10.04 [8.01, 12.20] | 7 | 0 |
| humaneval/dynamic | fixed_g8_vs_adaedl | 30 | 64.39 [56.89, 72.74] | -13.65 [-19.61, -6.98] | 6 | 0 |
| humaneval/dynamic | markov_w0_robust_vs_adaedl | 30 | 62.54 [51.34, 73.62] | 3.80 [-0.46, 8.00] | 7 | 0 |
| humaneval/dynamic | markov_w05_robust_vs_adaedl | 30 | 60.32 [53.61, 67.54] | 12.75 [10.11, 15.44] | 7 | 0 |
| humaneval/pooled | sync_g4 | 30 | -29.65 [-32.34, -26.58] | 6.11 [3.46, 8.53] | 1 | 0 |
| humaneval/pooled | fixed_g2 | 30 | -17.22 [-20.08, -14.14] | 4.87 [2.32, 7.24] | 15 | 0 |
| humaneval/pooled | fixed_g8 | 30 | 1.03 [-2.14, 4.98] | -26.43 [-30.12, -22.46] | 22 | 0 |
| humaneval/pooled | adaedl | 30 | -37.31 [-39.05, -35.46] | -10.06 [-11.60, -8.57] | 15 | 0 |
| humaneval/pooled | markov_w0_robust | 30 | 4.52 [1.31, 8.12] | -5.27 [-7.67, -2.94] | 23 | 0 |
| humaneval/pooled | markov_w05_robust | 30 | -0.20 [-2.94, 3.09] | 3.19 [0.93, 5.37] | 19 | 0 |
| humaneval/pooled | sync_g4_vs_fixed_g2 | 30 | -15.01 [-17.17, -12.28] | 1.30 [-0.30, 3.18] | 16 | 2 |
| humaneval/pooled | fixed_fast_vs_fixed_g2 | 30 | 20.80 [16.47, 25.12] | -5.12 [-7.80, -2.38] | 15 | 2 |
| humaneval/pooled | fixed_g8_vs_fixed_g2 | 30 | 22.04 [15.95, 28.75] | -32.90 [-39.48, -26.30] | 27 | 1 |
| humaneval/pooled | adaedl_vs_fixed_g2 | 30 | -24.27 [-26.57, -21.49] | -15.69 [-17.98, -13.07] | 18 | 1 |
| humaneval/pooled | markov_w0_robust_vs_fixed_g2 | 30 | 26.26 [21.41, 32.05] | -10.66 [-14.12, -6.89] | 21 | 0 |
| humaneval/pooled | markov_w05_robust_vs_fixed_g2 | 30 | 20.56 [17.13, 24.60] | -1.77 [-3.49, 0.22] | 9 | 0 |
| humaneval/pooled | sync_g4_vs_fixed_g8 | 30 | -30.36 [-34.18, -26.81] | 25.74 [21.60, 29.25] | 23 | 2 |
| humaneval/pooled | fixed_g2_vs_fixed_g8 | 30 | -18.06 [-22.33, -13.76] | 24.76 [20.82, 28.31] | 27 | 1 |
| humaneval/pooled | fixed_fast_vs_fixed_g8 | 30 | -1.02 [-4.74, 2.18] | 20.91 [18.34, 23.15] | 22 | 2 |
| humaneval/pooled | adaedl_vs_fixed_g8 | 30 | -37.95 [-40.31, -35.74] | 12.95 [9.67, 15.83] | 14 | 2 |
| humaneval/pooled | markov_w0_robust_vs_fixed_g8 | 30 | 3.46 [-0.83, 7.75] | 16.74 [13.73, 19.30] | 24 | 0 |
| humaneval/pooled | markov_w05_robust_vs_fixed_g8 | 30 | -1.22 [-4.78, 2.39] | 23.43 [19.78, 26.71] | 29 | 1 |
| humaneval/pooled | fixed_g2_vs_sync_g4 | 30 | 17.66 [13.99, 20.73] | -1.32 [-3.29, 0.30] | 16 | 0 |
| humaneval/pooled | fixed_fast_vs_sync_g4 | 30 | 42.14 [36.20, 47.80] | -6.50 [-9.32, -3.58] | 1 | 0 |
| humaneval/pooled | fixed_g8_vs_sync_g4 | 30 | 43.60 [36.62, 51.92] | -34.66 [-41.34, -27.55] | 23 | 0 |
| humaneval/pooled | adaedl_vs_sync_g4 | 30 | -10.89 [-12.95, -8.79] | -17.21 [-19.65, -14.66] | 16 | 0 |
| humaneval/pooled | markov_w0_robust_vs_sync_g4 | 30 | 48.56 [42.74, 55.24] | -12.12 [-15.96, -8.18] | 24 | 0 |
| humaneval/pooled | markov_w05_robust_vs_sync_g4 | 30 | 41.85 [37.02, 47.65] | -3.11 [-5.25, -1.09] | 20 | 0 |
| humaneval/pooled | sync_g4_vs_adaedl | 30 | 12.23 [9.64, 14.88] | 14.69 [12.78, 16.42] | 16 | 1 |
| humaneval/pooled | fixed_g2_vs_adaedl | 30 | 32.05 [27.37, 36.19] | 13.56 [11.56, 15.24] | 18 | 0 |
| humaneval/pooled | fixed_fast_vs_adaedl | 30 | 59.52 [54.95, 64.07] | 9.14 [7.89, 10.40] | 15 | 1 |
| humaneval/pooled | fixed_g8_vs_adaedl | 30 | 61.15 [55.63, 67.52] | -14.88 [-18.80, -10.70] | 14 | 1 |
| humaneval/pooled | markov_w0_robust_vs_adaedl | 30 | 66.73 [61.04, 72.59] | 4.35 [2.16, 6.44] | 22 | 0 |
| humaneval/pooled | markov_w05_robust_vs_adaedl | 30 | 59.19 [54.94, 63.83] | 12.03 [10.30, 13.54] | 21 | 0 |
| mtbench/low | sync_g4 | 30 | -9.89 [-14.33, -5.53] | 33.56 [29.83, 36.25] | 1 | 0 |
| mtbench/low | fixed_g2 | 30 | 16.41 [10.56, 21.73] | 29.25 [26.43, 31.50] | 8 | 0 |
| mtbench/low | fixed_g8 | 30 | -31.02 [-34.94, -24.59] | -61.49 [-67.13, -54.91] | 9 | 0 |
| mtbench/low | adaedl | 30 | -18.53 [-24.83, -10.49] | 18.87 [15.35, 21.81] | 5 | 0 |
| mtbench/low | markov_w0_robust | 30 | 6.22 [-0.70, 12.49] | 22.70 [15.44, 27.78] | 6 | 0 |
| mtbench/low | markov_w05_robust | 30 | 14.28 [5.31, 22.58] | 36.84 [30.71, 41.45] | 7 | 0 |
| mtbench/low | sync_g4_vs_fixed_g2 | 30 | -22.59 [-24.57, -20.41] | 6.08 [4.32, 7.58] | 8 | 0 |
| mtbench/low | fixed_fast_vs_fixed_g2 | 30 | -14.09 [-17.85, -9.55] | -41.35 [-45.98, -35.92] | 8 | 0 |
| mtbench/low | fixed_g8_vs_fixed_g2 | 30 | -40.74 [-45.67, -32.43] | -128.26 [-141.73, -111.22] | 11 | 0 |
| mtbench/low | adaedl_vs_fixed_g2 | 30 | -30.01 [-35.00, -21.11] | -14.67 [-18.22, -9.64] | 6 | 0 |
| mtbench/low | markov_w0_robust_vs_fixed_g2 | 30 | -8.76 [-11.48, -5.84] | -9.26 [-15.96, -4.11] | 6 | 0 |
| mtbench/low | markov_w05_robust_vs_fixed_g2 | 30 | -1.83 [-5.82, 2.18] | 10.72 [5.48, 14.70] | 5 | 0 |
| mtbench/low | sync_g4_vs_fixed_g8 | 30 | 30.64 [16.53, 41.93] | 58.86 [54.88, 61.58] | 9 | 0 |
| mtbench/low | fixed_g2_vs_fixed_g8 | 30 | 68.76 [47.99, 84.07] | 56.19 [52.66, 58.63] | 11 | 0 |
| mtbench/low | fixed_fast_vs_fixed_g8 | 30 | 44.97 [32.61, 53.71] | 38.08 [35.45, 40.17] | 9 | 0 |
| mtbench/low | adaedl_vs_fixed_g8 | 30 | 18.11 [9.06, 26.24] | 49.76 [46.37, 52.41] | 11 | 0 |
| mtbench/low | markov_w0_robust_vs_fixed_g8 | 30 | 53.98 [32.93, 69.64] | 52.14 [45.87, 56.06] | 13 | 0 |
| mtbench/low | markov_w05_robust_vs_fixed_g8 | 30 | 65.67 [40.31, 84.78] | 60.89 [55.33, 64.56] | 13 | 0 |
| mtbench/low | fixed_g2_vs_sync_g4 | 30 | 29.18 [25.65, 32.58] | -6.48 [-8.20, -4.52] | 8 | 0 |
| mtbench/low | fixed_fast_vs_sync_g4 | 30 | 10.97 [5.85, 16.73] | -50.50 [-56.87, -42.52] | 1 | 0 |
| mtbench/low | fixed_g8_vs_sync_g4 | 30 | -23.45 [-29.54, -14.19] | -143.05 [-160.25, -121.65] | 9 | 0 |
| mtbench/low | adaedl_vs_sync_g4 | 30 | -9.59 [-15.77, -0.05] | -22.10 [-26.95, -15.08] | 5 | 0 |
| mtbench/low | markov_w0_robust_vs_sync_g4 | 30 | 17.87 [12.28, 22.79] | -16.33 [-22.45, -10.54] | 6 | 0 |
| mtbench/low | markov_w05_robust_vs_sync_g4 | 30 | 26.82 [19.26, 32.27] | 4.94 [0.82, 8.43] | 7 | 0 |
| mtbench/low | sync_g4_vs_adaedl | 30 | 10.61 [0.05, 18.73] | 18.10 [13.11, 21.23] | 5 | 0 |
| mtbench/low | fixed_g2_vs_adaedl | 30 | 42.89 [26.75, 53.85] | 12.79 [8.79, 15.41] | 6 | 0 |
| mtbench/low | fixed_fast_vs_adaedl | 30 | 22.75 [11.72, 33.04] | -23.26 [-27.90, -18.14] | 5 | 0 |
| mtbench/low | fixed_g8_vs_adaedl | 30 | -15.33 [-20.79, -8.31] | -99.06 [-110.11, -86.47] | 11 | 0 |
| mtbench/low | markov_w0_robust_vs_adaedl | 30 | 30.38 [13.31, 42.85] | 4.72 [-5.38, 10.92] | 7 | 0 |
| mtbench/low | markov_w05_robust_vs_adaedl | 30 | 40.27 [19.83, 54.29] | 22.14 [14.29, 26.81] | 6 | 0 |
| mtbench/high | sync_g4 | 30 | -16.67 [-19.33, -14.47] | 15.93 [12.85, 18.29] | 0 | 0 |
| mtbench/high | fixed_g2 | 30 | -9.58 [-13.30, -6.39] | 13.97 [10.21, 16.94] | 9 | 0 |
| mtbench/high | fixed_g8 | 30 | -3.26 [-6.46, 0.15] | -44.27 [-48.13, -39.93] | 10 | 0 |
| mtbench/high | adaedl | 30 | -29.00 [-30.82, -26.94] | -2.32 [-5.13, 0.69] | 9 | 0 |
| mtbench/high | markov_w0_robust | 30 | 7.18 [5.15, 9.18] | -23.03 [-26.05, -19.95] | 10 | 0 |
| mtbench/high | markov_w05_robust | 30 | -7.99 [-9.66, -6.13] | 10.91 [7.07, 14.03] | 6 | 0 |
| mtbench/high | sync_g4_vs_fixed_g2 | 30 | -7.84 [-9.33, -6.48] | 2.28 [0.79, 3.56] | 9 | 0 |
| mtbench/high | fixed_fast_vs_fixed_g2 | 30 | 10.59 [6.83, 15.34] | -16.23 [-20.39, -11.37] | 9 | 0 |
| mtbench/high | fixed_g8_vs_fixed_g2 | 30 | 6.99 [0.26, 15.03] | -67.68 [-77.74, -56.33] | 15 | 0 |
| mtbench/high | adaedl_vs_fixed_g2 | 30 | -21.48 [-23.70, -18.65] | -18.93 [-21.84, -15.56] | 9 | 0 |
| mtbench/high | markov_w0_robust_vs_fixed_g2 | 30 | 18.54 [14.33, 23.60] | -43.00 [-47.92, -37.03] | 9 | 0 |
| mtbench/high | markov_w05_robust_vs_fixed_g2 | 30 | 1.76 [-1.78, 6.40] | -3.55 [-4.93, -2.35] | 8 | 0 |
| mtbench/high | sync_g4_vs_fixed_g8 | 30 | -13.87 [-19.16, -9.12] | 41.72 [37.87, 44.61] | 10 | 0 |
| mtbench/high | fixed_g2_vs_fixed_g8 | 30 | -6.53 [-13.07, -0.26] | 40.36 [36.03, 43.74] | 15 | 0 |
| mtbench/high | fixed_fast_vs_fixed_g8 | 30 | 3.37 [-0.15, 6.90] | 30.68 [28.54, 32.49] | 10 | 0 |
| mtbench/high | adaedl_vs_fixed_g8 | 30 | -26.61 [-30.12, -22.73] | 29.08 [25.43, 32.40] | 13 | 0 |
| mtbench/high | markov_w0_robust_vs_fixed_g8 | 30 | 10.79 [6.54, 14.70] | 14.72 [11.28, 17.72] | 14 | 0 |
| mtbench/high | markov_w05_robust_vs_fixed_g8 | 30 | -4.89 [-8.42, -1.38] | 38.25 [34.02, 41.64] | 13 | 0 |
| mtbench/high | fixed_g2_vs_sync_g4 | 30 | 8.51 [6.92, 10.29] | -2.33 [-3.69, -0.80] | 9 | 0 |
| mtbench/high | fixed_fast_vs_sync_g4 | 30 | 20.01 [16.92, 23.96] | -18.95 [-22.39, -14.75] | 0 | 0 |
| mtbench/high | fixed_g8_vs_sync_g4 | 30 | 16.10 [10.03, 23.70] | -71.60 [-80.53, -60.95] | 10 | 0 |
| mtbench/high | adaedl_vs_sync_g4 | 30 | -14.79 [-17.34, -12.01] | -21.71 [-25.12, -18.16] | 9 | 0 |
| mtbench/high | markov_w0_robust_vs_sync_g4 | 30 | 28.63 [24.80, 33.40] | -46.34 [-51.39, -40.25] | 10 | 0 |
| mtbench/high | markov_w05_robust_vs_sync_g4 | 30 | 10.43 [7.35, 14.36] | -5.97 [-7.71, -4.02] | 6 | 0 |
| mtbench/high | sync_g4_vs_adaedl | 30 | 17.36 [13.65, 20.98] | 17.83 [15.37, 20.08] | 9 | 0 |
| mtbench/high | fixed_g2_vs_adaedl | 30 | 27.35 [22.92, 31.06] | 15.92 [13.46, 17.93] | 9 | 0 |
| mtbench/high | fixed_fast_vs_adaedl | 30 | 40.84 [36.87, 44.55] | 2.27 [-0.70, 4.88] | 9 | 0 |
| mtbench/high | fixed_g8_vs_adaedl | 30 | 36.25 [29.42, 43.10] | -40.99 [-47.92, -34.10] | 13 | 0 |
| mtbench/high | markov_w0_robust_vs_adaedl | 30 | 50.96 [46.92, 55.06] | -20.24 [-23.31, -16.85] | 10 | 0 |
| mtbench/high | markov_w05_robust_vs_adaedl | 30 | 29.59 [26.09, 32.87] | 12.93 [10.33, 15.09] | 11 | 0 |
| mtbench/dynamic | sync_g4 | 30 | -23.74 [-37.31, -12.13] | 20.50 [8.20, 28.34] | 0 | 0 |
| mtbench/dynamic | fixed_g2 | 30 | 1.96 [-3.94, 6.88] | 24.87 [21.65, 27.55] | 6 | 0 |
| mtbench/dynamic | fixed_g8 | 30 | -23.17 [-26.46, -19.86] | -55.75 [-59.75, -50.95] | 7 | 0 |
| mtbench/dynamic | adaedl | 30 | -30.26 [-35.99, -25.10] | 7.17 [0.69, 12.01] | 5 | 0 |
| mtbench/dynamic | markov_w0_robust | 30 | -2.25 [-11.48, 4.87] | -1.85 [-9.80, 4.97] | 6 | 0 |
| mtbench/dynamic | markov_w05_robust | 30 | 3.88 [0.06, 8.17] | 28.31 [23.57, 32.35] | 10 | 0 |
| mtbench/dynamic | sync_g4_vs_fixed_g2 | 30 | -25.20 [-37.77, -15.56] | -5.81 [-20.86, 2.61] | 6 | 0 |
| mtbench/dynamic | fixed_fast_vs_fixed_g2 | 30 | -1.92 [-6.43, 4.10] | -33.10 [-38.03, -27.63] | 6 | 0 |
| mtbench/dynamic | fixed_g8_vs_fixed_g2 | 30 | -24.64 [-29.78, -18.63] | -107.29 [-119.31, -93.94] | 8 | 0 |
| mtbench/dynamic | adaedl_vs_fixed_g2 | 30 | -31.60 [-36.63, -27.20] | -23.55 [-30.22, -18.81] | 6 | 0 |
| mtbench/dynamic | markov_w0_robust_vs_fixed_g2 | 30 | -4.12 [-12.78, 2.82] | -35.56 [-45.04, -27.27] | 4 | 0 |
| mtbench/dynamic | markov_w05_robust_vs_fixed_g2 | 30 | 1.89 [-1.57, 7.54] | 4.58 [1.17, 8.02] | 6 | 0 |
| mtbench/dynamic | sync_g4_vs_fixed_g8 | 30 | -0.74 [-19.03, 16.21] | 48.95 [40.40, 54.70] | 7 | 0 |
| mtbench/dynamic | fixed_g2_vs_fixed_g8 | 30 | 32.71 [22.90, 42.40] | 51.76 [48.44, 54.40] | 8 | 0 |
| mtbench/dynamic | fixed_fast_vs_fixed_g8 | 30 | 30.16 [24.78, 35.98] | 35.79 [33.75, 37.40] | 7 | 0 |
| mtbench/dynamic | adaedl_vs_fixed_g8 | 30 | -9.23 [-17.62, -0.77] | 40.40 [35.14, 44.53] | 10 | 0 |
| mtbench/dynamic | markov_w0_robust_vs_fixed_g8 | 30 | 27.23 [14.72, 38.29] | 34.60 [28.60, 39.66] | 8 | 0 |
| mtbench/dynamic | markov_w05_robust_vs_fixed_g8 | 30 | 35.21 [25.81, 46.30] | 53.97 [49.57, 57.49] | 11 | 0 |
| mtbench/dynamic | fixed_g2_vs_sync_g4 | 30 | 33.69 [18.42, 60.70] | 5.50 [-2.68, 17.26] | 6 | 0 |
| mtbench/dynamic | fixed_fast_vs_sync_g4 | 30 | 31.13 [13.80, 59.52] | -25.78 [-39.55, -8.93] | 0 | 0 |
| mtbench/dynamic | fixed_g8_vs_sync_g4 | 30 | 0.74 [-13.95, 23.51] | -95.90 [-120.73, -67.78] | 7 | 0 |
| mtbench/dynamic | adaedl_vs_sync_g4 | 30 | -8.56 [-16.08, 2.93] | -16.76 [-24.27, -7.27] | 5 | 0 |
| mtbench/dynamic | markov_w0_robust_vs_sync_g4 | 30 | 28.18 [17.20, 42.25] | -28.11 [-37.65, -18.24] | 6 | 0 |
| mtbench/dynamic | markov_w05_robust_vs_sync_g4 | 30 | 36.21 [19.22, 64.63] | 9.83 [0.05, 21.39] | 10 | 0 |
| mtbench/dynamic | sync_g4_vs_adaedl | 30 | 9.36 [-2.85, 19.15] | 14.36 [6.77, 19.53] | 5 | 0 |
| mtbench/dynamic | fixed_g2_vs_adaedl | 30 | 46.20 [37.36, 57.81] | 19.06 [15.83, 23.21] | 6 | 0 |
| mtbench/dynamic | fixed_fast_vs_adaedl | 30 | 43.39 [33.52, 56.24] | -7.73 [-13.65, -0.69] | 5 | 0 |
| mtbench/dynamic | fixed_g8_vs_adaedl | 30 | 10.17 [0.78, 21.39] | -67.78 [-80.27, -54.19] | 10 | 0 |
| mtbench/dynamic | markov_w0_robust_vs_adaedl | 30 | 40.17 [34.60, 46.06] | -9.72 [-14.36, -4.82] | 6 | 0 |
| mtbench/dynamic | markov_w05_robust_vs_adaedl | 30 | 48.96 [40.02, 60.86] | 22.77 [18.27, 27.46] | 5 | 0 |
| mtbench/pooled | sync_g4 | 30 | -17.53 [-24.28, -12.31] | 22.77 [17.77, 26.48] | 1 | 0 |
| mtbench/pooled | fixed_g2 | 30 | -0.63 [-4.74, 2.79] | 22.15 [19.11, 24.53] | 23 | 0 |
| mtbench/pooled | fixed_g8 | 30 | -18.10 [-20.65, -14.95] | -53.26 [-56.95, -48.69] | 26 | 0 |
| mtbench/pooled | adaedl | 30 | -27.07 [-30.37, -23.82] | 7.23 [3.74, 10.33] | 19 | 0 |
| mtbench/pooled | markov_w0_robust | 30 | 3.83 [-0.35, 7.32] | -2.18 [-5.91, 1.26] | 22 | 0 |
| mtbench/pooled | markov_w05_robust | 30 | 0.45 [-2.48, 3.00] | 24.47 [20.02, 27.95] | 23 | 0 |
| mtbench/pooled | sync_g4_vs_fixed_g2 | 30 | -17.01 [-22.45, -13.40] | 0.80 [-4.03, 3.80] | 23 | 0 |
| mtbench/pooled | fixed_fast_vs_fixed_g2 | 30 | 0.64 [-2.72, 4.97] | -28.44 [-32.50, -23.62] | 23 | 0 |
| mtbench/pooled | fixed_g8_vs_fixed_g2 | 30 | -17.58 [-22.29, -11.47] | -96.86 [-107.54, -84.18] | 34 | 0 |
| mtbench/pooled | adaedl_vs_fixed_g2 | 30 | -26.61 [-29.30, -23.48] | -19.15 [-22.24, -16.01] | 21 | 0 |
| mtbench/pooled | markov_w0_robust_vs_fixed_g2 | 30 | 4.49 [0.67, 8.51] | -31.24 [-35.18, -26.68] | 19 | 0 |
| mtbench/pooled | markov_w05_robust_vs_fixed_g2 | 30 | 1.09 [-1.52, 4.16] | 2.99 [0.57, 5.01] | 19 | 0 |
| mtbench/pooled | sync_g4_vs_fixed_g8 | 30 | 0.70 [-8.65, 9.22] | 49.61 [45.25, 52.94] | 26 | 0 |
| mtbench/pooled | fixed_g2_vs_fixed_g8 | 30 | 21.33 [12.96, 28.68] | 49.20 [45.71, 51.82] | 34 | 0 |
| mtbench/pooled | fixed_fast_vs_fixed_g8 | 30 | 22.11 [17.58, 26.02] | 34.75 [32.75, 36.29] | 26 | 0 |
| mtbench/pooled | adaedl_vs_fixed_g8 | 30 | -10.95 [-16.46, -5.64] | 39.47 [35.67, 42.57] | 34 | 0 |
| mtbench/pooled | markov_w0_robust_vs_fixed_g8 | 30 | 26.78 [18.96, 33.61] | 33.33 [29.49, 36.52] | 35 | 0 |
| mtbench/pooled | markov_w05_robust_vs_fixed_g8 | 30 | 22.65 [15.19, 29.12] | 50.72 [46.43, 53.95] | 37 | 0 |
| mtbench/pooled | fixed_g2_vs_sync_g4 | 30 | 20.49 [15.48, 28.95] | -0.81 [-3.95, 3.87] | 23 | 0 |
| mtbench/pooled | fixed_fast_vs_sync_g4 | 30 | 21.26 [14.04, 32.07] | -29.48 [-36.01, -21.61] | 1 | 0 |
| mtbench/pooled | fixed_g8_vs_sync_g4 | 30 | -0.69 [-8.44, 9.47] | -98.45 [-112.49, -82.64] | 26 | 0 |
| mtbench/pooled | adaedl_vs_sync_g4 | 30 | -11.57 [-15.02, -7.07] | -20.12 [-23.67, -16.04] | 19 | 0 |
| mtbench/pooled | markov_w0_robust_vs_sync_g4 | 30 | 25.90 [20.81, 32.36] | -32.31 [-37.10, -26.75] | 22 | 0 |
| mtbench/pooled | markov_w05_robust_vs_sync_g4 | 30 | 21.80 [15.31, 31.79] | 2.20 [-2.18, 7.41] | 23 | 0 |
| mtbench/pooled | sync_g4_vs_adaedl | 30 | 13.08 [7.61, 17.68] | 16.75 [13.82, 19.14] | 19 | 0 |
| mtbench/pooled | fixed_g2_vs_adaedl | 30 | 36.26 [30.69, 41.44] | 16.07 [13.80, 18.19] | 21 | 0 |
| mtbench/pooled | fixed_fast_vs_adaedl | 30 | 37.12 [31.27, 43.63] | -7.80 [-11.52, -3.89] | 19 | 0 |
| mtbench/pooled | fixed_g8_vs_adaedl | 30 | 12.30 [5.98, 19.71] | -65.21 [-74.11, -55.45] | 34 | 0 |
| mtbench/pooled | markov_w0_robust_vs_adaedl | 30 | 42.37 [36.77, 46.96] | -10.15 [-13.31, -7.01] | 23 | 0 |
| mtbench/pooled | markov_w05_robust_vs_adaedl | 30 | 37.73 [31.00, 43.72] | 18.58 [14.82, 21.63] | 22 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
