# Progress probe: gemma_full_dist_110

State: complete; 1980/1980 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | sync_g4 | 110 | 24739 | 14.074 | 0.9537 | 8 | 0.00 |
| all/low | fixed_g2 | 110 | 24667 | 15.177 | 1.0677 | 8 | 47.47 |
| all/low | fixed_fast | 110 | 24739 | 12.568 | 1.3215 | 8 | 45.98 |
| all/low | fixed_g8 | 110 | 24671 | 9.093 | 1.8594 | 8 | 34.72 |
| all/low | markov_w0_dist | 110 | 24531 | 16.073 | 0.9841 | 8 | 44.95 |
| all/low | markov_w05_dist | 110 | 24464 | 16.139 | 0.9720 | 8 | 42.31 |
| all/high | sync_g4 | 110 | 24680 | 9.712 | 1.0665 | 8 | 0.00 |
| all/high | fixed_g2 | 110 | 24715 | 13.145 | 1.1347 | 8 | 47.47 |
| all/high | fixed_fast | 110 | 24664 | 12.452 | 1.3223 | 8 | 46.04 |
| all/high | fixed_g8 | 110 | 24672 | 9.038 | 1.8614 | 8 | 34.74 |
| all/high | markov_w0_dist | 110 | 24445 | 13.400 | 1.1664 | 8 | 51.50 |
| all/high | markov_w05_dist | 110 | 24697 | 13.263 | 1.1305 | 8 | 50.62 |
| all/dynamic | sync_g4 | 110 | 24713 | 11.823 | 1.0116 | 8 | 0.00 |
| all/dynamic | fixed_g2 | 110 | 24775 | 14.171 | 1.0989 | 8 | 47.44 |
| all/dynamic | fixed_fast | 110 | 24733 | 12.522 | 1.3227 | 8 | 46.03 |
| all/dynamic | fixed_g8 | 110 | 24717 | 9.078 | 1.8589 | 8 | 34.75 |
| all/dynamic | markov_w0_dist | 110 | 24762 | 14.352 | 1.0899 | 8 | 49.53 |
| all/dynamic | markov_w05_dist | 110 | 24761 | 14.426 | 1.0564 | 8 | 47.68 |
| all/pooled | sync_g4 | 330 | 74132 | 11.603 | 1.0106 | 24 | 0.00 |
| all/pooled | fixed_g2 | 330 | 74157 | 14.115 | 1.1005 | 24 | 47.46 |
| all/pooled | fixed_fast | 330 | 74136 | 12.514 | 1.3222 | 24 | 46.01 |
| all/pooled | fixed_g8 | 330 | 74060 | 9.070 | 1.8599 | 24 | 34.73 |
| all/pooled | markov_w0_dist | 330 | 73738 | 14.527 | 1.0801 | 24 | 48.82 |
| all/pooled | markov_w05_dist | 330 | 73922 | 14.510 | 1.0532 | 24 | 47.04 |
| gsm8k/low | sync_g4 | 50 | 7156 | 14.638 | 0.9097 | 0 | 0.00 |
| gsm8k/low | fixed_g2 | 50 | 7174 | 15.882 | 1.0036 | 0 | 50.93 |
| gsm8k/low | fixed_fast | 50 | 7156 | 13.852 | 1.1893 | 0 | 52.24 |
| gsm8k/low | fixed_g8 | 50 | 7174 | 10.772 | 1.5637 | 0 | 41.97 |
| gsm8k/low | markov_w0_dist | 50 | 7174 | 16.280 | 0.9641 | 0 | 47.68 |
| gsm8k/low | markov_w05_dist | 50 | 7152 | 16.387 | 0.9491 | 0 | 44.71 |
| gsm8k/high | sync_g4 | 50 | 7152 | 10.206 | 1.0190 | 0 | 0.00 |
| gsm8k/high | fixed_g2 | 50 | 7153 | 13.918 | 1.0669 | 0 | 51.07 |
| gsm8k/high | fixed_fast | 50 | 7152 | 13.671 | 1.1912 | 0 | 52.40 |
| gsm8k/high | fixed_g8 | 50 | 7156 | 10.641 | 1.5682 | 0 | 42.06 |
| gsm8k/high | markov_w0_dist | 50 | 7152 | 14.082 | 1.1013 | 0 | 54.89 |
| gsm8k/high | markov_w05_dist | 50 | 7152 | 13.947 | 1.0786 | 0 | 53.40 |
| gsm8k/dynamic | sync_g4 | 50 | 7152 | 12.388 | 0.9654 | 0 | 0.00 |
| gsm8k/dynamic | fixed_g2 | 50 | 7152 | 15.027 | 1.0308 | 0 | 50.95 |
| gsm8k/dynamic | fixed_fast | 50 | 7152 | 13.825 | 1.1901 | 0 | 52.24 |
| gsm8k/dynamic | fixed_g8 | 50 | 7154 | 10.754 | 1.5591 | 0 | 42.10 |
| gsm8k/dynamic | markov_w0_dist | 50 | 7152 | 14.824 | 1.0478 | 0 | 51.94 |
| gsm8k/dynamic | markov_w05_dist | 50 | 7152 | 14.985 | 1.0156 | 0 | 49.32 |
| gsm8k/pooled | sync_g4 | 150 | 21460 | 12.145 | 0.9647 | 0 | 0.00 |
| gsm8k/pooled | fixed_g2 | 150 | 21479 | 14.900 | 1.0337 | 0 | 50.98 |
| gsm8k/pooled | fixed_fast | 150 | 21460 | 13.782 | 1.1902 | 0 | 52.30 |
| gsm8k/pooled | fixed_g8 | 150 | 21484 | 10.722 | 1.5637 | 0 | 42.04 |
| gsm8k/pooled | markov_w0_dist | 150 | 21478 | 15.009 | 1.0377 | 0 | 51.64 |
| gsm8k/pooled | markov_w05_dist | 150 | 21456 | 15.041 | 1.0144 | 0 | 49.28 |
| mtbench/low | sync_g4 | 30 | 5823 | 11.528 | 1.1611 | 2 | 0.00 |
| mtbench/low | fixed_g2 | 30 | 5740 | 12.164 | 1.3436 | 2 | 32.34 |
| mtbench/low | fixed_fast | 30 | 5823 | 8.856 | 1.8808 | 2 | 24.47 |
| mtbench/low | fixed_g8 | 30 | 5760 | 5.614 | 3.0186 | 2 | 11.65 |
| mtbench/low | markov_w0_dist | 30 | 5615 | 13.928 | 1.1330 | 2 | 31.54 |
| mtbench/low | markov_w05_dist | 30 | 5570 | 14.065 | 1.1172 | 2 | 30.52 |
| mtbench/high | sync_g4 | 30 | 5765 | 8.031 | 1.3005 | 1 | 0.00 |
| mtbench/high | fixed_g2 | 30 | 5793 | 10.502 | 1.4247 | 1 | 32.42 |
| mtbench/high | fixed_fast | 30 | 5749 | 8.728 | 1.8920 | 1 | 24.19 |
| mtbench/high | fixed_g8 | 30 | 5747 | 5.561 | 3.0295 | 1 | 11.74 |
| mtbench/high | markov_w0_dist | 30 | 5542 | 10.253 | 1.4887 | 1 | 34.18 |
| mtbench/high | markov_w05_dist | 30 | 5794 | 10.263 | 1.3859 | 1 | 34.74 |
| mtbench/dynamic | sync_g4 | 30 | 5761 | 9.769 | 1.2358 | 1 | 0.00 |
| mtbench/dynamic | fixed_g2 | 30 | 5817 | 11.362 | 1.3756 | 1 | 32.63 |
| mtbench/dynamic | fixed_fast | 30 | 5781 | 8.798 | 1.8880 | 1 | 24.70 |
| mtbench/dynamic | fixed_g8 | 30 | 5747 | 5.614 | 3.0111 | 1 | 12.10 |
| mtbench/dynamic | markov_w0_dist | 30 | 5810 | 11.714 | 1.3085 | 1 | 33.96 |
| mtbench/dynamic | markov_w05_dist | 30 | 5810 | 11.961 | 1.2393 | 1 | 32.92 |
| mtbench/pooled | sync_g4 | 90 | 17349 | 9.571 | 1.2322 | 4 | 0.00 |
| mtbench/pooled | fixed_g2 | 90 | 17350 | 11.299 | 1.3814 | 4 | 32.46 |
| mtbench/pooled | fixed_fast | 90 | 17353 | 8.794 | 1.8869 | 4 | 24.46 |
| mtbench/pooled | fixed_g8 | 90 | 17254 | 5.596 | 3.0197 | 4 | 11.83 |
| mtbench/pooled | markov_w0_dist | 90 | 16967 | 11.786 | 1.3093 | 4 | 33.32 |
| mtbench/pooled | markov_w05_dist | 90 | 17174 | 11.874 | 1.2491 | 4 | 32.84 |
| humaneval/low | sync_g4 | 30 | 11760 | 15.397 | 0.8777 | 6 | 0.00 |
| humaneval/low | fixed_g2 | 30 | 11753 | 16.749 | 0.9722 | 6 | 53.96 |
| humaneval/low | fixed_fast | 30 | 11760 | 14.804 | 1.1250 | 6 | 56.32 |
| humaneval/low | fixed_g8 | 30 | 11737 | 11.493 | 1.4713 | 6 | 48.67 |
| humaneval/low | markov_w0_dist | 30 | 11742 | 17.206 | 0.9251 | 6 | 50.22 |
| humaneval/low | markov_w05_dist | 30 | 11742 | 17.183 | 0.9172 | 6 | 46.90 |
| humaneval/high | sync_g4 | 30 | 11763 | 10.478 | 0.9808 | 7 | 0.00 |
| humaneval/high | fixed_g2 | 30 | 11769 | 14.448 | 1.0332 | 7 | 53.92 |
| humaneval/high | fixed_fast | 30 | 11763 | 14.724 | 1.1237 | 7 | 56.40 |
| humaneval/high | fixed_g8 | 30 | 11769 | 11.494 | 1.4693 | 7 | 48.53 |
| humaneval/high | markov_w0_dist | 30 | 11751 | 15.146 | 1.0541 | 7 | 59.07 |
| humaneval/high | markov_w05_dist | 30 | 11751 | 14.974 | 1.0362 | 7 | 57.53 |
| humaneval/dynamic | sync_g4 | 30 | 11800 | 12.782 | 0.9302 | 7 | 0.00 |
| humaneval/dynamic | fixed_g2 | 30 | 11806 | 15.527 | 1.0037 | 7 | 53.78 |
| humaneval/dynamic | fixed_fast | 30 | 11800 | 14.736 | 1.1262 | 7 | 56.16 |
| humaneval/dynamic | fixed_g8 | 30 | 11816 | 11.430 | 1.4800 | 7 | 48.11 |
| humaneval/dynamic | markov_w0_dist | 30 | 11800 | 15.800 | 1.0078 | 7 | 56.60 |
| humaneval/dynamic | markov_w05_dist | 30 | 11799 | 15.661 | 0.9910 | 7 | 54.45 |
| humaneval/pooled | sync_g4 | 90 | 35323 | 12.572 | 0.9296 | 20 | 0.00 |
| humaneval/pooled | fixed_g2 | 90 | 35328 | 15.518 | 1.0031 | 20 | 53.89 |
| humaneval/pooled | fixed_fast | 90 | 35323 | 14.755 | 1.1250 | 20 | 56.29 |
| humaneval/pooled | fixed_g8 | 90 | 35322 | 11.472 | 1.4735 | 20 | 48.44 |
| humaneval/pooled | markov_w0_dist | 90 | 35293 | 16.005 | 0.9957 | 20 | 55.50 |
| humaneval/pooled | markov_w05_dist | 90 | 35292 | 15.886 | 0.9815 | 20 | 53.16 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | sync_g4 | 110 | 11.99 [8.28, 16.00] | 27.83 [25.66, 29.98] | 0 | 0 |
| all/low | fixed_g2 | 110 | 20.76 [17.32, 24.31] | 19.20 [17.21, 21.21] | 12 | 0 |
| all/low | fixed_g8 | 110 | -27.65 [-29.69, -25.48] | -40.71 [-44.74, -36.63] | 17 | 0 |
| all/low | markov_w0_dist | 110 | 27.89 [23.19, 32.97] | 25.53 [22.57, 28.42] | 13 | 0 |
| all/low | markov_w05_dist | 110 | 28.42 [23.39, 33.79] | 26.45 [23.50, 29.37] | 13 | 0 |
| all/low | sync_g4_vs_fixed_g2 | 110 | -7.27 [-9.70, -4.83] | 10.68 [9.72, 11.67] | 12 | 0 |
| all/low | fixed_fast_vs_fixed_g2 | 110 | -17.19 [-19.55, -14.76] | -23.77 [-26.92, -20.79] | 12 | 0 |
| all/low | fixed_g8_vs_fixed_g2 | 110 | -40.09 [-43.24, -36.65] | -74.15 [-83.18, -65.39] | 16 | 0 |
| all/low | markov_w0_dist_vs_fixed_g2 | 110 | 5.90 [4.23, 7.65] | 7.83 [6.39, 9.31] | 7 | 0 |
| all/low | markov_w05_dist_vs_fixed_g2 | 110 | 6.34 [4.56, 8.17] | 8.96 [7.52, 10.42] | 7 | 0 |
| all/low | sync_g4_vs_fixed_g8 | 110 | 54.78 [45.70, 64.54] | 48.71 [45.65, 51.50] | 17 | 0 |
| all/low | fixed_g2_vs_fixed_g8 | 110 | 66.90 [57.86, 76.18] | 42.58 [39.54, 45.41] | 16 | 0 |
| all/low | fixed_fast_vs_fixed_g8 | 110 | 38.21 [34.20, 42.22] | 28.93 [26.81, 30.91] | 17 | 0 |
| all/low | markov_w0_dist_vs_fixed_g8 | 110 | 76.76 [65.59, 88.82] | 47.07 [43.45, 50.44] | 16 | 0 |
| all/low | markov_w05_dist_vs_fixed_g8 | 110 | 77.49 [66.02, 89.83] | 47.72 [44.11, 51.08] | 17 | 0 |
| all/low | fixed_g2_vs_sync_g4 | 110 | 7.83 [5.08, 10.75] | -11.96 [-13.21, -10.77] | 12 | 0 |
| all/low | fixed_fast_vs_sync_g4 | 110 | -10.70 [-13.79, -7.65] | -38.57 [-42.82, -34.52] | 0 | 0 |
| all/low | fixed_g8_vs_sync_g4 | 110 | -35.39 [-39.22, -31.37] | -94.98 [-106.18, -83.98] | 17 | 0 |
| all/low | markov_w0_dist_vs_sync_g4 | 110 | 14.20 [11.93, 16.89] | -3.19 [-4.47, -1.89] | 13 | 0 |
| all/low | markov_w05_dist_vs_sync_g4 | 110 | 14.67 [12.35, 17.36] | -1.92 [-3.21, -0.65] | 13 | 0 |
| all/high | sync_g4 | 110 | -22.00 [-24.37, -19.56] | 19.35 [16.85, 21.71] | 1 | 0 |
| all/high | fixed_g2 | 110 | 5.57 [2.86, 8.39] | 14.19 [11.99, 16.31] | 6 | 0 |
| all/high | fixed_g8 | 110 | -27.42 [-29.46, -25.24] | -40.76 [-44.80, -36.71] | 11 | 0 |
| all/high | markov_w0_dist | 110 | 7.61 [5.51, 9.78] | 11.79 [9.68, 13.92] | 7 | 0 |
| all/high | markov_w05_dist | 110 | 6.51 [4.37, 8.77] | 14.51 [12.02, 16.96] | 3 | 0 |
| all/high | sync_g4_vs_fixed_g2 | 110 | -26.12 [-26.86, -25.33] | 6.01 [5.30, 6.72] | 7 | 0 |
| all/high | fixed_fast_vs_fixed_g2 | 110 | -5.27 [-7.74, -2.78] | -16.53 [-19.49, -13.63] | 6 | 0 |
| all/high | fixed_g8_vs_fixed_g2 | 110 | -31.25 [-34.76, -27.44] | -64.04 [-72.77, -55.52] | 12 | 0 |
| all/high | markov_w0_dist_vs_fixed_g2 | 110 | 1.94 [0.85, 3.03] | -2.79 [-3.51, -2.13] | 7 | 0 |
| all/high | markov_w05_dist_vs_fixed_g2 | 110 | 0.89 [-0.13, 1.91] | 0.37 [-0.36, 1.12] | 5 | 0 |
| all/high | sync_g4_vs_fixed_g8 | 110 | 7.46 [1.27, 13.97] | 42.70 [39.20, 45.87] | 12 | 0 |
| all/high | fixed_g2_vs_fixed_g8 | 110 | 45.44 [37.82, 53.27] | 39.04 [35.70, 42.12] | 12 | 0 |
| all/high | fixed_fast_vs_fixed_g8 | 110 | 37.77 [33.77, 41.76] | 28.96 [26.85, 30.94] | 11 | 0 |
| all/high | markov_w0_dist_vs_fixed_g8 | 110 | 48.26 [41.38, 55.31] | 37.34 [33.96, 40.46] | 14 | 0 |
| all/high | markov_w05_dist_vs_fixed_g8 | 110 | 46.74 [39.95, 53.72] | 39.26 [35.69, 42.58] | 12 | 0 |
| all/high | fixed_g2_vs_sync_g4 | 110 | 35.35 [33.93, 36.72] | -6.40 [-7.20, -5.60] | 7 | 0 |
| all/high | fixed_fast_vs_sync_g4 | 110 | 28.21 [24.32, 32.22] | -23.99 [-27.73, -20.27] | 1 | 0 |
| all/high | fixed_g8_vs_sync_g4 | 110 | -6.94 [-12.26, -1.25] | -74.53 [-84.75, -64.48] | 12 | 0 |
| all/high | markov_w0_dist_vs_sync_g4 | 110 | 37.97 [35.76, 40.20] | -9.37 [-10.52, -8.19] | 8 | 0 |
| all/high | markov_w05_dist_vs_sync_g4 | 110 | 36.56 [34.19, 38.74] | -6.00 [-6.90, -5.13] | 4 | 0 |
| all/dynamic | sync_g4 | 110 | -5.58 [-8.36, -2.42] | 23.52 [21.30, 25.73] | 1 | 0 |
| all/dynamic | fixed_g2 | 110 | 13.17 [10.47, 16.03] | 16.93 [14.87, 18.94] | 5 | 0 |
| all/dynamic | fixed_g8 | 110 | -27.50 [-29.41, -25.39] | -40.53 [-44.37, -36.70] | 13 | 0 |
| all/dynamic | markov_w0_dist | 110 | 14.62 [11.45, 18.02] | 17.60 [14.95, 20.27] | 6 | 0 |
| all/dynamic | markov_w05_dist | 110 | 15.20 [11.79, 19.02] | 20.14 [17.29, 23.02] | 7 | 0 |
| all/dynamic | sync_g4_vs_fixed_g2 | 110 | -16.57 [-17.61, -15.54] | 7.94 [7.22, 8.67] | 6 | 0 |
| all/dynamic | fixed_fast_vs_fixed_g2 | 110 | -11.64 [-13.82, -9.48] | -20.37 [-23.36, -17.46] | 5 | 0 |
| all/dynamic | fixed_g8_vs_fixed_g2 | 110 | -35.94 [-39.05, -32.56] | -69.17 [-77.92, -60.75] | 15 | 0 |
| all/dynamic | markov_w0_dist_vs_fixed_g2 | 110 | 1.28 [0.28, 2.25] | 0.81 [-0.27, 1.91] | 3 | 0 |
| all/dynamic | markov_w05_dist_vs_fixed_g2 | 110 | 1.80 [0.64, 3.09] | 3.87 [2.62, 5.19] | 2 | 0 |
| all/dynamic | sync_g4_vs_fixed_g8 | 110 | 30.24 [23.07, 38.01] | 45.58 [42.43, 48.53] | 14 | 0 |
| all/dynamic | fixed_g2_vs_fixed_g8 | 110 | 56.11 [48.28, 64.08] | 40.89 [37.79, 43.80] | 15 | 0 |
| all/dynamic | fixed_fast_vs_fixed_g8 | 110 | 37.94 [34.03, 41.66] | 28.84 [26.85, 30.73] | 13 | 0 |
| all/dynamic | markov_w0_dist_vs_fixed_g8 | 110 | 58.10 [49.69, 66.97] | 41.37 [37.81, 44.73] | 17 | 0 |
| all/dynamic | markov_w05_dist_vs_fixed_g8 | 110 | 58.91 [50.02, 68.39] | 43.17 [39.56, 46.59] | 17 | 0 |
| all/dynamic | fixed_g2_vs_sync_g4 | 110 | 19.86 [18.40, 21.38] | -8.62 [-9.49, -7.78] | 6 | 0 |
| all/dynamic | fixed_fast_vs_sync_g4 | 110 | 5.91 [2.48, 9.12] | -30.75 [-34.64, -27.06] | 1 | 0 |
| all/dynamic | fixed_g8_vs_sync_g4 | 110 | -23.22 [-27.54, -18.74] | -83.75 [-94.30, -73.70] | 14 | 0 |
| all/dynamic | markov_w0_dist_vs_sync_g4 | 110 | 21.39 [19.84, 22.95] | -7.74 [-8.78, -6.72] | 7 | 0 |
| all/dynamic | markov_w05_dist_vs_sync_g4 | 110 | 22.01 [20.40, 23.81] | -4.42 [-5.47, -3.18] | 8 | 0 |
| all/pooled | sync_g4 | 110 | -7.28 [-9.99, -4.31] | 23.57 [21.29, 25.80] | 2 | 0 |
| all/pooled | fixed_g2 | 110 | 12.80 [10.07, 15.75] | 16.77 [14.78, 18.78] | 23 | 0 |
| all/pooled | fixed_g8 | 110 | -27.52 [-29.47, -25.44] | -40.67 [-44.48, -36.69] | 41 | 0 |
| all/pooled | markov_w0_dist | 110 | 16.09 [13.03, 19.43] | 18.31 [15.74, 20.86] | 26 | 0 |
| all/pooled | markov_w05_dist | 110 | 15.96 [12.71, 19.39] | 20.34 [17.61, 23.04] | 23 | 0 |
| all/pooled | sync_g4_vs_fixed_g2 | 110 | -17.80 [-18.68, -16.84] | 8.17 [7.50, 8.86] | 25 | 0 |
| all/pooled | fixed_fast_vs_fixed_g2 | 110 | -11.35 [-13.61, -9.15] | -20.15 [-23.13, -17.34] | 23 | 0 |
| all/pooled | fixed_g8_vs_fixed_g2 | 110 | -35.75 [-38.96, -32.33] | -69.01 [-77.80, -60.46] | 43 | 0 |
| all/pooled | markov_w0_dist_vs_fixed_g2 | 110 | 2.92 [2.28, 3.56] | 1.85 [1.08, 2.64] | 17 | 0 |
| all/pooled | markov_w05_dist_vs_fixed_g2 | 110 | 2.80 [2.11, 3.54] | 4.29 [3.30, 5.32] | 14 | 0 |
| all/pooled | sync_g4_vs_fixed_g8 | 110 | 27.93 [20.83, 35.59] | 45.67 [42.45, 48.68] | 43 | 0 |
| all/pooled | fixed_g2_vs_fixed_g8 | 110 | 55.63 [47.79, 63.83] | 40.83 [37.68, 43.76] | 43 | 0 |
| all/pooled | fixed_fast_vs_fixed_g8 | 110 | 37.97 [34.11, 41.78] | 28.91 [26.84, 30.79] | 41 | 0 |
| all/pooled | markov_w0_dist_vs_fixed_g8 | 110 | 60.18 [51.77, 69.29] | 41.93 [38.52, 45.19] | 47 | 0 |
| all/pooled | markov_w05_dist_vs_fixed_g8 | 110 | 59.99 [51.26, 69.00] | 43.37 [39.74, 46.70] | 46 | 0 |
| all/pooled | fixed_g2_vs_sync_g4 | 110 | 21.65 [20.26, 22.98] | -8.90 [-9.72, -8.11] | 25 | 0 |
| all/pooled | fixed_fast_vs_sync_g4 | 110 | 7.85 [4.50, 11.09] | -30.84 [-34.77, -27.04] | 2 | 0 |
| all/pooled | fixed_g8_vs_sync_g4 | 110 | -21.83 [-26.25, -17.24] | -84.05 [-94.86, -73.77] | 43 | 0 |
| all/pooled | markov_w0_dist_vs_sync_g4 | 110 | 25.21 [24.01, 26.38] | -6.88 [-7.51, -6.21] | 28 | 0 |
| all/pooled | markov_w05_dist_vs_sync_g4 | 110 | 25.06 [23.93, 26.19] | -4.22 [-4.99, -3.39] | 25 | 0 |
| gsm8k/low | sync_g4 | 50 | 5.67 [0.73, 9.70] | 23.51 [21.41, 25.51] | 0 | 0 |
| gsm8k/low | fixed_g2 | 50 | 14.65 [7.80, 19.58] | 15.61 [13.37, 17.56] | 4 | 0 |
| gsm8k/low | fixed_g8 | 50 | -22.24 [-24.65, -19.62] | -31.48 [-35.26, -27.64] | 2 | 0 |
| gsm8k/low | markov_w0_dist | 50 | 17.52 [13.21, 21.54] | 18.93 [16.01, 21.60] | 4 | 0 |
| gsm8k/low | markov_w05_dist | 50 | 18.30 [13.84, 22.55] | 20.20 [17.47, 22.79] | 3 | 0 |
| gsm8k/low | sync_g4_vs_fixed_g2 | 50 | -7.83 [-13.56, -1.16] | 9.36 [7.32, 11.50] | 4 | 0 |
| gsm8k/low | fixed_fast_vs_fixed_g2 | 50 | -12.78 [-16.38, -7.24] | -18.50 [-21.31, -15.43] | 4 | 0 |
| gsm8k/low | fixed_g8_vs_fixed_g2 | 50 | -32.18 [-36.34, -26.75] | -55.80 [-63.27, -48.37] | 3 | 0 |
| gsm8k/low | markov_w0_dist_vs_fixed_g2 | 50 | 2.50 [-0.41, 6.21] | 3.94 [2.25, 5.46] | 0 | 0 |
| gsm8k/low | markov_w05_dist_vs_fixed_g2 | 50 | 3.18 [0.28, 6.81] | 5.44 [4.08, 6.83] | 1 | 0 |
| gsm8k/low | sync_g4_vs_fixed_g8 | 50 | 35.89 [26.51, 44.92] | 41.82 [38.59, 44.82] | 2 | 0 |
| gsm8k/low | fixed_g2_vs_fixed_g8 | 50 | 47.44 [36.51, 57.07] | 35.82 [32.60, 38.75] | 3 | 0 |
| gsm8k/low | fixed_fast_vs_fixed_g8 | 50 | 28.59 [24.41, 32.72] | 23.94 [21.65, 26.07] | 2 | 0 |
| gsm8k/low | markov_w0_dist_vs_fixed_g8 | 50 | 51.13 [41.75, 60.28] | 38.34 [34.46, 41.77] | 3 | 0 |
| gsm8k/low | markov_w05_dist_vs_fixed_g8 | 50 | 52.13 [42.60, 61.78] | 39.31 [35.62, 42.63] | 4 | 0 |
| gsm8k/low | fixed_g2_vs_sync_g4 | 50 | 8.50 [1.17, 15.68] | -10.33 [-12.99, -7.89] | 4 | 0 |
| gsm8k/low | fixed_fast_vs_sync_g4 | 50 | -5.37 [-8.84, -0.73] | -30.73 [-34.25, -27.23] | 0 | 0 |
| gsm8k/low | fixed_g8_vs_sync_g4 | 50 | -26.41 [-31.00, -20.95] | -71.89 [-81.23, -62.84] | 2 | 0 |
| gsm8k/low | markov_w0_dist_vs_sync_g4 | 50 | 11.22 [6.87, 17.17] | -5.98 [-8.40, -3.76] | 4 | 0 |
| gsm8k/low | markov_w05_dist_vs_sync_g4 | 50 | 11.95 [7.88, 16.99] | -4.33 [-6.47, -2.58] | 3 | 0 |
| gsm8k/high | sync_g4 | 50 | -25.35 [-27.14, -23.47] | 14.46 [12.33, 16.53] | 0 | 0 |
| gsm8k/high | fixed_g2 | 50 | 1.81 [-0.68, 4.32] | 10.44 [8.57, 12.24] | 1 | 0 |
| gsm8k/high | fixed_g8 | 50 | -22.17 [-24.58, -19.84] | -31.65 [-35.55, -27.98] | 2 | 0 |
| gsm8k/high | markov_w0_dist | 50 | 3.01 [0.48, 5.56] | 7.55 [5.51, 9.59] | 0 | 0 |
| gsm8k/high | markov_w05_dist | 50 | 2.02 [-0.11, 4.37] | 9.45 [7.59, 11.31] | 0 | 0 |
| gsm8k/high | sync_g4_vs_fixed_g2 | 50 | -26.67 [-27.67, -25.65] | 4.49 [3.54, 5.39] | 1 | 0 |
| gsm8k/high | fixed_fast_vs_fixed_g2 | 50 | -1.78 [-4.14, 0.69] | -11.66 [-13.95, -9.37] | 1 | 0 |
| gsm8k/high | fixed_g8_vs_fixed_g2 | 50 | -23.55 [-27.11, -19.73] | -46.99 [-54.03, -40.19] | 3 | 0 |
| gsm8k/high | markov_w0_dist_vs_fixed_g2 | 50 | 1.18 [-0.33, 2.81] | -3.23 [-4.61, -1.88] | 1 | 0 |
| gsm8k/high | markov_w05_dist_vs_fixed_g2 | 50 | 0.20 [-1.34, 1.92] | -1.10 [-1.99, -0.15] | 1 | 0 |
| gsm8k/high | sync_g4_vs_fixed_g8 | 50 | -4.08 [-8.74, 0.77] | 35.02 [31.61, 38.25] | 2 | 0 |
| gsm8k/high | fixed_g2_vs_fixed_g8 | 50 | 30.80 [24.58, 37.19] | 31.97 [28.67, 35.08] | 3 | 0 |
| gsm8k/high | fixed_fast_vs_fixed_g8 | 50 | 28.48 [24.75, 32.59] | 24.04 [21.86, 26.23] | 2 | 0 |
| gsm8k/high | markov_w0_dist_vs_fixed_g8 | 50 | 32.34 [26.77, 38.16] | 29.77 [26.62, 32.92] | 2 | 0 |
| gsm8k/high | markov_w05_dist_vs_fixed_g8 | 50 | 31.07 [25.63, 36.79] | 31.22 [28.08, 34.19] | 2 | 0 |
| gsm8k/high | fixed_g2_vs_sync_g4 | 50 | 36.37 [34.49, 38.26] | -4.70 [-5.70, -3.67] | 1 | 0 |
| gsm8k/high | fixed_fast_vs_sync_g4 | 50 | 33.95 [30.67, 37.24] | -16.90 [-19.80, -14.07] | 0 | 0 |
| gsm8k/high | fixed_g8_vs_sync_g4 | 50 | 4.26 [-0.76, 9.58] | -53.90 [-61.95, -46.21] | 2 | 0 |
| gsm8k/high | markov_w0_dist_vs_sync_g4 | 50 | 37.98 [35.17, 40.85] | -8.08 [-9.94, -6.26] | 0 | 0 |
| gsm8k/high | markov_w05_dist_vs_sync_g4 | 50 | 36.65 [34.32, 39.02] | -5.85 [-7.17, -4.49] | 0 | 0 |
| gsm8k/dynamic | sync_g4 | 50 | -10.40 [-13.72, -6.91] | 18.88 [16.69, 21.06] | 0 | 0 |
| gsm8k/dynamic | fixed_g2 | 50 | 8.69 [6.51, 11.10] | 13.38 [11.75, 15.06] | 0 | 0 |
| gsm8k/dynamic | fixed_g8 | 50 | -22.21 [-24.17, -20.12] | -31.01 [-34.35, -27.60] | 1 | 0 |
| gsm8k/dynamic | markov_w0_dist | 50 | 7.22 [4.57, 10.05] | 11.96 [9.58, 14.33] | 0 | 0 |
| gsm8k/dynamic | markov_w05_dist | 50 | 8.39 [5.32, 11.60] | 14.66 [12.24, 17.15] | 0 | 0 |
| gsm8k/dynamic | sync_g4_vs_fixed_g2 | 50 | -17.57 [-19.76, -15.54] | 6.35 [5.09, 7.52] | 0 | 0 |
| gsm8k/dynamic | fixed_fast_vs_fixed_g2 | 50 | -8.00 [-9.99, -6.11] | -15.45 [-17.73, -13.31] | 0 | 0 |
| gsm8k/dynamic | fixed_g8_vs_fixed_g2 | 50 | -28.44 [-31.50, -25.23] | -51.25 [-57.84, -44.88] | 1 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_fixed_g2 | 50 | -1.35 [-2.61, -0.05] | -1.65 [-3.02, -0.23] | 0 | 0 |
| gsm8k/dynamic | markov_w05_dist_vs_fixed_g2 | 50 | -0.28 [-2.01, 1.52] | 1.48 [0.12, 2.86] | 0 | 0 |
| gsm8k/dynamic | sync_g4_vs_fixed_g8 | 50 | 15.19 [8.45, 22.27] | 38.08 [34.81, 41.17] | 1 | 0 |
| gsm8k/dynamic | fixed_g2_vs_fixed_g8 | 50 | 39.74 [33.74, 45.98] | 33.89 [30.98, 36.65] | 1 | 0 |
| gsm8k/dynamic | fixed_fast_vs_fixed_g8 | 50 | 28.56 [25.18, 31.87] | 23.67 [21.63, 25.57] | 1 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_fixed_g8 | 50 | 37.84 [31.23, 44.74] | 32.80 [29.32, 36.15] | 1 | 0 |
| gsm8k/dynamic | markov_w05_dist_vs_fixed_g8 | 50 | 39.34 [32.27, 46.75] | 34.86 [31.31, 38.20] | 1 | 0 |
| gsm8k/dynamic | fixed_g2_vs_sync_g4 | 50 | 21.31 [18.41, 24.62] | -6.78 [-8.13, -5.37] | 0 | 0 |
| gsm8k/dynamic | fixed_fast_vs_sync_g4 | 50 | 11.61 [7.43, 15.90] | -23.28 [-26.68, -20.03] | 0 | 0 |
| gsm8k/dynamic | fixed_g8_vs_sync_g4 | 50 | -13.19 [-18.22, -7.79] | -61.50 [-69.98, -53.39] | 1 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_sync_g4 | 50 | 19.67 [17.00, 22.48] | -8.54 [-9.92, -7.12] | 0 | 0 |
| gsm8k/dynamic | markov_w05_dist_vs_sync_g4 | 50 | 20.97 [18.20, 24.06] | -5.20 [-6.41, -4.01] | 0 | 0 |
| gsm8k/pooled | sync_g4 | 50 | -11.88 [-14.28, -9.36] | 18.95 [16.85, 20.96] | 0 | 0 |
| gsm8k/pooled | fixed_g2 | 50 | 8.11 [5.29, 10.68] | 13.15 [11.39, 14.83] | 5 | 0 |
| gsm8k/pooled | fixed_g8 | 50 | -22.21 [-24.31, -19.94] | -31.38 [-34.87, -27.86] | 5 | 0 |
| gsm8k/pooled | markov_w0_dist | 50 | 8.90 [6.37, 11.50] | 12.82 [10.61, 14.97] | 4 | 0 |
| gsm8k/pooled | markov_w05_dist | 50 | 9.13 [6.48, 11.91] | 14.77 [12.64, 16.93] | 3 | 0 |
| gsm8k/pooled | sync_g4_vs_fixed_g2 | 50 | -18.49 [-20.33, -16.39] | 6.68 [5.55, 7.83] | 5 | 0 |
| gsm8k/pooled | fixed_fast_vs_fixed_g2 | 50 | -7.50 [-9.65, -5.02] | -15.14 [-17.41, -12.85] | 5 | 0 |
| gsm8k/pooled | fixed_g8_vs_fixed_g2 | 50 | -28.04 [-31.39, -24.40] | -51.26 [-57.95, -44.62] | 7 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_fixed_g2 | 50 | 0.73 [-0.48, 2.00] | -0.38 [-1.37, 0.62] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_fixed_g2 | 50 | 0.94 [-0.34, 2.39] | 1.87 [0.93, 2.82] | 2 | 0 |
| gsm8k/pooled | sync_g4_vs_fixed_g8 | 50 | 13.27 [7.31, 19.53] | 38.31 [35.10, 41.34] | 5 | 0 |
| gsm8k/pooled | fixed_g2_vs_fixed_g8 | 50 | 38.97 [32.27, 45.75] | 33.89 [30.85, 36.69] | 7 | 0 |
| gsm8k/pooled | fixed_fast_vs_fixed_g8 | 50 | 28.54 [24.91, 32.12] | 23.88 [21.79, 25.86] | 5 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_fixed_g8 | 50 | 39.98 [33.56, 46.77] | 33.64 [30.33, 36.76] | 6 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_fixed_g8 | 50 | 40.28 [33.53, 47.18] | 35.13 [31.80, 38.22] | 7 | 0 |
| gsm8k/pooled | fixed_g2_vs_sync_g4 | 50 | 22.68 [19.61, 25.52] | -7.16 [-8.49, -5.87] | 5 | 0 |
| gsm8k/pooled | fixed_fast_vs_sync_g4 | 50 | 13.48 [10.32, 16.66] | -23.38 [-26.51, -20.26] | 0 | 0 |
| gsm8k/pooled | fixed_g8_vs_sync_g4 | 50 | -11.72 [-16.34, -6.81] | -62.09 [-70.46, -54.09] | 5 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_sync_g4 | 50 | 23.58 [21.34, 25.80] | -7.57 [-8.89, -6.30] | 4 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_sync_g4 | 50 | 23.84 [21.65, 26.04] | -5.16 [-6.28, -4.06] | 3 | 0 |
| mtbench/low | sync_g4 | 30 | 30.17 [21.52, 37.88] | 38.27 [35.86, 40.32] | 0 | 0 |
| mtbench/low | fixed_g2 | 30 | 37.34 [33.23, 41.05] | 28.57 [26.35, 30.52] | 5 | 0 |
| mtbench/low | fixed_g8 | 30 | -36.61 [-38.72, -34.20] | -60.49 [-65.82, -54.63] | 10 | 0 |
| mtbench/low | markov_w0_dist | 30 | 57.27 [50.48, 64.88] | 39.76 [36.85, 42.64] | 6 | 0 |
| mtbench/low | markov_w05_dist | 30 | 58.82 [51.74, 66.88] | 40.60 [37.76, 43.52] | 7 | 0 |
| mtbench/low | sync_g4_vs_fixed_g2 | 30 | -5.23 [-11.33, -0.60] | 13.58 [11.48, 15.54] | 5 | 0 |
| mtbench/low | fixed_fast_vs_fixed_g2 | 30 | -27.19 [-29.10, -24.94] | -39.99 [-43.93, -35.77] | 5 | 0 |
| mtbench/low | fixed_g8_vs_fixed_g2 | 30 | -53.84 [-56.30, -50.99] | -124.67 [-137.37, -111.48] | 9 | 0 |
| mtbench/low | markov_w0_dist_vs_fixed_g2 | 30 | 14.51 [11.85, 17.76] | 15.67 [13.61, 18.08] | 5 | 0 |
| mtbench/low | markov_w05_dist_vs_fixed_g2 | 30 | 15.64 [12.95, 18.82] | 16.85 [14.86, 19.06] | 4 | 0 |
| mtbench/low | sync_g4_vs_fixed_g8 | 30 | 105.33 [87.50, 123.41] | 61.54 [58.82, 63.83] | 10 | 0 |
| mtbench/low | fixed_g2_vs_fixed_g8 | 30 | 116.65 [104.05, 128.83] | 55.49 [52.71, 57.87] | 9 | 0 |
| mtbench/low | fixed_fast_vs_fixed_g8 | 30 | 57.74 [51.98, 63.18] | 37.69 [35.33, 39.69] | 10 | 0 |
| mtbench/low | markov_w0_dist_vs_fixed_g8 | 30 | 148.08 [130.98, 166.60] | 62.47 [59.56, 65.13] | 10 | 0 |
| mtbench/low | markov_w05_dist_vs_fixed_g8 | 30 | 150.53 [132.38, 170.26] | 62.99 [60.10, 65.71] | 10 | 0 |
| mtbench/low | fixed_g2_vs_sync_g4 | 30 | 5.51 [0.60, 12.77] | -15.72 [-18.40, -12.97] | 5 | 0 |
| mtbench/low | fixed_fast_vs_sync_g4 | 30 | -23.18 [-27.47, -17.71] | -61.99 [-67.57, -55.91] | 0 | 0 |
| mtbench/low | fixed_g8_vs_sync_g4 | 30 | -51.30 [-55.24, -46.67] | -159.98 [-176.51, -142.83] | 10 | 0 |
| mtbench/low | markov_w0_dist_vs_sync_g4 | 30 | 20.82 [15.58, 28.23] | 2.42 [0.11, 4.86] | 6 | 0 |
| mtbench/low | markov_w05_dist_vs_sync_g4 | 30 | 22.01 [16.43, 29.70] | 3.78 [1.31, 6.38] | 7 | 0 |
| mtbench/high | sync_g4 | 30 | -7.98 [-11.12, -4.78] | 31.26 [28.94, 33.16] | 1 | 0 |
| mtbench/high | fixed_g2 | 30 | 20.33 [16.62, 23.56] | 24.70 [22.55, 26.56] | 3 | 0 |
| mtbench/high | fixed_g8 | 30 | -36.28 [-37.77, -34.60] | -60.12 [-63.99, -56.02] | 5 | 0 |
| mtbench/high | markov_w0_dist | 30 | 17.48 [14.29, 20.62] | 21.32 [18.85, 23.56] | 4 | 0 |
| mtbench/high | markov_w05_dist | 30 | 17.58 [13.67, 21.06] | 26.75 [23.75, 29.59] | 1 | 0 |
| mtbench/high | sync_g4_vs_fixed_g2 | 30 | -23.53 [-24.87, -21.66] | 8.72 [7.58, 9.70] | 4 | 0 |
| mtbench/high | fixed_fast_vs_fixed_g2 | 30 | -16.89 [-19.07, -14.25] | -32.80 [-36.16, -29.11] | 3 | 0 |
| mtbench/high | fixed_g8_vs_fixed_g2 | 30 | -47.04 [-49.44, -44.15] | -112.64 [-122.64, -101.91] | 7 | 0 |
| mtbench/high | markov_w0_dist_vs_fixed_g2 | 30 | -2.37 [-4.14, -1.02] | -4.49 [-6.44, -3.03] | 3 | 0 |
| mtbench/high | markov_w05_dist_vs_fixed_g2 | 30 | -2.28 [-3.78, -0.90] | 2.72 [1.08, 4.48] | 2 | 0 |
| mtbench/high | sync_g4_vs_fixed_g8 | 30 | 44.41 [35.84, 52.71] | 57.07 [54.47, 59.24] | 6 | 0 |
| mtbench/high | fixed_g2_vs_fixed_g8 | 30 | 88.84 [79.07, 97.80] | 52.97 [50.47, 55.08] | 7 | 0 |
| mtbench/high | fixed_fast_vs_fixed_g8 | 30 | 56.94 [52.90, 60.68] | 37.55 [35.90, 39.02] | 5 | 0 |
| mtbench/high | markov_w0_dist_vs_fixed_g8 | 30 | 84.37 [75.48, 92.46] | 50.86 [48.21, 53.07] | 8 | 0 |
| mtbench/high | markov_w05_dist_vs_fixed_g8 | 30 | 84.53 [74.87, 92.89] | 54.25 [51.19, 56.90] | 6 | 0 |
| mtbench/high | fixed_g2_vs_sync_g4 | 30 | 30.76 [27.64, 33.10] | -9.55 [-10.74, -8.21] | 4 | 0 |
| mtbench/high | fixed_fast_vs_sync_g4 | 30 | 8.67 [5.02, 12.51] | -45.48 [-49.62, -40.73] | 1 | 0 |
| mtbench/high | fixed_g8_vs_sync_g4 | 30 | -30.75 [-34.51, -26.39] | -132.94 [-145.32, -119.62] | 6 | 0 |
| mtbench/high | markov_w0_dist_vs_sync_g4 | 30 | 27.67 [24.33, 30.62] | -14.47 [-16.96, -12.45] | 5 | 0 |
| mtbench/high | markov_w05_dist_vs_sync_g4 | 30 | 27.78 [23.19, 31.33] | -6.57 [-8.47, -4.67] | 2 | 0 |
| mtbench/dynamic | sync_g4 | 30 | 11.04 [7.10, 15.07] | 34.55 [32.42, 36.37] | 1 | 0 |
| mtbench/dynamic | fixed_g2 | 30 | 29.14 [25.70, 32.72] | 27.14 [25.12, 28.96] | 3 | 0 |
| mtbench/dynamic | fixed_g8 | 30 | -36.19 [-37.89, -34.37] | -59.48 [-63.81, -55.05] | 6 | 0 |
| mtbench/dynamic | markov_w0_dist | 30 | 33.15 [27.65, 38.51] | 30.69 [27.51, 33.48] | 5 | 0 |
| mtbench/dynamic | markov_w05_dist | 30 | 35.95 [29.86, 42.20] | 34.36 [31.00, 37.43] | 4 | 0 |
| mtbench/dynamic | sync_g4_vs_fixed_g2 | 30 | -14.01 [-15.60, -12.35] | 10.17 [8.83, 11.44] | 4 | 0 |
| mtbench/dynamic | fixed_fast_vs_fixed_g2 | 30 | -22.57 [-24.66, -20.45] | -37.25 [-40.77, -33.55] | 3 | 0 |
| mtbench/dynamic | fixed_g8_vs_fixed_g2 | 30 | -50.59 [-52.90, -48.11] | -118.88 [-129.68, -108.42] | 8 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_fixed_g2 | 30 | 3.10 [0.59, 5.33] | 4.88 [2.65, 6.94] | 2 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_fixed_g2 | 30 | 5.28 [2.77, 7.88] | 9.91 [7.66, 12.16] | 1 | 0 |
| mtbench/dynamic | sync_g4_vs_fixed_g8 | 30 | 74.02 [64.46, 84.17] | 58.96 [56.57, 61.04] | 7 | 0 |
| mtbench/dynamic | fixed_g2_vs_fixed_g8 | 30 | 102.38 [92.72, 112.32] | 54.31 [52.02, 56.46] | 8 | 0 |
| mtbench/dynamic | fixed_fast_vs_fixed_g8 | 30 | 56.71 [52.38, 61.01] | 37.30 [35.50, 38.95] | 6 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_fixed_g8 | 30 | 108.66 [96.12, 121.20] | 56.54 [53.61, 59.05] | 9 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_fixed_g8 | 30 | 113.06 [99.32, 126.56] | 58.84 [55.74, 61.40] | 9 | 0 |
| mtbench/dynamic | fixed_g2_vs_sync_g4 | 30 | 16.30 [14.09, 18.48] | -11.32 [-12.91, -9.68] | 4 | 0 |
| mtbench/dynamic | fixed_fast_vs_sync_g4 | 30 | -9.95 [-13.09, -6.63] | -52.79 [-57.15, -47.96] | 1 | 0 |
| mtbench/dynamic | fixed_g8_vs_sync_g4 | 30 | -42.54 [-45.70, -39.20] | -143.66 [-156.66, -130.26] | 7 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_sync_g4 | 30 | 19.91 [16.69, 22.88] | -5.89 [-8.46, -3.40] | 6 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_sync_g4 | 30 | 22.43 [19.03, 25.97] | -0.29 [-2.62, 2.27] | 5 | 0 |
| mtbench/pooled | sync_g4 | 30 | 8.84 [4.74, 12.91] | 34.70 [32.46, 36.58] | 2 | 0 |
| mtbench/pooled | fixed_g2 | 30 | 28.49 [25.26, 31.57] | 26.79 [24.88, 28.49] | 11 | 0 |
| mtbench/pooled | fixed_g8 | 30 | -36.36 [-37.93, -34.55] | -60.03 [-64.13, -55.59] | 21 | 0 |
| mtbench/pooled | markov_w0_dist | 30 | 34.02 [29.67, 38.36] | 30.61 [28.03, 32.94] | 15 | 0 |
| mtbench/pooled | markov_w05_dist | 30 | 35.03 [30.24, 39.81] | 33.80 [30.91, 36.55] | 12 | 0 |
| mtbench/pooled | sync_g4_vs_fixed_g2 | 30 | -15.29 [-17.14, -13.54] | 10.80 [9.71, 11.81] | 13 | 0 |
| mtbench/pooled | fixed_fast_vs_fixed_g2 | 30 | -22.17 [-23.99, -20.16] | -36.59 [-39.85, -33.12] | 11 | 0 |
| mtbench/pooled | fixed_g8_vs_fixed_g2 | 30 | -50.47 [-52.65, -47.94] | -118.60 [-129.02, -107.52] | 24 | 0 |
| mtbench/pooled | markov_w0_dist_vs_fixed_g2 | 30 | 4.31 [3.03, 5.70] | 5.22 [3.80, 6.66] | 10 | 0 |
| mtbench/pooled | markov_w05_dist_vs_fixed_g2 | 30 | 5.09 [3.57, 6.67] | 9.57 [7.86, 11.52] | 7 | 0 |
| mtbench/pooled | sync_g4_vs_fixed_g8 | 30 | 71.02 [60.67, 81.37] | 59.19 [56.75, 61.27] | 23 | 0 |
| mtbench/pooled | fixed_g2_vs_fixed_g8 | 30 | 101.90 [92.09, 111.19] | 54.25 [51.81, 56.34] | 24 | 0 |
| mtbench/pooled | fixed_fast_vs_fixed_g8 | 30 | 57.13 [52.78, 61.11] | 37.51 [35.73, 39.07] | 21 | 0 |
| mtbench/pooled | markov_w0_dist_vs_fixed_g8 | 30 | 110.59 [98.96, 121.93] | 56.64 [53.92, 58.97] | 27 | 0 |
| mtbench/pooled | markov_w05_dist_vs_fixed_g8 | 30 | 112.17 [99.85, 124.20] | 58.63 [55.73, 61.13] | 25 | 0 |
| mtbench/pooled | fixed_g2_vs_sync_g4 | 30 | 18.06 [15.66, 20.68] | -12.11 [-13.39, -10.75] | 13 | 0 |
| mtbench/pooled | fixed_fast_vs_sync_g4 | 30 | -8.12 [-11.43, -4.52] | -53.13 [-57.69, -48.06] | 2 | 0 |
| mtbench/pooled | fixed_g8_vs_sync_g4 | 30 | -41.53 [-44.86, -37.76] | -145.06 [-158.18, -131.21] | 23 | 0 |
| mtbench/pooled | markov_w0_dist_vs_sync_g4 | 30 | 23.14 [20.95, 25.07] | -6.25 [-7.65, -4.89] | 17 | 0 |
| mtbench/pooled | markov_w05_dist_vs_sync_g4 | 30 | 24.06 [21.45, 26.39] | -1.37 [-2.95, 0.42] | 14 | 0 |
| humaneval/low | sync_g4 | 30 | 4.01 [1.29, 6.77] | 21.98 [20.11, 23.78] | 0 | 0 |
| humaneval/low | fixed_g2 | 30 | 13.14 [10.76, 15.48] | 13.59 [11.84, 15.19] | 3 | 0 |
| humaneval/low | fixed_g8 | 30 | -22.36 [-24.23, -20.45] | -30.78 [-34.08, -27.54] | 5 | 0 |
| humaneval/low | markov_w0_dist | 30 | 16.23 [13.31, 19.10] | 17.77 [15.46, 19.89] | 3 | 0 |
| humaneval/low | markov_w05_dist | 30 | 16.07 [12.46, 19.81] | 18.47 [15.91, 20.89] | 3 | 0 |
| humaneval/low | sync_g4_vs_fixed_g2 | 30 | -8.07 [-9.08, -7.05] | 9.71 [8.97, 10.48] | 3 | 0 |
| humaneval/low | fixed_fast_vs_fixed_g2 | 30 | -11.61 [-13.40, -9.71] | -15.72 [-17.91, -13.43] | 3 | 0 |
| humaneval/low | fixed_g8_vs_fixed_g2 | 30 | -31.38 [-34.21, -28.28] | -51.34 [-57.72, -44.89] | 4 | 0 |
| humaneval/low | markov_w0_dist_vs_fixed_g2 | 30 | 2.73 [1.68, 3.76] | 4.84 [3.87, 5.78] | 2 | 0 |
| humaneval/low | markov_w05_dist_vs_fixed_g2 | 30 | 2.59 [1.31, 3.90] | 5.66 [4.51, 6.78] | 2 | 0 |
| humaneval/low | sync_g4_vs_fixed_g8 | 30 | 33.97 [27.38, 40.56] | 40.34 [37.40, 43.05] | 5 | 0 |
| humaneval/low | fixed_g2_vs_fixed_g8 | 30 | 45.73 [39.43, 51.99] | 33.93 [30.98, 36.60] | 4 | 0 |
| humaneval/low | fixed_fast_vs_fixed_g8 | 30 | 28.81 [25.71, 31.98] | 23.54 [21.59, 25.42] | 5 | 0 |
| humaneval/low | markov_w0_dist_vs_fixed_g8 | 30 | 49.71 [42.54, 56.89] | 37.12 [33.83, 40.12] | 3 | 0 |
| humaneval/low | markov_w05_dist_vs_fixed_g8 | 30 | 49.50 [41.52, 57.71] | 37.66 [34.20, 40.84] | 3 | 0 |
| humaneval/low | fixed_g2_vs_sync_g4 | 30 | 8.78 [7.58, 9.98] | -10.76 [-11.70, -9.85] | 3 | 0 |
| humaneval/low | fixed_fast_vs_sync_g4 | 30 | -3.85 [-6.34, -1.27] | -28.17 [-31.20, -25.17] | 0 | 0 |
| humaneval/low | fixed_g8_vs_sync_g4 | 30 | -25.36 [-28.85, -21.50] | -67.63 [-75.59, -59.75] | 5 | 0 |
| humaneval/low | markov_w0_dist_vs_sync_g4 | 30 | 11.75 [10.56, 12.85] | -5.40 [-6.22, -4.51] | 3 | 0 |
| humaneval/low | markov_w05_dist_vs_sync_g4 | 30 | 11.59 [10.25, 12.88] | -4.50 [-5.47, -3.55] | 3 | 0 |
| humaneval/high | sync_g4 | 30 | -28.84 [-30.52, -27.13] | 12.72 [10.73, 14.74] | 0 | 0 |
| humaneval/high | fixed_g2 | 30 | -1.88 [-3.83, -0.04] | 8.05 [6.35, 9.63] | 2 | 0 |
| humaneval/high | fixed_g8 | 30 | -21.94 [-24.23, -19.81] | -30.75 [-34.67, -27.11] | 4 | 0 |
| humaneval/high | markov_w0_dist | 30 | 2.86 [1.46, 4.27] | 6.20 [4.81, 7.58] | 3 | 0 |
| humaneval/high | markov_w05_dist | 30 | 1.70 [0.32, 3.03] | 7.79 [6.37, 9.20] | 2 | 0 |
| humaneval/high | sync_g4_vs_fixed_g2 | 30 | -27.47 [-28.51, -26.40] | 5.08 [4.10, 6.03] | 2 | 0 |
| humaneval/high | fixed_fast_vs_fixed_g2 | 30 | 1.91 [0.04, 3.99] | -8.75 [-10.65, -6.78] | 2 | 0 |
| humaneval/high | fixed_g8_vs_fixed_g2 | 30 | -20.44 [-23.85, -16.98] | -42.20 [-48.65, -36.03] | 2 | 0 |
| humaneval/high | markov_w0_dist_vs_fixed_g2 | 30 | 4.83 [3.13, 6.46] | -2.01 [-3.15, -0.98] | 3 | 0 |
| humaneval/high | markov_w05_dist_vs_fixed_g2 | 30 | 3.64 [2.25, 5.14] | -0.29 [-1.15, 0.57] | 2 | 0 |
| humaneval/high | sync_g4_vs_fixed_g8 | 30 | -8.84 [-13.14, -3.97] | 33.25 [29.88, 36.64] | 4 | 0 |
| humaneval/high | fixed_g2_vs_fixed_g8 | 30 | 25.70 [20.46, 31.33] | 29.68 [26.49, 32.73] | 2 | 0 |
| humaneval/high | fixed_fast_vs_fixed_g8 | 30 | 28.10 [24.70, 31.98] | 23.52 [21.33, 25.74] | 4 | 0 |
| humaneval/high | markov_w0_dist_vs_fixed_g8 | 30 | 31.77 [27.23, 36.92] | 28.26 [25.35, 31.19] | 4 | 0 |
| humaneval/high | markov_w05_dist_vs_fixed_g8 | 30 | 30.27 [25.76, 35.34] | 29.48 [26.44, 32.47] | 4 | 0 |
| humaneval/high | fixed_g2_vs_sync_g4 | 30 | 37.88 [35.86, 39.88] | -5.35 [-6.42, -4.27] | 2 | 0 |
| humaneval/high | fixed_fast_vs_sync_g4 | 30 | 40.52 [37.24, 43.93] | -14.57 [-17.29, -12.02] | 0 | 0 |
| humaneval/high | fixed_g8_vs_sync_g4 | 30 | 9.70 [4.13, 15.13] | -49.81 [-57.83, -42.61] | 4 | 0 |
| humaneval/high | markov_w0_dist_vs_sync_g4 | 30 | 44.55 [41.74, 47.19] | -7.48 [-9.14, -5.94] | 3 | 0 |
| humaneval/high | markov_w05_dist_vs_sync_g4 | 30 | 42.91 [40.02, 45.57] | -5.65 [-7.04, -4.38] | 2 | 0 |
| humaneval/dynamic | sync_g4 | 30 | -13.26 [-15.62, -10.69] | 17.40 [15.48, 19.34] | 0 | 0 |
| humaneval/dynamic | fixed_g2 | 30 | 5.37 [3.60, 7.20] | 10.88 [9.30, 12.40] | 2 | 0 |
| humaneval/dynamic | fixed_g8 | 30 | -22.44 [-24.72, -20.35] | -31.42 [-35.39, -27.94] | 6 | 0 |
| humaneval/dynamic | markov_w0_dist | 30 | 7.22 [5.11, 9.29] | 10.51 [8.58, 12.31] | 1 | 0 |
| humaneval/dynamic | markov_w05_dist | 30 | 6.28 [3.81, 8.69] | 12.00 [9.81, 14.04] | 3 | 0 |
| humaneval/dynamic | sync_g4_vs_fixed_g2 | 30 | -17.68 [-19.01, -16.36] | 7.32 [6.50, 8.19] | 2 | 0 |
| humaneval/dynamic | fixed_fast_vs_fixed_g2 | 30 | -5.10 [-6.72, -3.48] | -12.20 [-14.15, -10.26] | 2 | 0 |
| humaneval/dynamic | fixed_g8_vs_fixed_g2 | 30 | -26.39 [-29.55, -23.26] | -47.45 [-54.12, -41.28] | 6 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_fixed_g2 | 30 | 1.75 [0.62, 2.93] | -0.41 [-1.55, 0.70] | 1 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_fixed_g2 | 30 | 0.86 [-0.56, 2.33] | 1.27 [0.01, 2.47] | 1 | 0 |
| humaneval/dynamic | sync_g4_vs_fixed_g8 | 30 | 11.83 [6.46, 18.17] | 37.15 [34.10, 40.27] | 6 | 0 |
| humaneval/dynamic | fixed_g2_vs_fixed_g8 | 30 | 35.85 [30.31, 41.95] | 32.18 [29.22, 35.11] | 6 | 0 |
| humaneval/dynamic | fixed_fast_vs_fixed_g8 | 30 | 28.92 [25.56, 32.84] | 23.91 [21.84, 26.14] | 6 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_fixed_g8 | 30 | 38.23 [32.44, 44.48] | 31.90 [28.73, 34.99] | 7 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_fixed_g8 | 30 | 37.02 [31.00, 43.80] | 33.04 [29.73, 36.26] | 7 | 0 |
| humaneval/dynamic | fixed_g2_vs_sync_g4 | 30 | 21.48 [19.56, 23.48] | -7.90 [-8.93, -6.96] | 2 | 0 |
| humaneval/dynamic | fixed_fast_vs_sync_g4 | 30 | 15.28 [11.98, 18.52] | -21.07 [-23.98, -18.31] | 0 | 0 |
| humaneval/dynamic | fixed_g8_vs_sync_g4 | 30 | -10.58 [-15.37, -6.07] | -59.10 [-67.43, -51.74] | 6 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_sync_g4 | 30 | 23.61 [21.38, 25.82] | -8.34 [-9.65, -7.08] | 1 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_sync_g4 | 30 | 22.52 [19.94, 25.21] | -6.53 [-7.91, -5.27] | 3 | 0 |
| humaneval/pooled | sync_g4 | 30 | -14.79 [-16.74, -12.65] | 17.37 [15.51, 19.24] | 0 | 0 |
| humaneval/pooled | fixed_g2 | 30 | 5.17 [3.32, 6.95] | 10.84 [9.21, 12.34] | 7 | 0 |
| humaneval/pooled | fixed_g8 | 30 | -22.25 [-24.33, -20.24] | -30.99 [-34.58, -27.62] | 15 | 0 |
| humaneval/pooled | markov_w0_dist | 30 | 8.47 [6.68, 10.21] | 11.49 [9.78, 13.06] | 7 | 0 |
| humaneval/pooled | markov_w05_dist | 30 | 7.67 [5.64, 9.64] | 12.75 [10.84, 14.53] | 8 | 0 |
| humaneval/pooled | sync_g4_vs_fixed_g2 | 30 | -18.98 [-19.80, -18.09] | 7.33 [6.56, 8.14] | 7 | 0 |
| humaneval/pooled | fixed_fast_vs_fixed_g2 | 30 | -4.92 [-6.50, -3.21] | -12.15 [-14.08, -10.14] | 7 | 0 |
| humaneval/pooled | fixed_g8_vs_fixed_g2 | 30 | -26.07 [-29.09, -22.93] | -46.91 [-53.30, -40.80] | 12 | 0 |
| humaneval/pooled | markov_w0_dist_vs_fixed_g2 | 30 | 3.14 [2.46, 3.81] | 0.73 [0.14, 1.28] | 6 | 0 |
| humaneval/pooled | markov_w05_dist_vs_fixed_g2 | 30 | 2.38 [1.70, 3.10] | 2.15 [1.47, 2.81] | 5 | 0 |
| humaneval/pooled | sync_g4_vs_fixed_g8 | 30 | 9.59 [4.59, 15.20] | 36.92 [33.89, 39.90] | 15 | 0 |
| humaneval/pooled | fixed_g2_vs_fixed_g8 | 30 | 35.26 [29.75, 41.01] | 31.93 [28.98, 34.77] | 12 | 0 |
| humaneval/pooled | fixed_fast_vs_fixed_g8 | 30 | 28.61 [25.38, 32.15] | 23.66 [21.64, 25.69] | 15 | 0 |
| humaneval/pooled | markov_w0_dist_vs_fixed_g8 | 30 | 39.51 [34.02, 45.36] | 32.43 [29.40, 35.31] | 14 | 0 |
| humaneval/pooled | markov_w05_dist_vs_fixed_g8 | 30 | 38.48 [32.56, 44.72] | 33.39 [30.23, 36.40] | 14 | 0 |
| humaneval/pooled | fixed_g2_vs_sync_g4 | 30 | 23.43 [22.09, 24.69] | -7.91 [-8.86, -7.02] | 7 | 0 |
| humaneval/pooled | fixed_fast_vs_sync_g4 | 30 | 17.36 [14.48, 20.11] | -21.02 [-23.82, -18.35] | 0 | 0 |
| humaneval/pooled | fixed_g8_vs_sync_g4 | 30 | -8.75 [-13.20, -4.39] | -58.52 [-66.39, -51.26] | 15 | 0 |
| humaneval/pooled | markov_w0_dist_vs_sync_g4 | 30 | 27.30 [25.60, 28.96] | -7.11 [-8.06, -6.17] | 7 | 0 |
| humaneval/pooled | markov_w05_dist_vs_sync_g4 | 30 | 26.36 [24.86, 27.89] | -5.58 [-6.41, -4.74] | 8 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
