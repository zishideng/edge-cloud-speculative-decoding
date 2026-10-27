# Progress probe: full_110

State: complete; 1540/1540 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high; pooled = low+high.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | sync_g4 | 110 | 24751 | 10.167 | 1.0506 | 7 | 0.00 |
| all/low | fixed_g2 | 110 | 24751 | 12.305 | 1.1512 | 7 | 47.38 |
| all/low | fixed_fast | 110 | 24751 | 12.074 | 1.3420 | 7 | 45.96 |
| all/low | fixed_g8 | 110 | 24782 | 8.959 | 1.8739 | 8 | 34.55 |
| all/low | adaedl | 110 | 24782 | 9.980 | 1.2808 | 8 | 0.00 |
| all/low | markov_w0 | 110 | 24751 | 13.332 | 1.1464 | 7 | 48.47 |
| all/low | markov_w05 | 110 | 24751 | 13.204 | 1.1239 | 7 | 47.66 |
| all/high | sync_g4 | 110 | 24751 | 7.634 | 1.1460 | 7 | 0.00 |
| all/high | fixed_g2 | 110 | 24751 | 8.906 | 1.2942 | 7 | 47.38 |
| all/high | fixed_fast | 110 | 24751 | 10.727 | 1.3999 | 7 | 46.04 |
| all/high | fixed_g8 | 110 | 24782 | 8.887 | 1.8692 | 8 | 34.61 |
| all/high | adaedl | 110 | 24782 | 7.943 | 1.3711 | 8 | 0.00 |
| all/high | markov_w0 | 110 | 24753 | 11.351 | 1.3629 | 7 | 50.86 |
| all/high | markov_w05 | 110 | 24753 | 10.984 | 1.3073 | 7 | 51.65 |
| all/pooled | sync_g4 | 220 | 49502 | 8.720 | 1.0983 | 14 | 0.00 |
| all/pooled | fixed_g2 | 220 | 49502 | 10.333 | 1.2227 | 14 | 47.38 |
| all/pooled | fixed_fast | 220 | 49502 | 11.361 | 1.3710 | 14 | 46.00 |
| all/pooled | fixed_g8 | 220 | 49564 | 8.923 | 1.8716 | 16 | 34.58 |
| all/pooled | adaedl | 220 | 49564 | 8.846 | 1.3260 | 16 | 0.00 |
| all/pooled | markov_w0 | 220 | 49504 | 12.262 | 1.2547 | 14 | 49.77 |
| all/pooled | markov_w05 | 220 | 49504 | 11.992 | 1.2156 | 14 | 49.77 |
| gsm8k/low | sync_g4 | 50 | 7166 | 11.801 | 0.9843 | 0 | 0.00 |
| gsm8k/low | fixed_g2 | 50 | 7166 | 14.692 | 1.0336 | 0 | 50.76 |
| gsm8k/low | fixed_fast | 50 | 7166 | 13.434 | 1.2056 | 0 | 51.85 |
| gsm8k/low | fixed_g8 | 50 | 7166 | 10.536 | 1.5800 | 0 | 41.56 |
| gsm8k/low | adaedl | 50 | 7166 | 11.466 | 1.1529 | 0 | 0.00 |
| gsm8k/low | markov_w0 | 50 | 7166 | 14.921 | 1.0152 | 0 | 49.58 |
| gsm8k/low | markov_w05 | 50 | 7166 | 14.771 | 1.0070 | 0 | 47.31 |
| gsm8k/high | sync_g4 | 50 | 7166 | 8.644 | 1.0688 | 0 | 0.00 |
| gsm8k/high | fixed_g2 | 50 | 7166 | 10.773 | 1.1731 | 0 | 50.73 |
| gsm8k/high | fixed_fast | 50 | 7166 | 12.385 | 1.2415 | 0 | 51.97 |
| gsm8k/high | fixed_g8 | 50 | 7166 | 10.362 | 1.5851 | 0 | 41.71 |
| gsm8k/high | adaedl | 50 | 7166 | 9.241 | 1.2251 | 0 | 0.00 |
| gsm8k/high | markov_w0 | 50 | 7166 | 12.706 | 1.2041 | 0 | 55.87 |
| gsm8k/high | markov_w05 | 50 | 7166 | 12.365 | 1.1809 | 0 | 55.02 |
| gsm8k/pooled | sync_g4 | 100 | 14332 | 9.979 | 1.0266 | 0 | 0.00 |
| gsm8k/pooled | fixed_g2 | 100 | 14332 | 12.431 | 1.1034 | 0 | 50.75 |
| gsm8k/pooled | fixed_fast | 100 | 14332 | 12.888 | 1.2235 | 0 | 51.91 |
| gsm8k/pooled | fixed_g8 | 100 | 14332 | 10.448 | 1.5826 | 0 | 41.64 |
| gsm8k/pooled | adaedl | 100 | 14332 | 10.234 | 1.1890 | 0 | 0.00 |
| gsm8k/pooled | markov_w0 | 100 | 14332 | 13.725 | 1.1096 | 0 | 52.99 |
| gsm8k/pooled | markov_w05 | 100 | 14332 | 13.461 | 1.0940 | 0 | 51.41 |
| humaneval/low | sync_g4 | 30 | 11834 | 9.933 | 0.9922 | 6 | 0.00 |
| humaneval/low | fixed_g2 | 30 | 11834 | 12.039 | 1.0942 | 6 | 54.07 |
| humaneval/low | fixed_fast | 30 | 11834 | 13.838 | 1.1537 | 6 | 56.55 |
| humaneval/low | fixed_g8 | 30 | 11834 | 11.444 | 1.4649 | 6 | 48.93 |
| humaneval/low | adaedl | 30 | 11834 | 10.225 | 1.1720 | 6 | 0.00 |
| humaneval/low | markov_w0 | 30 | 11834 | 13.565 | 1.1330 | 6 | 55.31 |
| humaneval/low | markov_w05 | 30 | 11834 | 13.516 | 1.1113 | 6 | 54.84 |
| humaneval/high | sync_g4 | 30 | 11834 | 7.656 | 1.0825 | 6 | 0.00 |
| humaneval/high | fixed_g2 | 30 | 11834 | 8.560 | 1.2218 | 6 | 54.05 |
| humaneval/high | fixed_fast | 30 | 11834 | 11.726 | 1.2272 | 6 | 56.52 |
| humaneval/high | fixed_g8 | 30 | 11834 | 11.354 | 1.4640 | 6 | 48.85 |
| humaneval/high | adaedl | 30 | 11834 | 8.415 | 1.2320 | 6 | 0.00 |
| humaneval/high | markov_w0 | 30 | 11834 | 12.435 | 1.2551 | 6 | 58.02 |
| humaneval/high | markov_w05 | 30 | 11834 | 12.098 | 1.2362 | 6 | 58.39 |
| humaneval/pooled | sync_g4 | 60 | 23668 | 8.647 | 1.0373 | 12 | 0.00 |
| humaneval/pooled | fixed_g2 | 60 | 23668 | 10.006 | 1.1580 | 12 | 54.06 |
| humaneval/pooled | fixed_fast | 60 | 23668 | 12.695 | 1.1905 | 12 | 56.53 |
| humaneval/pooled | fixed_g8 | 60 | 23668 | 11.399 | 1.4645 | 12 | 48.89 |
| humaneval/pooled | adaedl | 60 | 23668 | 9.232 | 1.2020 | 12 | 0.00 |
| humaneval/pooled | markov_w0 | 60 | 23668 | 12.976 | 1.1940 | 12 | 56.75 |
| humaneval/pooled | markov_w05 | 60 | 23668 | 12.768 | 1.1738 | 12 | 56.71 |
| mtbench/low | sync_g4 | 30 | 5751 | 9.046 | 1.2535 | 1 | 0.00 |
| mtbench/low | fixed_g2 | 30 | 5751 | 10.634 | 1.4149 | 1 | 32.04 |
| mtbench/low | fixed_fast | 30 | 5751 | 8.695 | 1.8993 | 1 | 24.00 |
| mtbench/low | fixed_g8 | 30 | 5782 | 5.497 | 3.0751 | 2 | 11.23 |
| mtbench/low | adaedl | 30 | 5782 | 8.251 | 1.6621 | 2 | 0.00 |
| mtbench/low | markov_w0 | 30 | 5751 | 11.415 | 1.3375 | 1 | 33.95 |
| mtbench/low | markov_w05 | 30 | 5751 | 11.193 | 1.2956 | 1 | 33.28 |
| mtbench/high | sync_g4 | 30 | 5751 | 6.630 | 1.3726 | 1 | 0.00 |
| mtbench/high | fixed_g2 | 30 | 5751 | 7.861 | 1.5941 | 1 | 32.08 |
| mtbench/high | fixed_fast | 30 | 5751 | 7.993 | 1.9528 | 1 | 24.20 |
| mtbench/high | fixed_g8 | 30 | 5782 | 5.482 | 3.0507 | 2 | 11.39 |
| mtbench/high | adaedl | 30 | 5782 | 6.163 | 1.8367 | 2 | 0.00 |
| mtbench/high | markov_w0 | 30 | 5753 | 8.649 | 1.7825 | 1 | 34.27 |
| mtbench/high | markov_w05 | 30 | 5753 | 8.268 | 1.6109 | 1 | 34.38 |
| mtbench/pooled | sync_g4 | 60 | 11502 | 7.652 | 1.3131 | 2 | 0.00 |
| mtbench/pooled | fixed_g2 | 60 | 11502 | 9.039 | 1.5045 | 2 | 32.06 |
| mtbench/pooled | fixed_fast | 60 | 11502 | 8.329 | 1.9260 | 2 | 24.10 |
| mtbench/pooled | fixed_g8 | 60 | 11564 | 5.489 | 3.0629 | 4 | 11.31 |
| mtbench/pooled | adaedl | 60 | 11564 | 7.056 | 1.7494 | 4 | 0.00 |
| mtbench/pooled | markov_w0 | 60 | 11504 | 9.841 | 1.5601 | 2 | 34.13 |
| mtbench/pooled | markov_w05 | 60 | 11504 | 9.511 | 1.4533 | 2 | 33.87 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | sync_g4 | 110 | -15.79 [-19.31, -11.69] | 21.71 [19.15, 24.21] | 0 | 0 |
| all/low | fixed_g2 | 110 | 1.92 [-2.20, 6.73] | 14.22 [11.83, 16.63] | 1 | 0 |
| all/low | fixed_g8 | 110 | -25.80 [-28.38, -23.05] | -39.64 [-44.37, -34.96] | 1 | 1 |
| all/low | adaedl | 110 | -17.34 [-19.77, -14.63] | 4.56 [2.83, 6.46] | 2 | 1 |
| all/low | markov_w0 | 110 | 10.43 [6.81, 14.48] | 14.57 [11.27, 17.96] | 1 | 0 |
| all/low | markov_w05 | 110 | 9.36 [5.68, 13.66] | 16.25 [12.90, 19.74] | 1 | 0 |
| all/low | fixed_g2_vs_sync_g4 | 110 | 21.02 [19.32, 22.76] | -9.57 [-10.71, -8.44] | 1 | 0 |
| all/low | fixed_fast_vs_sync_g4 | 110 | 18.75 [13.23, 23.93] | -27.73 [-31.94, -23.69] | 0 | 0 |
| all/low | fixed_g8_vs_sync_g4 | 110 | -11.88 [-18.71, -4.89] | -78.36 [-90.23, -67.13] | 1 | 1 |
| all/low | adaedl_vs_sync_g4 | 110 | -1.84 [-3.93, 0.22] | -21.91 [-24.31, -19.56] | 2 | 1 |
| all/low | markov_w0_vs_sync_g4 | 110 | 31.13 [28.30, 33.76] | -9.12 [-11.47, -6.76] | 1 | 0 |
| all/low | markov_w05_vs_sync_g4 | 110 | 29.87 [26.65, 32.78] | -6.98 [-9.11, -4.84] | 1 | 0 |
| all/high | sync_g4 | 110 | -28.84 [-30.92, -26.48] | 18.14 [15.83, 20.37] | 0 | 0 |
| all/high | fixed_g2 | 110 | -16.98 [-19.87, -13.84] | 7.55 [5.51, 9.72] | 1 | 0 |
| all/high | fixed_g8 | 110 | -17.16 [-20.68, -13.28] | -33.52 [-38.17, -28.87] | 1 | 1 |
| all/high | adaedl | 110 | -25.96 [-27.08, -24.72] | 2.06 [0.85, 3.31] | 2 | 1 |
| all/high | markov_w0 | 110 | 5.81 [4.10, 7.54] | 2.65 [1.09, 4.26] | 1 | 0 |
| all/high | markov_w05 | 110 | 2.40 [0.73, 4.06] | 6.62 [4.39, 8.91] | 2 | 0 |
| all/high | fixed_g2_vs_sync_g4 | 110 | 16.66 [14.95, 18.68] | -12.94 [-13.93, -11.93] | 1 | 0 |
| all/high | fixed_fast_vs_sync_g4 | 110 | 40.52 [36.01, 44.75] | -22.16 [-25.58, -18.81] | 0 | 0 |
| all/high | fixed_g8_vs_sync_g4 | 110 | 16.41 [8.32, 24.73] | -63.12 [-73.22, -53.34] | 1 | 1 |
| all/high | adaedl_vs_sync_g4 | 110 | 4.05 [1.29, 6.70] | -19.65 [-22.45, -16.94] | 2 | 1 |
| all/high | markov_w0_vs_sync_g4 | 110 | 48.68 [44.31, 52.99] | -18.93 [-21.46, -16.31] | 1 | 0 |
| all/high | markov_w05_vs_sync_g4 | 110 | 43.89 [39.22, 48.60] | -14.08 [-15.57, -12.41] | 2 | 0 |
| all/pooled | sync_g4 | 110 | -23.24 [-25.75, -20.27] | 19.89 [17.47, 22.21] | 0 | 0 |
| all/pooled | fixed_g2 | 110 | -9.05 [-12.40, -5.41] | 10.81 [8.60, 13.10] | 2 | 0 |
| all/pooled | fixed_g8 | 110 | -21.46 [-24.37, -18.25] | -36.51 [-41.11, -31.92] | 2 | 2 |
| all/pooled | adaedl | 110 | -22.14 [-23.62, -20.43] | 3.28 [1.83, 4.80] | 4 | 2 |
| all/pooled | markov_w0 | 110 | 7.93 [5.89, 10.11] | 8.48 [6.15, 10.98] | 2 | 0 |
| all/pooled | markov_w05 | 110 | 5.56 [3.61, 7.71] | 11.33 [8.65, 14.18] | 3 | 0 |
| all/pooled | fixed_g2_vs_sync_g4 | 110 | 18.49 [17.13, 20.04] | -11.33 [-12.33, -10.31] | 2 | 0 |
| all/pooled | fixed_fast_vs_sync_g4 | 110 | 30.28 [25.43, 34.67] | -24.83 [-28.54, -21.17] | 0 | 0 |
| all/pooled | fixed_g8_vs_sync_g4 | 110 | 2.32 [-5.09, 9.86] | -70.41 [-81.11, -60.07] | 2 | 2 |
| all/pooled | adaedl_vs_sync_g4 | 110 | 1.44 [-0.89, 3.74] | -20.73 [-23.26, -18.22] | 4 | 2 |
| all/pooled | markov_w0_vs_sync_g4 | 110 | 40.61 [37.28, 43.82] | -14.24 [-16.40, -12.09] | 2 | 0 |
| all/pooled | markov_w05_vs_sync_g4 | 110 | 37.52 [33.80, 41.17] | -10.68 [-12.25, -9.02] | 3 | 0 |
| gsm8k/low | sync_g4 | 50 | -12.16 [-15.25, -8.59] | 18.35 [16.20, 20.48] | 0 | 0 |
| gsm8k/low | fixed_g2 | 50 | 9.36 [5.82, 12.94] | 14.27 [12.17, 16.23] | 0 | 0 |
| gsm8k/low | fixed_g8 | 50 | -21.57 [-24.06, -18.97] | -31.06 [-34.82, -27.22] | 0 | 0 |
| gsm8k/low | adaedl | 50 | -14.65 [-16.29, -12.69] | 4.37 [2.71, 6.07] | 0 | 0 |
| gsm8k/low | markov_w0 | 50 | 11.07 [8.10, 14.29] | 15.79 [13.18, 18.45] | 0 | 0 |
| gsm8k/low | markov_w05 | 50 | 9.95 [4.97, 14.56] | 16.47 [13.08, 19.59] | 0 | 0 |
| gsm8k/low | fixed_g2_vs_sync_g4 | 50 | 24.50 [21.60, 27.06] | -5.01 [-6.31, -3.71] | 0 | 0 |
| gsm8k/low | fixed_fast_vs_sync_g4 | 50 | 13.84 [9.40, 18.00] | -22.48 [-25.75, -19.33] | 0 | 0 |
| gsm8k/low | fixed_g8_vs_sync_g4 | 50 | -10.72 [-16.38, -4.98] | -60.52 [-69.35, -52.28] | 0 | 0 |
| gsm8k/low | adaedl_vs_sync_g4 | 50 | -2.84 [-5.84, 0.12] | -17.13 [-19.48, -14.97] | 0 | 0 |
| gsm8k/low | markov_w0_vs_sync_g4 | 50 | 26.43 [23.37, 29.96] | -3.14 [-4.69, -1.48] | 0 | 0 |
| gsm8k/low | markov_w05_vs_sync_g4 | 50 | 25.17 [20.71, 29.06] | -2.31 [-4.46, -0.38] | 0 | 0 |
| gsm8k/high | sync_g4 | 50 | -30.20 [-32.34, -27.98] | 13.91 [11.59, 16.20] | 0 | 0 |
| gsm8k/high | fixed_g2 | 50 | -13.01 [-15.44, -10.30] | 5.51 [3.71, 7.40] | 0 | 0 |
| gsm8k/high | fixed_g8 | 50 | -16.33 [-20.19, -12.20] | -27.67 [-32.13, -23.22] | 0 | 0 |
| gsm8k/high | adaedl | 50 | -25.38 [-27.52, -23.03] | 1.32 [-0.73, 3.40] | 0 | 0 |
| gsm8k/high | markov_w0 | 50 | 2.60 [-0.07, 5.28] | 3.02 [1.45, 4.67] | 0 | 0 |
| gsm8k/high | markov_w05 | 50 | -0.16 [-3.11, 2.88] | 4.88 [3.22, 6.59] | 0 | 0 |
| gsm8k/high | fixed_g2_vs_sync_g4 | 50 | 24.63 [21.67, 28.11] | -9.76 [-11.37, -7.97] | 0 | 0 |
| gsm8k/high | fixed_fast_vs_sync_g4 | 50 | 43.27 [38.84, 47.79] | -16.16 [-19.34, -13.11] | 0 | 0 |
| gsm8k/high | fixed_g8_vs_sync_g4 | 50 | 19.87 [12.38, 27.89] | -48.30 [-56.84, -39.98] | 0 | 0 |
| gsm8k/high | adaedl_vs_sync_g4 | 50 | 6.90 [3.59, 10.86] | -14.62 [-17.31, -11.73] | 0 | 0 |
| gsm8k/high | markov_w0_vs_sync_g4 | 50 | 46.99 [42.56, 51.95] | -12.65 [-15.15, -9.93] | 0 | 0 |
| gsm8k/high | markov_w05_vs_sync_g4 | 50 | 43.04 [39.16, 46.87] | -10.48 [-12.36, -8.47] | 0 | 0 |
| gsm8k/pooled | sync_g4 | 50 | -22.57 [-24.46, -20.50] | 16.10 [14.08, 18.13] | 0 | 0 |
| gsm8k/pooled | fixed_g2 | 50 | -3.54 [-5.85, -1.05] | 9.82 [8.07, 11.57] | 0 | 0 |
| gsm8k/pooled | fixed_g8 | 50 | -18.93 [-21.91, -15.85] | -29.34 [-33.49, -25.36] | 0 | 0 |
| gsm8k/pooled | adaedl | 50 | -20.59 [-22.18, -18.88] | 2.82 [1.06, 4.56] | 0 | 0 |
| gsm8k/pooled | markov_w0 | 50 | 6.49 [4.64, 8.52] | 9.31 [7.60, 11.23] | 0 | 0 |
| gsm8k/pooled | markov_w05 | 50 | 4.45 [1.65, 7.09] | 10.59 [8.43, 12.68] | 0 | 0 |
| gsm8k/pooled | fixed_g2_vs_sync_g4 | 50 | 24.57 [22.68, 26.71] | -7.48 [-8.80, -6.06] | 0 | 0 |
| gsm8k/pooled | fixed_fast_vs_sync_g4 | 50 | 29.15 [25.78, 32.38] | -19.19 [-22.15, -16.38] | 0 | 0 |
| gsm8k/pooled | fixed_g8_vs_sync_g4 | 50 | 4.70 [-1.50, 11.10] | -54.16 [-62.78, -46.02] | 0 | 0 |
| gsm8k/pooled | adaedl_vs_sync_g4 | 50 | 2.55 [-0.18, 5.35] | -15.82 [-18.30, -13.40] | 0 | 0 |
| gsm8k/pooled | markov_w0_vs_sync_g4 | 50 | 37.53 [34.77, 40.41] | -8.09 [-9.72, -6.30] | 0 | 0 |
| gsm8k/pooled | markov_w05_vs_sync_g4 | 50 | 34.90 [31.64, 37.88] | -6.56 [-8.20, -4.99] | 0 | 0 |
| humaneval/low | sync_g4 | 30 | -28.22 [-30.29, -25.70] | 14.00 [11.90, 16.18] | 0 | 0 |
| humaneval/low | fixed_g2 | 30 | -13.00 [-15.83, -9.63] | 5.16 [3.21, 7.16] | 0 | 0 |
| humaneval/low | fixed_g8 | 30 | -17.31 [-19.84, -14.89] | -26.97 [-30.85, -23.69] | 0 | 0 |
| humaneval/low | adaedl | 30 | -26.11 [-27.44, -24.49] | -1.58 [-2.74, -0.43] | 0 | 0 |
| humaneval/low | markov_w0 | 30 | -1.97 [-3.83, -0.14] | 1.80 [-0.27, 4.00] | 0 | 0 |
| humaneval/low | markov_w05 | 30 | -2.33 [-3.72, -0.68] | 3.68 [2.02, 5.59] | 0 | 0 |
| humaneval/low | fixed_g2_vs_sync_g4 | 30 | 21.20 [18.94, 23.63] | -10.28 [-11.40, -9.18] | 0 | 0 |
| humaneval/low | fixed_fast_vs_sync_g4 | 30 | 39.32 [34.60, 43.46] | -16.28 [-19.30, -13.51] | 0 | 0 |
| humaneval/low | fixed_g8_vs_sync_g4 | 30 | 15.21 [8.70, 21.63] | -47.64 [-55.58, -40.65] | 0 | 0 |
| humaneval/low | adaedl_vs_sync_g4 | 30 | 2.94 [0.60, 5.38] | -18.12 [-20.70, -15.72] | 0 | 0 |
| humaneval/low | markov_w0_vs_sync_g4 | 30 | 36.56 [32.51, 40.26] | -14.19 [-17.67, -11.23] | 0 | 0 |
| humaneval/low | markov_w05_vs_sync_g4 | 30 | 36.07 [32.70, 39.27] | -12.00 [-14.24, -9.77] | 0 | 0 |
| humaneval/high | sync_g4 | 30 | -34.71 [-35.96, -33.44] | 11.79 [9.86, 13.69] | 0 | 0 |
| humaneval/high | fixed_g2 | 30 | -27.00 [-28.71, -25.28] | 0.44 [-1.45, 2.19] | 0 | 0 |
| humaneval/high | fixed_g8 | 30 | -3.17 [-7.53, 0.93] | -19.30 [-23.39, -15.76] | 0 | 0 |
| humaneval/high | adaedl | 30 | -28.24 [-29.35, -27.12] | -0.39 [-1.63, 0.80] | 0 | 0 |
| humaneval/high | markov_w0 | 30 | 6.05 [3.77, 8.44] | -2.27 [-3.58, -1.02] | 0 | 0 |
| humaneval/high | markov_w05 | 30 | 3.18 [0.76, 5.81] | -0.74 [-1.55, 0.05] | 0 | 0 |
| humaneval/high | fixed_g2_vs_sync_g4 | 30 | 11.82 [10.14, 13.78] | -12.87 [-13.79, -12.07] | 0 | 0 |
| humaneval/high | fixed_fast_vs_sync_g4 | 30 | 53.17 [50.24, 56.14] | -13.37 [-15.86, -10.94] | 0 | 0 |
| humaneval/high | fixed_g8_vs_sync_g4 | 30 | 48.31 [40.20, 56.16] | -35.25 [-42.71, -28.85] | 0 | 0 |
| humaneval/high | adaedl_vs_sync_g4 | 30 | 9.91 [7.22, 12.35] | -13.81 [-16.42, -11.38] | 0 | 0 |
| humaneval/high | markov_w0_vs_sync_g4 | 30 | 62.44 [57.27, 67.63] | -15.95 [-19.68, -12.65] | 0 | 0 |
| humaneval/high | markov_w05_vs_sync_g4 | 30 | 58.03 [52.36, 63.76] | -14.20 [-16.62, -11.80] | 0 | 0 |
| humaneval/pooled | sync_g4 | 30 | -31.89 [-33.32, -30.33] | 12.86 [10.93, 14.85] | 0 | 0 |
| humaneval/pooled | fixed_g2 | 30 | -21.18 [-23.18, -19.04] | 2.73 [0.88, 4.47] | 0 | 0 |
| humaneval/pooled | fixed_g8 | 30 | -10.21 [-13.62, -7.01] | -23.02 [-26.98, -19.59] | 0 | 0 |
| humaneval/pooled | adaedl | 30 | -27.28 [-28.15, -26.40] | -0.97 [-2.08, 0.16] | 0 | 0 |
| humaneval/pooled | markov_w0 | 30 | 2.21 [0.76, 3.66] | -0.30 [-1.74, 1.10] | 0 | 0 |
| humaneval/pooled | markov_w05 | 30 | 0.58 [-0.83, 2.17] | 1.40 [0.37, 2.51] | 0 | 0 |
| humaneval/pooled | fixed_g2_vs_sync_g4 | 30 | 15.72 [14.18, 17.47] | -11.63 [-12.54, -10.84] | 0 | 0 |
| humaneval/pooled | fixed_fast_vs_sync_g4 | 30 | 46.81 [43.53, 49.96] | -14.76 [-17.44, -12.28] | 0 | 0 |
| humaneval/pooled | fixed_g8_vs_sync_g4 | 30 | 31.82 [24.52, 38.84] | -41.17 [-48.90, -34.42] | 0 | 0 |
| humaneval/pooled | adaedl_vs_sync_g4 | 30 | 6.77 [4.31, 9.11] | -15.87 [-18.42, -13.49] | 0 | 0 |
| humaneval/pooled | markov_w0_vs_sync_g4 | 30 | 50.06 [45.62, 54.24] | -15.11 [-18.44, -12.06] | 0 | 0 |
| humaneval/pooled | markov_w05_vs_sync_g4 | 30 | 47.66 [43.19, 51.85] | -13.15 [-15.32, -10.95] | 0 | 0 |
| mtbench/low | sync_g4 | 30 | 4.04 [-1.61, 11.07] | 34.00 [31.49, 36.21] | 0 | 0 |
| mtbench/low | fixed_g2 | 30 | 22.31 [16.07, 30.35] | 25.50 [22.90, 28.26] | 1 | 0 |
| mtbench/low | fixed_g8 | 30 | -36.78 [-38.37, -34.84] | -61.91 [-66.03, -56.90] | 1 | 1 |
| mtbench/low | adaedl | 30 | -5.10 [-10.07, 1.58] | 12.49 [9.30, 15.87] | 2 | 1 |
| mtbench/low | markov_w0 | 30 | 31.29 [23.20, 42.51] | 29.58 [24.93, 35.23] | 1 | 0 |
| mtbench/low | markov_w05 | 30 | 28.74 [18.92, 42.27] | 31.78 [26.72, 37.31] | 1 | 0 |
| mtbench/low | fixed_g2_vs_sync_g4 | 30 | 17.56 [14.65, 20.56] | -12.87 [-15.16, -10.31] | 1 | 0 |
| mtbench/low | fixed_fast_vs_sync_g4 | 30 | -3.88 [-9.97, 1.63] | -51.51 [-56.78, -45.96] | 0 | 0 |
| mtbench/low | fixed_g8_vs_sync_g4 | 30 | -39.24 [-44.42, -33.99] | -145.31 [-159.98, -129.20] | 1 | 1 |
| mtbench/low | adaedl_vs_sync_g4 | 30 | -8.79 [-11.38, -5.79] | -32.59 [-36.05, -28.59] | 2 | 1 |
| mtbench/low | markov_w0_vs_sync_g4 | 30 | 26.19 [22.70, 30.36] | -6.70 [-12.11, -0.35] | 1 | 0 |
| mtbench/low | markov_w05_vs_sync_g4 | 30 | 23.74 [18.25, 30.09] | -3.36 [-8.93, 2.94] | 1 | 0 |
| mtbench/high | sync_g4 | 30 | -17.06 [-20.68, -13.41] | 29.71 [27.40, 31.87] | 0 | 0 |
| mtbench/high | fixed_g2 | 30 | -1.66 [-6.42, 3.82] | 18.37 [15.58, 21.35] | 1 | 0 |
| mtbench/high | fixed_g8 | 30 | -31.42 [-34.70, -28.14] | -56.22 [-61.13, -51.61] | 1 | 1 |
| mtbench/high | adaedl | 30 | -22.90 [-25.54, -20.01] | 5.94 [3.33, 8.75] | 2 | 1 |
| mtbench/high | markov_w0 | 30 | 8.20 [4.95, 11.88] | 8.72 [6.00, 11.91] | 1 | 0 |
| mtbench/high | markov_w05 | 30 | 3.44 [0.58, 6.81] | 17.51 [13.81, 21.64] | 2 | 0 |
| mtbench/high | fixed_g2_vs_sync_g4 | 30 | 18.56 [15.06, 22.44] | -16.14 [-17.76, -14.08] | 1 | 0 |
| mtbench/high | fixed_fast_vs_sync_g4 | 30 | 20.56 [15.49, 26.08] | -42.26 [-46.77, -37.73] | 0 | 0 |
| mtbench/high | fixed_g8_vs_sync_g4 | 30 | -17.32 [-23.59, -11.22] | -122.25 [-136.22, -109.07] | 1 | 1 |
| mtbench/high | adaedl_vs_sync_g4 | 30 | -7.05 [-9.60, -3.77] | -33.81 [-36.80, -30.24] | 2 | 1 |
| mtbench/high | markov_w0_vs_sync_g4 | 30 | 30.46 [27.07, 34.35] | -29.86 [-33.11, -26.29] | 1 | 0 |
| mtbench/high | markov_w05_vs_sync_g4 | 30 | 24.71 [21.18, 29.48] | -17.36 [-20.15, -13.90] | 2 | 0 |
| mtbench/pooled | sync_g4 | 30 | -8.13 [-12.27, -3.52] | 31.82 [29.41, 34.00] | 0 | 0 |
| mtbench/pooled | fixed_g2 | 30 | 8.53 [3.43, 14.90] | 21.88 [19.20, 24.74] | 2 | 0 |
| mtbench/pooled | fixed_g8 | 30 | -34.10 [-36.41, -31.83] | -59.03 [-63.36, -54.47] | 2 | 2 |
| mtbench/pooled | adaedl | 30 | -15.29 [-18.57, -11.16] | 9.17 [6.33, 12.28] | 4 | 2 |
| mtbench/pooled | markov_w0 | 30 | 18.15 [13.85, 23.57] | 19.00 [15.38, 23.35] | 2 | 0 |
| mtbench/pooled | markov_w05 | 30 | 14.18 [9.53, 20.98] | 24.55 [20.21, 29.26] | 3 | 0 |
| mtbench/pooled | fixed_g2_vs_sync_g4 | 30 | 18.14 [15.34, 21.07] | -14.58 [-16.44, -12.40] | 2 | 0 |
| mtbench/pooled | fixed_fast_vs_sync_g4 | 30 | 8.85 [3.65, 13.98] | -46.68 [-51.52, -41.66] | 0 | 0 |
| mtbench/pooled | fixed_g8_vs_sync_g4 | 30 | -28.26 [-33.96, -22.51] | -133.26 [-147.41, -118.99] | 2 | 2 |
| mtbench/pooled | adaedl_vs_sync_g4 | 30 | -7.79 [-10.25, -4.74] | -33.23 [-36.30, -29.53] | 4 | 2 |
| mtbench/pooled | markov_w0_vs_sync_g4 | 30 | 28.61 [25.78, 31.96] | -18.81 [-22.55, -14.44] | 2 | 0 |
| mtbench/pooled | markov_w05_vs_sync_g4 | 30 | 24.29 [20.58, 28.78] | -10.68 [-14.40, -6.04] | 3 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
