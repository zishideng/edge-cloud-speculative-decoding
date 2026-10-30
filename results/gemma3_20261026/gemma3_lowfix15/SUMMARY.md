# Progress probe: gemma3_lowfix15

State: complete; 285/285 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low; pooled = low.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | fixed_fast | 15 | 3658 | 28.387 | 0.3257 | 2 | 28.15 |
| all/low | fixed_g2 | 15 | 3732 | 27.810 | 0.2642 | 2 | 33.91 |
| all/low | picospec | 15 | 3658 | 29.742 | 0.3224 | 2 | 34.65 |
| all/low | markov_w0_dist | 15 | 3732 | 27.819 | 0.2693 | 2 | 38.57 |
| all/low | markov_w0_dist_pos | 15 | 3705 | 27.877 | 0.2821 | 2 | 36.41 |
| all/low | markov_w0_dist_int | 15 | 3732 | 29.217 | 0.2826 | 2 | 45.30 |
| all/low | markov_w0_dist_h0 | 15 | 3705 | 26.645 | 0.2707 | 2 | 41.94 |
| all/low | markov_w0_dist_pos_int | 15 | 3705 | 29.302 | 0.2896 | 2 | 45.28 |
| all/low | markov_w0_dist_pos_h0 | 15 | 3705 | 27.057 | 0.2799 | 2 | 38.54 |
| all/low | markov_w0_dist_int_h0 | 15 | 3732 | 28.492 | 0.2789 | 2 | 45.36 |
| all/low | markov_w0_dist_pos_int_h0 | 15 | 3732 | 29.778 | 0.2944 | 2 | 44.82 |
| all/low | markov_w05_dist | 15 | 3705 | 27.966 | 0.2578 | 2 | 38.70 |
| all/low | markov_w05_dist_pos | 15 | 3705 | 28.050 | 0.2706 | 2 | 39.57 |
| all/low | markov_w05_dist_int | 15 | 3705 | 29.224 | 0.2569 | 2 | 44.11 |
| all/low | markov_w05_dist_h0 | 15 | 3705 | 22.194 | 0.2656 | 2 | 61.79 |
| all/low | markov_w05_dist_pos_int | 15 | 3705 | 29.240 | 0.2604 | 2 | 45.96 |
| all/low | markov_w05_dist_pos_h0 | 15 | 3705 | 22.978 | 0.2723 | 2 | 58.80 |
| all/low | markov_w05_dist_int_h0 | 15 | 3705 | 23.829 | 0.2588 | 2 | 65.73 |
| all/low | markov_w05_dist_pos_int_h0 | 15 | 3705 | 24.007 | 0.2758 | 2 | 64.53 |
| all/pooled | fixed_fast | 15 | 3658 | 28.387 | 0.3257 | 2 | 28.15 |
| all/pooled | fixed_g2 | 15 | 3732 | 27.810 | 0.2642 | 2 | 33.91 |
| all/pooled | picospec | 15 | 3658 | 29.742 | 0.3224 | 2 | 34.65 |
| all/pooled | markov_w0_dist | 15 | 3732 | 27.819 | 0.2693 | 2 | 38.57 |
| all/pooled | markov_w0_dist_pos | 15 | 3705 | 27.877 | 0.2821 | 2 | 36.41 |
| all/pooled | markov_w0_dist_int | 15 | 3732 | 29.217 | 0.2826 | 2 | 45.30 |
| all/pooled | markov_w0_dist_h0 | 15 | 3705 | 26.645 | 0.2707 | 2 | 41.94 |
| all/pooled | markov_w0_dist_pos_int | 15 | 3705 | 29.302 | 0.2896 | 2 | 45.28 |
| all/pooled | markov_w0_dist_pos_h0 | 15 | 3705 | 27.057 | 0.2799 | 2 | 38.54 |
| all/pooled | markov_w0_dist_int_h0 | 15 | 3732 | 28.492 | 0.2789 | 2 | 45.36 |
| all/pooled | markov_w0_dist_pos_int_h0 | 15 | 3732 | 29.778 | 0.2944 | 2 | 44.82 |
| all/pooled | markov_w05_dist | 15 | 3705 | 27.966 | 0.2578 | 2 | 38.70 |
| all/pooled | markov_w05_dist_pos | 15 | 3705 | 28.050 | 0.2706 | 2 | 39.57 |
| all/pooled | markov_w05_dist_int | 15 | 3705 | 29.224 | 0.2569 | 2 | 44.11 |
| all/pooled | markov_w05_dist_h0 | 15 | 3705 | 22.194 | 0.2656 | 2 | 61.79 |
| all/pooled | markov_w05_dist_pos_int | 15 | 3705 | 29.240 | 0.2604 | 2 | 45.96 |
| all/pooled | markov_w05_dist_pos_h0 | 15 | 3705 | 22.978 | 0.2723 | 2 | 58.80 |
| all/pooled | markov_w05_dist_int_h0 | 15 | 3705 | 23.829 | 0.2588 | 2 | 65.73 |
| all/pooled | markov_w05_dist_pos_int_h0 | 15 | 3705 | 24.007 | 0.2758 | 2 | 64.53 |
| humaneval/low | fixed_fast | 5 | 855 | 56.349 | 0.1658 | 0 | 70.18 |
| humaneval/low | fixed_g2 | 5 | 855 | 41.467 | 0.1808 | 0 | 61.55 |
| humaneval/low | picospec | 5 | 855 | 55.619 | 0.1681 | 0 | 73.34 |
| humaneval/low | markov_w0_dist | 5 | 855 | 52.186 | 0.1670 | 0 | 69.56 |
| humaneval/low | markov_w0_dist_pos | 5 | 855 | 57.919 | 0.1732 | 0 | 68.48 |
| humaneval/low | markov_w0_dist_int | 5 | 855 | 57.217 | 0.1686 | 0 | 76.58 |
| humaneval/low | markov_w0_dist_h0 | 5 | 855 | 55.410 | 0.1698 | 0 | 70.57 |
| humaneval/low | markov_w0_dist_pos_int | 5 | 855 | 63.619 | 0.1558 | 0 | 77.73 |
| humaneval/low | markov_w0_dist_pos_h0 | 5 | 855 | 58.896 | 0.1704 | 0 | 67.68 |
| humaneval/low | markov_w0_dist_int_h0 | 5 | 855 | 55.249 | 0.1584 | 0 | 75.97 |
| humaneval/low | markov_w0_dist_pos_int_h0 | 5 | 855 | 66.669 | 0.1596 | 0 | 76.88 |
| humaneval/low | markov_w05_dist | 5 | 855 | 50.702 | 0.1749 | 0 | 69.78 |
| humaneval/low | markov_w05_dist_pos | 5 | 855 | 57.974 | 0.1765 | 0 | 69.75 |
| humaneval/low | markov_w05_dist_int | 5 | 855 | 57.975 | 0.1721 | 0 | 75.78 |
| humaneval/low | markov_w05_dist_h0 | 5 | 855 | 42.748 | 0.1865 | 0 | 66.85 |
| humaneval/low | markov_w05_dist_pos_int | 5 | 855 | 59.330 | 0.1586 | 0 | 76.43 |
| humaneval/low | markov_w05_dist_pos_h0 | 5 | 855 | 52.420 | 0.1798 | 0 | 68.59 |
| humaneval/low | markov_w05_dist_int_h0 | 5 | 855 | 52.758 | 0.1712 | 0 | 75.65 |
| humaneval/low | markov_w05_dist_pos_int_h0 | 5 | 855 | 54.605 | 0.1689 | 0 | 77.55 |
| humaneval/pooled | fixed_fast | 5 | 855 | 56.349 | 0.1658 | 0 | 70.18 |
| humaneval/pooled | fixed_g2 | 5 | 855 | 41.467 | 0.1808 | 0 | 61.55 |
| humaneval/pooled | picospec | 5 | 855 | 55.619 | 0.1681 | 0 | 73.34 |
| humaneval/pooled | markov_w0_dist | 5 | 855 | 52.186 | 0.1670 | 0 | 69.56 |
| humaneval/pooled | markov_w0_dist_pos | 5 | 855 | 57.919 | 0.1732 | 0 | 68.48 |
| humaneval/pooled | markov_w0_dist_int | 5 | 855 | 57.217 | 0.1686 | 0 | 76.58 |
| humaneval/pooled | markov_w0_dist_h0 | 5 | 855 | 55.410 | 0.1698 | 0 | 70.57 |
| humaneval/pooled | markov_w0_dist_pos_int | 5 | 855 | 63.619 | 0.1558 | 0 | 77.73 |
| humaneval/pooled | markov_w0_dist_pos_h0 | 5 | 855 | 58.896 | 0.1704 | 0 | 67.68 |
| humaneval/pooled | markov_w0_dist_int_h0 | 5 | 855 | 55.249 | 0.1584 | 0 | 75.97 |
| humaneval/pooled | markov_w0_dist_pos_int_h0 | 5 | 855 | 66.669 | 0.1596 | 0 | 76.88 |
| humaneval/pooled | markov_w05_dist | 5 | 855 | 50.702 | 0.1749 | 0 | 69.78 |
| humaneval/pooled | markov_w05_dist_pos | 5 | 855 | 57.974 | 0.1765 | 0 | 69.75 |
| humaneval/pooled | markov_w05_dist_int | 5 | 855 | 57.975 | 0.1721 | 0 | 75.78 |
| humaneval/pooled | markov_w05_dist_h0 | 5 | 855 | 42.748 | 0.1865 | 0 | 66.85 |
| humaneval/pooled | markov_w05_dist_pos_int | 5 | 855 | 59.330 | 0.1586 | 0 | 76.43 |
| humaneval/pooled | markov_w05_dist_pos_h0 | 5 | 855 | 52.420 | 0.1798 | 0 | 68.59 |
| humaneval/pooled | markov_w05_dist_int_h0 | 5 | 855 | 52.758 | 0.1712 | 0 | 75.65 |
| humaneval/pooled | markov_w05_dist_pos_int_h0 | 5 | 855 | 54.605 | 0.1689 | 0 | 77.55 |
| gsm8k/low | fixed_fast | 5 | 1388 | 34.636 | 0.2584 | 1 | 38.60 |
| gsm8k/low | fixed_g2 | 5 | 1388 | 32.080 | 0.2274 | 1 | 43.56 |
| gsm8k/low | picospec | 5 | 1388 | 35.696 | 0.2600 | 1 | 45.96 |
| gsm8k/low | markov_w0_dist | 5 | 1388 | 31.493 | 0.2417 | 1 | 45.42 |
| gsm8k/low | markov_w0_dist_pos | 5 | 1388 | 32.575 | 0.2614 | 1 | 40.59 |
| gsm8k/low | markov_w0_dist_int | 5 | 1388 | 34.140 | 0.2642 | 1 | 53.49 |
| gsm8k/low | markov_w0_dist_h0 | 5 | 1388 | 29.328 | 0.2513 | 1 | 45.09 |
| gsm8k/low | markov_w0_dist_pos_int | 5 | 1388 | 35.629 | 0.2659 | 1 | 53.14 |
| gsm8k/low | markov_w0_dist_pos_h0 | 5 | 1388 | 30.542 | 0.2637 | 1 | 43.43 |
| gsm8k/low | markov_w0_dist_int_h0 | 5 | 1388 | 33.531 | 0.2538 | 1 | 52.33 |
| gsm8k/low | markov_w0_dist_pos_int_h0 | 5 | 1388 | 35.807 | 0.2824 | 1 | 50.81 |
| gsm8k/low | markov_w05_dist | 5 | 1388 | 29.676 | 0.2416 | 1 | 41.40 |
| gsm8k/low | markov_w05_dist_pos | 5 | 1388 | 30.914 | 0.2576 | 1 | 43.55 |
| gsm8k/low | markov_w05_dist_int | 5 | 1388 | 31.835 | 0.2391 | 1 | 50.68 |
| gsm8k/low | markov_w05_dist_h0 | 5 | 1388 | 21.923 | 0.2633 | 1 | 45.95 |
| gsm8k/low | markov_w05_dist_pos_int | 5 | 1388 | 32.342 | 0.2521 | 1 | 53.04 |
| gsm8k/low | markov_w05_dist_pos_h0 | 5 | 1388 | 23.116 | 0.2774 | 1 | 47.01 |
| gsm8k/low | markov_w05_dist_int_h0 | 5 | 1388 | 25.137 | 0.2504 | 1 | 56.04 |
| gsm8k/low | markov_w05_dist_pos_int_h0 | 5 | 1388 | 25.607 | 0.2838 | 1 | 54.07 |
| gsm8k/pooled | fixed_fast | 5 | 1388 | 34.636 | 0.2584 | 1 | 38.60 |
| gsm8k/pooled | fixed_g2 | 5 | 1388 | 32.080 | 0.2274 | 1 | 43.56 |
| gsm8k/pooled | picospec | 5 | 1388 | 35.696 | 0.2600 | 1 | 45.96 |
| gsm8k/pooled | markov_w0_dist | 5 | 1388 | 31.493 | 0.2417 | 1 | 45.42 |
| gsm8k/pooled | markov_w0_dist_pos | 5 | 1388 | 32.575 | 0.2614 | 1 | 40.59 |
| gsm8k/pooled | markov_w0_dist_int | 5 | 1388 | 34.140 | 0.2642 | 1 | 53.49 |
| gsm8k/pooled | markov_w0_dist_h0 | 5 | 1388 | 29.328 | 0.2513 | 1 | 45.09 |
| gsm8k/pooled | markov_w0_dist_pos_int | 5 | 1388 | 35.629 | 0.2659 | 1 | 53.14 |
| gsm8k/pooled | markov_w0_dist_pos_h0 | 5 | 1388 | 30.542 | 0.2637 | 1 | 43.43 |
| gsm8k/pooled | markov_w0_dist_int_h0 | 5 | 1388 | 33.531 | 0.2538 | 1 | 52.33 |
| gsm8k/pooled | markov_w0_dist_pos_int_h0 | 5 | 1388 | 35.807 | 0.2824 | 1 | 50.81 |
| gsm8k/pooled | markov_w05_dist | 5 | 1388 | 29.676 | 0.2416 | 1 | 41.40 |
| gsm8k/pooled | markov_w05_dist_pos | 5 | 1388 | 30.914 | 0.2576 | 1 | 43.55 |
| gsm8k/pooled | markov_w05_dist_int | 5 | 1388 | 31.835 | 0.2391 | 1 | 50.68 |
| gsm8k/pooled | markov_w05_dist_h0 | 5 | 1388 | 21.923 | 0.2633 | 1 | 45.95 |
| gsm8k/pooled | markov_w05_dist_pos_int | 5 | 1388 | 32.342 | 0.2521 | 1 | 53.04 |
| gsm8k/pooled | markov_w05_dist_pos_h0 | 5 | 1388 | 23.116 | 0.2774 | 1 | 47.01 |
| gsm8k/pooled | markov_w05_dist_int_h0 | 5 | 1388 | 25.137 | 0.2504 | 1 | 56.04 |
| gsm8k/pooled | markov_w05_dist_pos_int_h0 | 5 | 1388 | 25.607 | 0.2838 | 1 | 54.07 |
| mtbench/low | fixed_fast | 5 | 1415 | 19.222 | 0.4883 | 1 | 8.79 |
| mtbench/low | fixed_g2 | 5 | 1489 | 21.177 | 0.3464 | 1 | 15.73 |
| mtbench/low | picospec | 5 | 1415 | 20.586 | 0.4768 | 1 | 11.71 |
| mtbench/low | markov_w0_dist | 5 | 1489 | 20.204 | 0.3537 | 1 | 18.71 |
| mtbench/low | markov_w0_dist_pos | 5 | 1462 | 19.355 | 0.3654 | 1 | 18.87 |
| mtbench/low | markov_w0_dist_int | 5 | 1489 | 20.642 | 0.3653 | 1 | 23.40 |
| mtbench/low | markov_w0_dist_h0 | 5 | 1462 | 19.163 | 0.3482 | 1 | 19.47 |
| mtbench/low | markov_w0_dist_pos_int | 5 | 1462 | 19.744 | 0.3904 | 1 | 24.26 |
| mtbench/low | markov_w0_dist_pos_h0 | 5 | 1462 | 18.994 | 0.3595 | 1 | 18.61 |
| mtbench/low | markov_w0_dist_int_h0 | 5 | 1489 | 20.091 | 0.3716 | 1 | 25.29 |
| mtbench/low | markov_w0_dist_pos_int_h0 | 5 | 1489 | 20.193 | 0.3829 | 1 | 24.44 |
| mtbench/low | markov_w05_dist | 5 | 1462 | 21.236 | 0.3218 | 1 | 18.76 |
| mtbench/low | markov_w05_dist_pos | 5 | 1462 | 20.182 | 0.3380 | 1 | 18.10 |
| mtbench/low | markov_w05_dist_int | 5 | 1462 | 21.365 | 0.3235 | 1 | 20.97 |
| mtbench/low | markov_w05_dist_h0 | 5 | 1462 | 17.483 | 0.3141 | 1 | 37.78 |
| mtbench/low | markov_w05_dist_pos_int | 5 | 1462 | 21.072 | 0.3278 | 1 | 23.00 |
| mtbench/low | markov_w05_dist_pos_h0 | 5 | 1462 | 17.224 | 0.3216 | 1 | 20.43 |
| mtbench/low | markov_w05_dist_int_h0 | 5 | 1462 | 17.393 | 0.3181 | 1 | 36.36 |
| mtbench/low | markov_w05_dist_pos_int_h0 | 5 | 1462 | 17.309 | 0.3308 | 1 | 52.44 |
| mtbench/pooled | fixed_fast | 5 | 1415 | 19.222 | 0.4883 | 1 | 8.79 |
| mtbench/pooled | fixed_g2 | 5 | 1489 | 21.177 | 0.3464 | 1 | 15.73 |
| mtbench/pooled | picospec | 5 | 1415 | 20.586 | 0.4768 | 1 | 11.71 |
| mtbench/pooled | markov_w0_dist | 5 | 1489 | 20.204 | 0.3537 | 1 | 18.71 |
| mtbench/pooled | markov_w0_dist_pos | 5 | 1462 | 19.355 | 0.3654 | 1 | 18.87 |
| mtbench/pooled | markov_w0_dist_int | 5 | 1489 | 20.642 | 0.3653 | 1 | 23.40 |
| mtbench/pooled | markov_w0_dist_h0 | 5 | 1462 | 19.163 | 0.3482 | 1 | 19.47 |
| mtbench/pooled | markov_w0_dist_pos_int | 5 | 1462 | 19.744 | 0.3904 | 1 | 24.26 |
| mtbench/pooled | markov_w0_dist_pos_h0 | 5 | 1462 | 18.994 | 0.3595 | 1 | 18.61 |
| mtbench/pooled | markov_w0_dist_int_h0 | 5 | 1489 | 20.091 | 0.3716 | 1 | 25.29 |
| mtbench/pooled | markov_w0_dist_pos_int_h0 | 5 | 1489 | 20.193 | 0.3829 | 1 | 24.44 |
| mtbench/pooled | markov_w05_dist | 5 | 1462 | 21.236 | 0.3218 | 1 | 18.76 |
| mtbench/pooled | markov_w05_dist_pos | 5 | 1462 | 20.182 | 0.3380 | 1 | 18.10 |
| mtbench/pooled | markov_w05_dist_int | 5 | 1462 | 21.365 | 0.3235 | 1 | 20.97 |
| mtbench/pooled | markov_w05_dist_h0 | 5 | 1462 | 17.483 | 0.3141 | 1 | 37.78 |
| mtbench/pooled | markov_w05_dist_pos_int | 5 | 1462 | 21.072 | 0.3278 | 1 | 23.00 |
| mtbench/pooled | markov_w05_dist_pos_h0 | 5 | 1462 | 17.224 | 0.3216 | 1 | 20.43 |
| mtbench/pooled | markov_w05_dist_int_h0 | 5 | 1462 | 17.393 | 0.3181 | 1 | 36.36 |
| mtbench/pooled | markov_w05_dist_pos_int_h0 | 5 | 1462 | 17.309 | 0.3308 | 1 | 52.44 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | fixed_fast_vs_fixed_g2 | 15 | 2.08 [-4.55, 11.83] | -23.28 [-33.52, -10.28] | 4 | 0 |
| all/low | picospec_vs_fixed_g2 | 15 | 6.95 [1.28, 15.26] | -22.03 [-30.97, -10.35] | 4 | 0 |
| all/low | markov_w0_dist_vs_fixed_g2 | 15 | 0.03 [-3.80, 5.76] | -1.93 [-5.54, 2.01] | 0 | 0 |
| all/low | markov_w0_dist_pos_vs_fixed_g2 | 15 | 0.24 [-5.88, 9.99] | -6.77 [-12.86, -0.02] | 1 | 0 |
| all/low | markov_w0_dist_int_vs_fixed_g2 | 15 | 5.06 [0.54, 13.09] | -6.98 [-12.51, -1.38] | 1 | 0 |
| all/low | markov_w0_dist_h0_vs_fixed_g2 | 15 | -4.19 [-8.93, 3.60] | -2.47 [-6.89, 1.87] | 1 | 0 |
| all/low | markov_w0_dist_pos_int_vs_fixed_g2 | 15 | 5.36 [-2.10, 16.96] | -9.62 [-15.70, -1.14] | 1 | 0 |
| all/low | markov_w0_dist_pos_h0_vs_fixed_g2 | 15 | -2.71 [-8.48, 6.76] | -5.97 [-11.64, -0.17] | 1 | 0 |
| all/low | markov_w0_dist_int_h0_vs_fixed_g2 | 15 | 2.45 [-2.76, 10.54] | -5.59 [-9.01, -0.27] | 1 | 0 |
| all/low | markov_w0_dist_pos_int_h0_vs_fixed_g2 | 15 | 7.08 [-0.23, 19.59] | -11.42 [-18.19, -2.90] | 0 | 0 |
| all/low | markov_w05_dist_vs_fixed_g2 | 15 | 0.56 [-3.54, 6.16] | 2.40 [-2.23, 6.55] | 2 | 0 |
| all/low | markov_w05_dist_pos_vs_fixed_g2 | 15 | 0.86 [-4.40, 9.19] | -2.44 [-9.83, 3.87] | 2 | 0 |
| all/low | markov_w05_dist_int_vs_fixed_g2 | 15 | 5.09 [0.54, 12.84] | 2.74 [-1.38, 6.72] | 1 | 0 |
| all/low | markov_w05_dist_h0_vs_fixed_g2 | 15 | -20.19 [-25.69, -13.56] | -0.53 [-9.28, 6.33] | 1 | 0 |
| all/low | markov_w05_dist_pos_int_vs_fixed_g2 | 15 | 5.14 [-0.13, 13.52] | 1.44 [-3.85, 6.76] | 1 | 0 |
| all/low | markov_w05_dist_pos_h0_vs_fixed_g2 | 15 | -17.37 [-22.79, -8.94] | -3.07 [-13.30, 5.18] | 2 | 0 |
| all/low | markov_w05_dist_int_h0_vs_fixed_g2 | 15 | -14.31 [-20.06, -6.24] | 2.03 [-4.69, 7.72] | 1 | 0 |
| all/low | markov_w05_dist_pos_int_h0_vs_fixed_g2 | 15 | -13.67 [-20.36, -3.65] | -4.40 [-15.01, 4.69] | 2 | 0 |
| all/low | fixed_fast_vs_markov_w0_dist | 15 | 2.05 [-3.62, 8.83] | -20.95 [-32.70, -7.54] | 4 | 0 |
| all/low | fixed_g2_vs_markov_w0_dist | 15 | -0.03 [-5.44, 3.95] | 1.89 [-2.05, 5.25] | 0 | 0 |
| all/low | picospec_vs_markov_w0_dist | 15 | 6.91 [2.27, 11.93] | -19.72 [-29.96, -7.81] | 4 | 0 |
| all/low | markov_w0_dist_pos_vs_markov_w0_dist | 15 | 0.21 [-3.91, 4.98] | -4.75 [-9.25, -0.20] | 1 | 0 |
| all/low | markov_w0_dist_int_vs_markov_w0_dist | 15 | 5.03 [1.89, 9.45] | -4.96 [-10.09, 0.00] | 1 | 0 |
| all/low | markov_w0_dist_h0_vs_markov_w0_dist | 15 | -4.22 [-6.88, -0.71] | -0.53 [-3.20, 2.10] | 1 | 0 |
| all/low | markov_w0_dist_pos_int_vs_markov_w0_dist | 15 | 5.33 [-0.70, 13.48] | -7.55 [-13.16, -0.21] | 1 | 0 |
| all/low | markov_w0_dist_pos_h0_vs_markov_w0_dist | 15 | -2.74 [-6.23, 2.20] | -3.96 [-8.08, -0.32] | 1 | 0 |
| all/low | markov_w0_dist_int_h0_vs_markov_w0_dist | 15 | 2.42 [-1.98, 7.53] | -3.59 [-7.12, 1.17] | 1 | 0 |
| all/low | markov_w0_dist_pos_int_h0_vs_markov_w0_dist | 15 | 7.05 [1.32, 15.13] | -9.32 [-14.33, -2.77] | 0 | 0 |
| all/low | markov_w05_dist_vs_markov_w0_dist | 15 | 0.53 [-3.63, 4.11] | 4.25 [0.44, 7.38] | 2 | 0 |
| all/low | markov_w05_dist_pos_vs_markov_w0_dist | 15 | 0.83 [-2.44, 5.00] | -0.50 [-6.92, 4.19] | 2 | 0 |
| all/low | markov_w05_dist_int_vs_markov_w0_dist | 15 | 5.05 [2.03, 8.97] | 4.58 [1.31, 7.79] | 1 | 0 |
| all/low | markov_w05_dist_h0_vs_markov_w0_dist | 15 | -20.22 [-26.07, -14.86] | 1.37 [-6.21, 7.04] | 1 | 0 |
| all/low | markov_w05_dist_pos_int_vs_markov_w0_dist | 15 | 5.11 [1.59, 9.42] | 3.30 [-0.97, 7.40] | 1 | 0 |
| all/low | markov_w05_dist_pos_h0_vs_markov_w0_dist | 15 | -17.40 [-21.69, -12.36] | -1.12 [-10.16, 5.49] | 2 | 0 |
| all/low | markov_w05_dist_int_h0_vs_markov_w0_dist | 15 | -14.34 [-18.79, -9.93] | 3.88 [-1.50, 7.86] | 1 | 0 |
| all/low | markov_w05_dist_pos_int_h0_vs_markov_w0_dist | 15 | -13.70 [-18.71, -7.19] | -2.42 [-11.99, 4.54] | 2 | 0 |
| all/low | fixed_fast_vs_markov_w05_dist | 15 | 1.51 [-6.06, 11.83] | -26.31 [-41.25, -8.95] | 3 | 0 |
| all/low | fixed_g2_vs_markov_w05_dist | 15 | -0.56 [-5.80, 3.67] | -2.46 [-7.01, 2.18] | 2 | 0 |
| all/low | picospec_vs_markov_w05_dist | 15 | 6.35 [-0.53, 15.13] | -25.03 [-38.38, -8.99] | 3 | 0 |
| all/low | markov_w0_dist_vs_markov_w05_dist | 15 | -0.53 [-3.95, 3.76] | -4.43 [-7.96, -0.44] | 2 | 0 |
| all/low | markov_w0_dist_pos_vs_markov_w05_dist | 15 | -0.32 [-6.28, 7.57] | -9.40 [-13.00, -4.65] | 1 | 0 |
| all/low | markov_w0_dist_int_vs_markov_w05_dist | 15 | 4.47 [-0.76, 11.64] | -9.61 [-13.55, -4.14] | 2 | 0 |
| all/low | markov_w0_dist_h0_vs_markov_w05_dist | 15 | -4.72 [-8.06, 0.02] | -4.99 [-7.34, -2.29] | 1 | 0 |
| all/low | markov_w0_dist_pos_int_vs_markov_w05_dist | 15 | 4.78 [-3.49, 16.57] | -12.32 [-18.72, -3.96] | 1 | 0 |
| all/low | markov_w0_dist_pos_h0_vs_markov_w05_dist | 15 | -3.25 [-8.13, 3.95] | -8.57 [-11.26, -4.71] | 1 | 0 |
| all/low | markov_w0_dist_int_h0_vs_markov_w05_dist | 15 | 1.88 [-4.07, 9.64] | -8.18 [-12.91, -2.11] | 1 | 0 |
| all/low | markov_w0_dist_pos_int_h0_vs_markov_w05_dist | 15 | 6.48 [-1.21, 18.50] | -14.16 [-19.28, -6.85] | 2 | 0 |
| all/low | markov_w05_dist_pos_vs_markov_w05_dist | 15 | 0.30 [-3.50, 4.89] | -4.96 [-8.74, -1.62] | 1 | 0 |
| all/low | markov_w05_dist_int_vs_markov_w05_dist | 15 | 4.50 [0.96, 8.73] | 0.35 [-1.34, 1.80] | 1 | 0 |
| all/low | markov_w05_dist_h0_vs_markov_w05_dist | 15 | -20.64 [-23.76, -17.74] | -3.01 [-7.34, 0.27] | 1 | 0 |
| all/low | markov_w05_dist_pos_int_vs_markov_w05_dist | 15 | 4.56 [0.10, 10.35] | -0.99 [-3.27, 2.04] | 1 | 0 |
| all/low | markov_w05_dist_pos_h0_vs_markov_w05_dist | 15 | -17.83 [-20.27, -13.95] | -5.60 [-11.71, -0.90] | 0 | 0 |
| all/low | markov_w05_dist_int_h0_vs_markov_w05_dist | 15 | -14.79 [-18.70, -10.07] | -0.38 [-4.16, 2.25] | 1 | 0 |
| all/low | markov_w05_dist_pos_int_h0_vs_markov_w05_dist | 15 | -14.16 [-19.27, -6.33] | -6.97 [-13.94, -1.34] | 1 | 0 |
| all/pooled | fixed_fast_vs_fixed_g2 | 15 | 2.08 [-4.55, 11.83] | -23.28 [-33.52, -10.28] | 4 | 0 |
| all/pooled | picospec_vs_fixed_g2 | 15 | 6.95 [1.28, 15.26] | -22.03 [-30.97, -10.35] | 4 | 0 |
| all/pooled | markov_w0_dist_vs_fixed_g2 | 15 | 0.03 [-3.80, 5.76] | -1.93 [-5.54, 2.01] | 0 | 0 |
| all/pooled | markov_w0_dist_pos_vs_fixed_g2 | 15 | 0.24 [-5.88, 9.99] | -6.77 [-12.86, -0.02] | 1 | 0 |
| all/pooled | markov_w0_dist_int_vs_fixed_g2 | 15 | 5.06 [0.54, 13.09] | -6.98 [-12.51, -1.38] | 1 | 0 |
| all/pooled | markov_w0_dist_h0_vs_fixed_g2 | 15 | -4.19 [-8.93, 3.60] | -2.47 [-6.89, 1.87] | 1 | 0 |
| all/pooled | markov_w0_dist_pos_int_vs_fixed_g2 | 15 | 5.36 [-2.10, 16.96] | -9.62 [-15.70, -1.14] | 1 | 0 |
| all/pooled | markov_w0_dist_pos_h0_vs_fixed_g2 | 15 | -2.71 [-8.48, 6.76] | -5.97 [-11.64, -0.17] | 1 | 0 |
| all/pooled | markov_w0_dist_int_h0_vs_fixed_g2 | 15 | 2.45 [-2.76, 10.54] | -5.59 [-9.01, -0.27] | 1 | 0 |
| all/pooled | markov_w0_dist_pos_int_h0_vs_fixed_g2 | 15 | 7.08 [-0.23, 19.59] | -11.42 [-18.19, -2.90] | 0 | 0 |
| all/pooled | markov_w05_dist_vs_fixed_g2 | 15 | 0.56 [-3.54, 6.16] | 2.40 [-2.23, 6.55] | 2 | 0 |
| all/pooled | markov_w05_dist_pos_vs_fixed_g2 | 15 | 0.86 [-4.40, 9.19] | -2.44 [-9.83, 3.87] | 2 | 0 |
| all/pooled | markov_w05_dist_int_vs_fixed_g2 | 15 | 5.09 [0.54, 12.84] | 2.74 [-1.38, 6.72] | 1 | 0 |
| all/pooled | markov_w05_dist_h0_vs_fixed_g2 | 15 | -20.19 [-25.69, -13.56] | -0.53 [-9.28, 6.33] | 1 | 0 |
| all/pooled | markov_w05_dist_pos_int_vs_fixed_g2 | 15 | 5.14 [-0.13, 13.52] | 1.44 [-3.85, 6.76] | 1 | 0 |
| all/pooled | markov_w05_dist_pos_h0_vs_fixed_g2 | 15 | -17.37 [-22.79, -8.94] | -3.07 [-13.30, 5.18] | 2 | 0 |
| all/pooled | markov_w05_dist_int_h0_vs_fixed_g2 | 15 | -14.31 [-20.06, -6.24] | 2.03 [-4.69, 7.72] | 1 | 0 |
| all/pooled | markov_w05_dist_pos_int_h0_vs_fixed_g2 | 15 | -13.67 [-20.36, -3.65] | -4.40 [-15.01, 4.69] | 2 | 0 |
| all/pooled | fixed_fast_vs_markov_w0_dist | 15 | 2.05 [-3.62, 8.83] | -20.95 [-32.70, -7.54] | 4 | 0 |
| all/pooled | fixed_g2_vs_markov_w0_dist | 15 | -0.03 [-5.44, 3.95] | 1.89 [-2.05, 5.25] | 0 | 0 |
| all/pooled | picospec_vs_markov_w0_dist | 15 | 6.91 [2.27, 11.93] | -19.72 [-29.96, -7.81] | 4 | 0 |
| all/pooled | markov_w0_dist_pos_vs_markov_w0_dist | 15 | 0.21 [-3.91, 4.98] | -4.75 [-9.25, -0.20] | 1 | 0 |
| all/pooled | markov_w0_dist_int_vs_markov_w0_dist | 15 | 5.03 [1.89, 9.45] | -4.96 [-10.09, 0.00] | 1 | 0 |
| all/pooled | markov_w0_dist_h0_vs_markov_w0_dist | 15 | -4.22 [-6.88, -0.71] | -0.53 [-3.20, 2.10] | 1 | 0 |
| all/pooled | markov_w0_dist_pos_int_vs_markov_w0_dist | 15 | 5.33 [-0.70, 13.48] | -7.55 [-13.16, -0.21] | 1 | 0 |
| all/pooled | markov_w0_dist_pos_h0_vs_markov_w0_dist | 15 | -2.74 [-6.23, 2.20] | -3.96 [-8.08, -0.32] | 1 | 0 |
| all/pooled | markov_w0_dist_int_h0_vs_markov_w0_dist | 15 | 2.42 [-1.98, 7.53] | -3.59 [-7.12, 1.17] | 1 | 0 |
| all/pooled | markov_w0_dist_pos_int_h0_vs_markov_w0_dist | 15 | 7.05 [1.32, 15.13] | -9.32 [-14.33, -2.77] | 0 | 0 |
| all/pooled | markov_w05_dist_vs_markov_w0_dist | 15 | 0.53 [-3.63, 4.11] | 4.25 [0.44, 7.38] | 2 | 0 |
| all/pooled | markov_w05_dist_pos_vs_markov_w0_dist | 15 | 0.83 [-2.44, 5.00] | -0.50 [-6.92, 4.19] | 2 | 0 |
| all/pooled | markov_w05_dist_int_vs_markov_w0_dist | 15 | 5.05 [2.03, 8.97] | 4.58 [1.31, 7.79] | 1 | 0 |
| all/pooled | markov_w05_dist_h0_vs_markov_w0_dist | 15 | -20.22 [-26.07, -14.86] | 1.37 [-6.21, 7.04] | 1 | 0 |
| all/pooled | markov_w05_dist_pos_int_vs_markov_w0_dist | 15 | 5.11 [1.59, 9.42] | 3.30 [-0.97, 7.40] | 1 | 0 |
| all/pooled | markov_w05_dist_pos_h0_vs_markov_w0_dist | 15 | -17.40 [-21.69, -12.36] | -1.12 [-10.16, 5.49] | 2 | 0 |
| all/pooled | markov_w05_dist_int_h0_vs_markov_w0_dist | 15 | -14.34 [-18.79, -9.93] | 3.88 [-1.50, 7.86] | 1 | 0 |
| all/pooled | markov_w05_dist_pos_int_h0_vs_markov_w0_dist | 15 | -13.70 [-18.71, -7.19] | -2.42 [-11.99, 4.54] | 2 | 0 |
| all/pooled | fixed_fast_vs_markov_w05_dist | 15 | 1.51 [-6.06, 11.83] | -26.31 [-41.25, -8.95] | 3 | 0 |
| all/pooled | fixed_g2_vs_markov_w05_dist | 15 | -0.56 [-5.80, 3.67] | -2.46 [-7.01, 2.18] | 2 | 0 |
| all/pooled | picospec_vs_markov_w05_dist | 15 | 6.35 [-0.53, 15.13] | -25.03 [-38.38, -8.99] | 3 | 0 |
| all/pooled | markov_w0_dist_vs_markov_w05_dist | 15 | -0.53 [-3.95, 3.76] | -4.43 [-7.96, -0.44] | 2 | 0 |
| all/pooled | markov_w0_dist_pos_vs_markov_w05_dist | 15 | -0.32 [-6.28, 7.57] | -9.40 [-13.00, -4.65] | 1 | 0 |
| all/pooled | markov_w0_dist_int_vs_markov_w05_dist | 15 | 4.47 [-0.76, 11.64] | -9.61 [-13.55, -4.14] | 2 | 0 |
| all/pooled | markov_w0_dist_h0_vs_markov_w05_dist | 15 | -4.72 [-8.06, 0.02] | -4.99 [-7.34, -2.29] | 1 | 0 |
| all/pooled | markov_w0_dist_pos_int_vs_markov_w05_dist | 15 | 4.78 [-3.49, 16.57] | -12.32 [-18.72, -3.96] | 1 | 0 |
| all/pooled | markov_w0_dist_pos_h0_vs_markov_w05_dist | 15 | -3.25 [-8.13, 3.95] | -8.57 [-11.26, -4.71] | 1 | 0 |
| all/pooled | markov_w0_dist_int_h0_vs_markov_w05_dist | 15 | 1.88 [-4.07, 9.64] | -8.18 [-12.91, -2.11] | 1 | 0 |
| all/pooled | markov_w0_dist_pos_int_h0_vs_markov_w05_dist | 15 | 6.48 [-1.21, 18.50] | -14.16 [-19.28, -6.85] | 2 | 0 |
| all/pooled | markov_w05_dist_pos_vs_markov_w05_dist | 15 | 0.30 [-3.50, 4.89] | -4.96 [-8.74, -1.62] | 1 | 0 |
| all/pooled | markov_w05_dist_int_vs_markov_w05_dist | 15 | 4.50 [0.96, 8.73] | 0.35 [-1.34, 1.80] | 1 | 0 |
| all/pooled | markov_w05_dist_h0_vs_markov_w05_dist | 15 | -20.64 [-23.76, -17.74] | -3.01 [-7.34, 0.27] | 1 | 0 |
| all/pooled | markov_w05_dist_pos_int_vs_markov_w05_dist | 15 | 4.56 [0.10, 10.35] | -0.99 [-3.27, 2.04] | 1 | 0 |
| all/pooled | markov_w05_dist_pos_h0_vs_markov_w05_dist | 15 | -17.83 [-20.27, -13.95] | -5.60 [-11.71, -0.90] | 0 | 0 |
| all/pooled | markov_w05_dist_int_h0_vs_markov_w05_dist | 15 | -14.79 [-18.70, -10.07] | -0.38 [-4.16, 2.25] | 1 | 0 |
| all/pooled | markov_w05_dist_pos_int_h0_vs_markov_w05_dist | 15 | -14.16 [-19.27, -6.33] | -6.97 [-13.94, -1.34] | 1 | 0 |
| humaneval/low | fixed_fast_vs_fixed_g2 | 5 | 35.89 [30.30, 40.22] | 8.29 [3.22, 13.19] | 0 | 0 |
| humaneval/low | picospec_vs_fixed_g2 | 5 | 34.13 [24.43, 45.58] | 7.04 [0.83, 12.08] | 0 | 0 |
| humaneval/low | markov_w0_dist_vs_fixed_g2 | 5 | 25.85 [15.51, 37.57] | 7.66 [-0.10, 14.75] | 0 | 0 |
| humaneval/low | markov_w0_dist_pos_vs_fixed_g2 | 5 | 39.67 [25.00, 56.41] | 4.22 [-8.39, 14.45] | 0 | 0 |
| humaneval/low | markov_w0_dist_int_vs_fixed_g2 | 5 | 37.98 [24.24, 53.40] | 6.78 [-1.55, 14.40] | 0 | 0 |
| humaneval/low | markov_w0_dist_h0_vs_fixed_g2 | 5 | 33.62 [20.76, 46.02] | 6.09 [-2.80, 15.46] | 0 | 0 |
| humaneval/low | markov_w0_dist_pos_int_vs_fixed_g2 | 5 | 53.42 [42.37, 63.73] | 13.84 [4.66, 21.29] | 0 | 0 |
| humaneval/low | markov_w0_dist_pos_h0_vs_fixed_g2 | 5 | 42.03 [29.09, 56.85] | 5.78 [-4.82, 14.37] | 0 | 0 |
| humaneval/low | markov_w0_dist_int_h0_vs_fixed_g2 | 5 | 33.23 [27.44, 38.15] | 12.39 [6.67, 16.70] | 0 | 0 |
| humaneval/low | markov_w0_dist_pos_int_h0_vs_fixed_g2 | 5 | 60.77 [43.62, 77.93] | 11.70 [3.49, 20.26] | 0 | 0 |
| humaneval/low | markov_w05_dist_vs_fixed_g2 | 5 | 22.27 [13.56, 30.08] | 3.27 [-2.09, 8.61] | 0 | 0 |
| humaneval/low | markov_w05_dist_pos_vs_fixed_g2 | 5 | 39.80 [20.46, 61.08] | 2.37 [-8.20, 12.35] | 0 | 0 |
| humaneval/low | markov_w05_dist_int_vs_fixed_g2 | 5 | 39.81 [27.03, 49.88] | 4.83 [-1.17, 10.47] | 0 | 0 |
| humaneval/low | markov_w05_dist_h0_vs_fixed_g2 | 5 | 3.09 [-7.52, 12.51] | -3.12 [-10.34, 3.48] | 0 | 0 |
| humaneval/low | markov_w05_dist_pos_int_vs_fixed_g2 | 5 | 43.08 [30.63, 57.03] | 12.27 [3.06, 20.74] | 0 | 0 |
| humaneval/low | markov_w05_dist_pos_h0_vs_fixed_g2 | 5 | 26.41 [9.60, 49.47] | 0.56 [-9.76, 10.86] | 0 | 0 |
| humaneval/low | markov_w05_dist_int_h0_vs_fixed_g2 | 5 | 27.23 [9.15, 42.41] | 5.32 [-1.54, 11.72] | 0 | 0 |
| humaneval/low | markov_w05_dist_pos_int_h0_vs_fixed_g2 | 5 | 31.68 [17.58, 43.63] | 6.61 [-3.80, 16.14] | 0 | 0 |
| humaneval/low | fixed_fast_vs_markov_w0_dist | 5 | 7.98 [1.03, 14.00] | 0.69 [-3.48, 4.96] | 0 | 0 |
| humaneval/low | fixed_g2_vs_markov_w0_dist | 5 | -20.54 [-27.31, -13.43] | -8.29 [-17.30, 0.10] | 0 | 0 |
| humaneval/low | picospec_vs_markov_w0_dist | 5 | 6.58 [2.58, 11.00] | -0.66 [-5.54, 5.04] | 0 | 0 |
| humaneval/low | markov_w0_dist_pos_vs_markov_w0_dist | 5 | 10.99 [1.92, 20.38] | -3.72 [-9.89, 2.97] | 0 | 0 |
| humaneval/low | markov_w0_dist_int_vs_markov_w0_dist | 5 | 9.64 [6.35, 15.13] | -0.95 [-2.52, 0.98] | 0 | 0 |
| humaneval/low | markov_w0_dist_h0_vs_markov_w0_dist | 5 | 6.18 [-4.67, 18.47] | -1.70 [-6.47, 5.30] | 0 | 0 |
| humaneval/low | markov_w0_dist_pos_int_vs_markov_w0_dist | 5 | 21.91 [14.11, 31.99] | 6.70 [2.49, 12.17] | 0 | 0 |
| humaneval/low | markov_w0_dist_pos_h0_vs_markov_w0_dist | 5 | 12.86 [7.87, 19.19] | -2.03 [-7.26, 3.94] | 0 | 0 |
| humaneval/low | markov_w0_dist_int_h0_vs_markov_w0_dist | 5 | 5.87 [-1.58, 13.04] | 5.13 [1.55, 10.27] | 0 | 0 |
| humaneval/low | markov_w0_dist_pos_int_h0_vs_markov_w0_dist | 5 | 27.75 [14.90, 37.59] | 4.38 [1.36, 8.58] | 0 | 0 |
| humaneval/low | markov_w05_dist_vs_markov_w0_dist | 5 | -2.84 [-9.16, 2.37] | -4.75 [-9.65, -0.08] | 0 | 0 |
| humaneval/low | markov_w05_dist_pos_vs_markov_w0_dist | 5 | 11.09 [-1.14, 24.12] | -5.73 [-9.61, -1.04] | 0 | 0 |
| humaneval/low | markov_w05_dist_int_vs_markov_w0_dist | 5 | 11.09 [4.01, 16.85] | -3.06 [-5.74, -0.50] | 0 | 0 |
| humaneval/low | markov_w05_dist_h0_vs_markov_w0_dist | 5 | -18.09 [-30.47, -5.20] | -11.67 [-15.75, -8.70] | 0 | 0 |
| humaneval/low | markov_w05_dist_pos_int_vs_markov_w0_dist | 5 | 13.69 [4.31, 22.13] | 4.99 [0.44, 11.35] | 0 | 0 |
| humaneval/low | markov_w05_dist_pos_h0_vs_markov_w0_dist | 5 | 0.45 [-12.35, 15.50] | -7.68 [-11.20, -2.71] | 0 | 0 |
| humaneval/low | markov_w05_dist_int_h0_vs_markov_w0_dist | 5 | 1.10 [-9.29, 9.68] | -2.52 [-4.97, -0.13] | 0 | 0 |
| humaneval/low | markov_w05_dist_pos_int_h0_vs_markov_w0_dist | 5 | 4.64 [-4.60, 13.72] | -1.13 [-3.70, 1.63] | 0 | 0 |
| humaneval/low | fixed_fast_vs_markov_w05_dist | 5 | 11.14 [7.34, 15.71] | 5.19 [0.80, 8.67] | 0 | 0 |
| humaneval/low | fixed_g2_vs_markov_w05_dist | 5 | -18.21 [-23.12, -11.94] | -3.38 [-9.42, 2.05] | 0 | 0 |
| humaneval/low | picospec_vs_markov_w05_dist | 5 | 9.70 [3.65, 19.03] | 3.90 [0.40, 7.71] | 0 | 0 |
| humaneval/low | markov_w0_dist_vs_markov_w05_dist | 5 | 2.93 [-2.32, 10.08] | 4.53 [0.08, 8.80] | 0 | 0 |
| humaneval/low | markov_w0_dist_pos_vs_markov_w05_dist | 5 | 14.24 [5.40, 27.40] | 0.98 [-6.06, 8.23] | 0 | 0 |
| humaneval/low | markov_w0_dist_int_vs_markov_w05_dist | 5 | 12.85 [6.23, 20.06] | 3.63 [0.27, 7.05] | 0 | 0 |
| humaneval/low | markov_w0_dist_h0_vs_markov_w05_dist | 5 | 9.29 [1.62, 19.23] | 2.91 [-1.91, 9.31] | 0 | 0 |
| humaneval/low | markov_w0_dist_pos_int_vs_markov_w05_dist | 5 | 25.48 [16.82, 38.15] | 10.93 [6.40, 15.09] | 0 | 0 |
| humaneval/low | markov_w0_dist_pos_h0_vs_markov_w05_dist | 5 | 16.16 [10.89, 22.19] | 2.59 [-2.65, 7.31] | 0 | 0 |
| humaneval/low | markov_w0_dist_int_h0_vs_markov_w05_dist | 5 | 8.97 [6.20, 12.22] | 9.43 [7.69, 11.57] | 0 | 0 |
| humaneval/low | markov_w0_dist_pos_int_h0_vs_markov_w05_dist | 5 | 31.49 [23.70, 37.54] | 8.72 [5.08, 14.02] | 0 | 0 |
| humaneval/low | markov_w05_dist_pos_vs_markov_w05_dist | 5 | 14.34 [6.00, 24.64] | -0.93 [-6.27, 4.37] | 0 | 0 |
| humaneval/low | markov_w05_dist_int_vs_markov_w05_dist | 5 | 14.35 [8.45, 23.59] | 1.61 [-2.12, 4.98] | 0 | 0 |
| humaneval/low | markov_w05_dist_h0_vs_markov_w05_dist | 5 | -15.69 [-25.10, -7.02] | -6.61 [-9.86, -4.60] | 0 | 0 |
| humaneval/low | markov_w05_dist_pos_int_vs_markov_w05_dist | 5 | 17.02 [12.60, 22.96] | 9.30 [4.70, 13.48] | 0 | 0 |
| humaneval/low | markov_w05_dist_pos_h0_vs_markov_w05_dist | 5 | 3.39 [-4.57, 15.82] | -2.80 [-7.80, 2.26] | 0 | 0 |
| humaneval/low | markov_w05_dist_int_h0_vs_markov_w05_dist | 5 | 4.06 [-3.96, 9.48] | 2.12 [-3.23, 6.33] | 0 | 0 |
| humaneval/low | markov_w05_dist_pos_int_h0_vs_markov_w05_dist | 5 | 7.70 [2.00, 12.73] | 3.45 [-3.02, 9.14] | 0 | 0 |
| humaneval/pooled | fixed_fast_vs_fixed_g2 | 5 | 35.89 [30.30, 40.22] | 8.29 [3.22, 13.19] | 0 | 0 |
| humaneval/pooled | picospec_vs_fixed_g2 | 5 | 34.13 [24.43, 45.58] | 7.04 [0.83, 12.08] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_vs_fixed_g2 | 5 | 25.85 [15.51, 37.57] | 7.66 [-0.10, 14.75] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_pos_vs_fixed_g2 | 5 | 39.67 [25.00, 56.41] | 4.22 [-8.39, 14.45] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_fixed_g2 | 5 | 37.98 [24.24, 53.40] | 6.78 [-1.55, 14.40] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_h0_vs_fixed_g2 | 5 | 33.62 [20.76, 46.02] | 6.09 [-2.80, 15.46] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_pos_int_vs_fixed_g2 | 5 | 53.42 [42.37, 63.73] | 13.84 [4.66, 21.29] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_pos_h0_vs_fixed_g2 | 5 | 42.03 [29.09, 56.85] | 5.78 [-4.82, 14.37] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_int_h0_vs_fixed_g2 | 5 | 33.23 [27.44, 38.15] | 12.39 [6.67, 16.70] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_pos_int_h0_vs_fixed_g2 | 5 | 60.77 [43.62, 77.93] | 11.70 [3.49, 20.26] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_vs_fixed_g2 | 5 | 22.27 [13.56, 30.08] | 3.27 [-2.09, 8.61] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_pos_vs_fixed_g2 | 5 | 39.80 [20.46, 61.08] | 2.37 [-8.20, 12.35] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_fixed_g2 | 5 | 39.81 [27.03, 49.88] | 4.83 [-1.17, 10.47] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_h0_vs_fixed_g2 | 5 | 3.09 [-7.52, 12.51] | -3.12 [-10.34, 3.48] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_pos_int_vs_fixed_g2 | 5 | 43.08 [30.63, 57.03] | 12.27 [3.06, 20.74] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_pos_h0_vs_fixed_g2 | 5 | 26.41 [9.60, 49.47] | 0.56 [-9.76, 10.86] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_int_h0_vs_fixed_g2 | 5 | 27.23 [9.15, 42.41] | 5.32 [-1.54, 11.72] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_pos_int_h0_vs_fixed_g2 | 5 | 31.68 [17.58, 43.63] | 6.61 [-3.80, 16.14] | 0 | 0 |
| humaneval/pooled | fixed_fast_vs_markov_w0_dist | 5 | 7.98 [1.03, 14.00] | 0.69 [-3.48, 4.96] | 0 | 0 |
| humaneval/pooled | fixed_g2_vs_markov_w0_dist | 5 | -20.54 [-27.31, -13.43] | -8.29 [-17.30, 0.10] | 0 | 0 |
| humaneval/pooled | picospec_vs_markov_w0_dist | 5 | 6.58 [2.58, 11.00] | -0.66 [-5.54, 5.04] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_pos_vs_markov_w0_dist | 5 | 10.99 [1.92, 20.38] | -3.72 [-9.89, 2.97] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_markov_w0_dist | 5 | 9.64 [6.35, 15.13] | -0.95 [-2.52, 0.98] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_h0_vs_markov_w0_dist | 5 | 6.18 [-4.67, 18.47] | -1.70 [-6.47, 5.30] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_pos_int_vs_markov_w0_dist | 5 | 21.91 [14.11, 31.99] | 6.70 [2.49, 12.17] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_pos_h0_vs_markov_w0_dist | 5 | 12.86 [7.87, 19.19] | -2.03 [-7.26, 3.94] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_int_h0_vs_markov_w0_dist | 5 | 5.87 [-1.58, 13.04] | 5.13 [1.55, 10.27] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_pos_int_h0_vs_markov_w0_dist | 5 | 27.75 [14.90, 37.59] | 4.38 [1.36, 8.58] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_vs_markov_w0_dist | 5 | -2.84 [-9.16, 2.37] | -4.75 [-9.65, -0.08] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_pos_vs_markov_w0_dist | 5 | 11.09 [-1.14, 24.12] | -5.73 [-9.61, -1.04] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_markov_w0_dist | 5 | 11.09 [4.01, 16.85] | -3.06 [-5.74, -0.50] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_h0_vs_markov_w0_dist | 5 | -18.09 [-30.47, -5.20] | -11.67 [-15.75, -8.70] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_pos_int_vs_markov_w0_dist | 5 | 13.69 [4.31, 22.13] | 4.99 [0.44, 11.35] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_pos_h0_vs_markov_w0_dist | 5 | 0.45 [-12.35, 15.50] | -7.68 [-11.20, -2.71] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_int_h0_vs_markov_w0_dist | 5 | 1.10 [-9.29, 9.68] | -2.52 [-4.97, -0.13] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_pos_int_h0_vs_markov_w0_dist | 5 | 4.64 [-4.60, 13.72] | -1.13 [-3.70, 1.63] | 0 | 0 |
| humaneval/pooled | fixed_fast_vs_markov_w05_dist | 5 | 11.14 [7.34, 15.71] | 5.19 [0.80, 8.67] | 0 | 0 |
| humaneval/pooled | fixed_g2_vs_markov_w05_dist | 5 | -18.21 [-23.12, -11.94] | -3.38 [-9.42, 2.05] | 0 | 0 |
| humaneval/pooled | picospec_vs_markov_w05_dist | 5 | 9.70 [3.65, 19.03] | 3.90 [0.40, 7.71] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_vs_markov_w05_dist | 5 | 2.93 [-2.32, 10.08] | 4.53 [0.08, 8.80] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_pos_vs_markov_w05_dist | 5 | 14.24 [5.40, 27.40] | 0.98 [-6.06, 8.23] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_int_vs_markov_w05_dist | 5 | 12.85 [6.23, 20.06] | 3.63 [0.27, 7.05] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_h0_vs_markov_w05_dist | 5 | 9.29 [1.62, 19.23] | 2.91 [-1.91, 9.31] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_pos_int_vs_markov_w05_dist | 5 | 25.48 [16.82, 38.15] | 10.93 [6.40, 15.09] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_pos_h0_vs_markov_w05_dist | 5 | 16.16 [10.89, 22.19] | 2.59 [-2.65, 7.31] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_int_h0_vs_markov_w05_dist | 5 | 8.97 [6.20, 12.22] | 9.43 [7.69, 11.57] | 0 | 0 |
| humaneval/pooled | markov_w0_dist_pos_int_h0_vs_markov_w05_dist | 5 | 31.49 [23.70, 37.54] | 8.72 [5.08, 14.02] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_pos_vs_markov_w05_dist | 5 | 14.34 [6.00, 24.64] | -0.93 [-6.27, 4.37] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_int_vs_markov_w05_dist | 5 | 14.35 [8.45, 23.59] | 1.61 [-2.12, 4.98] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_h0_vs_markov_w05_dist | 5 | -15.69 [-25.10, -7.02] | -6.61 [-9.86, -4.60] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_pos_int_vs_markov_w05_dist | 5 | 17.02 [12.60, 22.96] | 9.30 [4.70, 13.48] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_pos_h0_vs_markov_w05_dist | 5 | 3.39 [-4.57, 15.82] | -2.80 [-7.80, 2.26] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_int_h0_vs_markov_w05_dist | 5 | 4.06 [-3.96, 9.48] | 2.12 [-3.23, 6.33] | 0 | 0 |
| humaneval/pooled | markov_w05_dist_pos_int_h0_vs_markov_w05_dist | 5 | 7.70 [2.00, 12.73] | 3.45 [-3.02, 9.14] | 0 | 0 |
| gsm8k/low | fixed_fast_vs_fixed_g2 | 5 | 7.97 [2.41, 12.00] | -13.62 [-17.89, -6.76] | 1 | 0 |
| gsm8k/low | picospec_vs_fixed_g2 | 5 | 11.27 [5.00, 17.34] | -14.33 [-17.53, -8.55] | 1 | 0 |
| gsm8k/low | markov_w0_dist_vs_fixed_g2 | 5 | -1.83 [-6.03, 1.69] | -6.29 [-10.60, -2.87] | 0 | 0 |
| gsm8k/low | markov_w0_dist_pos_vs_fixed_g2 | 5 | 1.54 [-3.54, 5.82] | -14.96 [-19.61, -3.64] | 0 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_fixed_g2 | 5 | 6.42 [2.14, 8.96] | -16.20 [-21.99, -6.87] | 1 | 0 |
| gsm8k/low | markov_w0_dist_h0_vs_fixed_g2 | 5 | -8.58 [-15.47, -2.45] | -10.49 [-14.97, -7.08] | 0 | 0 |
| gsm8k/low | markov_w0_dist_pos_int_vs_fixed_g2 | 5 | 11.06 [-0.30, 18.81] | -16.92 [-22.63, -7.04] | 0 | 0 |
| gsm8k/low | markov_w0_dist_pos_h0_vs_fixed_g2 | 5 | -4.79 [-14.04, 5.32] | -15.95 [-21.38, -6.78] | 0 | 0 |
| gsm8k/low | markov_w0_dist_int_h0_vs_fixed_g2 | 5 | 4.52 [0.08, 7.80] | -11.61 [-15.73, -6.42] | 1 | 0 |
| gsm8k/low | markov_w0_dist_pos_int_h0_vs_fixed_g2 | 5 | 11.62 [1.47, 21.30] | -24.17 [-31.60, -14.82] | 0 | 0 |
| gsm8k/low | markov_w05_dist_vs_fixed_g2 | 5 | -7.49 [-10.41, -3.96] | -6.24 [-8.86, -2.42] | 1 | 0 |
| gsm8k/low | markov_w05_dist_pos_vs_fixed_g2 | 5 | -3.63 [-7.94, -0.49] | -13.29 [-18.58, -4.56] | 1 | 0 |
| gsm8k/low | markov_w05_dist_int_vs_fixed_g2 | 5 | -0.76 [-4.57, 1.67] | -5.17 [-8.17, -2.19] | 0 | 0 |
| gsm8k/low | markov_w05_dist_h0_vs_fixed_g2 | 5 | -31.66 [-34.32, -29.35] | -15.77 [-18.09, -11.69] | 0 | 0 |
| gsm8k/low | markov_w05_dist_pos_int_vs_fixed_g2 | 5 | 0.82 [-8.58, 8.69] | -10.85 [-13.68, -8.31] | 0 | 0 |
| gsm8k/low | markov_w05_dist_pos_h0_vs_fixed_g2 | 5 | -27.94 [-31.42, -24.58] | -21.96 [-25.48, -16.65] | 1 | 0 |
| gsm8k/low | markov_w05_dist_int_h0_vs_fixed_g2 | 5 | -21.64 [-32.14, -15.29] | -10.12 [-16.90, -6.67] | 0 | 0 |
| gsm8k/low | markov_w05_dist_pos_int_h0_vs_fixed_g2 | 5 | -20.18 [-32.34, -6.88] | -24.80 [-31.26, -16.55] | 1 | 0 |
| gsm8k/low | fixed_fast_vs_markov_w0_dist | 5 | 9.98 [4.51, 16.52] | -6.90 [-13.36, 1.13] | 1 | 0 |
| gsm8k/low | fixed_g2_vs_markov_w0_dist | 5 | 1.86 [-1.66, 6.41] | 5.91 [2.79, 9.59] | 0 | 0 |
| gsm8k/low | picospec_vs_markov_w0_dist | 5 | 13.34 [10.19, 15.93] | -7.57 [-12.01, -0.30] | 1 | 0 |
| gsm8k/low | markov_w0_dist_pos_vs_markov_w0_dist | 5 | 3.44 [-0.37, 5.99] | -8.16 [-14.84, 2.93] | 0 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_markov_w0_dist | 5 | 8.41 [3.52, 15.04] | -9.33 [-18.10, -0.09] | 1 | 0 |
| gsm8k/low | markov_w0_dist_h0_vs_markov_w0_dist | 5 | -6.87 [-10.88, -3.60] | -3.96 [-5.20, -1.39] | 0 | 0 |
| gsm8k/low | markov_w0_dist_pos_int_vs_markov_w0_dist | 5 | 13.13 [3.97, 18.05] | -10.00 [-15.36, -0.25] | 0 | 0 |
| gsm8k/low | markov_w0_dist_pos_h0_vs_markov_w0_dist | 5 | -3.02 [-8.86, 3.42] | -9.10 [-14.10, -0.01] | 0 | 0 |
| gsm8k/low | markov_w0_dist_int_h0_vs_markov_w0_dist | 5 | 6.47 [3.06, 10.15] | -5.01 [-7.67, 0.15] | 1 | 0 |
| gsm8k/low | markov_w0_dist_pos_int_h0_vs_markov_w0_dist | 5 | 13.70 [5.39, 19.39] | -16.83 [-20.93, -7.82] | 0 | 0 |
| gsm8k/low | markov_w05_dist_vs_markov_w0_dist | 5 | -5.77 [-7.95, -0.83] | 0.04 [-2.71, 5.32] | 1 | 0 |
| gsm8k/low | markov_w05_dist_pos_vs_markov_w0_dist | 5 | -1.84 [-5.41, 2.02] | -6.59 [-14.89, 4.11] | 1 | 0 |
| gsm8k/low | markov_w05_dist_int_vs_markov_w0_dist | 5 | 1.09 [-1.35, 3.94] | 1.05 [-0.74, 4.13] | 0 | 0 |
| gsm8k/low | markov_w05_dist_h0_vs_markov_w0_dist | 5 | -30.39 [-32.65, -26.97] | -8.93 [-13.19, -3.03] | 0 | 0 |
| gsm8k/low | markov_w05_dist_pos_int_vs_markov_w0_dist | 5 | 2.70 [-2.85, 6.92] | -4.30 [-7.71, 0.74] | 0 | 0 |
| gsm8k/low | markov_w05_dist_pos_h0_vs_markov_w0_dist | 5 | -26.60 [-27.83, -24.83] | -14.75 [-21.36, -7.16] | 1 | 0 |
| gsm8k/low | markov_w05_dist_int_h0_vs_markov_w0_dist | 5 | -20.18 [-29.57, -13.70] | -3.61 [-9.90, 1.20] | 0 | 0 |
| gsm8k/low | markov_w05_dist_pos_int_h0_vs_markov_w0_dist | 5 | -18.69 [-28.66, -8.05] | -17.42 [-27.47, -7.85] | 1 | 0 |
| gsm8k/low | fixed_fast_vs_markov_w05_dist | 5 | 16.72 [8.04, 23.81] | -6.94 [-12.00, -1.14] | 1 | 0 |
| gsm8k/low | fixed_g2_vs_markov_w05_dist | 5 | 8.10 [4.12, 11.61] | 5.88 [2.36, 8.14] | 1 | 0 |
| gsm8k/low | picospec_vs_markov_w05_dist | 5 | 20.28 [11.66, 25.27] | -7.61 [-11.12, -4.35] | 1 | 0 |
| gsm8k/low | markov_w0_dist_vs_markov_w05_dist | 5 | 6.12 [0.83, 8.63] | -0.04 [-5.62, 2.64] | 1 | 0 |
| gsm8k/low | markov_w0_dist_pos_vs_markov_w05_dist | 5 | 9.77 [2.25, 13.13] | -8.21 [-12.20, -0.59] | 1 | 0 |
| gsm8k/low | markov_w0_dist_int_vs_markov_w05_dist | 5 | 15.04 [8.51, 20.58] | -9.37 [-15.49, -2.25] | 1 | 0 |
| gsm8k/low | markov_w0_dist_h0_vs_markov_w05_dist | 5 | -1.17 [-7.50, 3.53] | -4.00 [-7.37, -2.12] | 1 | 0 |
| gsm8k/low | markov_w0_dist_pos_int_vs_markov_w05_dist | 5 | 20.06 [5.39, 27.08] | -10.05 [-13.89, -2.88] | 1 | 0 |
| gsm8k/low | markov_w0_dist_pos_h0_vs_markov_w05_dist | 5 | 2.92 [-6.43, 11.96] | -9.14 [-13.38, -1.83] | 1 | 0 |
| gsm8k/low | markov_w0_dist_int_h0_vs_markov_w05_dist | 5 | 12.99 [5.92, 16.32] | -5.06 [-6.78, -3.03] | 0 | 0 |
| gsm8k/low | markov_w0_dist_pos_int_h0_vs_markov_w05_dist | 5 | 20.66 [7.27, 29.08] | -16.87 [-20.95, -11.67] | 1 | 0 |
| gsm8k/low | markov_w05_dist_pos_vs_markov_w05_dist | 5 | 4.17 [-0.74, 6.90] | -6.63 [-11.94, -0.40] | 1 | 0 |
| gsm8k/low | markov_w05_dist_int_vs_markov_w05_dist | 5 | 7.28 [0.88, 10.26] | 1.01 [-1.11, 2.30] | 1 | 0 |
| gsm8k/low | markov_w05_dist_h0_vs_markov_w05_dist | 5 | -26.12 [-29.44, -24.00] | -8.97 [-13.56, -5.60] | 1 | 0 |
| gsm8k/low | markov_w05_dist_pos_int_vs_markov_w05_dist | 5 | 8.98 [-0.28, 15.55] | -4.34 [-7.81, -2.17] | 1 | 0 |
| gsm8k/low | markov_w05_dist_pos_h0_vs_markov_w05_dist | 5 | -22.11 [-25.49, -20.05] | -14.80 [-20.22, -9.40] | 0 | 0 |
| gsm8k/low | markov_w05_dist_int_h0_vs_markov_w05_dist | 5 | -15.30 [-26.67, -8.27] | -3.65 [-12.14, 0.45] | 1 | 0 |
| gsm8k/low | markov_w05_dist_pos_int_h0_vs_markov_w05_dist | 5 | -13.71 [-27.43, -0.65] | -17.47 [-26.26, -8.65] | 1 | 0 |
| gsm8k/pooled | fixed_fast_vs_fixed_g2 | 5 | 7.97 [2.41, 12.00] | -13.62 [-17.89, -6.76] | 1 | 0 |
| gsm8k/pooled | picospec_vs_fixed_g2 | 5 | 11.27 [5.00, 17.34] | -14.33 [-17.53, -8.55] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_fixed_g2 | 5 | -1.83 [-6.03, 1.69] | -6.29 [-10.60, -2.87] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_pos_vs_fixed_g2 | 5 | 1.54 [-3.54, 5.82] | -14.96 [-19.61, -3.64] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_int_vs_fixed_g2 | 5 | 6.42 [2.14, 8.96] | -16.20 [-21.99, -6.87] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_h0_vs_fixed_g2 | 5 | -8.58 [-15.47, -2.45] | -10.49 [-14.97, -7.08] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_pos_int_vs_fixed_g2 | 5 | 11.06 [-0.30, 18.81] | -16.92 [-22.63, -7.04] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_pos_h0_vs_fixed_g2 | 5 | -4.79 [-14.04, 5.32] | -15.95 [-21.38, -6.78] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_int_h0_vs_fixed_g2 | 5 | 4.52 [0.08, 7.80] | -11.61 [-15.73, -6.42] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_pos_int_h0_vs_fixed_g2 | 5 | 11.62 [1.47, 21.30] | -24.17 [-31.60, -14.82] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_fixed_g2 | 5 | -7.49 [-10.41, -3.96] | -6.24 [-8.86, -2.42] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_pos_vs_fixed_g2 | 5 | -3.63 [-7.94, -0.49] | -13.29 [-18.58, -4.56] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_int_vs_fixed_g2 | 5 | -0.76 [-4.57, 1.67] | -5.17 [-8.17, -2.19] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_h0_vs_fixed_g2 | 5 | -31.66 [-34.32, -29.35] | -15.77 [-18.09, -11.69] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_pos_int_vs_fixed_g2 | 5 | 0.82 [-8.58, 8.69] | -10.85 [-13.68, -8.31] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_pos_h0_vs_fixed_g2 | 5 | -27.94 [-31.42, -24.58] | -21.96 [-25.48, -16.65] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_int_h0_vs_fixed_g2 | 5 | -21.64 [-32.14, -15.29] | -10.12 [-16.90, -6.67] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_pos_int_h0_vs_fixed_g2 | 5 | -20.18 [-32.34, -6.88] | -24.80 [-31.26, -16.55] | 1 | 0 |
| gsm8k/pooled | fixed_fast_vs_markov_w0_dist | 5 | 9.98 [4.51, 16.52] | -6.90 [-13.36, 1.13] | 1 | 0 |
| gsm8k/pooled | fixed_g2_vs_markov_w0_dist | 5 | 1.86 [-1.66, 6.41] | 5.91 [2.79, 9.59] | 0 | 0 |
| gsm8k/pooled | picospec_vs_markov_w0_dist | 5 | 13.34 [10.19, 15.93] | -7.57 [-12.01, -0.30] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_pos_vs_markov_w0_dist | 5 | 3.44 [-0.37, 5.99] | -8.16 [-14.84, 2.93] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_int_vs_markov_w0_dist | 5 | 8.41 [3.52, 15.04] | -9.33 [-18.10, -0.09] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_h0_vs_markov_w0_dist | 5 | -6.87 [-10.88, -3.60] | -3.96 [-5.20, -1.39] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_pos_int_vs_markov_w0_dist | 5 | 13.13 [3.97, 18.05] | -10.00 [-15.36, -0.25] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_pos_h0_vs_markov_w0_dist | 5 | -3.02 [-8.86, 3.42] | -9.10 [-14.10, -0.01] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_int_h0_vs_markov_w0_dist | 5 | 6.47 [3.06, 10.15] | -5.01 [-7.67, 0.15] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_pos_int_h0_vs_markov_w0_dist | 5 | 13.70 [5.39, 19.39] | -16.83 [-20.93, -7.82] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_markov_w0_dist | 5 | -5.77 [-7.95, -0.83] | 0.04 [-2.71, 5.32] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_pos_vs_markov_w0_dist | 5 | -1.84 [-5.41, 2.02] | -6.59 [-14.89, 4.11] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_int_vs_markov_w0_dist | 5 | 1.09 [-1.35, 3.94] | 1.05 [-0.74, 4.13] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_h0_vs_markov_w0_dist | 5 | -30.39 [-32.65, -26.97] | -8.93 [-13.19, -3.03] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_pos_int_vs_markov_w0_dist | 5 | 2.70 [-2.85, 6.92] | -4.30 [-7.71, 0.74] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_pos_h0_vs_markov_w0_dist | 5 | -26.60 [-27.83, -24.83] | -14.75 [-21.36, -7.16] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_int_h0_vs_markov_w0_dist | 5 | -20.18 [-29.57, -13.70] | -3.61 [-9.90, 1.20] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_pos_int_h0_vs_markov_w0_dist | 5 | -18.69 [-28.66, -8.05] | -17.42 [-27.47, -7.85] | 1 | 0 |
| gsm8k/pooled | fixed_fast_vs_markov_w05_dist | 5 | 16.72 [8.04, 23.81] | -6.94 [-12.00, -1.14] | 1 | 0 |
| gsm8k/pooled | fixed_g2_vs_markov_w05_dist | 5 | 8.10 [4.12, 11.61] | 5.88 [2.36, 8.14] | 1 | 0 |
| gsm8k/pooled | picospec_vs_markov_w05_dist | 5 | 20.28 [11.66, 25.27] | -7.61 [-11.12, -4.35] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_markov_w05_dist | 5 | 6.12 [0.83, 8.63] | -0.04 [-5.62, 2.64] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_pos_vs_markov_w05_dist | 5 | 9.77 [2.25, 13.13] | -8.21 [-12.20, -0.59] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_int_vs_markov_w05_dist | 5 | 15.04 [8.51, 20.58] | -9.37 [-15.49, -2.25] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_h0_vs_markov_w05_dist | 5 | -1.17 [-7.50, 3.53] | -4.00 [-7.37, -2.12] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_pos_int_vs_markov_w05_dist | 5 | 20.06 [5.39, 27.08] | -10.05 [-13.89, -2.88] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_pos_h0_vs_markov_w05_dist | 5 | 2.92 [-6.43, 11.96] | -9.14 [-13.38, -1.83] | 1 | 0 |
| gsm8k/pooled | markov_w0_dist_int_h0_vs_markov_w05_dist | 5 | 12.99 [5.92, 16.32] | -5.06 [-6.78, -3.03] | 0 | 0 |
| gsm8k/pooled | markov_w0_dist_pos_int_h0_vs_markov_w05_dist | 5 | 20.66 [7.27, 29.08] | -16.87 [-20.95, -11.67] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_pos_vs_markov_w05_dist | 5 | 4.17 [-0.74, 6.90] | -6.63 [-11.94, -0.40] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_int_vs_markov_w05_dist | 5 | 7.28 [0.88, 10.26] | 1.01 [-1.11, 2.30] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_h0_vs_markov_w05_dist | 5 | -26.12 [-29.44, -24.00] | -8.97 [-13.56, -5.60] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_pos_int_vs_markov_w05_dist | 5 | 8.98 [-0.28, 15.55] | -4.34 [-7.81, -2.17] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_pos_h0_vs_markov_w05_dist | 5 | -22.11 [-25.49, -20.05] | -14.80 [-20.22, -9.40] | 0 | 0 |
| gsm8k/pooled | markov_w05_dist_int_h0_vs_markov_w05_dist | 5 | -15.30 [-26.67, -8.27] | -3.65 [-12.14, 0.45] | 1 | 0 |
| gsm8k/pooled | markov_w05_dist_pos_int_h0_vs_markov_w05_dist | 5 | -13.71 [-27.43, -0.65] | -17.47 [-26.26, -8.65] | 1 | 0 |
| mtbench/low | fixed_fast_vs_fixed_g2 | 5 | -9.23 [-12.58, -4.91] | -40.99 [-47.32, -31.52] | 3 | 0 |
| mtbench/low | picospec_vs_fixed_g2 | 5 | -2.79 [-5.74, 0.41] | -37.67 [-42.85, -29.79] | 3 | 0 |
| mtbench/low | markov_w0_dist_vs_fixed_g2 | 5 | -4.60 [-8.41, -1.58] | -2.13 [-8.16, 2.76] | 0 | 0 |
| mtbench/low | markov_w0_dist_pos_vs_fixed_g2 | 5 | -8.60 [-12.65, -2.38] | -5.49 [-12.61, 3.16] | 1 | 0 |
| mtbench/low | markov_w0_dist_int_vs_fixed_g2 | 5 | -2.53 [-3.89, -1.04] | -5.46 [-9.24, -0.93] | 0 | 0 |
| mtbench/low | markov_w0_dist_h0_vs_fixed_g2 | 5 | -9.51 [-13.32, -7.01] | -0.53 [-5.06, 3.80] | 1 | 0 |
| mtbench/low | markov_w0_dist_pos_int_vs_fixed_g2 | 5 | -6.77 [-8.96, -3.83] | -12.72 [-19.54, -5.09] | 1 | 0 |
| mtbench/low | markov_w0_dist_pos_h0_vs_fixed_g2 | 5 | -10.31 [-12.46, -8.00] | -3.79 [-8.70, 1.50] | 1 | 0 |
| mtbench/low | markov_w0_dist_int_h0_vs_fixed_g2 | 5 | -5.13 [-7.95, -0.34] | -7.29 [-9.68, -4.26] | 0 | 0 |
| mtbench/low | markov_w0_dist_pos_int_h0_vs_fixed_g2 | 5 | -4.65 [-6.31, -2.43] | -10.56 [-17.65, -0.55] | 0 | 0 |
| mtbench/low | markov_w05_dist_vs_fixed_g2 | 5 | 0.28 [-2.62, 3.14] | 7.09 [3.19, 10.63] | 1 | 0 |
| mtbench/low | markov_w05_dist_pos_vs_fixed_g2 | 5 | -4.70 [-10.31, 0.98] | 2.41 [-4.44, 8.68] | 1 | 0 |
| mtbench/low | markov_w05_dist_int_vs_fixed_g2 | 5 | 0.88 [-2.23, 6.09] | 6.61 [3.10, 11.41] | 1 | 0 |
| mtbench/low | markov_w05_dist_h0_vs_fixed_g2 | 5 | -17.45 [-20.94, -13.09] | 9.32 [4.08, 14.21] | 1 | 0 |
| mtbench/low | markov_w05_dist_pos_int_vs_fixed_g2 | 5 | -0.50 [-2.99, 2.24] | 5.36 [2.13, 9.67] | 1 | 0 |
| mtbench/low | markov_w05_dist_pos_h0_vs_fixed_g2 | 5 | -18.67 [-22.14, -14.46] | 7.15 [0.38, 13.73] | 1 | 0 |
| mtbench/low | markov_w05_dist_int_h0_vs_fixed_g2 | 5 | -17.87 [-22.05, -12.79] | 8.16 [1.56, 14.66] | 1 | 0 |
| mtbench/low | markov_w05_dist_pos_int_h0_vs_fixed_g2 | 5 | -18.27 [-22.08, -11.90] | 4.50 [-3.18, 12.31] | 1 | 0 |
| mtbench/low | fixed_fast_vs_markov_w0_dist | 5 | -4.86 [-11.41, 3.83] | -38.05 [-51.04, -21.60] | 3 | 0 |
| mtbench/low | fixed_g2_vs_markov_w0_dist | 5 | 4.82 [1.61, 9.19] | 2.09 [-2.84, 7.54] | 0 | 0 |
| mtbench/low | picospec_vs_markov_w0_dist | 5 | 1.89 [-4.50, 9.64] | -34.80 [-45.44, -20.11] | 3 | 0 |
| mtbench/low | markov_w0_dist_pos_vs_markov_w0_dist | 5 | -4.20 [-8.27, 0.15] | -3.29 [-7.79, 1.52] | 1 | 0 |
| mtbench/low | markov_w0_dist_int_vs_markov_w0_dist | 5 | 2.17 [-1.40, 7.37] | -3.26 [-7.80, 2.13] | 0 | 0 |
| mtbench/low | markov_w0_dist_h0_vs_markov_w0_dist | 5 | -5.15 [-7.62, -2.41] | 1.57 [-1.27, 4.55] | 1 | 0 |
| mtbench/low | markov_w0_dist_pos_int_vs_markov_w0_dist | 5 | -2.28 [-6.88, 4.28] | -10.37 [-17.72, -1.29] | 1 | 0 |
| mtbench/low | markov_w0_dist_pos_h0_vs_markov_w0_dist | 5 | -5.99 [-8.82, -2.52] | -1.62 [-4.08, 0.97] | 1 | 0 |
| mtbench/low | markov_w0_dist_int_h0_vs_markov_w0_dist | 5 | -0.56 [-6.10, 7.92] | -5.05 [-10.47, 2.40] | 0 | 0 |
| mtbench/low | markov_w0_dist_pos_int_h0_vs_markov_w0_dist | 5 | -0.05 [-4.26, 6.22] | -8.25 [-15.09, -0.24] | 0 | 0 |
| mtbench/low | markov_w05_dist_vs_markov_w0_dist | 5 | 5.11 [3.55, 7.97] | 9.03 [7.31, 12.19] | 1 | 0 |
| mtbench/low | markov_w05_dist_pos_vs_markov_w0_dist | 5 | -0.11 [-4.63, 4.42] | 4.44 [-0.06, 8.34] | 1 | 0 |
| mtbench/low | markov_w05_dist_int_vs_markov_w0_dist | 5 | 5.74 [1.72, 11.86] | 8.56 [5.40, 13.11] | 1 | 0 |
| mtbench/low | markov_w05_dist_h0_vs_markov_w0_dist | 5 | -13.47 [-15.67, -10.28] | 11.21 [8.95, 14.44] | 1 | 0 |
| mtbench/low | markov_w05_dist_pos_int_vs_markov_w0_dist | 5 | 4.29 [0.35, 10.38] | 7.34 [3.91, 11.87] | 1 | 0 |
| mtbench/low | markov_w05_dist_pos_h0_vs_markov_w0_dist | 5 | -14.75 [-17.09, -11.85] | 9.09 [4.84, 12.55] | 1 | 0 |
| mtbench/low | markov_w05_dist_int_h0_vs_markov_w0_dist | 5 | -13.91 [-16.88, -10.13] | 10.08 [6.70, 13.76] | 1 | 0 |
| mtbench/low | markov_w05_dist_pos_int_h0_vs_markov_w0_dist | 5 | -14.33 [-17.99, -8.59] | 6.49 [2.58, 12.13] | 1 | 0 |
| mtbench/low | fixed_fast_vs_markov_w05_dist | 5 | -9.48 [-14.87, -2.99] | -51.76 [-63.78, -36.91] | 2 | 0 |
| mtbench/low | fixed_g2_vs_markov_w05_dist | 5 | -0.27 [-3.04, 2.69] | -7.64 [-11.89, -3.29] | 1 | 0 |
| mtbench/low | picospec_vs_markov_w05_dist | 5 | -3.06 [-8.32, 2.88] | -48.19 [-58.13, -35.23] | 2 | 0 |
| mtbench/low | markov_w0_dist_vs_markov_w05_dist | 5 | -4.86 [-7.38, -3.43] | -9.93 [-13.89, -7.89] | 1 | 0 |
| mtbench/low | markov_w0_dist_pos_vs_markov_w05_dist | 5 | -8.86 [-11.95, -4.31] | -13.55 [-18.85, -7.87] | 0 | 0 |
| mtbench/low | markov_w0_dist_int_vs_markov_w05_dist | 5 | -2.80 [-5.66, 1.13] | -13.51 [-17.65, -8.10] | 1 | 0 |
| mtbench/low | markov_w0_dist_h0_vs_markov_w05_dist | 5 | -9.76 [-12.83, -8.43] | -8.21 [-12.69, -6.03] | 0 | 0 |
| mtbench/low | markov_w0_dist_pos_int_vs_markov_w05_dist | 5 | -7.02 [-10.96, -2.46] | -21.33 [-28.18, -14.05] | 0 | 0 |
| mtbench/low | markov_w0_dist_pos_h0_vs_markov_w05_dist | 5 | -10.55 [-12.87, -8.36] | -11.72 [-14.63, -9.42] | 0 | 0 |
| mtbench/low | markov_w0_dist_int_h0_vs_markov_w05_dist | 5 | -5.39 [-9.96, 0.83] | -15.48 [-19.29, -9.89] | 1 | 0 |
| mtbench/low | markov_w0_dist_pos_int_h0_vs_markov_w05_dist | 5 | -4.91 [-8.12, -0.37] | -19.00 [-25.16, -12.39] | 1 | 0 |
| mtbench/low | markov_w05_dist_pos_vs_markov_w05_dist | 5 | -4.96 [-9.86, -1.45] | -5.05 [-11.77, -1.21] | 0 | 0 |
| mtbench/low | markov_w05_dist_int_vs_markov_w05_dist | 5 | 0.61 [-2.16, 4.20] | -0.52 [-2.67, 1.65] | 0 | 0 |
| mtbench/low | markov_w05_dist_h0_vs_markov_w05_dist | 5 | -17.67 [-19.04, -15.73] | 2.39 [-0.62, 4.55] | 0 | 0 |
| mtbench/low | markov_w05_dist_pos_int_vs_markov_w05_dist | 5 | -0.77 [-3.32, 3.35] | -1.86 [-4.51, 1.27] | 0 | 0 |
| mtbench/low | markov_w05_dist_pos_h0_vs_markov_w05_dist | 5 | -18.89 [-20.55, -16.54] | 0.06 [-6.15, 3.85] | 0 | 0 |
| mtbench/low | markov_w05_dist_int_h0_vs_markov_w05_dist | 5 | -18.09 [-20.37, -15.04] | 1.15 [-4.10, 4.89] | 0 | 0 |
| mtbench/low | markov_w05_dist_pos_int_h0_vs_markov_w05_dist | 5 | -18.49 [-21.12, -14.47] | -2.79 [-7.41, 1.99] | 0 | 0 |
| mtbench/pooled | fixed_fast_vs_fixed_g2 | 5 | -9.23 [-12.58, -4.91] | -40.99 [-47.32, -31.52] | 3 | 0 |
| mtbench/pooled | picospec_vs_fixed_g2 | 5 | -2.79 [-5.74, 0.41] | -37.67 [-42.85, -29.79] | 3 | 0 |
| mtbench/pooled | markov_w0_dist_vs_fixed_g2 | 5 | -4.60 [-8.41, -1.58] | -2.13 [-8.16, 2.76] | 0 | 0 |
| mtbench/pooled | markov_w0_dist_pos_vs_fixed_g2 | 5 | -8.60 [-12.65, -2.38] | -5.49 [-12.61, 3.16] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_fixed_g2 | 5 | -2.53 [-3.89, -1.04] | -5.46 [-9.24, -0.93] | 0 | 0 |
| mtbench/pooled | markov_w0_dist_h0_vs_fixed_g2 | 5 | -9.51 [-13.32, -7.01] | -0.53 [-5.06, 3.80] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_pos_int_vs_fixed_g2 | 5 | -6.77 [-8.96, -3.83] | -12.72 [-19.54, -5.09] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_pos_h0_vs_fixed_g2 | 5 | -10.31 [-12.46, -8.00] | -3.79 [-8.70, 1.50] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_int_h0_vs_fixed_g2 | 5 | -5.13 [-7.95, -0.34] | -7.29 [-9.68, -4.26] | 0 | 0 |
| mtbench/pooled | markov_w0_dist_pos_int_h0_vs_fixed_g2 | 5 | -4.65 [-6.31, -2.43] | -10.56 [-17.65, -0.55] | 0 | 0 |
| mtbench/pooled | markov_w05_dist_vs_fixed_g2 | 5 | 0.28 [-2.62, 3.14] | 7.09 [3.19, 10.63] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_pos_vs_fixed_g2 | 5 | -4.70 [-10.31, 0.98] | 2.41 [-4.44, 8.68] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_fixed_g2 | 5 | 0.88 [-2.23, 6.09] | 6.61 [3.10, 11.41] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_h0_vs_fixed_g2 | 5 | -17.45 [-20.94, -13.09] | 9.32 [4.08, 14.21] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_pos_int_vs_fixed_g2 | 5 | -0.50 [-2.99, 2.24] | 5.36 [2.13, 9.67] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_pos_h0_vs_fixed_g2 | 5 | -18.67 [-22.14, -14.46] | 7.15 [0.38, 13.73] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_int_h0_vs_fixed_g2 | 5 | -17.87 [-22.05, -12.79] | 8.16 [1.56, 14.66] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_pos_int_h0_vs_fixed_g2 | 5 | -18.27 [-22.08, -11.90] | 4.50 [-3.18, 12.31] | 1 | 0 |
| mtbench/pooled | fixed_fast_vs_markov_w0_dist | 5 | -4.86 [-11.41, 3.83] | -38.05 [-51.04, -21.60] | 3 | 0 |
| mtbench/pooled | fixed_g2_vs_markov_w0_dist | 5 | 4.82 [1.61, 9.19] | 2.09 [-2.84, 7.54] | 0 | 0 |
| mtbench/pooled | picospec_vs_markov_w0_dist | 5 | 1.89 [-4.50, 9.64] | -34.80 [-45.44, -20.11] | 3 | 0 |
| mtbench/pooled | markov_w0_dist_pos_vs_markov_w0_dist | 5 | -4.20 [-8.27, 0.15] | -3.29 [-7.79, 1.52] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_markov_w0_dist | 5 | 2.17 [-1.40, 7.37] | -3.26 [-7.80, 2.13] | 0 | 0 |
| mtbench/pooled | markov_w0_dist_h0_vs_markov_w0_dist | 5 | -5.15 [-7.62, -2.41] | 1.57 [-1.27, 4.55] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_pos_int_vs_markov_w0_dist | 5 | -2.28 [-6.88, 4.28] | -10.37 [-17.72, -1.29] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_pos_h0_vs_markov_w0_dist | 5 | -5.99 [-8.82, -2.52] | -1.62 [-4.08, 0.97] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_int_h0_vs_markov_w0_dist | 5 | -0.56 [-6.10, 7.92] | -5.05 [-10.47, 2.40] | 0 | 0 |
| mtbench/pooled | markov_w0_dist_pos_int_h0_vs_markov_w0_dist | 5 | -0.05 [-4.26, 6.22] | -8.25 [-15.09, -0.24] | 0 | 0 |
| mtbench/pooled | markov_w05_dist_vs_markov_w0_dist | 5 | 5.11 [3.55, 7.97] | 9.03 [7.31, 12.19] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_pos_vs_markov_w0_dist | 5 | -0.11 [-4.63, 4.42] | 4.44 [-0.06, 8.34] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_markov_w0_dist | 5 | 5.74 [1.72, 11.86] | 8.56 [5.40, 13.11] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_h0_vs_markov_w0_dist | 5 | -13.47 [-15.67, -10.28] | 11.21 [8.95, 14.44] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_pos_int_vs_markov_w0_dist | 5 | 4.29 [0.35, 10.38] | 7.34 [3.91, 11.87] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_pos_h0_vs_markov_w0_dist | 5 | -14.75 [-17.09, -11.85] | 9.09 [4.84, 12.55] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_int_h0_vs_markov_w0_dist | 5 | -13.91 [-16.88, -10.13] | 10.08 [6.70, 13.76] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_pos_int_h0_vs_markov_w0_dist | 5 | -14.33 [-17.99, -8.59] | 6.49 [2.58, 12.13] | 1 | 0 |
| mtbench/pooled | fixed_fast_vs_markov_w05_dist | 5 | -9.48 [-14.87, -2.99] | -51.76 [-63.78, -36.91] | 2 | 0 |
| mtbench/pooled | fixed_g2_vs_markov_w05_dist | 5 | -0.27 [-3.04, 2.69] | -7.64 [-11.89, -3.29] | 1 | 0 |
| mtbench/pooled | picospec_vs_markov_w05_dist | 5 | -3.06 [-8.32, 2.88] | -48.19 [-58.13, -35.23] | 2 | 0 |
| mtbench/pooled | markov_w0_dist_vs_markov_w05_dist | 5 | -4.86 [-7.38, -3.43] | -9.93 [-13.89, -7.89] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_pos_vs_markov_w05_dist | 5 | -8.86 [-11.95, -4.31] | -13.55 [-18.85, -7.87] | 0 | 0 |
| mtbench/pooled | markov_w0_dist_int_vs_markov_w05_dist | 5 | -2.80 [-5.66, 1.13] | -13.51 [-17.65, -8.10] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_h0_vs_markov_w05_dist | 5 | -9.76 [-12.83, -8.43] | -8.21 [-12.69, -6.03] | 0 | 0 |
| mtbench/pooled | markov_w0_dist_pos_int_vs_markov_w05_dist | 5 | -7.02 [-10.96, -2.46] | -21.33 [-28.18, -14.05] | 0 | 0 |
| mtbench/pooled | markov_w0_dist_pos_h0_vs_markov_w05_dist | 5 | -10.55 [-12.87, -8.36] | -11.72 [-14.63, -9.42] | 0 | 0 |
| mtbench/pooled | markov_w0_dist_int_h0_vs_markov_w05_dist | 5 | -5.39 [-9.96, 0.83] | -15.48 [-19.29, -9.89] | 1 | 0 |
| mtbench/pooled | markov_w0_dist_pos_int_h0_vs_markov_w05_dist | 5 | -4.91 [-8.12, -0.37] | -19.00 [-25.16, -12.39] | 1 | 0 |
| mtbench/pooled | markov_w05_dist_pos_vs_markov_w05_dist | 5 | -4.96 [-9.86, -1.45] | -5.05 [-11.77, -1.21] | 0 | 0 |
| mtbench/pooled | markov_w05_dist_int_vs_markov_w05_dist | 5 | 0.61 [-2.16, 4.20] | -0.52 [-2.67, 1.65] | 0 | 0 |
| mtbench/pooled | markov_w05_dist_h0_vs_markov_w05_dist | 5 | -17.67 [-19.04, -15.73] | 2.39 [-0.62, 4.55] | 0 | 0 |
| mtbench/pooled | markov_w05_dist_pos_int_vs_markov_w05_dist | 5 | -0.77 [-3.32, 3.35] | -1.86 [-4.51, 1.27] | 0 | 0 |
| mtbench/pooled | markov_w05_dist_pos_h0_vs_markov_w05_dist | 5 | -18.89 [-20.55, -16.54] | 0.06 [-6.15, 3.85] | 0 | 0 |
| mtbench/pooled | markov_w05_dist_int_h0_vs_markov_w05_dist | 5 | -18.09 [-20.37, -15.04] | 1.15 [-4.10, 4.89] | 0 | 0 |
| mtbench/pooled | markov_w05_dist_pos_int_h0_vs_markov_w05_dist | 5 | -18.49 [-21.12, -14.47] | -2.79 [-7.41, 1.99] | 0 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
