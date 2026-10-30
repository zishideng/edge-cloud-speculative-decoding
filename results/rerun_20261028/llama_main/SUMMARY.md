# Progress probe: llama_main

State: complete; 2970/2970 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | picospec_g2 | 110 | 27183 | 26.966 | 0.5595 | 11 | 50.75 |
| all/low | picospec | 110 | 27319 | 24.668 | 0.6600 | 12 | 55.13 |
| all/low | picospec_g8 | 110 | 27147 | 19.909 | 0.8394 | 12 | 53.41 |
| all/low | sync_g4 | 110 | 27597 | 23.456 | 0.5047 | 13 | 0.00 |
| all/low | hf_default | 110 | 27210 | 22.030 | 0.6587 | 12 | 0.00 |
| all/low | pipesd | 110 | 27251 | 24.924 | 0.6318 | 12 | 0.00 |
| all/low | pearl | 110 | 27174 | 27.006 | 0.5026 | 11 | 0.00 |
| all/low | markov_w0_dist_int | 110 | 27524 | 26.323 | 0.5902 | 13 | 56.35 |
| all/low | markov_w05_dist_int | 110 | 27713 | 26.944 | 0.5558 | 14 | 52.83 |
| all/high | picospec_g2 | 110 | 27308 | 14.374 | 0.6994 | 11 | 43.29 |
| all/high | picospec | 110 | 27203 | 18.187 | 0.7762 | 12 | 39.71 |
| all/high | picospec_g8 | 110 | 26941 | 16.310 | 0.9975 | 11 | 31.96 |
| all/high | sync_g4 | 110 | 26925 | 12.848 | 0.6221 | 11 | 0.00 |
| all/high | hf_default | 110 | 26692 | 13.182 | 0.7596 | 7 | 0.00 |
| all/high | pipesd | 110 | 27249 | 15.477 | 1.0002 | 11 | 0.00 |
| all/high | pearl | 110 | 27129 | 18.188 | 0.7497 | 11 | 0.00 |
| all/high | markov_w0_dist_int | 110 | 26900 | 18.570 | 0.8207 | 11 | 45.01 |
| all/high | markov_w05_dist_int | 110 | 27326 | 17.400 | 0.7315 | 12 | 46.92 |
| all/dynamic | picospec_g2 | 110 | 26443 | 20.261 | 0.6240 | 9 | 47.70 |
| all/dynamic | picospec | 110 | 26804 | 21.259 | 0.7131 | 10 | 46.72 |
| all/dynamic | picospec_g8 | 110 | 26774 | 18.014 | 0.9181 | 11 | 40.22 |
| all/dynamic | sync_g4 | 110 | 26805 | 17.588 | 0.5452 | 10 | 0.00 |
| all/dynamic | hf_default | 110 | 26106 | 17.056 | 0.7152 | 7 | 0.00 |
| all/dynamic | pipesd | 110 | 26759 | 20.225 | 0.7726 | 9 | 0.00 |
| all/dynamic | pearl | 110 | 27268 | 19.871 | 0.6143 | 11 | 0.00 |
| all/dynamic | markov_w0_dist_int | 110 | 26323 | 21.866 | 0.7028 | 9 | 51.03 |
| all/dynamic | markov_w05_dist_int | 110 | 26639 | 21.703 | 0.6392 | 10 | 50.79 |
| all/pooled | picospec_g2 | 330 | 80934 | 19.211 | 0.6278 | 31 | 47.04 |
| all/pooled | picospec | 330 | 81326 | 21.047 | 0.7164 | 34 | 46.36 |
| all/pooled | picospec_g8 | 330 | 80862 | 17.963 | 0.9181 | 34 | 40.07 |
| all/pooled | sync_g4 | 330 | 81327 | 16.956 | 0.5569 | 34 | 0.00 |
| all/pooled | hf_default | 330 | 80008 | 16.701 | 0.7108 | 26 | 0.00 |
| all/pooled | pipesd | 330 | 81259 | 19.454 | 0.8017 | 32 | 0.00 |
| all/pooled | pearl | 330 | 81571 | 21.077 | 0.6221 | 33 | 0.00 |
| all/pooled | markov_w0_dist_int | 330 | 80747 | 21.835 | 0.7037 | 33 | 50.01 |
| all/pooled | markov_w05_dist_int | 330 | 81678 | 21.345 | 0.6418 | 36 | 49.94 |
| mtbench/low | picospec_g2 | 30 | 8085 | 23.115 | 0.6597 | 6 | 41.41 |
| mtbench/low | picospec | 30 | 8145 | 19.525 | 0.8368 | 6 | 39.92 |
| mtbench/low | picospec_g8 | 30 | 7802 | 14.494 | 1.1602 | 5 | 30.00 |
| mtbench/low | sync_g4 | 30 | 8145 | 20.752 | 0.5779 | 6 | 0.00 |
| mtbench/low | hf_default | 30 | 8147 | 18.731 | 0.7760 | 7 | 0.00 |
| mtbench/low | pipesd | 30 | 8137 | 20.449 | 0.7733 | 6 | 0.00 |
| mtbench/low | pearl | 30 | 8108 | 24.646 | 0.5521 | 5 | 0.00 |
| mtbench/low | markov_w0_dist_int | 30 | 8195 | 22.219 | 0.6877 | 6 | 44.11 |
| mtbench/low | markov_w05_dist_int | 30 | 8202 | 23.094 | 0.6323 | 6 | 39.99 |
| mtbench/high | picospec_g2 | 30 | 8152 | 12.327 | 0.8193 | 7 | 32.43 |
| mtbench/high | picospec | 30 | 8168 | 14.287 | 0.9939 | 7 | 24.64 |
| mtbench/high | picospec_g8 | 30 | 7745 | 11.576 | 1.4140 | 5 | 14.18 |
| mtbench/high | sync_g4 | 30 | 8168 | 11.075 | 0.7156 | 7 | 0.00 |
| mtbench/high | hf_default | 30 | 7779 | 10.614 | 0.9089 | 4 | 0.00 |
| mtbench/high | pipesd | 30 | 8238 | 11.624 | 1.3437 | 7 | 0.00 |
| mtbench/high | pearl | 30 | 8147 | 14.274 | 0.9586 | 6 | 0.00 |
| mtbench/high | markov_w0_dist_int | 30 | 8093 | 14.113 | 1.0686 | 7 | 30.71 |
| mtbench/high | markov_w05_dist_int | 30 | 8123 | 13.232 | 0.8702 | 7 | 32.54 |
| mtbench/dynamic | picospec_g2 | 30 | 8119 | 16.992 | 0.7383 | 6 | 37.57 |
| mtbench/dynamic | picospec | 30 | 8193 | 16.559 | 0.9177 | 6 | 30.68 |
| mtbench/dynamic | picospec_g8 | 30 | 7863 | 12.780 | 1.2995 | 5 | 19.00 |
| mtbench/dynamic | sync_g4 | 30 | 8193 | 14.880 | 0.6322 | 6 | 0.00 |
| mtbench/dynamic | hf_default | 30 | 7896 | 13.546 | 0.8652 | 5 | 0.00 |
| mtbench/dynamic | pipesd | 30 | 8108 | 15.669 | 1.0005 | 5 | 0.00 |
| mtbench/dynamic | pearl | 30 | 8231 | 16.569 | 0.7252 | 6 | 0.00 |
| mtbench/dynamic | markov_w0_dist_int | 30 | 7864 | 17.162 | 0.8790 | 5 | 37.19 |
| mtbench/dynamic | markov_w05_dist_int | 30 | 8072 | 17.264 | 0.7574 | 6 | 36.95 |
| mtbench/pooled | picospec_g2 | 90 | 24356 | 16.358 | 0.7393 | 19 | 36.76 |
| mtbench/pooled | picospec | 90 | 24506 | 16.518 | 0.9162 | 19 | 30.54 |
| mtbench/pooled | picospec_g8 | 90 | 23410 | 12.844 | 1.2910 | 15 | 19.11 |
| mtbench/pooled | sync_g4 | 90 | 24506 | 14.582 | 0.6419 | 19 | 0.00 |
| mtbench/pooled | hf_default | 90 | 23822 | 13.607 | 0.8490 | 16 | 0.00 |
| mtbench/pooled | pipesd | 90 | 24483 | 15.075 | 1.0405 | 18 | 0.00 |
| mtbench/pooled | pearl | 90 | 24486 | 17.534 | 0.7455 | 17 | 0.00 |
| mtbench/pooled | markov_w0_dist_int | 90 | 24152 | 17.246 | 0.8776 | 18 | 35.98 |
| mtbench/pooled | markov_w05_dist_int | 90 | 24397 | 16.982 | 0.7529 | 19 | 36.21 |
| humaneval/low | picospec_g2 | 30 | 9004 | 30.339 | 0.4902 | 1 | 57.43 |
| humaneval/low | picospec | 30 | 9052 | 30.292 | 0.5362 | 1 | 65.92 |
| humaneval/low | picospec_g8 | 30 | 9061 | 26.618 | 0.6262 | 1 | 68.40 |
| humaneval/low | sync_g4 | 30 | 9052 | 25.647 | 0.4528 | 1 | 0.00 |
| humaneval/low | hf_default | 30 | 9067 | 25.932 | 0.5598 | 1 | 0.00 |
| humaneval/low | pipesd | 30 | 8992 | 29.659 | 0.5305 | 1 | 0.00 |
| humaneval/low | pearl | 30 | 9004 | 28.706 | 0.4683 | 1 | 0.00 |
| humaneval/low | markov_w0_dist_int | 30 | 9004 | 30.224 | 0.5236 | 1 | 65.33 |
| humaneval/low | markov_w05_dist_int | 30 | 9164 | 30.787 | 0.5020 | 2 | 63.12 |
| humaneval/high | picospec_g2 | 30 | 9270 | 16.252 | 0.6112 | 1 | 52.32 |
| humaneval/high | picospec | 30 | 9142 | 22.438 | 0.6265 | 1 | 53.50 |
| humaneval/high | picospec_g8 | 30 | 9150 | 22.107 | 0.7326 | 1 | 49.72 |
| humaneval/high | sync_g4 | 30 | 9142 | 14.441 | 0.5545 | 1 | 0.00 |
| humaneval/high | hf_default | 30 | 9251 | 16.132 | 0.6364 | 1 | 0.00 |
| humaneval/high | pipesd | 30 | 9238 | 20.528 | 0.7513 | 1 | 0.00 |
| humaneval/high | pearl | 30 | 9067 | 22.451 | 0.6100 | 1 | 0.00 |
| humaneval/high | markov_w0_dist_int | 30 | 9143 | 23.432 | 0.6624 | 1 | 58.65 |
| humaneval/high | markov_w05_dist_int | 30 | 9142 | 22.342 | 0.6324 | 1 | 57.77 |
| humaneval/dynamic | picospec_g2 | 30 | 9173 | 23.689 | 0.5416 | 1 | 55.84 |
| humaneval/dynamic | picospec | 30 | 9336 | 26.467 | 0.5732 | 1 | 59.88 |
| humaneval/dynamic | picospec_g8 | 30 | 9287 | 24.832 | 0.6652 | 1 | 59.61 |
| humaneval/dynamic | sync_g4 | 30 | 9337 | 20.256 | 0.4803 | 1 | 0.00 |
| humaneval/dynamic | hf_default | 30 | 9221 | 20.864 | 0.5989 | 1 | 0.00 |
| humaneval/dynamic | pipesd | 30 | 9149 | 25.400 | 0.6143 | 1 | 0.00 |
| humaneval/dynamic | pearl | 30 | 9167 | 23.160 | 0.5391 | 1 | 0.00 |
| humaneval/dynamic | markov_w0_dist_int | 30 | 9345 | 27.051 | 0.5819 | 1 | 63.22 |
| humaneval/dynamic | markov_w05_dist_int | 30 | 9333 | 26.845 | 0.5549 | 1 | 61.35 |
| humaneval/pooled | picospec_g2 | 90 | 27447 | 21.881 | 0.5482 | 3 | 55.09 |
| humaneval/pooled | picospec | 90 | 27530 | 25.996 | 0.5787 | 3 | 59.33 |
| humaneval/pooled | picospec_g8 | 90 | 27498 | 24.372 | 0.6748 | 3 | 58.25 |
| humaneval/pooled | sync_g4 | 90 | 27531 | 19.027 | 0.4959 | 3 | 0.00 |
| humaneval/pooled | hf_default | 90 | 27539 | 20.174 | 0.5986 | 3 | 0.00 |
| humaneval/pooled | pipesd | 90 | 27379 | 24.591 | 0.6330 | 3 | 0.00 |
| humaneval/pooled | pearl | 90 | 27238 | 24.466 | 0.5393 | 3 | 0.00 |
| humaneval/pooled | markov_w0_dist_int | 90 | 27492 | 26.599 | 0.5896 | 3 | 62.08 |
| humaneval/pooled | markov_w05_dist_int | 90 | 27639 | 26.210 | 0.5630 | 4 | 60.53 |
| gsm8k/low | picospec_g2 | 50 | 10094 | 27.922 | 0.5410 | 4 | 52.26 |
| gsm8k/low | picospec | 50 | 10122 | 25.854 | 0.6285 | 5 | 57.65 |
| gsm8k/low | picospec_g8 | 50 | 10284 | 21.212 | 0.7840 | 6 | 56.79 |
| gsm8k/low | sync_g4 | 50 | 10400 | 24.126 | 0.4924 | 6 | 0.00 |
| gsm8k/low | hf_default | 50 | 9996 | 22.188 | 0.6528 | 4 | 0.00 |
| gsm8k/low | pipesd | 50 | 10122 | 25.804 | 0.6081 | 5 | 0.00 |
| gsm8k/low | pearl | 50 | 10062 | 27.674 | 0.4933 | 5 | 0.00 |
| gsm8k/low | markov_w0_dist_int | 50 | 10325 | 27.250 | 0.5710 | 6 | 57.79 |
| gsm8k/low | markov_w05_dist_int | 50 | 10347 | 27.538 | 0.5428 | 6 | 53.44 |
| gsm8k/high | picospec_g2 | 50 | 9886 | 14.797 | 0.6831 | 3 | 45.14 |
| gsm8k/high | picospec | 50 | 9893 | 19.151 | 0.7347 | 4 | 42.96 |
| gsm8k/high | picospec_g8 | 50 | 10046 | 17.660 | 0.9176 | 5 | 35.70 |
| gsm8k/high | sync_g4 | 50 | 9615 | 13.260 | 0.6071 | 3 | 0.00 |
| gsm8k/high | hf_default | 50 | 9662 | 13.448 | 0.7575 | 2 | 0.00 |
| gsm8k/high | pipesd | 50 | 9773 | 16.238 | 0.9459 | 3 | 0.00 |
| gsm8k/high | pearl | 50 | 9915 | 19.177 | 0.7059 | 4 | 0.00 |
| gsm8k/high | markov_w0_dist_int | 50 | 9664 | 19.927 | 0.7630 | 3 | 48.02 |
| gsm8k/high | markov_w05_dist_int | 50 | 10061 | 18.379 | 0.7095 | 4 | 48.12 |
| gsm8k/dynamic | picospec_g2 | 50 | 9151 | 20.794 | 0.6051 | 2 | 49.22 |
| gsm8k/dynamic | picospec | 50 | 9275 | 22.441 | 0.6732 | 3 | 49.98 |
| gsm8k/dynamic | picospec_g8 | 50 | 9624 | 19.363 | 0.8505 | 5 | 43.52 |
| gsm8k/dynamic | sync_g4 | 50 | 9275 | 18.096 | 0.5338 | 3 | 0.00 |
| gsm8k/dynamic | hf_default | 50 | 8989 | 17.773 | 0.7027 | 1 | 0.00 |
| gsm8k/dynamic | pipesd | 50 | 9502 | 21.333 | 0.7305 | 3 | 0.00 |
| gsm8k/dynamic | pearl | 50 | 9870 | 20.576 | 0.5915 | 4 | 0.00 |
| gsm8k/dynamic | markov_w0_dist_int | 50 | 9114 | 22.777 | 0.6748 | 3 | 52.74 |
| gsm8k/dynamic | markov_w05_dist_int | 50 | 9234 | 22.401 | 0.6209 | 3 | 52.11 |
| gsm8k/pooled | picospec_g2 | 150 | 29131 | 19.821 | 0.6094 | 9 | 48.72 |
| gsm8k/pooled | picospec | 150 | 29290 | 22.166 | 0.6785 | 12 | 49.51 |
| gsm8k/pooled | picospec_g8 | 150 | 29954 | 19.316 | 0.8501 | 16 | 43.80 |
| gsm8k/pooled | sync_g4 | 150 | 29290 | 17.552 | 0.5431 | 12 | 0.00 |
| gsm8k/pooled | hf_default | 150 | 28647 | 17.105 | 0.7038 | 7 | 0.00 |
| gsm8k/pooled | pipesd | 150 | 29397 | 20.421 | 0.7600 | 11 | 0.00 |
| gsm8k/pooled | pearl | 150 | 29847 | 21.942 | 0.5964 | 13 | 0.00 |
| gsm8k/pooled | markov_w0_dist_int | 150 | 29103 | 23.024 | 0.6673 | 12 | 52.30 |
| gsm8k/pooled | markov_w05_dist_int | 150 | 29642 | 22.198 | 0.6237 | 13 | 50.98 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | picospec_vs_picospec_g2 | 110 | -8.52 [-10.44, -6.29] | -17.97 [-20.13, -15.77] | 18 | 2 |
| all/low | picospec_g8_vs_picospec_g2 | 110 | -26.17 [-28.66, -23.44] | -50.04 [-55.00, -45.09] | 32 | 3 |
| all/low | sync_g4_vs_picospec_g2 | 110 | -13.01 [-14.19, -11.73] | 9.80 [8.84, 10.78] | 17 | 2 |
| all/low | hf_default_vs_picospec_g2 | 110 | -18.30 [-20.12, -16.51] | -17.74 [-20.37, -15.36] | 33 | 3 |
| all/low | pipesd_vs_picospec_g2 | 110 | -7.57 [-8.81, -6.27] | -12.93 [-14.39, -11.51] | 17 | 1 |
| all/low | pearl_vs_picospec_g2 | 110 | 0.15 [-1.52, 1.89] | 10.17 [8.83, 11.54] | 13 | 1 |
| all/low | markov_w0_dist_int_vs_picospec_g2 | 110 | -2.38 [-3.44, -0.93] | -5.50 [-6.37, -4.59] | 8 | 2 |
| all/low | markov_w05_dist_int_vs_picospec_g2 | 110 | -0.08 [-1.38, 1.56] | 0.66 [-0.57, 1.95] | 14 | 3 |
| all/low | picospec_g2_vs_picospec | 110 | 9.32 [6.71, 11.65] | 15.23 [13.62, 16.76] | 18 | 1 |
| all/low | picospec_g8_vs_picospec | 110 | -19.29 [-20.79, -17.85] | -27.18 [-29.51, -24.94] | 25 | 2 |
| all/low | sync_g4_vs_picospec | 110 | -4.91 [-7.37, -2.59] | 23.54 [21.84, 25.15] | 1 | 1 |
| all/low | hf_default_vs_picospec | 110 | -10.69 [-13.17, -8.25] | 0.20 [-2.56, 2.80] | 35 | 3 |
| all/low | pipesd_vs_picospec | 110 | 1.04 [-0.61, 2.58] | 4.27 [2.61, 5.74] | 27 | 1 |
| all/low | pearl_vs_picospec | 110 | 9.48 [5.49, 13.31] | 23.85 [21.43, 26.16] | 27 | 1 |
| all/low | markov_w0_dist_int_vs_picospec | 110 | 6.71 [4.75, 8.56] | 10.57 [8.56, 12.39] | 21 | 2 |
| all/low | markov_w05_dist_int_vs_picospec | 110 | 9.23 [6.78, 11.70] | 15.79 [13.42, 18.14] | 21 | 3 |
| all/low | picospec_g2_vs_picospec_g8 | 110 | 35.44 [30.61, 40.17] | 33.35 [31.08, 35.48] | 32 | 2 |
| all/low | picospec_vs_picospec_g8 | 110 | 23.90 [21.72, 26.25] | 21.37 [19.96, 22.79] | 25 | 2 |
| all/low | sync_g4_vs_picospec_g8 | 110 | 17.82 [13.28, 22.62] | 39.88 [37.60, 42.02] | 24 | 2 |
| all/low | hf_default_vs_picospec_g8 | 110 | 10.65 [6.56, 14.85] | 21.53 [18.53, 24.45] | 34 | 3 |
| all/low | pipesd_vs_picospec_g8 | 110 | 25.19 [21.65, 28.61] | 24.73 [22.53, 26.81] | 32 | 2 |
| all/low | pearl_vs_picospec_g8 | 110 | 35.64 [29.12, 42.23] | 40.13 [37.27, 42.84] | 41 | 1 |
| all/low | markov_w0_dist_int_vs_picospec_g8 | 110 | 32.21 [27.96, 36.44] | 29.69 [27.07, 32.08] | 35 | 3 |
| all/low | markov_w05_dist_int_vs_picospec_g8 | 110 | 35.33 [30.58, 40.25] | 33.79 [31.01, 36.47] | 34 | 4 |
| all/low | picospec_g2_vs_sync_g4 | 110 | 14.96 [13.28, 16.53] | -10.87 [-12.08, -9.70] | 17 | 0 |
| all/low | picospec_vs_sync_g4 | 110 | 5.16 [2.66, 7.96] | -30.79 [-33.60, -27.94] | 1 | 0 |
| all/low | picospec_g8_vs_sync_g4 | 110 | -15.12 [-18.45, -11.73] | -66.34 [-72.47, -60.26] | 24 | 1 |
| all/low | hf_default_vs_sync_g4 | 110 | -6.08 [-8.53, -3.77] | -30.53 [-33.73, -27.69] | 36 | 3 |
| all/low | pipesd_vs_sync_g4 | 110 | 6.26 [4.19, 8.48] | -25.20 [-27.45, -22.95] | 26 | 0 |
| all/low | pearl_vs_sync_g4 | 110 | 15.13 [13.07, 17.02] | 0.41 [-0.95, 1.69] | 26 | 0 |
| all/low | markov_w0_dist_int_vs_sync_g4 | 110 | 12.22 [10.31, 14.28] | -16.96 [-18.50, -15.47] | 20 | 1 |
| all/low | markov_w05_dist_int_vs_sync_g4 | 110 | 14.87 [12.86, 17.07] | -10.14 [-11.71, -8.60] | 20 | 2 |
| all/high | picospec_vs_picospec_g2 | 110 | 26.53 [23.66, 29.41] | -10.98 [-13.30, -8.70] | 18 | 1 |
| all/high | picospec_g8_vs_picospec_g2 | 110 | 13.47 [9.02, 17.99] | -42.62 [-48.25, -37.25] | 35 | 2 |
| all/high | sync_g4_vs_picospec_g2 | 110 | -10.62 [-11.88, -9.10] | 11.04 [10.09, 12.06] | 19 | 1 |
| all/high | hf_default_vs_picospec_g2 | 110 | -8.29 [-10.50, -6.05] | -8.62 [-10.84, -6.49] | 30 | 0 |
| all/high | pipesd_vs_picospec_g2 | 110 | 7.68 [4.29, 11.14] | -43.02 [-47.56, -38.57] | 13 | 0 |
| all/high | pearl_vs_picospec_g2 | 110 | 26.53 [23.71, 29.54] | -7.20 [-9.23, -5.14] | 15 | 1 |
| all/high | markov_w0_dist_int_vs_picospec_g2 | 110 | 29.19 [25.10, 33.11] | -17.36 [-20.98, -14.18] | 20 | 1 |
| all/high | markov_w05_dist_int_vs_picospec_g2 | 110 | 21.05 [17.43, 24.87] | -4.59 [-5.97, -3.21] | 16 | 1 |
| all/high | picospec_g2_vs_picospec | 110 | -20.97 [-22.73, -19.14] | 9.90 [8.00, 11.74] | 18 | 0 |
| all/high | picospec_g8_vs_picospec | 110 | -10.32 [-12.29, -8.36] | -28.51 [-31.25, -25.81] | 28 | 1 |
| all/high | sync_g4_vs_picospec | 110 | -29.36 [-30.84, -27.82] | 19.85 [17.96, 21.65] | 1 | 0 |
| all/high | hf_default_vs_picospec | 110 | -27.52 [-29.20, -25.94] | 2.13 [-0.53, 4.52] | 38 | 0 |
| all/high | pipesd_vs_picospec | 110 | -14.90 [-16.72, -13.13] | -28.87 [-31.57, -26.38] | 21 | 0 |
| all/high | pearl_vs_picospec | 110 | 0.00 [-1.48, 1.39] | 3.41 [2.02, 4.62] | 16 | 0 |
| all/high | markov_w0_dist_int_vs_picospec | 110 | 2.10 [-0.87, 4.52] | -5.74 [-8.21, -3.64] | 19 | 1 |
| all/high | markov_w05_dist_int_vs_picospec | 110 | -4.33 [-6.26, -2.49] | 5.76 [3.72, 7.74] | 19 | 0 |
| all/high | picospec_g2_vs_picospec_g8 | 110 | -11.87 [-15.25, -8.28] | 29.89 [27.14, 32.55] | 35 | 2 |
| all/high | picospec_vs_picospec_g8 | 110 | 11.51 [9.13, 14.01] | 22.18 [20.52, 23.81] | 28 | 2 |
| all/high | sync_g4_vs_picospec_g8 | 110 | -21.23 [-24.26, -18.03] | 37.63 [34.97, 40.16] | 29 | 2 |
| all/high | hf_default_vs_picospec_g8 | 110 | -19.18 [-21.79, -16.69] | 23.84 [20.67, 26.64] | 39 | 0 |
| all/high | pipesd_vs_picospec_g8 | 110 | -5.11 [-7.08, -3.06] | -0.28 [-2.39, 1.75] | 37 | 2 |
| all/high | pearl_vs_picospec_g8 | 110 | 11.51 [8.64, 14.37] | 24.84 [22.85, 26.76] | 30 | 1 |
| all/high | markov_w0_dist_int_vs_picospec_g8 | 110 | 13.86 [10.06, 17.22] | 17.72 [15.20, 20.01] | 25 | 2 |
| all/high | markov_w05_dist_int_vs_picospec_g8 | 110 | 6.68 [4.06, 9.10] | 26.67 [23.93, 29.25] | 25 | 2 |
| all/high | picospec_g2_vs_sync_g4 | 110 | 11.88 [10.01, 13.49] | -12.41 [-13.71, -11.23] | 19 | 1 |
| all/high | picospec_vs_sync_g4 | 110 | 41.56 [38.55, 44.60] | -24.76 [-27.63, -21.89] | 1 | 1 |
| all/high | picospec_g8_vs_sync_g4 | 110 | 26.95 [21.99, 32.03] | -60.33 [-67.12, -53.78] | 29 | 2 |
| all/high | hf_default_vs_sync_g4 | 110 | 2.61 [0.20, 4.91] | -22.10 [-24.84, -19.67] | 37 | 0 |
| all/high | pipesd_vs_sync_g4 | 110 | 20.47 [16.44, 24.71] | -60.77 [-66.86, -54.90] | 22 | 1 |
| all/high | pearl_vs_sync_g4 | 110 | 41.56 [38.43, 44.51] | -20.51 [-23.37, -17.76] | 17 | 1 |
| all/high | markov_w0_dist_int_vs_sync_g4 | 110 | 44.54 [38.56, 49.87] | -31.92 [-37.05, -27.66] | 20 | 2 |
| all/high | markov_w05_dist_int_vs_sync_g4 | 110 | 35.43 [31.16, 39.92] | -17.57 [-19.35, -15.81] | 20 | 1 |
| all/dynamic | picospec_vs_picospec_g2 | 110 | 4.93 [2.62, 7.34] | -14.28 [-16.66, -12.02] | 19 | 1 |
| all/dynamic | picospec_g8_vs_picospec_g2 | 110 | -11.09 [-14.54, -7.77] | -47.14 [-52.89, -41.52] | 33 | 3 |
| all/dynamic | sync_g4_vs_picospec_g2 | 110 | -13.19 [-14.26, -12.10] | 12.62 [11.68, 13.51] | 18 | 1 |
| all/dynamic | hf_default_vs_picospec_g2 | 110 | -15.82 [-17.96, -13.58] | -14.62 [-17.33, -12.07] | 27 | 1 |
| all/dynamic | pipesd_vs_picospec_g2 | 110 | -0.18 [-2.32, 2.13] | -23.81 [-26.45, -21.05] | 18 | 1 |
| all/dynamic | pearl_vs_picospec_g2 | 110 | -1.93 [-3.03, -0.70] | 1.56 [0.65, 2.56] | 13 | 2 |
| all/dynamic | markov_w0_dist_int_vs_picospec_g2 | 110 | 7.92 [5.80, 10.16] | -12.64 [-14.47, -10.92] | 20 | 2 |
| all/dynamic | markov_w05_dist_int_vs_picospec_g2 | 110 | 7.12 [5.08, 9.37] | -2.43 [-3.64, -1.31] | 18 | 2 |
| all/dynamic | picospec_g2_vs_picospec | 110 | -4.70 [-6.84, -2.55] | 12.49 [10.73, 14.28] | 19 | 0 |
| all/dynamic | picospec_g8_vs_picospec | 110 | -15.27 [-17.24, -13.26] | -28.75 [-31.95, -25.72] | 29 | 2 |
| all/dynamic | sync_g4_vs_picospec | 110 | -17.27 [-18.88, -15.60] | 23.54 [21.82, 25.17] | 1 | 0 |
| all/dynamic | hf_default_vs_picospec | 110 | -19.77 [-21.71, -17.90] | -0.30 [-3.05, 2.22] | 36 | 1 |
| all/dynamic | pipesd_vs_picospec | 110 | -4.87 [-6.18, -3.50] | -8.34 [-9.80, -6.87] | 29 | 1 |
| all/dynamic | pearl_vs_picospec | 110 | -6.53 [-8.57, -4.46] | 13.86 [11.99, 15.77] | 22 | 1 |
| all/dynamic | markov_w0_dist_int_vs_picospec | 110 | 2.85 [1.48, 4.32] | 1.44 [-0.01, 2.92] | 25 | 2 |
| all/dynamic | markov_w05_dist_int_vs_picospec | 110 | 2.09 [0.81, 3.43] | 10.37 [8.49, 12.20] | 23 | 2 |
| all/dynamic | picospec_g2_vs_picospec_g8 | 110 | 12.47 [8.42, 17.01] | 32.04 [29.34, 34.59] | 33 | 1 |
| all/dynamic | picospec_vs_picospec_g8 | 110 | 18.02 [15.28, 20.83] | 22.33 [20.46, 24.22] | 29 | 1 |
| all/dynamic | sync_g4_vs_picospec_g8 | 110 | -2.37 [-6.00, 1.48] | 40.61 [38.04, 43.04] | 30 | 1 |
| all/dynamic | hf_default_vs_picospec_g8 | 110 | -5.32 [-8.47, -2.02] | 22.10 [18.87, 25.23] | 37 | 1 |
| all/dynamic | pipesd_vs_picospec_g8 | 110 | 12.27 [9.49, 15.17] | 15.85 [13.71, 17.94] | 37 | 1 |
| all/dynamic | pearl_vs_picospec_g8 | 110 | 10.31 [6.12, 14.74] | 33.09 [30.33, 35.82] | 39 | 2 |
| all/dynamic | markov_w0_dist_int_vs_picospec_g8 | 110 | 21.38 [18.02, 24.79] | 23.45 [20.96, 25.80] | 30 | 1 |
| all/dynamic | markov_w05_dist_int_vs_picospec_g8 | 110 | 20.48 [17.17, 23.72] | 30.38 [27.52, 33.10] | 30 | 2 |
| all/dynamic | picospec_g2_vs_sync_g4 | 110 | 15.20 [13.77, 16.63] | -14.44 [-15.63, -13.23] | 18 | 0 |
| all/dynamic | picospec_vs_sync_g4 | 110 | 20.88 [18.48, 23.27] | -30.78 [-33.64, -27.91] | 1 | 0 |
| all/dynamic | picospec_g8_vs_sync_g4 | 110 | 2.42 [-1.46, 6.38] | -68.38 [-75.55, -61.39] | 30 | 2 |
| all/dynamic | hf_default_vs_sync_g4 | 110 | -3.02 [-5.56, -0.40] | -31.17 [-34.59, -28.03] | 37 | 1 |
| all/dynamic | pipesd_vs_sync_g4 | 110 | 14.99 [12.37, 17.70] | -41.70 [-45.38, -37.97] | 28 | 1 |
| all/dynamic | pearl_vs_sync_g4 | 110 | 12.98 [11.56, 14.43] | -12.66 [-13.89, -11.36] | 21 | 1 |
| all/dynamic | markov_w0_dist_int_vs_sync_g4 | 110 | 24.33 [21.71, 26.87] | -28.91 [-31.35, -26.57] | 24 | 2 |
| all/dynamic | markov_w05_dist_int_vs_sync_g4 | 110 | 23.40 [21.00, 25.73] | -17.23 [-18.72, -15.79] | 22 | 2 |
| all/pooled | picospec_vs_picospec_g2 | 110 | 9.56 [7.45, 11.62] | -14.11 [-16.26, -12.04] | 55 | 4 |
| all/pooled | picospec_g8_vs_picospec_g2 | 110 | -6.50 [-9.83, -3.15] | -46.26 [-51.49, -41.21] | 100 | 8 |
| all/pooled | sync_g4_vs_picospec_g2 | 110 | -11.74 [-12.62, -10.79] | 11.28 [10.51, 12.07] | 54 | 4 |
| all/pooled | hf_default_vs_picospec_g2 | 110 | -13.06 [-14.66, -11.43] | -13.23 [-15.47, -11.18] | 90 | 4 |
| all/pooled | pipesd_vs_picospec_g2 | 110 | 1.27 [-0.80, 3.45] | -27.71 [-30.42, -24.97] | 48 | 2 |
| all/pooled | pearl_vs_picospec_g2 | 110 | 9.72 [8.64, 10.88] | 0.90 [0.21, 1.62] | 41 | 4 |
| all/pooled | markov_w0_dist_int_vs_picospec_g2 | 110 | 13.66 [11.65, 15.67] | -12.10 [-13.89, -10.51] | 48 | 5 |
| all/pooled | markov_w05_dist_int_vs_picospec_g2 | 110 | 11.11 [9.18, 13.06] | -2.23 [-3.18, -1.32] | 48 | 6 |
| all/pooled | picospec_g2_vs_picospec | 110 | -8.73 [-10.41, -6.94] | 12.37 [10.75, 13.98] | 55 | 1 |
| all/pooled | picospec_g8_vs_picospec | 110 | -14.65 [-16.30, -12.98] | -28.17 [-30.69, -25.72] | 82 | 5 |
| all/pooled | sync_g4_vs_picospec | 110 | -19.44 [-21.04, -17.82] | 22.26 [20.54, 23.90] | 3 | 1 |
| all/pooled | hf_default_vs_picospec | 110 | -20.65 [-22.16, -19.23] | 0.77 [-1.70, 3.02] | 109 | 4 |
| all/pooled | pipesd_vs_picospec | 110 | -7.57 [-8.61, -6.60] | -11.91 [-13.24, -10.76] | 77 | 2 |
| all/pooled | pearl_vs_picospec | 110 | 0.14 [-1.59, 1.91] | 13.16 [11.63, 14.67] | 65 | 2 |
| all/pooled | markov_w0_dist_int_vs_picospec | 110 | 3.74 [2.37, 5.09] | 1.76 [0.39, 3.08] | 65 | 5 |
| all/pooled | markov_w05_dist_int_vs_picospec | 110 | 1.42 [0.14, 2.65] | 10.41 [8.43, 12.30] | 63 | 5 |
| all/pooled | picospec_g2_vs_picospec_g8 | 110 | 6.95 [3.25, 10.90] | 31.63 [29.18, 33.99] | 100 | 5 |
| all/pooled | picospec_vs_picospec_g8 | 110 | 17.17 [14.91, 19.47] | 21.98 [20.46, 23.48] | 82 | 5 |
| all/pooled | sync_g4_vs_picospec_g8 | 110 | -5.60 [-9.00, -2.01] | 39.34 [36.91, 41.67] | 83 | 5 |
| all/pooled | hf_default_vs_picospec_g8 | 110 | -7.02 [-9.81, -4.21] | 22.58 [19.66, 25.33] | 110 | 4 |
| all/pooled | pipesd_vs_picospec_g8 | 110 | 8.30 [6.18, 10.44] | 12.68 [10.95, 14.40] | 106 | 5 |
| all/pooled | pearl_vs_picospec_g8 | 110 | 17.34 [13.47, 21.31] | 32.24 [29.91, 34.52] | 110 | 4 |
| all/pooled | markov_w0_dist_int_vs_picospec_g8 | 110 | 21.56 [18.71, 24.47] | 23.35 [21.27, 25.42] | 90 | 6 |
| all/pooled | markov_w05_dist_int_vs_picospec_g8 | 110 | 18.83 [15.93, 21.74] | 30.10 [27.41, 32.69] | 89 | 8 |
| all/pooled | picospec_g2_vs_sync_g4 | 110 | 13.30 [12.10, 14.45] | -12.72 [-13.72, -11.74] | 54 | 1 |
| all/pooled | picospec_vs_sync_g4 | 110 | 24.13 [21.68, 26.65] | -28.63 [-31.40, -25.85] | 3 | 1 |
| all/pooled | picospec_g8_vs_sync_g4 | 110 | 5.94 [2.05, 9.90] | -64.86 [-71.45, -58.49] | 83 | 5 |
| all/pooled | hf_default_vs_sync_g4 | 110 | -1.50 [-3.46, 0.40] | -27.63 [-30.33, -25.13] | 110 | 4 |
| all/pooled | pipesd_vs_sync_g4 | 110 | 14.73 [12.07, 17.54] | -43.95 [-47.63, -40.15] | 76 | 2 |
| all/pooled | pearl_vs_sync_g4 | 110 | 24.30 [22.83, 25.77] | -11.70 [-12.97, -10.52] | 64 | 2 |
| all/pooled | markov_w0_dist_int_vs_sync_g4 | 110 | 28.77 [25.74, 31.58] | -26.36 [-29.03, -23.94] | 64 | 5 |
| all/pooled | markov_w05_dist_int_vs_sync_g4 | 110 | 25.89 [23.31, 28.48] | -15.23 [-16.62, -13.93] | 62 | 5 |
| mtbench/low | picospec_vs_picospec_g2 | 30 | -15.53 [-18.11, -12.66] | -26.84 [-30.46, -23.10] | 6 | 0 |
| mtbench/low | picospec_g8_vs_picospec_g2 | 30 | -37.30 [-40.13, -34.40] | -75.87 [-83.79, -68.60] | 11 | 1 |
| mtbench/low | sync_g4_vs_picospec_g2 | 30 | -10.22 [-12.17, -8.01] | 12.40 [11.00, 13.97] | 6 | 0 |
| mtbench/low | hf_default_vs_picospec_g2 | 30 | -18.97 [-23.49, -15.06] | -17.64 [-24.13, -12.63] | 14 | 2 |
| mtbench/low | pipesd_vs_picospec_g2 | 30 | -11.54 [-13.28, -9.88] | -17.22 [-19.44, -15.19] | 5 | 0 |
| mtbench/low | pearl_vs_picospec_g2 | 30 | 6.62 [3.21, 10.03] | 16.30 [14.26, 18.35] | 8 | 0 |
| mtbench/low | markov_w0_dist_int_vs_picospec_g2 | 30 | -3.87 [-4.99, -2.87] | -4.25 [-5.61, -2.78] | 3 | 0 |
| mtbench/low | markov_w05_dist_int_vs_picospec_g2 | 30 | -0.09 [-2.08, 1.90] | 4.16 [1.63, 6.64] | 5 | 0 |
| mtbench/low | picospec_g2_vs_picospec | 30 | 18.39 [14.50, 22.11] | 21.16 [18.77, 23.35] | 6 | 0 |
| mtbench/low | picospec_g8_vs_picospec | 30 | -25.77 [-28.62, -23.42] | -38.65 [-43.94, -34.44] | 11 | 1 |
| mtbench/low | sync_g4_vs_picospec | 30 | 6.28 [3.57, 9.06] | 30.94 [29.46, 32.23] | 0 | 0 |
| mtbench/low | hf_default_vs_picospec | 30 | -4.07 [-9.93, 1.38] | 7.26 [1.37, 12.20] | 15 | 2 |
| mtbench/low | pipesd_vs_picospec | 30 | 4.73 [1.72, 7.39] | 7.59 [4.86, 9.85] | 10 | 0 |
| mtbench/low | pearl_vs_picospec | 30 | 26.22 [19.32, 33.41] | 34.02 [30.69, 37.04] | 12 | 0 |
| mtbench/low | markov_w0_dist_int_vs_picospec | 30 | 13.80 [10.14, 17.42] | 17.81 [14.60, 20.70] | 6 | 0 |
| mtbench/low | markov_w05_dist_int_vs_picospec | 30 | 18.28 [13.25, 23.59] | 24.44 [20.49, 28.02] | 10 | 0 |
| mtbench/low | picospec_g2_vs_picospec_g8 | 30 | 59.49 [52.45, 67.04] | 43.14 [40.69, 45.59] | 11 | 2 |
| mtbench/low | picospec_vs_picospec_g8 | 30 | 34.72 [30.59, 40.10] | 27.87 [25.62, 30.53] | 11 | 2 |
| mtbench/low | sync_g4_vs_picospec_g8 | 30 | 43.18 [37.94, 49.09] | 50.19 [48.41, 52.09] | 11 | 2 |
| mtbench/low | hf_default_vs_picospec_g8 | 30 | 29.24 [21.42, 37.27] | 33.11 [28.72, 37.09] | 11 | 2 |
| mtbench/low | pipesd_vs_picospec_g8 | 30 | 41.09 [34.95, 48.49] | 33.35 [30.32, 36.61] | 12 | 2 |
| mtbench/low | pearl_vs_picospec_g8 | 30 | 70.04 [60.37, 80.79] | 52.41 [49.67, 55.09] | 17 | 1 |
| mtbench/low | markov_w0_dist_int_vs_picospec_g8 | 30 | 53.31 [46.33, 61.26] | 40.72 [37.68, 43.69] | 13 | 2 |
| mtbench/low | markov_w05_dist_int_vs_picospec_g8 | 30 | 59.34 [50.74, 68.92] | 45.50 [42.07, 48.78] | 14 | 2 |
| mtbench/low | picospec_g2_vs_sync_g4 | 30 | 11.39 [8.71, 13.85] | -14.15 [-16.23, -12.36] | 6 | 0 |
| mtbench/low | picospec_vs_sync_g4 | 30 | -5.91 [-8.31, -3.45] | -44.79 [-47.56, -41.76] | 0 | 0 |
| mtbench/low | picospec_g8_vs_sync_g4 | 30 | -30.16 [-32.93, -27.50] | -100.75 [-108.73, -93.84] | 11 | 1 |
| mtbench/low | hf_default_vs_sync_g4 | 30 | -9.74 [-14.74, -5.25] | -34.28 [-41.95, -28.18] | 15 | 2 |
| mtbench/low | pipesd_vs_sync_g4 | 30 | -1.46 [-3.99, 1.04] | -33.81 [-36.57, -31.02] | 10 | 0 |
| mtbench/low | pearl_vs_sync_g4 | 30 | 18.76 [14.31, 23.56] | 4.46 [1.46, 7.41] | 12 | 0 |
| mtbench/low | markov_w0_dist_int_vs_sync_g4 | 30 | 7.07 [4.60, 9.49] | -19.00 [-21.78, -16.43] | 6 | 0 |
| mtbench/low | markov_w05_dist_int_vs_sync_g4 | 30 | 11.29 [8.03, 14.56] | -9.41 [-13.02, -5.90] | 10 | 0 |
| mtbench/high | picospec_vs_picospec_g2 | 30 | 15.90 [10.97, 20.54] | -21.32 [-25.18, -17.62] | 7 | 0 |
| mtbench/high | picospec_g8_vs_picospec_g2 | 30 | -6.09 [-11.73, -0.51] | -72.59 [-81.38, -64.85] | 13 | 0 |
| mtbench/high | sync_g4_vs_picospec_g2 | 30 | -10.16 [-13.20, -6.50] | 12.66 [10.79, 14.45] | 7 | 0 |
| mtbench/high | hf_default_vs_picospec_g2 | 30 | -13.89 [-18.01, -9.92] | -10.94 [-16.84, -6.44] | 11 | 0 |
| mtbench/high | pipesd_vs_picospec_g2 | 30 | -5.70 [-8.99, -2.06] | -64.01 [-67.81, -60.23] | 3 | 0 |
| mtbench/high | pearl_vs_picospec_g2 | 30 | 15.80 [11.22, 20.62] | -17.00 [-19.62, -14.71] | 6 | 0 |
| mtbench/high | markov_w0_dist_int_vs_picospec_g2 | 30 | 14.49 [10.04, 18.75] | -30.43 [-36.38, -25.73] | 5 | 0 |
| mtbench/high | markov_w05_dist_int_vs_picospec_g2 | 30 | 7.34 [3.18, 11.48] | -6.21 [-8.17, -4.01] | 4 | 0 |
| mtbench/high | picospec_g2_vs_picospec | 30 | -13.72 [-17.04, -9.89] | 17.57 [14.98, 20.11] | 7 | 0 |
| mtbench/high | picospec_g8_vs_picospec | 30 | -18.98 [-22.05, -16.57] | -42.26 [-46.94, -38.62] | 12 | 0 |
| mtbench/high | sync_g4_vs_picospec | 30 | -22.48 [-24.57, -20.12] | 28.00 [26.20, 29.86] | 0 | 0 |
| mtbench/high | hf_default_vs_picospec | 30 | -25.71 [-29.12, -22.21] | 8.55 [3.09, 13.55] | 11 | 0 |
| mtbench/high | pipesd_vs_picospec | 30 | -18.64 [-21.29, -15.93] | -35.19 [-39.42, -31.44] | 7 | 0 |
| mtbench/high | pearl_vs_picospec | 30 | -0.09 [-2.90, 2.38] | 3.56 [0.77, 5.92] | 9 | 0 |
| mtbench/high | markov_w0_dist_int_vs_picospec | 30 | -1.22 [-6.73, 3.98] | -7.51 [-12.83, -2.87] | 6 | 0 |
| mtbench/high | markov_w05_dist_int_vs_picospec | 30 | -7.39 [-9.82, -4.56] | 12.45 [8.77, 16.00] | 8 | 0 |
| mtbench/high | picospec_g2_vs_picospec_g8 | 30 | 6.49 [0.51, 13.28] | 42.06 [39.34, 44.87] | 13 | 2 |
| mtbench/high | picospec_vs_picospec_g8 | 30 | 23.42 [19.86, 28.28] | 29.71 [27.86, 31.95] | 12 | 2 |
| mtbench/high | sync_g4_vs_picospec_g8 | 30 | -4.33 [-8.29, 0.43] | 49.39 [47.31, 51.67] | 12 | 2 |
| mtbench/high | hf_default_vs_picospec_g8 | 30 | -8.31 [-13.20, -3.19] | 35.72 [31.29, 39.90] | 14 | 0 |
| mtbench/high | pipesd_vs_picospec_g8 | 30 | 0.42 [-3.70, 5.12] | 4.97 [1.05, 9.10] | 15 | 2 |
| mtbench/high | pearl_vs_picospec_g8 | 30 | 23.31 [18.45, 28.91] | 32.21 [29.55, 34.96] | 13 | 1 |
| mtbench/high | markov_w0_dist_int_vs_picospec_g8 | 30 | 21.92 [13.07, 30.47] | 24.43 [19.44, 28.97] | 12 | 2 |
| mtbench/high | markov_w05_dist_int_vs_picospec_g8 | 30 | 14.31 [10.20, 19.11] | 38.46 [35.04, 41.84] | 11 | 2 |
| mtbench/high | picospec_g2_vs_sync_g4 | 30 | 11.30 [6.96, 15.20] | -14.49 [-16.89, -12.09] | 7 | 0 |
| mtbench/high | picospec_vs_sync_g4 | 30 | 29.00 [25.18, 32.58] | -38.89 [-42.58, -35.50] | 0 | 0 |
| mtbench/high | picospec_g8_vs_sync_g4 | 30 | 4.52 [-0.43, 9.03] | -97.60 [-106.92, -89.80] | 12 | 0 |
| mtbench/high | hf_default_vs_sync_g4 | 30 | -4.16 [-7.43, -1.11] | -27.02 [-33.22, -21.68] | 11 | 0 |
| mtbench/high | pipesd_vs_sync_g4 | 30 | 4.96 [1.98, 7.76] | -87.77 [-93.14, -82.53] | 7 | 0 |
| mtbench/high | pearl_vs_sync_g4 | 30 | 28.89 [25.30, 32.00] | -33.96 [-37.24, -31.04] | 9 | 0 |
| mtbench/high | markov_w0_dist_int_vs_sync_g4 | 30 | 27.43 [18.57, 34.53] | -49.32 [-58.52, -42.39] | 6 | 0 |
| mtbench/high | markov_w05_dist_int_vs_sync_g4 | 30 | 19.48 [15.43, 24.01] | -21.60 [-24.34, -19.03] | 8 | 0 |
| mtbench/dynamic | picospec_vs_picospec_g2 | 30 | -2.55 [-5.59, 0.61] | -24.30 [-27.45, -21.43] | 8 | 0 |
| mtbench/dynamic | picospec_g8_vs_picospec_g2 | 30 | -24.79 [-28.32, -21.57] | -76.01 [-84.37, -68.73] | 11 | 0 |
| mtbench/dynamic | sync_g4_vs_picospec_g2 | 30 | -12.43 [-14.25, -10.14] | 14.38 [12.80, 15.81] | 8 | 0 |
| mtbench/dynamic | hf_default_vs_picospec_g2 | 30 | -20.28 [-23.79, -16.47] | -17.19 [-23.20, -11.84] | 10 | 1 |
| mtbench/dynamic | pipesd_vs_picospec_g2 | 30 | -7.79 [-9.96, -5.42] | -35.51 [-38.50, -32.58] | 6 | 0 |
| mtbench/dynamic | pearl_vs_picospec_g2 | 30 | -2.49 [-4.66, 0.05] | 1.78 [0.01, 3.52] | 6 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_picospec_g2 | 30 | 1.00 [-1.15, 3.08] | -19.05 [-21.65, -16.78] | 5 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_picospec_g2 | 30 | 1.60 [-0.77, 4.63] | -2.59 [-4.74, -0.34] | 6 | 0 |
| mtbench/dynamic | picospec_g2_vs_picospec | 30 | 2.61 [-0.60, 5.92] | 19.55 [17.65, 21.54] | 8 | 0 |
| mtbench/dynamic | picospec_g8_vs_picospec | 30 | -22.82 [-25.83, -20.12] | -41.60 [-47.02, -36.58] | 13 | 0 |
| mtbench/dynamic | sync_g4_vs_picospec | 30 | -10.14 [-11.76, -8.40] | 31.11 [29.86, 32.25] | 0 | 0 |
| mtbench/dynamic | hf_default_vs_picospec | 30 | -18.19 [-22.72, -13.76] | 5.72 [-0.24, 10.88] | 12 | 1 |
| mtbench/dynamic | pipesd_vs_picospec | 30 | -5.38 [-7.18, -3.69] | -9.02 [-11.18, -6.97] | 9 | 0 |
| mtbench/dynamic | pearl_vs_picospec | 30 | 0.06 [-3.34, 3.42] | 20.98 [18.60, 23.32] | 9 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_picospec | 30 | 3.64 [0.58, 6.62] | 4.22 [1.26, 7.20] | 9 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_picospec | 30 | 4.25 [2.37, 6.82] | 17.46 [14.98, 20.22] | 8 | 0 |
| mtbench/dynamic | picospec_g2_vs_picospec_g8 | 30 | 32.96 [27.51, 39.51] | 43.19 [40.73, 45.76] | 11 | 1 |
| mtbench/dynamic | picospec_vs_picospec_g8 | 30 | 29.58 [25.18, 34.82] | 29.38 [26.78, 31.98] | 13 | 1 |
| mtbench/dynamic | sync_g4_vs_picospec_g8 | 30 | 16.44 [12.35, 21.81] | 51.35 [49.21, 53.55] | 13 | 1 |
| mtbench/dynamic | hf_default_vs_picospec_g8 | 30 | 6.00 [-0.51, 12.86] | 33.42 [28.27, 37.95] | 14 | 1 |
| mtbench/dynamic | pipesd_vs_picospec_g8 | 30 | 22.61 [18.73, 27.24] | 23.01 [20.57, 25.73] | 13 | 0 |
| mtbench/dynamic | pearl_vs_picospec_g8 | 30 | 29.65 [23.70, 36.77] | 44.20 [41.55, 46.98] | 15 | 1 |
| mtbench/dynamic | markov_w0_dist_int_vs_picospec_g8 | 30 | 34.29 [29.70, 39.52] | 32.36 [29.56, 35.18] | 10 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_picospec_g8 | 30 | 35.09 [30.42, 41.18] | 41.71 [38.76, 44.82] | 10 | 1 |
| mtbench/dynamic | picospec_g2_vs_sync_g4 | 30 | 14.19 [11.28, 16.62] | -16.79 [-18.78, -14.68] | 8 | 0 |
| mtbench/dynamic | picospec_vs_sync_g4 | 30 | 11.28 [9.17, 13.32] | -45.17 [-47.60, -42.56] | 0 | 0 |
| mtbench/dynamic | picospec_g8_vs_sync_g4 | 30 | -14.12 [-17.91, -10.99] | -105.56 [-115.27, -96.91] | 13 | 0 |
| mtbench/dynamic | hf_default_vs_sync_g4 | 30 | -8.96 [-13.33, -4.68] | -36.87 [-44.59, -30.23] | 12 | 1 |
| mtbench/dynamic | pipesd_vs_sync_g4 | 30 | 5.30 [3.06, 7.08] | -58.26 [-61.92, -54.89] | 9 | 0 |
| mtbench/dynamic | pearl_vs_sync_g4 | 30 | 11.35 [9.00, 13.56] | -14.71 [-17.02, -12.36] | 9 | 0 |
| mtbench/dynamic | markov_w0_dist_int_vs_sync_g4 | 30 | 15.33 [12.18, 18.22] | -39.04 [-42.50, -35.72] | 9 | 0 |
| mtbench/dynamic | markov_w05_dist_int_vs_sync_g4 | 30 | 16.01 [14.50, 17.90] | -19.82 [-22.14, -17.06] | 8 | 0 |
| mtbench/pooled | picospec_vs_picospec_g2 | 30 | 0.97 [-2.03, 3.97] | -23.93 [-27.18, -20.72] | 21 | 0 |
| mtbench/pooled | picospec_g8_vs_picospec_g2 | 30 | -21.48 [-25.01, -18.28] | -74.61 [-81.96, -68.34] | 35 | 1 |
| mtbench/pooled | sync_g4_vs_picospec_g2 | 30 | -10.86 [-12.71, -8.83] | 13.17 [11.77, 14.51] | 21 | 0 |
| mtbench/pooled | hf_default_vs_picospec_g2 | 30 | -16.82 [-20.15, -14.00] | -14.83 [-20.37, -10.45] | 35 | 3 |
| mtbench/pooled | pipesd_vs_picospec_g2 | 30 | -7.85 [-9.78, -5.90] | -40.73 [-42.90, -38.37] | 14 | 0 |
| mtbench/pooled | pearl_vs_picospec_g2 | 30 | 7.19 [5.19, 9.19] | -0.84 [-2.01, 0.30] | 20 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec_g2 | 30 | 5.42 [3.55, 7.12] | -18.71 [-21.31, -16.58] | 13 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_picospec_g2 | 30 | 3.81 [2.08, 5.55] | -1.84 [-3.72, 0.12] | 15 | 0 |
| mtbench/pooled | picospec_g2_vs_picospec | 30 | -0.97 [-3.82, 2.07] | 19.31 [17.16, 21.37] | 21 | 0 |
| mtbench/pooled | picospec_g8_vs_picospec | 30 | -22.24 [-24.93, -20.08] | -40.90 [-45.67, -37.13] | 36 | 1 |
| mtbench/pooled | sync_g4_vs_picospec | 30 | -11.72 [-13.48, -9.86] | 29.94 [28.55, 31.28] | 0 | 0 |
| mtbench/pooled | hf_default_vs_picospec | 30 | -17.62 [-21.10, -14.29] | 7.34 [2.38, 11.75] | 38 | 3 |
| mtbench/pooled | pipesd_vs_picospec | 30 | -8.74 [-10.74, -6.83] | -13.56 [-16.19, -11.36] | 26 | 0 |
| mtbench/pooled | pearl_vs_picospec | 30 | 6.15 [2.94, 9.33] | 18.63 [16.15, 21.02] | 30 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec | 30 | 4.41 [1.39, 7.41] | 4.21 [1.37, 7.01] | 21 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_picospec | 30 | 2.81 [0.44, 5.45] | 17.83 [14.62, 21.08] | 26 | 0 |
| mtbench/pooled | picospec_g2_vs_picospec_g8 | 30 | 27.36 [22.37, 33.34] | 42.73 [40.60, 45.04] | 35 | 5 |
| mtbench/pooled | picospec_vs_picospec_g8 | 30 | 28.60 [25.13, 33.20] | 29.03 [27.08, 31.35] | 36 | 5 |
| mtbench/pooled | sync_g4_vs_picospec_g8 | 30 | 13.53 [9.40, 18.74] | 50.27 [48.48, 52.32] | 36 | 5 |
| mtbench/pooled | hf_default_vs_picospec_g8 | 30 | 5.94 [1.04, 11.30] | 34.24 [30.23, 38.11] | 39 | 3 |
| mtbench/pooled | pipesd_vs_picospec_g8 | 30 | 17.37 [13.32, 22.08] | 19.40 [16.55, 22.48] | 40 | 4 |
| mtbench/pooled | pearl_vs_picospec_g8 | 30 | 36.51 [30.87, 43.09] | 42.25 [39.87, 44.82] | 45 | 3 |
| mtbench/pooled | markov_w0_dist_int_vs_picospec_g8 | 30 | 34.27 [29.35, 40.22] | 32.02 [29.46, 35.02] | 35 | 4 |
| mtbench/pooled | markov_w05_dist_int_vs_picospec_g8 | 30 | 32.22 [27.48, 38.01] | 41.68 [38.60, 44.82] | 35 | 5 |
| mtbench/pooled | picospec_g2_vs_sync_g4 | 30 | 12.18 [9.68, 14.56] | -15.17 [-16.97, -13.33] | 21 | 0 |
| mtbench/pooled | picospec_vs_sync_g4 | 30 | 13.28 [10.94, 15.58] | -42.73 [-45.51, -39.97] | 0 | 0 |
| mtbench/pooled | picospec_g8_vs_sync_g4 | 30 | -11.92 [-15.78, -8.60] | -101.10 [-109.74, -94.09] | 36 | 1 |
| mtbench/pooled | hf_default_vs_sync_g4 | 30 | -6.68 [-9.94, -3.69] | -32.25 [-38.20, -26.79] | 38 | 3 |
| mtbench/pooled | pipesd_vs_sync_g4 | 30 | 3.38 [1.37, 5.26] | -62.08 [-65.37, -58.83] | 26 | 0 |
| mtbench/pooled | pearl_vs_sync_g4 | 30 | 20.24 [17.88, 22.43] | -16.14 [-18.26, -14.05] | 30 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_sync_g4 | 30 | 18.27 [14.50, 21.48] | -36.71 [-40.65, -33.34] | 21 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_sync_g4 | 30 | 16.46 [14.23, 18.93] | -17.28 [-20.05, -14.59] | 26 | 0 |
| humaneval/low | picospec_vs_picospec_g2 | 30 | -0.16 [-3.56, 4.85] | -9.37 [-11.76, -7.19] | 5 | 0 |
| humaneval/low | picospec_g8_vs_picospec_g2 | 30 | -12.26 [-16.37, -6.97] | -27.75 [-32.55, -23.16] | 8 | 0 |
| humaneval/low | sync_g4_vs_picospec_g2 | 30 | -15.47 [-16.59, -14.20] | 7.63 [6.57, 8.62] | 5 | 0 |
| humaneval/low | hf_default_vs_picospec_g2 | 30 | -14.53 [-17.12, -11.68] | -14.20 [-17.10, -11.75] | 4 | 0 |
| humaneval/low | pipesd_vs_picospec_g2 | 30 | -2.24 [-4.35, 0.47] | -8.21 [-10.31, -6.38] | 3 | 0 |
| humaneval/low | pearl_vs_picospec_g2 | 30 | -5.38 [-6.57, -4.09] | 4.47 [3.62, 5.49] | 0 | 0 |
| humaneval/low | markov_w0_dist_int_vs_picospec_g2 | 30 | -0.38 [-3.34, 4.48] | -6.80 [-8.40, -5.18] | 1 | 0 |
| humaneval/low | markov_w05_dist_int_vs_picospec_g2 | 30 | 1.47 [-1.54, 6.23] | -2.41 [-3.82, -0.78] | 3 | 1 |
| humaneval/low | picospec_g2_vs_picospec | 30 | 0.16 [-4.62, 3.70] | 8.57 [6.71, 10.52] | 5 | 0 |
| humaneval/low | picospec_g8_vs_picospec | 30 | -12.13 [-13.78, -10.29] | -16.80 [-19.07, -14.41] | 4 | 0 |
| humaneval/low | sync_g4_vs_picospec | 30 | -15.33 [-18.73, -12.79] | 15.54 [13.77, 17.17] | 0 | 0 |
| humaneval/low | hf_default_vs_picospec | 30 | -14.39 [-17.27, -11.84] | -4.42 [-7.32, -1.53] | 3 | 0 |
| humaneval/low | pipesd_vs_picospec | 30 | -2.09 [-4.54, -0.04] | 1.06 [-1.83, 3.21] | 6 | 0 |
| humaneval/low | pearl_vs_picospec | 30 | -5.23 [-10.56, -1.12] | 12.66 [10.34, 15.11] | 5 | 0 |
| humaneval/low | markov_w0_dist_int_vs_picospec | 30 | -0.22 [-1.62, 1.37] | 2.35 [0.93, 3.90] | 6 | 0 |
| humaneval/low | markov_w05_dist_int_vs_picospec | 30 | 1.63 [-0.73, 5.04] | 6.37 [4.05, 9.38] | 5 | 1 |
| humaneval/low | picospec_g2_vs_picospec_g8 | 30 | 13.98 [7.49, 19.57] | 21.72 [18.81, 24.56] | 8 | 0 |
| humaneval/low | picospec_vs_picospec_g8 | 30 | 13.80 [11.47, 15.98] | 14.38 [12.59, 16.02] | 4 | 0 |
| humaneval/low | sync_g4_vs_picospec_g8 | 30 | -3.65 [-8.43, 0.63] | 27.69 [24.92, 30.23] | 4 | 0 |
| humaneval/low | hf_default_vs_picospec_g8 | 30 | -2.58 [-6.78, 1.50] | 10.60 [6.88, 13.99] | 6 | 0 |
| humaneval/low | pipesd_vs_picospec_g8 | 30 | 11.42 [7.70, 14.93] | 15.29 [12.13, 17.96] | 9 | 0 |
| humaneval/low | pearl_vs_picospec_g8 | 30 | 7.84 [0.82, 13.92] | 25.22 [21.86, 28.49] | 8 | 0 |
| humaneval/low | markov_w0_dist_int_vs_picospec_g8 | 30 | 13.54 [10.60, 16.72] | 16.40 [14.02, 18.80] | 9 | 0 |
| humaneval/low | markov_w05_dist_int_vs_picospec_g8 | 30 | 15.66 [11.58, 20.91] | 19.83 [16.63, 23.50] | 8 | 1 |
| humaneval/low | picospec_g2_vs_sync_g4 | 30 | 18.30 [16.55, 19.89] | -8.25 [-9.43, -7.03] | 5 | 0 |
| humaneval/low | picospec_vs_sync_g4 | 30 | 18.11 [14.67, 23.04] | -18.40 [-20.73, -15.97] | 0 | 0 |
| humaneval/low | picospec_g8_vs_sync_g4 | 30 | 3.79 [-0.63, 9.21] | -38.29 [-43.33, -33.20] | 4 | 0 |
| humaneval/low | hf_default_vs_sync_g4 | 30 | 1.11 [-1.87, 4.18] | -23.63 [-26.75, -20.65] | 3 | 0 |
| humaneval/low | pipesd_vs_sync_g4 | 30 | 15.65 [13.26, 18.20] | -17.14 [-19.57, -15.02] | 6 | 0 |
| humaneval/low | pearl_vs_sync_g4 | 30 | 11.93 [9.81, 13.88] | -3.41 [-4.59, -2.12] | 5 | 0 |
| humaneval/low | markov_w0_dist_int_vs_sync_g4 | 30 | 17.85 [14.41, 22.62] | -15.62 [-17.89, -13.39] | 6 | 0 |
| humaneval/low | markov_w05_dist_int_vs_sync_g4 | 30 | 20.04 [16.29, 24.97] | -10.86 [-13.03, -8.28] | 5 | 1 |
| humaneval/high | picospec_vs_picospec_g2 | 30 | 38.06 [34.78, 41.34] | -2.50 [-4.81, -0.41] | 4 | 0 |
| humaneval/high | picospec_g8_vs_picospec_g2 | 30 | 36.03 [30.36, 41.90] | -19.85 [-24.87, -14.95] | 9 | 0 |
| humaneval/high | sync_g4_vs_picospec_g2 | 30 | -11.15 [-12.64, -9.54] | 9.29 [8.10, 10.44] | 4 | 0 |
| humaneval/high | hf_default_vs_picospec_g2 | 30 | -0.74 [-5.23, 2.94] | -4.11 [-6.68, -1.79] | 5 | 0 |
| humaneval/high | pipesd_vs_picospec_g2 | 30 | 26.31 [22.59, 30.10] | -22.92 [-26.64, -19.26] | 3 | 0 |
| humaneval/high | pearl_vs_picospec_g2 | 30 | 38.15 [35.95, 40.39] | 0.21 [-1.03, 1.57] | 3 | 0 |
| humaneval/high | markov_w0_dist_int_vs_picospec_g2 | 30 | 44.18 [39.77, 48.77] | -8.37 [-11.47, -5.28] | 6 | 0 |
| humaneval/high | markov_w05_dist_int_vs_picospec_g2 | 30 | 37.47 [27.65, 45.21] | -3.47 [-6.83, -0.38] | 7 | 0 |
| humaneval/high | picospec_g2_vs_picospec | 30 | -27.57 [-29.25, -25.81] | 2.44 [0.41, 4.58] | 4 | 0 |
| humaneval/high | picospec_g8_vs_picospec | 30 | -1.47 [-3.67, 1.00] | -16.92 [-19.54, -14.10] | 5 | 0 |
| humaneval/high | sync_g4_vs_picospec | 30 | -35.64 [-36.69, -34.57] | 11.50 [9.89, 13.03] | 0 | 0 |
| humaneval/high | hf_default_vs_picospec | 30 | -28.11 [-31.02, -25.87] | -1.57 [-4.03, 0.85] | 7 | 0 |
| humaneval/high | pipesd_vs_picospec | 30 | -8.51 [-10.80, -6.44] | -19.92 [-22.60, -17.53] | 5 | 0 |
| humaneval/high | pearl_vs_picospec | 30 | 0.06 [-1.41, 1.71] | 2.64 [1.31, 4.18] | 2 | 0 |
| humaneval/high | markov_w0_dist_int_vs_picospec | 30 | 4.43 [1.87, 6.63] | -5.72 [-7.78, -3.80] | 2 | 0 |
| humaneval/high | markov_w05_dist_int_vs_picospec | 30 | -0.43 [-6.80, 3.75] | -0.94 [-3.32, 0.96] | 3 | 0 |
| humaneval/high | picospec_g2_vs_picospec_g8 | 30 | -26.49 [-29.53, -23.29] | 16.56 [13.00, 19.91] | 9 | 0 |
| humaneval/high | picospec_vs_picospec_g8 | 30 | 1.50 [-0.99, 3.81] | 14.47 [12.36, 16.35] | 5 | 0 |
| humaneval/high | sync_g4_vs_picospec_g8 | 30 | -34.68 [-37.03, -32.29] | 24.31 [21.23, 27.08] | 5 | 0 |
| humaneval/high | hf_default_vs_picospec_g8 | 30 | -27.03 [-30.51, -23.95] | 13.13 [9.66, 16.36] | 8 | 0 |
| humaneval/high | pipesd_vs_picospec_g8 | 30 | -7.14 [-9.92, -4.42] | -2.56 [-5.54, 0.14] | 8 | 0 |
| humaneval/high | pearl_vs_picospec_g8 | 30 | 1.56 [-1.42, 4.90] | 16.74 [14.13, 19.37] | 7 | 0 |
| humaneval/high | markov_w0_dist_int_vs_picospec_g8 | 30 | 5.99 [3.26, 8.51] | 9.58 [7.22, 11.70] | 5 | 0 |
| humaneval/high | markov_w05_dist_int_vs_picospec_g8 | 30 | 1.06 [-5.40, 5.18] | 13.67 [11.22, 15.77] | 4 | 0 |
| humaneval/high | picospec_g2_vs_sync_g4 | 30 | 12.54 [10.54, 14.47] | -10.24 [-11.66, -8.82] | 4 | 0 |
| humaneval/high | picospec_vs_sync_g4 | 30 | 55.38 [52.83, 57.95] | -13.00 [-14.98, -10.98] | 0 | 0 |
| humaneval/high | picospec_g8_vs_sync_g4 | 30 | 53.09 [47.69, 58.81] | -32.12 [-37.13, -26.95] | 5 | 0 |
| humaneval/high | hf_default_vs_sync_g4 | 30 | 11.71 [7.08, 15.41] | -14.77 [-17.55, -12.17] | 7 | 0 |
| humaneval/high | pipesd_vs_sync_g4 | 30 | 42.16 [37.91, 46.48] | -35.51 [-39.67, -31.48] | 5 | 0 |
| humaneval/high | pearl_vs_sync_g4 | 30 | 55.47 [52.55, 58.24] | -10.01 [-11.97, -8.15] | 2 | 0 |
| humaneval/high | markov_w0_dist_int_vs_sync_g4 | 30 | 62.26 [57.11, 67.14] | -19.46 [-22.78, -16.20] | 2 | 0 |
| humaneval/high | markov_w05_dist_int_vs_sync_g4 | 30 | 54.71 [44.78, 62.63] | -14.06 [-17.47, -10.81] | 3 | 0 |
| humaneval/dynamic | picospec_vs_picospec_g2 | 30 | 11.73 [8.56, 14.91] | -5.83 [-7.75, -4.02] | 4 | 0 |
| humaneval/dynamic | picospec_g8_vs_picospec_g2 | 30 | 4.83 [0.69, 9.13] | -22.83 [-26.67, -19.00] | 7 | 0 |
| humaneval/dynamic | sync_g4_vs_picospec_g2 | 30 | -14.49 [-16.26, -12.79] | 11.31 [10.34, 12.24] | 3 | 0 |
| humaneval/dynamic | hf_default_vs_picospec_g2 | 30 | -11.93 [-14.85, -9.02] | -10.59 [-13.37, -8.05] | 4 | 0 |
| humaneval/dynamic | pipesd_vs_picospec_g2 | 30 | 7.22 [3.97, 10.81] | -13.44 [-15.88, -10.80] | 3 | 0 |
| humaneval/dynamic | pearl_vs_picospec_g2 | 30 | -2.23 [-3.13, -1.33] | 0.45 [-0.36, 1.32] | 1 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_picospec_g2 | 30 | 14.19 [10.85, 17.74] | -7.45 [-9.45, -5.40] | 3 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_picospec_g2 | 30 | 13.32 [9.94, 16.74] | -2.47 [-4.13, -0.89] | 2 | 0 |
| humaneval/dynamic | picospec_g2_vs_picospec | 30 | -10.50 [-12.98, -7.89] | 5.51 [3.86, 7.19] | 4 | 0 |
| humaneval/dynamic | picospec_g8_vs_picospec | 30 | -6.18 [-7.87, -4.37] | -16.06 [-18.12, -14.02] | 4 | 0 |
| humaneval/dynamic | sync_g4_vs_picospec | 30 | -23.47 [-25.37, -21.48] | 16.20 [14.75, 17.59] | 1 | 0 |
| humaneval/dynamic | hf_default_vs_picospec | 30 | -21.17 [-23.86, -18.56] | -4.49 [-7.48, -1.85] | 6 | 0 |
| humaneval/dynamic | pipesd_vs_picospec | 30 | -4.03 [-6.06, -2.14] | -7.19 [-9.20, -5.44] | 7 | 0 |
| humaneval/dynamic | pearl_vs_picospec | 30 | -12.50 [-14.95, -9.82] | 5.94 [4.08, 7.92] | 5 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_picospec | 30 | 2.21 [1.07, 3.38] | -1.53 [-2.81, -0.23] | 5 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_picospec | 30 | 1.43 [0.01, 2.83] | 3.18 [1.83, 4.66] | 4 | 0 |
| humaneval/dynamic | picospec_g2_vs_picospec_g8 | 30 | -4.60 [-8.37, -0.69] | 18.59 [15.97, 21.05] | 7 | 0 |
| humaneval/dynamic | picospec_vs_picospec_g8 | 30 | 6.58 [4.57, 8.54] | 13.84 [12.30, 15.34] | 4 | 0 |
| humaneval/dynamic | sync_g4_vs_picospec_g8 | 30 | -18.43 [-21.54, -15.32] | 27.79 [25.41, 30.11] | 5 | 0 |
| humaneval/dynamic | hf_default_vs_picospec_g8 | 30 | -15.98 [-19.13, -12.94] | 9.97 [6.76, 12.74] | 7 | 0 |
| humaneval/dynamic | pipesd_vs_picospec_g8 | 30 | 2.29 [-0.01, 4.77] | 7.65 [5.62, 9.61] | 8 | 0 |
| humaneval/dynamic | pearl_vs_picospec_g8 | 30 | -6.74 [-10.45, -2.77] | 18.95 [16.28, 21.51] | 6 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_picospec_g8 | 30 | 8.93 [6.88, 10.94] | 12.52 [10.66, 14.30] | 6 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_picospec_g8 | 30 | 8.11 [5.78, 10.58] | 16.58 [14.54, 18.57] | 5 | 0 |
| humaneval/dynamic | picospec_g2_vs_sync_g4 | 30 | 16.95 [14.66, 19.42] | -12.75 [-13.95, -11.53] | 3 | 0 |
| humaneval/dynamic | picospec_vs_sync_g4 | 30 | 30.66 [27.35, 34.00] | -19.33 [-21.35, -17.31] | 1 | 0 |
| humaneval/dynamic | picospec_g8_vs_sync_g4 | 30 | 22.59 [18.09, 27.45] | -38.49 [-43.09, -34.07] | 5 | 0 |
| humaneval/dynamic | hf_default_vs_sync_g4 | 30 | 3.00 [-0.60, 6.71] | -24.69 [-27.98, -21.69] | 7 | 0 |
| humaneval/dynamic | pipesd_vs_sync_g4 | 30 | 25.39 [21.43, 29.30] | -27.90 [-30.69, -24.89] | 6 | 0 |
| humaneval/dynamic | pearl_vs_sync_g4 | 30 | 14.34 [12.31, 16.41] | -12.24 [-13.55, -10.90] | 4 | 0 |
| humaneval/dynamic | markov_w0_dist_int_vs_sync_g4 | 30 | 33.54 [29.80, 37.26] | -21.15 [-23.48, -18.70] | 4 | 0 |
| humaneval/dynamic | markov_w05_dist_int_vs_sync_g4 | 30 | 32.53 [29.15, 36.05] | -15.54 [-17.25, -13.73] | 3 | 0 |
| humaneval/pooled | picospec_vs_picospec_g2 | 30 | 18.81 [15.98, 21.55] | -5.56 [-7.59, -3.69] | 13 | 0 |
| humaneval/pooled | picospec_g8_vs_picospec_g2 | 30 | 11.38 [6.97, 15.85] | -23.08 [-27.58, -18.83] | 24 | 0 |
| humaneval/pooled | sync_g4_vs_picospec_g2 | 30 | -13.04 [-14.35, -11.76] | 9.55 [8.68, 10.34] | 12 | 0 |
| humaneval/pooled | hf_default_vs_picospec_g2 | 30 | -7.80 [-10.34, -5.49] | -9.19 [-11.61, -7.03] | 13 | 0 |
| humaneval/pooled | pipesd_vs_picospec_g2 | 30 | 12.39 [9.93, 14.89] | -15.46 [-17.68, -13.18] | 9 | 0 |
| humaneval/pooled | pearl_vs_picospec_g2 | 30 | 11.81 [10.74, 12.80] | 1.63 [1.13, 2.15] | 4 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec_g2 | 30 | 21.56 [18.50, 24.69] | -7.53 [-9.75, -5.35] | 10 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_picospec_g2 | 30 | 19.79 [15.44, 23.55] | -2.70 [-4.37, -1.01] | 12 | 1 |
| humaneval/pooled | picospec_g2_vs_picospec | 30 | -15.83 [-17.73, -13.78] | 5.26 [3.56, 7.06] | 13 | 0 |
| humaneval/pooled | picospec_g8_vs_picospec | 30 | -6.25 [-8.05, -4.38] | -16.60 [-18.77, -14.29] | 13 | 0 |
| humaneval/pooled | sync_g4_vs_picospec | 30 | -26.81 [-28.12, -25.52] | 14.31 [12.85, 15.70] | 1 | 0 |
| humaneval/pooled | hf_default_vs_picospec | 30 | -22.40 [-24.13, -20.65] | -3.44 [-5.81, -1.15] | 16 | 0 |
| humaneval/pooled | pipesd_vs_picospec | 30 | -5.41 [-6.73, -4.15] | -9.38 [-10.87, -8.01] | 18 | 0 |
| humaneval/pooled | pearl_vs_picospec | 30 | -5.89 [-8.01, -3.76] | 6.81 [5.27, 8.45] | 12 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec | 30 | 2.32 [1.00, 3.53] | -1.87 [-3.17, -0.64] | 13 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_picospec | 30 | 0.82 [-1.84, 2.91] | 2.71 [1.33, 4.11] | 12 | 1 |
| humaneval/pooled | picospec_g2_vs_picospec_g8 | 30 | -10.22 [-13.68, -6.52] | 18.75 [15.85, 21.62] | 24 | 0 |
| humaneval/pooled | picospec_vs_picospec_g8 | 30 | 6.67 [4.58, 8.75] | 14.24 [12.50, 15.80] | 13 | 0 |
| humaneval/pooled | sync_g4_vs_picospec_g8 | 30 | -21.93 [-24.68, -19.19] | 26.51 [23.83, 28.96] | 14 | 0 |
| humaneval/pooled | hf_default_vs_picospec_g8 | 30 | -17.22 [-20.06, -14.50] | 11.29 [8.03, 14.40] | 21 | 0 |
| humaneval/pooled | pipesd_vs_picospec_g8 | 30 | 0.90 [-1.42, 3.41] | 6.19 [3.99, 8.38] | 25 | 0 |
| humaneval/pooled | pearl_vs_picospec_g8 | 30 | 0.39 [-3.41, 4.25] | 20.08 [17.25, 22.87] | 21 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_picospec_g8 | 30 | 9.14 [6.97, 11.33] | 12.63 [10.66, 14.51] | 20 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_picospec_g8 | 30 | 7.54 [4.10, 10.89] | 16.56 [14.33, 18.91] | 17 | 1 |
| humaneval/pooled | picospec_g2_vs_sync_g4 | 30 | 15.00 [13.33, 16.75] | -10.56 [-11.53, -9.51] | 12 | 0 |
| humaneval/pooled | picospec_vs_sync_g4 | 30 | 36.63 [34.27, 39.13] | -16.70 [-18.62, -14.75] | 1 | 0 |
| humaneval/pooled | picospec_g8_vs_sync_g4 | 30 | 28.09 [23.75, 32.77] | -36.07 [-40.77, -31.28] | 14 | 0 |
| humaneval/pooled | hf_default_vs_sync_g4 | 30 | 6.03 [3.35, 8.87] | -20.71 [-23.51, -18.13] | 17 | 0 |
| humaneval/pooled | pipesd_vs_sync_g4 | 30 | 29.24 [26.59, 32.01] | -27.65 [-30.14, -25.10] | 17 | 0 |
| humaneval/pooled | pearl_vs_sync_g4 | 30 | 28.59 [26.92, 30.23] | -8.75 [-9.72, -7.75] | 11 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_sync_g4 | 30 | 39.80 [36.59, 43.00] | -18.88 [-21.20, -16.53] | 12 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_sync_g4 | 30 | 37.76 [33.31, 41.92] | -13.54 [-15.38, -11.70] | 11 | 1 |
| gsm8k/low | picospec_vs_picospec_g2 | 50 | -7.40 [-9.31, -5.43] | -16.17 [-18.50, -14.02] | 7 | 2 |
| gsm8k/low | picospec_g8_vs_picospec_g2 | 50 | -24.03 [-25.97, -21.98] | -44.90 [-48.72, -40.96] | 13 | 2 |
| gsm8k/low | sync_g4_vs_picospec_g2 | 50 | -13.59 [-15.50, -11.76] | 8.99 [7.50, 10.22] | 6 | 2 |
| gsm8k/low | hf_default_vs_picospec_g2 | 50 | -20.54 [-22.98, -18.32] | -20.66 [-24.49, -17.46] | 15 | 1 |
| gsm8k/low | pipesd_vs_picospec_g2 | 50 | -7.59 [-9.08, -6.24] | -12.40 [-15.06, -10.33] | 9 | 1 |
| gsm8k/low | pearl_vs_picospec_g2 | 50 | -0.89 [-2.71, 0.59] | 8.82 [7.48, 9.98] | 5 | 1 |
| gsm8k/low | markov_w0_dist_int_vs_picospec_g2 | 50 | -2.40 [-3.45, -1.25] | -5.54 [-6.79, -4.26] | 4 | 2 |
| gsm8k/low | markov_w05_dist_int_vs_picospec_g2 | 50 | -1.37 [-2.82, 0.13] | -0.33 [-1.56, 0.75] | 6 | 2 |
| gsm8k/low | picospec_g2_vs_picospec | 50 | 8.00 [5.74, 10.27] | 13.92 [12.29, 15.61] | 7 | 1 |
| gsm8k/low | picospec_g8_vs_picospec | 50 | -17.96 [-19.35, -16.62] | -24.73 [-26.47, -22.94] | 10 | 1 |
| gsm8k/low | sync_g4_vs_picospec | 50 | -6.68 [-8.57, -4.75] | 21.66 [20.10, 23.01] | 1 | 1 |
| gsm8k/low | hf_default_vs_picospec | 50 | -14.18 [-17.66, -10.99] | -3.86 [-7.81, -0.39] | 17 | 1 |
| gsm8k/low | pipesd_vs_picospec | 50 | -0.20 [-2.87, 2.28] | 3.25 [0.18, 5.77] | 11 | 1 |
| gsm8k/low | pearl_vs_picospec | 50 | 7.04 [3.36, 10.24] | 21.51 [19.21, 23.52] | 10 | 1 |
| gsm8k/low | markov_w0_dist_int_vs_picospec | 50 | 5.40 [3.49, 7.52] | 9.15 [7.13, 11.26] | 9 | 2 |
| gsm8k/low | markov_w05_dist_int_vs_picospec | 50 | 6.51 [4.69, 8.21] | 13.64 [11.81, 15.29] | 6 | 2 |
| gsm8k/low | picospec_g2_vs_picospec_g8 | 50 | 31.63 [28.16, 35.08] | 30.99 [29.06, 32.76] | 13 | 0 |
| gsm8k/low | picospec_vs_picospec_g8 | 50 | 21.89 [19.93, 23.99] | 19.82 [18.66, 20.93] | 10 | 0 |
| gsm8k/low | sync_g4_vs_picospec_g8 | 50 | 13.74 [10.50, 17.27] | 37.19 [35.33, 38.89] | 9 | 0 |
| gsm8k/low | hf_default_vs_picospec_g8 | 50 | 4.60 [0.13, 8.85] | 16.73 [12.92, 19.99] | 17 | 1 |
| gsm8k/low | pipesd_vs_picospec_g8 | 50 | 21.65 [18.03, 25.19] | 22.43 [19.58, 24.83] | 11 | 0 |
| gsm8k/low | pearl_vs_picospec_g8 | 50 | 30.47 [25.87, 35.03] | 37.07 [34.66, 39.24] | 16 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_picospec_g8 | 50 | 28.47 [24.99, 32.09] | 27.16 [25.04, 29.24] | 13 | 1 |
| gsm8k/low | markov_w05_dist_int_vs_picospec_g8 | 50 | 29.82 [26.38, 33.25] | 30.76 [28.73, 32.60] | 12 | 1 |
| gsm8k/low | picospec_g2_vs_sync_g4 | 50 | 15.73 [13.32, 18.34] | -9.88 [-11.39, -8.10] | 6 | 0 |
| gsm8k/low | picospec_vs_sync_g4 | 50 | 7.16 [4.98, 9.37] | -27.65 [-29.88, -25.15] | 1 | 0 |
| gsm8k/low | picospec_g8_vs_sync_g4 | 50 | -12.08 [-14.72, -9.50] | -59.22 [-63.65, -54.62] | 9 | 0 |
| gsm8k/low | hf_default_vs_sync_g4 | 50 | -8.03 [-11.88, -4.59] | -32.58 [-37.40, -28.56] | 18 | 1 |
| gsm8k/low | pipesd_vs_sync_g4 | 50 | 6.95 [4.01, 9.82] | -23.51 [-26.95, -20.39] | 10 | 0 |
| gsm8k/low | pearl_vs_sync_g4 | 50 | 14.71 [11.29, 17.72] | -0.19 [-1.88, 1.43] | 9 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_sync_g4 | 50 | 12.95 [10.66, 15.56] | -15.97 [-18.24, -13.39] | 8 | 1 |
| gsm8k/low | markov_w05_dist_int_vs_sync_g4 | 50 | 14.14 [12.16, 16.16] | -10.24 [-11.72, -8.80] | 5 | 1 |
| gsm8k/high | picospec_vs_picospec_g2 | 50 | 29.42 [26.95, 32.09] | -7.55 [-9.70, -5.17] | 7 | 1 |
| gsm8k/high | picospec_g8_vs_picospec_g2 | 50 | 19.35 [15.49, 24.05] | -34.32 [-38.72, -29.16] | 13 | 2 |
| gsm8k/high | sync_g4_vs_picospec_g2 | 50 | -10.39 [-11.79, -9.06] | 11.13 [9.83, 12.39] | 8 | 1 |
| gsm8k/high | hf_default_vs_picospec_g2 | 50 | -9.12 [-11.98, -6.28] | -10.89 [-14.33, -7.88] | 14 | 0 |
| gsm8k/high | pipesd_vs_picospec_g2 | 50 | 9.74 [6.66, 13.48] | -38.48 [-42.75, -33.70] | 7 | 0 |
| gsm8k/high | pearl_vs_picospec_g2 | 50 | 29.60 [26.23, 33.08] | -3.34 [-5.54, -0.88] | 6 | 1 |
| gsm8k/high | markov_w0_dist_int_vs_picospec_g2 | 50 | 34.67 [31.19, 38.50] | -11.70 [-14.54, -8.63] | 9 | 1 |
| gsm8k/high | markov_w05_dist_int_vs_picospec_g2 | 50 | 24.21 [20.89, 28.12] | -3.86 [-5.62, -1.78] | 5 | 1 |
| gsm8k/high | picospec_g2_vs_picospec | 50 | -22.73 [-24.29, -21.23] | 7.02 [4.92, 8.85] | 7 | 0 |
| gsm8k/high | picospec_g8_vs_picospec | 50 | -7.79 [-9.96, -5.43] | -24.89 [-27.45, -22.04] | 11 | 1 |
| gsm8k/high | sync_g4_vs_picospec | 50 | -30.76 [-32.00, -29.63] | 17.37 [15.43, 19.00] | 1 | 0 |
| gsm8k/high | hf_default_vs_picospec | 50 | -29.78 [-31.90, -27.62] | -3.10 [-6.73, 0.10] | 20 | 0 |
| gsm8k/high | pipesd_vs_picospec | 50 | -15.21 [-17.20, -13.05] | -28.75 [-31.79, -25.63] | 9 | 0 |
| gsm8k/high | pearl_vs_picospec | 50 | 0.14 [-1.92, 2.02] | 3.92 [2.57, 5.40] | 5 | 0 |
| gsm8k/high | markov_w0_dist_int_vs_picospec | 50 | 4.05 [1.96, 6.16] | -3.86 [-5.91, -1.79] | 11 | 1 |
| gsm8k/high | markov_w05_dist_int_vs_picospec | 50 | -4.03 [-5.67, -2.32] | 3.44 [1.89, 4.84] | 8 | 0 |
| gsm8k/high | picospec_g2_vs_picospec_g8 | 50 | -16.21 [-19.39, -13.42] | 25.55 [22.58, 27.91] | 13 | 0 |
| gsm8k/high | picospec_vs_picospec_g8 | 50 | 8.44 [5.74, 11.06] | 19.93 [18.06, 21.54] | 11 | 0 |
| gsm8k/high | sync_g4_vs_picospec_g8 | 50 | -24.92 [-27.66, -22.55] | 33.84 [31.03, 36.01] | 12 | 0 |
| gsm8k/high | hf_default_vs_picospec_g8 | 50 | -23.85 [-26.62, -21.31] | 17.45 [13.37, 20.78] | 17 | 0 |
| gsm8k/high | pipesd_vs_picospec_g8 | 50 | -8.05 [-10.39, -5.79] | -3.09 [-5.76, -0.59] | 14 | 0 |
| gsm8k/high | pearl_vs_picospec_g8 | 50 | 8.59 [5.43, 11.50] | 23.07 [20.81, 25.04] | 10 | 0 |
| gsm8k/high | markov_w0_dist_int_vs_picospec_g8 | 50 | 12.84 [9.64, 15.61] | 16.84 [14.34, 18.79] | 8 | 0 |
| gsm8k/high | markov_w05_dist_int_vs_picospec_g8 | 50 | 4.07 [1.19, 6.65] | 22.68 [20.27, 24.80] | 10 | 0 |
| gsm8k/high | picospec_g2_vs_sync_g4 | 50 | 11.59 [9.96, 13.36] | -12.53 [-14.15, -10.91] | 8 | 1 |
| gsm8k/high | picospec_vs_sync_g4 | 50 | 44.43 [42.10, 47.05] | -21.02 [-23.46, -18.25] | 1 | 1 |
| gsm8k/high | picospec_g8_vs_sync_g4 | 50 | 33.18 [29.11, 38.24] | -51.15 [-56.28, -45.00] | 12 | 2 |
| gsm8k/high | hf_default_vs_sync_g4 | 50 | 1.42 [-1.84, 4.91] | -24.78 [-28.49, -21.33] | 19 | 0 |
| gsm8k/high | pipesd_vs_sync_g4 | 50 | 22.46 [18.50, 27.01] | -55.82 [-61.70, -49.75] | 10 | 1 |
| gsm8k/high | pearl_vs_sync_g4 | 50 | 44.63 [40.94, 48.33] | -16.28 [-18.93, -13.32] | 6 | 1 |
| gsm8k/high | markov_w0_dist_int_vs_sync_g4 | 50 | 50.28 [46.37, 54.50] | -25.69 [-29.09, -21.96] | 12 | 2 |
| gsm8k/high | markov_w05_dist_int_vs_sync_g4 | 50 | 38.61 [35.01, 42.83] | -16.87 [-19.42, -14.11] | 9 | 1 |
| gsm8k/dynamic | picospec_vs_picospec_g2 | 50 | 7.92 [5.47, 10.40] | -11.24 [-13.07, -9.27] | 7 | 1 |
| gsm8k/dynamic | picospec_g8_vs_picospec_g2 | 50 | -6.88 [-9.87, -3.36] | -40.54 [-44.79, -36.12] | 15 | 3 |
| gsm8k/dynamic | sync_g4_vs_picospec_g2 | 50 | -12.98 [-14.35, -11.65] | 11.79 [10.31, 13.25] | 7 | 1 |
| gsm8k/dynamic | hf_default_vs_picospec_g2 | 50 | -14.53 [-17.96, -11.27] | -16.12 [-20.60, -12.36] | 13 | 0 |
| gsm8k/dynamic | pipesd_vs_picospec_g2 | 50 | 2.59 [-0.43, 5.82] | -20.71 [-23.95, -17.28] | 9 | 1 |
| gsm8k/dynamic | pearl_vs_picospec_g2 | 50 | -1.05 [-3.08, 0.98] | 2.25 [0.58, 3.91] | 6 | 2 |
| gsm8k/dynamic | markov_w0_dist_int_vs_picospec_g2 | 50 | 9.53 [6.34, 13.29] | -11.52 [-13.70, -9.26] | 12 | 2 |
| gsm8k/dynamic | markov_w05_dist_int_vs_picospec_g2 | 50 | 7.73 [4.79, 10.99] | -2.60 [-4.32, -0.85] | 10 | 2 |
| gsm8k/dynamic | picospec_g2_vs_picospec | 50 | -7.34 [-9.42, -5.19] | 10.10 [8.48, 11.56] | 7 | 0 |
| gsm8k/dynamic | picospec_g8_vs_picospec | 50 | -13.72 [-15.54, -11.61] | -26.35 [-29.18, -23.20] | 12 | 2 |
| gsm8k/dynamic | sync_g4_vs_picospec | 50 | -19.36 [-21.30, -17.33] | 20.70 [19.07, 22.18] | 0 | 0 |
| gsm8k/dynamic | hf_default_vs_picospec | 50 | -20.80 [-23.32, -18.45] | -4.39 [-8.12, -1.27] | 18 | 0 |
| gsm8k/dynamic | pipesd_vs_picospec | 50 | -4.94 [-7.12, -2.04] | -8.51 [-11.26, -5.27] | 13 | 1 |
| gsm8k/dynamic | pearl_vs_picospec | 50 | -8.31 [-11.00, -5.54] | 12.13 [9.96, 14.14] | 8 | 1 |
| gsm8k/dynamic | markov_w0_dist_int_vs_picospec | 50 | 1.49 [-0.48, 3.57] | -0.25 [-2.29, 1.61] | 11 | 2 |
| gsm8k/dynamic | markov_w05_dist_int_vs_picospec | 50 | -0.18 [-2.20, 1.79] | 7.77 [5.88, 9.51] | 11 | 2 |
| gsm8k/dynamic | picospec_g2_vs_picospec_g8 | 50 | 7.39 [3.47, 10.95] | 28.85 [26.54, 30.93] | 15 | 0 |
| gsm8k/dynamic | picospec_vs_picospec_g8 | 50 | 15.90 [13.14, 18.40] | 20.85 [18.83, 22.59] | 12 | 0 |
| gsm8k/dynamic | sync_g4_vs_picospec_g8 | 50 | -6.54 [-9.87, -3.26] | 37.24 [34.86, 39.21] | 12 | 0 |
| gsm8k/dynamic | hf_default_vs_picospec_g8 | 50 | -8.21 [-12.15, -4.58] | 17.38 [12.94, 21.04] | 16 | 0 |
| gsm8k/dynamic | pipesd_vs_picospec_g8 | 50 | 10.17 [6.76, 13.94] | 14.12 [11.24, 16.83] | 16 | 1 |
| gsm8k/dynamic | pearl_vs_picospec_g8 | 50 | 6.27 [1.74, 10.63] | 30.45 [27.66, 32.82] | 18 | 1 |
| gsm8k/dynamic | markov_w0_dist_int_vs_picospec_g8 | 50 | 17.63 [13.47, 21.76] | 20.65 [17.53, 23.39] | 14 | 1 |
| gsm8k/dynamic | markov_w05_dist_int_vs_picospec_g8 | 50 | 15.69 [11.79, 19.41] | 27.00 [24.23, 29.49] | 15 | 1 |
| gsm8k/dynamic | picospec_g2_vs_sync_g4 | 50 | 14.91 [13.18, 16.76] | -13.37 [-15.28, -11.50] | 7 | 0 |
| gsm8k/dynamic | picospec_vs_sync_g4 | 50 | 24.01 [20.96, 27.07] | -26.11 [-28.50, -23.57] | 0 | 0 |
| gsm8k/dynamic | picospec_g8_vs_sync_g4 | 50 | 7.00 [3.37, 10.95] | -59.33 [-64.51, -53.52] | 12 | 2 |
| gsm8k/dynamic | hf_default_vs_sync_g4 | 50 | -1.78 [-5.58, 1.78] | -31.64 [-36.07, -27.76] | 18 | 0 |
| gsm8k/dynamic | pipesd_vs_sync_g4 | 50 | 17.89 [14.11, 22.00] | -36.84 [-41.05, -32.20] | 13 | 1 |
| gsm8k/dynamic | pearl_vs_sync_g4 | 50 | 13.71 [11.19, 16.52] | -10.82 [-12.75, -8.65] | 8 | 1 |
| gsm8k/dynamic | markov_w0_dist_int_vs_sync_g4 | 50 | 25.87 [21.95, 30.19] | -26.42 [-29.34, -23.30] | 11 | 2 |
| gsm8k/dynamic | markov_w05_dist_int_vs_sync_g4 | 50 | 23.79 [20.35, 27.71] | -16.31 [-18.49, -14.04] | 11 | 2 |
| gsm8k/pooled | picospec_vs_picospec_g2 | 50 | 11.83 [10.26, 13.62] | -11.34 [-13.09, -9.42] | 21 | 4 |
| gsm8k/pooled | picospec_g8_vs_picospec_g2 | 50 | -2.55 [-5.06, 0.25] | -39.51 [-42.98, -35.51] | 41 | 7 |
| gsm8k/pooled | sync_g4_vs_picospec_g2 | 50 | -11.45 [-12.62, -10.26] | 10.87 [9.85, 11.78] | 21 | 4 |
| gsm8k/pooled | hf_default_vs_picospec_g2 | 50 | -13.70 [-16.40, -11.17] | -15.49 [-19.02, -12.49] | 42 | 1 |
| gsm8k/pooled | pipesd_vs_picospec_g2 | 50 | 3.03 [1.16, 5.10] | -24.71 [-27.04, -22.23] | 25 | 2 |
| gsm8k/pooled | pearl_vs_picospec_g2 | 50 | 10.70 [9.07, 12.23] | 2.13 [1.12, 3.14] | 17 | 4 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec_g2 | 50 | 16.16 [14.29, 18.11] | -9.50 [-11.03, -7.88] | 25 | 5 |
| gsm8k/pooled | markov_w05_dist_int_vs_picospec_g2 | 50 | 11.99 [10.15, 13.84] | -2.35 [-3.38, -1.33] | 21 | 5 |
| gsm8k/pooled | picospec_g2_vs_picospec | 50 | -10.58 [-11.99, -9.31] | 10.19 [8.61, 11.57] | 21 | 1 |
| gsm8k/pooled | picospec_g8_vs_picospec | 50 | -12.86 [-14.20, -11.39] | -25.29 [-27.06, -23.29] | 33 | 4 |
| gsm8k/pooled | sync_g4_vs_picospec | 50 | -20.82 [-22.19, -19.57] | 19.95 [18.40, 21.29] | 2 | 1 |
| gsm8k/pooled | hf_default_vs_picospec | 50 | -22.83 [-25.00, -20.81] | -3.72 [-7.21, -0.72] | 55 | 1 |
| gsm8k/pooled | pipesd_vs_picospec | 50 | -7.87 [-9.11, -6.51] | -12.00 [-13.53, -10.50] | 33 | 2 |
| gsm8k/pooled | pearl_vs_picospec | 50 | -1.01 [-2.77, 0.55] | 12.10 [10.85, 13.21] | 23 | 2 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec | 50 | 3.87 [2.26, 5.55] | 1.65 [-0.04, 3.28] | 31 | 5 |
| gsm8k/pooled | markov_w05_dist_int_vs_picospec | 50 | 0.14 [-1.15, 1.42] | 8.08 [6.58, 9.46] | 25 | 4 |
| gsm8k/pooled | picospec_g2_vs_picospec_g8 | 50 | 2.61 [-0.25, 5.32] | 28.32 [26.21, 30.06] | 41 | 0 |
| gsm8k/pooled | picospec_vs_picospec_g8 | 50 | 14.75 [12.85, 16.54] | 20.19 [18.89, 21.29] | 33 | 0 |
| gsm8k/pooled | sync_g4_vs_picospec_g8 | 50 | -9.13 [-11.77, -6.87] | 36.11 [34.05, 37.75] | 33 | 0 |
| gsm8k/pooled | hf_default_vs_picospec_g8 | 50 | -11.45 [-14.32, -8.76] | 17.22 [13.63, 20.24] | 50 | 1 |
| gsm8k/pooled | pipesd_vs_picospec_g8 | 50 | 5.72 [3.91, 7.56] | 10.61 [8.94, 12.20] | 41 | 1 |
| gsm8k/pooled | pearl_vs_picospec_g8 | 50 | 13.59 [10.45, 16.37] | 29.84 [27.90, 31.47] | 44 | 1 |
| gsm8k/pooled | markov_w0_dist_int_vs_picospec_g8 | 50 | 19.20 [16.19, 21.85] | 21.51 [19.31, 23.40] | 35 | 2 |
| gsm8k/pooled | markov_w05_dist_int_vs_picospec_g8 | 50 | 14.92 [12.34, 17.30] | 26.64 [24.59, 28.39] | 37 | 2 |
| gsm8k/pooled | picospec_g2_vs_sync_g4 | 50 | 12.93 [11.43, 14.44] | -12.20 [-13.36, -10.92] | 21 | 1 |
| gsm8k/pooled | picospec_vs_sync_g4 | 50 | 26.29 [24.33, 28.52] | -24.93 [-27.05, -22.55] | 2 | 1 |
| gsm8k/pooled | picospec_g8_vs_sync_g4 | 50 | 10.05 [7.38, 13.34] | -56.52 [-60.64, -51.62] | 33 | 4 |
| gsm8k/pooled | hf_default_vs_sync_g4 | 50 | -2.55 [-5.69, 0.45] | -29.57 [-33.44, -26.20] | 55 | 1 |
| gsm8k/pooled | pipesd_vs_sync_g4 | 50 | 16.34 [13.75, 19.24] | -39.92 [-43.11, -36.40] | 33 | 2 |
| gsm8k/pooled | pearl_vs_sync_g4 | 50 | 25.01 [22.93, 27.16] | -9.81 [-11.17, -8.35] | 23 | 2 |
| gsm8k/pooled | markov_w0_dist_int_vs_sync_g4 | 50 | 31.18 [28.74, 33.74] | -22.86 [-24.93, -20.43] | 31 | 5 |
| gsm8k/pooled | markov_w05_dist_int_vs_sync_g4 | 50 | 26.47 [24.05, 29.00] | -14.83 [-16.58, -13.11] | 25 | 4 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
