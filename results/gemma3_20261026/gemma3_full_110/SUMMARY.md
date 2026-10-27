# Progress probe: gemma3_full_110

State: complete; 3300/3300 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | sync_g4 | 110 | 29512 | 24.972 | 0.2650 | 20 | 0.00 |
| all/low | fixed_g2 | 110 | 29668 | 36.806 | 0.2183 | 21 | 36.00 |
| all/low | fixed_fast | 110 | 29512 | 36.507 | 0.2911 | 20 | 30.26 |
| all/low | fixed_g8 | 110 | 29285 | 28.450 | 0.4305 | 20 | 19.39 |
| all/low | markov_w0_dist | 110 | 29661 | 36.967 | 0.2149 | 21 | 39.62 |
| all/low | markov_w05_dist | 110 | 29632 | 34.808 | 0.2125 | 21 | 37.23 |
| all/low | pearl | 110 | 30008 | 35.264 | 0.2075 | 23 | 0.00 |
| all/low | picospec | 110 | 29512 | 39.288 | 0.2849 | 20 | 36.09 |
| all/low | pipesd | 110 | 29484 | 23.043 | 0.3369 | 21 | 0.00 |
| all/low | hf_default | 110 | 29526 | 21.924 | 0.3258 | 21 | 0.00 |
| all/high | sync_g4 | 110 | 29869 | 13.912 | 0.4098 | 21 | 0.00 |
| all/high | fixed_g2 | 110 | 29827 | 14.414 | 0.4222 | 22 | 36.49 |
| all/high | fixed_fast | 110 | 29869 | 17.171 | 0.4012 | 21 | 30.96 |
| all/high | fixed_g8 | 110 | 29820 | 18.501 | 0.5005 | 22 | 19.67 |
| all/high | markov_w0_dist | 110 | 29839 | 19.865 | 0.4368 | 22 | 31.53 |
| all/high | markov_w05_dist | 110 | 29808 | 17.358 | 0.3830 | 22 | 41.35 |
| all/high | pearl | 110 | 29930 | 17.865 | 0.4140 | 22 | 0.00 |
| all/high | picospec | 110 | 29869 | 17.178 | 0.4013 | 21 | 30.93 |
| all/high | pipesd | 110 | 29785 | 15.100 | 0.4817 | 20 | 0.00 |
| all/high | hf_default | 110 | 29832 | 13.316 | 0.4616 | 21 | 0.00 |
| all/dynamic | sync_g4 | 110 | 29326 | 18.945 | 0.3214 | 19 | 0.00 |
| all/dynamic | fixed_g2 | 110 | 29544 | 23.577 | 0.2915 | 20 | 36.40 |
| all/dynamic | fixed_fast | 110 | 29326 | 24.273 | 0.3354 | 19 | 30.71 |
| all/dynamic | fixed_g8 | 110 | 29245 | 23.081 | 0.4608 | 19 | 19.87 |
| all/dynamic | markov_w0_dist | 110 | 29602 | 26.662 | 0.2987 | 20 | 37.38 |
| all/dynamic | markov_w05_dist | 110 | 29376 | 24.999 | 0.2790 | 19 | 39.82 |
| all/dynamic | pearl | 110 | 29484 | 24.344 | 0.2979 | 20 | 0.00 |
| all/dynamic | picospec | 110 | 29326 | 25.181 | 0.3326 | 19 | 36.03 |
| all/dynamic | pipesd | 110 | 29472 | 19.079 | 0.3892 | 20 | 0.00 |
| all/dynamic | hf_default | 110 | 29484 | 16.555 | 0.3943 | 20 | 0.00 |
| all/pooled | sync_g4 | 330 | 88707 | 18.190 | 0.3324 | 60 | 0.00 |
| all/pooled | fixed_g2 | 330 | 89039 | 21.567 | 0.3109 | 63 | 36.29 |
| all/pooled | fixed_fast | 330 | 88707 | 23.617 | 0.3428 | 60 | 30.64 |
| all/pooled | fixed_g8 | 330 | 88350 | 22.606 | 0.4642 | 61 | 19.64 |
| all/pooled | markov_w0_dist | 330 | 89102 | 26.093 | 0.3171 | 63 | 35.16 |
| all/pooled | markov_w05_dist | 330 | 88816 | 23.725 | 0.2917 | 62 | 39.57 |
| all/pooled | pearl | 330 | 89422 | 23.926 | 0.3064 | 65 | 0.00 |
| all/pooled | picospec | 330 | 88707 | 24.273 | 0.3398 | 60 | 34.15 |
| all/pooled | pipesd | 330 | 88741 | 18.500 | 0.4029 | 61 | 0.00 |
| all/pooled | hf_default | 330 | 88842 | 16.551 | 0.3942 | 62 | 0.00 |
| gsm8k/low | sync_g4 | 50 | 15773 | 28.508 | 0.2319 | 11 | 0.00 |
| gsm8k/low | fixed_g2 | 50 | 15996 | 42.807 | 0.1883 | 12 | 44.59 |
| gsm8k/low | fixed_fast | 50 | 15773 | 45.698 | 0.2307 | 11 | 41.64 |
| gsm8k/low | fixed_g8 | 50 | 15705 | 38.309 | 0.3178 | 11 | 29.04 |
| gsm8k/low | markov_w0_dist | 50 | 15996 | 41.888 | 0.1960 | 12 | 45.34 |
| gsm8k/low | markov_w05_dist | 50 | 15996 | 37.936 | 0.1964 | 12 | 41.69 |
| gsm8k/low | pearl | 50 | 16317 | 37.648 | 0.1946 | 13 | 0.00 |
| gsm8k/low | picospec | 50 | 15773 | 49.090 | 0.2250 | 11 | 48.22 |
| gsm8k/low | pipesd | 50 | 15907 | 26.179 | 0.3019 | 12 | 0.00 |
| gsm8k/low | hf_default | 50 | 15918 | 24.835 | 0.2892 | 12 | 0.00 |
| gsm8k/high | sync_g4 | 50 | 16257 | 15.987 | 0.3557 | 12 | 0.00 |
| gsm8k/high | fixed_g2 | 50 | 16224 | 16.175 | 0.3741 | 12 | 45.37 |
| gsm8k/high | fixed_fast | 50 | 16257 | 21.090 | 0.3243 | 12 | 42.21 |
| gsm8k/high | fixed_g8 | 50 | 16237 | 24.927 | 0.3719 | 12 | 29.47 |
| gsm8k/high | markov_w0_dist | 50 | 16257 | 25.362 | 0.3445 | 12 | 42.45 |
| gsm8k/high | markov_w05_dist | 50 | 16225 | 21.709 | 0.3266 | 12 | 46.50 |
| gsm8k/high | pearl | 50 | 16247 | 22.674 | 0.3265 | 12 | 0.00 |
| gsm8k/high | picospec | 50 | 16257 | 21.094 | 0.3249 | 12 | 42.12 |
| gsm8k/high | pipesd | 50 | 16148 | 18.643 | 0.3906 | 11 | 0.00 |
| gsm8k/high | hf_default | 50 | 16148 | 15.708 | 0.3944 | 11 | 0.00 |
| gsm8k/dynamic | sync_g4 | 50 | 15779 | 21.789 | 0.2783 | 10 | 0.00 |
| gsm8k/dynamic | fixed_g2 | 50 | 15995 | 27.348 | 0.2510 | 11 | 45.41 |
| gsm8k/dynamic | fixed_fast | 50 | 15779 | 30.471 | 0.2659 | 10 | 42.45 |
| gsm8k/dynamic | fixed_g8 | 50 | 15816 | 31.328 | 0.3375 | 10 | 30.14 |
| gsm8k/dynamic | markov_w0_dist | 50 | 16087 | 31.841 | 0.2605 | 11 | 45.12 |
| gsm8k/dynamic | markov_w05_dist | 50 | 15799 | 28.479 | 0.2520 | 10 | 45.18 |
| gsm8k/dynamic | pearl | 50 | 16020 | 28.827 | 0.2518 | 11 | 0.00 |
| gsm8k/dynamic | picospec | 50 | 15779 | 31.568 | 0.2627 | 10 | 47.86 |
| gsm8k/dynamic | pipesd | 50 | 16027 | 22.451 | 0.3323 | 11 | 0.00 |
| gsm8k/dynamic | hf_default | 50 | 16025 | 19.124 | 0.3423 | 11 | 0.00 |
| gsm8k/pooled | sync_g4 | 150 | 47809 | 20.838 | 0.2893 | 33 | 0.00 |
| gsm8k/pooled | fixed_g2 | 150 | 48215 | 24.580 | 0.2716 | 35 | 45.12 |
| gsm8k/pooled | fixed_fast | 150 | 47809 | 29.262 | 0.2741 | 33 | 42.10 |
| gsm8k/pooled | fixed_g8 | 150 | 47758 | 30.493 | 0.3427 | 33 | 29.55 |
| gsm8k/pooled | markov_w0_dist | 150 | 48340 | 31.634 | 0.2674 | 35 | 44.04 |
| gsm8k/pooled | markov_w05_dist | 150 | 48020 | 27.857 | 0.2587 | 34 | 44.64 |
| gsm8k/pooled | pearl | 150 | 48584 | 28.484 | 0.2576 | 36 | 0.00 |
| gsm8k/pooled | picospec | 150 | 47809 | 30.034 | 0.2714 | 33 | 45.85 |
| gsm8k/pooled | pipesd | 150 | 48082 | 21.979 | 0.3418 | 34 | 0.00 |
| gsm8k/pooled | hf_default | 150 | 48091 | 19.183 | 0.3422 | 34 | 0.00 |
| mtbench/low | sync_g4 | 30 | 9064 | 18.448 | 0.3578 | 9 | 0.00 |
| mtbench/low | fixed_g2 | 30 | 8997 | 26.184 | 0.3082 | 9 | 15.41 |
| mtbench/low | fixed_fast | 30 | 9064 | 23.308 | 0.4704 | 9 | 8.16 |
| mtbench/low | fixed_g8 | 30 | 8905 | 16.195 | 0.7736 | 9 | 2.69 |
| mtbench/low | markov_w0_dist | 30 | 8990 | 26.170 | 0.2821 | 9 | 19.32 |
| mtbench/low | markov_w05_dist | 30 | 8961 | 26.060 | 0.2733 | 9 | 18.85 |
| mtbench/low | pearl | 30 | 9016 | 29.295 | 0.2483 | 10 | 0.00 |
| mtbench/low | picospec | 30 | 9064 | 25.555 | 0.4611 | 9 | 10.42 |
| mtbench/low | pipesd | 30 | 8902 | 15.806 | 0.4747 | 9 | 0.00 |
| mtbench/low | hf_default | 30 | 8938 | 15.506 | 0.4565 | 9 | 0.00 |
| mtbench/high | sync_g4 | 30 | 8961 | 10.112 | 0.5657 | 9 | 0.00 |
| mtbench/high | fixed_g2 | 30 | 8952 | 10.859 | 0.5673 | 10 | 15.44 |
| mtbench/high | fixed_fast | 30 | 8961 | 11.034 | 0.6316 | 9 | 8.43 |
| mtbench/high | fixed_g8 | 30 | 8908 | 10.406 | 0.8971 | 10 | 2.49 |
| mtbench/high | markov_w0_dist | 30 | 8936 | 11.911 | 0.7291 | 10 | 14.97 |
| mtbench/high | markov_w05_dist | 30 | 8937 | 10.478 | 0.5815 | 10 | 14.83 |
| mtbench/high | pearl | 30 | 9032 | 10.827 | 0.6842 | 10 | 0.00 |
| mtbench/high | picospec | 30 | 8961 | 11.039 | 0.6317 | 9 | 8.42 |
| mtbench/high | pipesd | 30 | 8962 | 9.279 | 0.7816 | 9 | 0.00 |
| mtbench/high | hf_default | 30 | 9014 | 8.818 | 0.6885 | 10 | 0.00 |
| mtbench/dynamic | sync_g4 | 30 | 8876 | 13.994 | 0.4382 | 9 | 0.00 |
| mtbench/dynamic | fixed_g2 | 30 | 8878 | 17.137 | 0.4045 | 9 | 15.31 |
| mtbench/dynamic | fixed_fast | 30 | 8876 | 15.446 | 0.5379 | 9 | 8.07 |
| mtbench/dynamic | fixed_g8 | 30 | 8758 | 13.013 | 0.8348 | 9 | 2.53 |
| mtbench/dynamic | markov_w0_dist | 30 | 8849 | 17.594 | 0.4291 | 9 | 17.13 |
| mtbench/dynamic | markov_w05_dist | 30 | 8906 | 17.467 | 0.3759 | 9 | 16.71 |
| mtbench/dynamic | pearl | 30 | 8793 | 16.773 | 0.4354 | 9 | 0.00 |
| mtbench/dynamic | picospec | 30 | 8876 | 16.176 | 0.5346 | 9 | 10.31 |
| mtbench/dynamic | pipesd | 30 | 8774 | 12.508 | 0.5886 | 9 | 0.00 |
| mtbench/dynamic | hf_default | 30 | 8793 | 11.334 | 0.5736 | 9 | 0.00 |
| mtbench/pooled | sync_g4 | 90 | 26901 | 13.372 | 0.4536 | 27 | 0.00 |
| mtbench/pooled | fixed_g2 | 90 | 26827 | 15.911 | 0.4265 | 28 | 15.38 |
| mtbench/pooled | fixed_fast | 90 | 26901 | 15.150 | 0.5463 | 27 | 8.22 |
| mtbench/pooled | fixed_g8 | 90 | 26571 | 12.781 | 0.8352 | 28 | 2.57 |
| mtbench/pooled | markov_w0_dist | 90 | 26775 | 16.769 | 0.4798 | 28 | 16.35 |
| mtbench/pooled | markov_w05_dist | 90 | 26804 | 15.705 | 0.4101 | 28 | 16.81 |
| mtbench/pooled | pearl | 90 | 26841 | 16.109 | 0.4563 | 29 | 0.00 |
| mtbench/pooled | picospec | 90 | 26901 | 15.684 | 0.5422 | 27 | 9.61 |
| mtbench/pooled | pipesd | 90 | 26638 | 11.943 | 0.6154 | 27 | 0.00 |
| mtbench/pooled | hf_default | 90 | 26745 | 11.264 | 0.5732 | 28 | 0.00 |
| humaneval/low | sync_g4 | 30 | 4675 | 34.073 | 0.1967 | 0 | 0.00 |
| humaneval/low | fixed_g2 | 30 | 4675 | 52.661 | 0.1482 | 0 | 61.27 |
| humaneval/low | fixed_fast | 30 | 4675 | 62.868 | 0.1474 | 0 | 69.69 |
| humaneval/low | fixed_g8 | 30 | 4675 | 67.259 | 0.1556 | 0 | 70.02 |
| humaneval/low | markov_w0_dist | 30 | 4675 | 60.737 | 0.1503 | 0 | 65.98 |
| humaneval/low | markov_w05_dist | 30 | 4675 | 54.502 | 0.1508 | 0 | 62.61 |
| humaneval/low | pearl | 30 | 4675 | 42.590 | 0.1740 | 0 | 0.00 |
| humaneval/low | picospec | 30 | 4675 | 62.194 | 0.1449 | 0 | 72.54 |
| humaneval/low | pipesd | 30 | 4675 | 43.019 | 0.1935 | 0 | 0.00 |
| humaneval/low | hf_default | 30 | 4670 | 36.103 | 0.2008 | 0 | 0.00 |
| humaneval/high | sync_g4 | 30 | 4651 | 19.070 | 0.2984 | 0 | 0.00 |
| humaneval/high | fixed_g2 | 30 | 4651 | 19.224 | 0.3110 | 0 | 61.46 |
| humaneval/high | fixed_fast | 30 | 4651 | 29.721 | 0.2262 | 0 | 70.05 |
| humaneval/high | fixed_g8 | 30 | 4675 | 44.788 | 0.1916 | 0 | 69.84 |
| humaneval/high | markov_w0_dist | 30 | 4646 | 41.914 | 0.1974 | 0 | 72.46 |
| humaneval/high | markov_w05_dist | 30 | 4646 | 39.758 | 0.1983 | 0 | 71.53 |
| humaneval/high | pearl | 30 | 4651 | 37.321 | 0.1951 | 0 | 0.00 |
| humaneval/high | picospec | 30 | 4651 | 29.748 | 0.2245 | 0 | 69.90 |
| humaneval/high | pipesd | 30 | 4675 | 33.260 | 0.2218 | 0 | 0.00 |
| humaneval/high | hf_default | 30 | 4670 | 24.573 | 0.2562 | 0 | 0.00 |
| humaneval/dynamic | sync_g4 | 30 | 4671 | 24.648 | 0.2450 | 0 | 0.00 |
| humaneval/dynamic | fixed_g2 | 30 | 4671 | 31.109 | 0.2156 | 0 | 61.15 |
| humaneval/dynamic | fixed_fast | 30 | 4671 | 40.373 | 0.1858 | 0 | 69.29 |
| humaneval/dynamic | fixed_g8 | 30 | 4671 | 52.354 | 0.1774 | 0 | 69.51 |
| humaneval/dynamic | markov_w0_dist | 30 | 4666 | 45.706 | 0.1835 | 0 | 68.42 |
| humaneval/dynamic | markov_w05_dist | 30 | 4671 | 42.282 | 0.1859 | 0 | 67.03 |
| humaneval/dynamic | pearl | 30 | 4671 | 35.603 | 0.1969 | 0 | 0.00 |
| humaneval/dynamic | picospec | 30 | 4671 | 40.253 | 0.1848 | 0 | 71.15 |
| humaneval/dynamic | pipesd | 30 | 4671 | 36.089 | 0.2097 | 0 | 0.00 |
| humaneval/dynamic | hf_default | 30 | 4666 | 27.913 | 0.2351 | 0 | 0.00 |
| humaneval/pooled | sync_g4 | 90 | 13997 | 24.530 | 0.2466 | 0 | 0.00 |
| humaneval/pooled | fixed_g2 | 90 | 13997 | 29.108 | 0.2248 | 0 | 61.29 |
| humaneval/pooled | fixed_fast | 90 | 13997 | 40.390 | 0.1864 | 0 | 69.67 |
| humaneval/pooled | fixed_g8 | 90 | 14021 | 53.290 | 0.1749 | 0 | 69.79 |
| humaneval/pooled | markov_w0_dist | 90 | 13987 | 48.247 | 0.1770 | 0 | 69.10 |
| humaneval/pooled | markov_w05_dist | 90 | 13992 | 44.688 | 0.1783 | 0 | 67.29 |
| humaneval/pooled | pearl | 90 | 13997 | 38.287 | 0.1886 | 0 | 0.00 |
| humaneval/pooled | picospec | 90 | 13997 | 40.273 | 0.1847 | 0 | 71.18 |
| humaneval/pooled | pipesd | 90 | 14021 | 37.028 | 0.2083 | 0 | 0.00 |
| humaneval/pooled | hf_default | 90 | 14006 | 28.786 | 0.2307 | 0 | 0.00 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|
| all/low | sync_g4 | 110 | -31.60 [-33.96, -29.46] | 8.97 [4.62, 12.53] | 2 | 0 |
| all/low | fixed_g2 | 110 | 0.82 [-2.12, 3.62] | 25.00 [22.07, 27.44] | 17 | 1 |
| all/low | fixed_g8 | 110 | -22.07 [-24.60, -19.18] | -47.89 [-52.50, -42.90] | 23 | 0 |
| all/low | markov_w0_dist | 110 | 1.26 [-2.00, 4.51] | 26.19 [21.85, 29.83] | 14 | 1 |
| all/low | markov_w05_dist | 110 | -4.65 [-8.58, -0.74] | 27.02 [22.61, 30.71] | 15 | 1 |
| all/low | pearl | 110 | -3.40 [-9.12, 2.03] | 28.71 [23.25, 33.14] | 20 | 3 |
| all/low | picospec | 110 | 7.62 [6.52, 8.75] | 2.14 [1.74, 2.54] | 0 | 0 |
| all/low | pipesd | 110 | -36.88 [-38.61, -35.10] | -15.73 [-20.44, -11.58] | 22 | 1 |
| all/low | hf_default | 110 | -39.94 [-42.72, -37.15] | -11.94 [-18.11, -6.33] | 23 | 1 |
| all/low | sync_g4_vs_fixed_g2 | 110 | -32.15 [-33.06, -31.18] | -21.37 [-22.74, -20.04] | 16 | 0 |
| all/low | fixed_fast_vs_fixed_g2 | 110 | -0.81 [-3.49, 2.17] | -33.33 [-37.81, -28.32] | 17 | 0 |
| all/low | fixed_g8_vs_fixed_g2 | 110 | -22.70 [-26.77, -17.78] | -97.19 [-109.32, -83.68] | 29 | 0 |
| all/low | markov_w0_dist_vs_fixed_g2 | 110 | 0.44 [-1.57, 2.63] | 1.59 [-0.58, 3.68] | 5 | 0 |
| all/low | markov_w05_dist_vs_fixed_g2 | 110 | -5.43 [-7.50, -3.14] | 2.69 [0.43, 4.89] | 8 | 0 |
| all/low | pearl_vs_fixed_g2 | 110 | -4.19 [-7.38, -0.93] | 4.96 [1.54, 8.16] | 10 | 2 |
| all/low | picospec_vs_fixed_g2 | 110 | 6.74 [4.10, 9.45] | -30.47 [-35.04, -25.45] | 17 | 0 |
| all/low | pipesd_vs_fixed_g2 | 110 | -37.39 [-38.71, -35.74] | -54.31 [-57.05, -51.64] | 24 | 0 |
| all/low | hf_default_vs_fixed_g2 | 110 | -40.43 [-43.05, -38.30] | -49.25 [-56.30, -44.15] | 26 | 0 |
| all/low | sync_g4_vs_fixed_g8 | 110 | -12.23 [-17.95, -6.91] | 38.45 [33.41, 42.43] | 24 | 0 |
| all/low | fixed_g2_vs_fixed_g8 | 110 | 29.37 [21.62, 36.56] | 49.29 [45.56, 52.23] | 29 | 1 |
| all/low | fixed_fast_vs_fixed_g8 | 110 | 28.32 [23.73, 32.62] | 32.38 [30.02, 34.43] | 23 | 0 |
| all/low | markov_w0_dist_vs_fixed_g8 | 110 | 29.93 [22.22, 37.23] | 50.09 [45.63, 53.75] | 28 | 1 |
| all/low | markov_w05_dist_vs_fixed_g8 | 110 | 22.35 [13.96, 30.58] | 50.65 [46.11, 54.34] | 30 | 1 |
| all/low | pearl_vs_fixed_g8 | 110 | 23.95 [13.19, 34.56] | 51.80 [46.51, 55.98] | 32 | 3 |
| all/low | picospec_vs_fixed_g8 | 110 | 38.09 [32.60, 43.10] | 33.83 [31.54, 35.79] | 23 | 0 |
| all/low | pipesd_vs_fixed_g8 | 110 | -19.01 [-23.12, -15.20] | 21.75 [16.19, 26.33] | 24 | 1 |
| all/low | hf_default_vs_fixed_g8 | 110 | -22.94 [-28.09, -17.56] | 24.31 [18.11, 29.71] | 25 | 1 |
| all/low | fixed_g2_vs_sync_g4 | 110 | 47.39 [45.31, 49.38] | 17.61 [16.69, 18.53] | 16 | 1 |
| all/low | fixed_fast_vs_sync_g4 | 110 | 46.19 [41.77, 51.43] | -9.86 [-14.32, -4.85] | 2 | 0 |
| all/low | fixed_g8_vs_sync_g4 | 110 | 13.93 [7.42, 21.88] | -62.47 [-73.69, -50.17] | 24 | 0 |
| all/low | markov_w0_dist_vs_sync_g4 | 110 | 48.03 [44.77, 51.58] | 18.91 [17.42, 20.37] | 13 | 1 |
| all/low | markov_w05_dist_vs_sync_g4 | 110 | 39.39 [36.46, 42.33] | 19.82 [18.31, 21.23] | 14 | 1 |
| all/low | pearl_vs_sync_g4 | 110 | 41.21 [37.40, 45.05] | 21.69 [19.48, 23.75] | 19 | 3 |
| all/low | picospec_vs_sync_g4 | 110 | 57.33 [52.94, 62.06] | -7.50 [-11.95, -2.60] | 2 | 0 |
| all/low | pipesd_vs_sync_g4 | 110 | -7.72 [-9.84, -5.21] | -27.14 [-29.50, -24.51] | 21 | 1 |
| all/low | hf_default_vs_sync_g4 | 110 | -12.20 [-16.06, -8.64] | -22.97 [-28.51, -18.49] | 23 | 1 |
| all/high | sync_g4 | 110 | -18.98 [-21.29, -16.89] | -2.13 [-5.38, 0.60] | 1 | 0 |
| all/high | fixed_g2 | 110 | -16.06 [-19.10, -13.27] | -5.23 [-9.23, -1.80] | 16 | 1 |
| all/high | fixed_g8 | 110 | 7.75 [4.20, 12.06] | -24.75 [-29.32, -19.67] | 26 | 1 |
| all/high | markov_w0_dist | 110 | 15.69 [13.64, 18.03] | -8.86 [-10.81, -6.58] | 20 | 1 |
| all/high | markov_w05_dist | 110 | 1.09 [-1.01, 3.52] | 4.54 [2.81, 6.34] | 21 | 1 |
| all/high | pearl | 110 | 4.04 [2.24, 6.22] | -3.19 [-4.86, -1.20] | 21 | 1 |
| all/high | picospec | 110 | 0.04 [-0.22, 0.35] | -0.02 [-0.26, 0.27] | 0 | 0 |
| all/high | pipesd | 110 | -12.06 [-13.44, -10.46] | -20.06 [-21.80, -18.12] | 20 | 0 |
| all/high | hf_default | 110 | -22.45 [-25.87, -19.68] | -15.04 [-20.88, -10.41] | 22 | 1 |
| all/high | sync_g4_vs_fixed_g2 | 110 | -3.48 [-4.36, -2.56] | 2.95 [2.18, 3.71] | 16 | 0 |
| all/high | fixed_fast_vs_fixed_g2 | 110 | 19.13 [15.30, 23.60] | 4.97 [1.76, 8.45] | 16 | 0 |
| all/high | fixed_g8_vs_fixed_g2 | 110 | 28.36 [20.33, 38.01] | -18.54 [-26.67, -9.72] | 31 | 0 |
| all/high | markov_w0_dist_vs_fixed_g2 | 110 | 37.82 [31.39, 45.62] | -3.45 [-8.52, 2.01] | 17 | 0 |
| all/high | markov_w05_dist_vs_fixed_g2 | 110 | 20.43 [14.77, 27.33] | 9.29 [6.80, 12.06] | 12 | 0 |
| all/high | pearl_vs_fixed_g2 | 110 | 23.94 [18.17, 30.97] | 1.95 [-2.60, 7.09] | 21 | 0 |
| all/high | picospec_vs_fixed_g2 | 110 | 19.18 [15.35, 23.61] | 4.96 [1.78, 8.46] | 16 | 0 |
| all/high | pipesd_vs_fixed_g2 | 110 | 4.76 [0.18, 10.31] | -14.09 [-19.00, -8.63] | 15 | 0 |
| all/high | hf_default_vs_fixed_g2 | 110 | -7.61 [-12.52, -3.24] | -9.32 [-15.73, -4.65] | 22 | 0 |
| all/high | sync_g4_vs_fixed_g8 | 110 | -24.80 [-29.62, -20.28] | 18.13 [12.08, 23.17] | 27 | 0 |
| all/high | fixed_g2_vs_fixed_g8 | 110 | -22.09 [-27.54, -16.89] | 15.64 [8.86, 21.05] | 31 | 0 |
| all/high | fixed_fast_vs_fixed_g8 | 110 | -7.19 [-10.76, -4.03] | 19.84 [16.44, 22.67] | 26 | 0 |
| all/high | markov_w0_dist_vs_fixed_g8 | 110 | 7.37 [4.87, 9.67] | 12.73 [10.34, 14.77] | 28 | 0 |
| all/high | markov_w05_dist_vs_fixed_g8 | 110 | -6.18 [-8.68, -3.68] | 23.48 [19.44, 26.82] | 25 | 0 |
| all/high | pearl_vs_fixed_g8 | 110 | -3.44 [-5.72, -1.37] | 17.28 [15.06, 19.19] | 24 | 0 |
| all/high | picospec_vs_fixed_g8 | 110 | -7.15 [-10.70, -3.97] | 19.83 [16.38, 22.65] | 26 | 0 |
| all/high | pipesd_vs_fixed_g8 | 110 | -18.38 [-20.71, -16.26] | 3.76 [0.61, 6.45] | 28 | 0 |
| all/high | hf_default_vs_fixed_g8 | 110 | -28.03 [-32.21, -23.88] | 7.78 [1.44, 13.43] | 27 | 0 |
| all/high | fixed_g2_vs_sync_g4 | 110 | 3.60 [2.62, 4.56] | -3.04 [-3.85, -2.23] | 16 | 1 |
| all/high | fixed_fast_vs_sync_g4 | 110 | 23.42 [20.32, 27.04] | 2.08 [-0.60, 5.11] | 1 | 0 |
| all/high | fixed_g8_vs_sync_g4 | 110 | 32.98 [25.43, 42.08] | -22.15 [-30.16, -13.74] | 27 | 1 |
| all/high | markov_w0_dist_vs_sync_g4 | 110 | 42.79 [36.98, 49.69] | -6.59 [-11.24, -1.47] | 20 | 1 |
| all/high | markov_w05_dist_vs_sync_g4 | 110 | 24.77 [19.70, 31.06] | 6.53 [4.27, 9.12] | 21 | 1 |
| all/high | pearl_vs_sync_g4 | 110 | 28.41 [23.33, 34.66] | -1.04 [-5.28, 3.80] | 21 | 1 |
| all/high | picospec_vs_sync_g4 | 110 | 23.47 [20.41, 27.15] | 2.07 [-0.63, 5.18] | 1 | 0 |
| all/high | pipesd_vs_sync_g4 | 110 | 8.54 [4.43, 13.58] | -17.56 [-22.10, -12.40] | 20 | 0 |
| all/high | hf_default_vs_sync_g4 | 110 | -4.28 [-9.17, -0.33] | -12.65 [-18.97, -8.12] | 22 | 1 |
| all/dynamic | sync_g4 | 110 | -21.95 [-24.89, -19.33] | 4.19 [0.12, 7.55] | 0 | 0 |
| all/dynamic | fixed_g2 | 110 | -2.87 [-6.31, 0.27] | 13.09 [9.49, 16.06] | 16 | 1 |
| all/dynamic | fixed_g8 | 110 | -4.91 [-7.93, -1.29] | -37.38 [-42.00, -32.02] | 19 | 0 |
| all/dynamic | markov_w0_dist | 110 | 9.84 [7.84, 12.01] | 10.94 [7.76, 13.92] | 16 | 1 |
| all/dynamic | markov_w05_dist | 110 | 2.99 [0.00, 6.05] | 16.82 [12.97, 20.21] | 15 | 0 |
| all/dynamic | pearl | 110 | 0.29 [-2.07, 2.54] | 11.21 [8.66, 13.49] | 15 | 1 |
| all/dynamic | picospec | 110 | 3.74 [3.02, 4.45] | 0.85 [0.50, 1.19] | 0 | 0 |
| all/dynamic | pipesd | 110 | -21.40 [-23.39, -19.38] | -16.01 [-18.82, -13.52] | 13 | 1 |
| all/dynamic | hf_default | 110 | -31.80 [-35.77, -28.32] | -17.56 [-24.67, -11.93] | 16 | 1 |
| all/dynamic | sync_g4_vs_fixed_g2 | 110 | -19.65 [-20.87, -18.38] | -10.25 [-11.43, -9.05] | 16 | 0 |
| all/dynamic | fixed_fast_vs_fixed_g2 | 110 | 2.95 [-0.27, 6.74] | -15.07 [-19.13, -10.48] | 16 | 0 |
| all/dynamic | fixed_g8_vs_fixed_g2 | 110 | -2.11 [-7.75, 4.96] | -58.08 [-68.78, -46.47] | 28 | 0 |
| all/dynamic | markov_w0_dist_vs_fixed_g2 | 110 | 13.08 [10.21, 16.52] | -2.48 [-4.16, -0.63] | 12 | 0 |
| all/dynamic | markov_w05_dist_vs_fixed_g2 | 110 | 6.03 [3.69, 8.76] | 4.28 [2.78, 5.82] | 12 | 0 |
| all/dynamic | pearl_vs_fixed_g2 | 110 | 3.25 [1.63, 4.95] | -2.17 [-3.62, -0.60] | 14 | 0 |
| all/dynamic | picospec_vs_fixed_g2 | 110 | 6.80 [3.67, 10.50] | -14.09 [-18.16, -9.51] | 16 | 0 |
| all/dynamic | pipesd_vs_fixed_g2 | 110 | -19.08 [-21.60, -16.06] | -33.49 [-36.79, -29.71] | 13 | 0 |
| all/dynamic | hf_default_vs_fixed_g2 | 110 | -29.78 [-34.01, -26.35] | -35.27 [-43.50, -29.42] | 20 | 0 |
| all/dynamic | sync_g4_vs_fixed_g8 | 110 | -17.92 [-23.45, -12.98] | 30.26 [24.56, 34.69] | 19 | 0 |
| all/dynamic | fixed_g2_vs_fixed_g8 | 110 | 2.15 [-4.73, 8.40] | 36.74 [31.73, 40.75] | 28 | 1 |
| all/dynamic | fixed_fast_vs_fixed_g8 | 110 | 5.17 [1.30, 8.61] | 27.21 [24.26, 29.58] | 19 | 0 |
| all/dynamic | markov_w0_dist_vs_fixed_g8 | 110 | 15.51 [10.22, 20.29] | 35.17 [30.46, 39.10] | 26 | 1 |
| all/dynamic | markov_w05_dist_vs_fixed_g8 | 110 | 8.31 [2.17, 14.00] | 39.45 [34.41, 43.64] | 27 | 0 |
| all/dynamic | pearl_vs_fixed_g8 | 110 | 5.47 [-0.42, 10.83] | 35.36 [31.10, 38.82] | 25 | 1 |
| all/dynamic | picospec_vs_fixed_g8 | 110 | 9.10 [4.60, 13.06] | 27.83 [24.89, 30.18] | 19 | 0 |
| all/dynamic | pipesd_vs_fixed_g8 | 110 | -17.34 [-20.99, -14.05] | 15.55 [10.60, 19.59] | 22 | 1 |
| all/dynamic | hf_default_vs_fixed_g8 | 110 | -28.27 [-32.90, -23.68] | 14.43 [7.92, 20.09] | 22 | 1 |
| all/dynamic | fixed_g2_vs_sync_g4 | 110 | 24.45 [22.52, 26.38] | 9.29 [8.30, 10.26] | 16 | 1 |
| all/dynamic | fixed_fast_vs_sync_g4 | 110 | 28.12 [23.96, 33.15] | -4.37 [-8.16, -0.12] | 0 | 0 |
| all/dynamic | fixed_g8_vs_sync_g4 | 110 | 21.83 [14.92, 30.63] | -43.38 [-53.11, -32.56] | 19 | 0 |
| all/dynamic | markov_w0_dist_vs_sync_g4 | 110 | 40.73 [37.06, 44.92] | 7.05 [5.24, 8.93] | 16 | 1 |
| all/dynamic | markov_w05_dist_vs_sync_g4 | 110 | 31.95 [29.10, 35.15] | 13.18 [11.83, 14.56] | 15 | 0 |
| all/dynamic | pearl_vs_sync_g4 | 110 | 28.50 [25.93, 31.43] | 7.32 [5.69, 9.07] | 15 | 1 |
| all/dynamic | picospec_vs_sync_g4 | 110 | 32.92 [28.68, 37.83] | -3.48 [-7.27, 0.78] | 0 | 0 |
| all/dynamic | pipesd_vs_sync_g4 | 110 | 0.71 [-2.05, 3.98] | -21.08 [-24.07, -17.60] | 13 | 1 |
| all/dynamic | hf_default_vs_sync_g4 | 110 | -12.61 [-17.63, -8.68] | -22.70 [-30.04, -17.55] | 16 | 1 |
| all/pooled | sync_g4 | 110 | -22.98 [-25.43, -20.80] | 3.05 [-0.77, 6.15] | 3 | 0 |
| all/pooled | fixed_g2 | 110 | -8.68 [-11.80, -5.87] | 9.31 [5.79, 12.30] | 49 | 3 |
| all/pooled | fixed_g8 | 110 | -4.28 [-7.28, -0.78] | -35.39 [-39.95, -30.36] | 68 | 1 |
| all/pooled | markov_w0_dist | 110 | 10.49 [9.29, 11.72] | 7.52 [5.83, 9.13] | 50 | 3 |
| all/pooled | markov_w05_dist | 110 | 0.46 [-1.18, 2.18] | 14.91 [12.02, 17.43] | 51 | 2 |
| all/pooled | pearl | 110 | 1.31 [-0.21, 2.81] | 10.62 [8.83, 12.19] | 56 | 5 |
| all/pooled | picospec | 110 | 2.78 [2.39, 3.13] | 0.87 [0.71, 1.05] | 0 | 0 |
| all/pooled | pipesd | 110 | -21.67 [-22.79, -20.46] | -17.51 [-19.50, -15.69] | 55 | 2 |
| all/pooled | hf_default | 110 | -29.92 [-33.21, -27.04] | -14.97 [-21.13, -9.91] | 61 | 3 |
| all/pooled | sync_g4_vs_fixed_g2 | 110 | -15.66 [-16.29, -15.02] | -6.90 [-7.48, -6.29] | 48 | 0 |
| all/pooled | fixed_fast_vs_fixed_g2 | 110 | 9.51 [6.24, 13.37] | -10.27 [-14.03, -6.14] | 49 | 0 |
| all/pooled | fixed_g8_vs_fixed_g2 | 110 | 4.82 [-1.29, 12.36] | -49.29 [-59.36, -38.43] | 88 | 0 |
| all/pooled | markov_w0_dist_vs_fixed_g2 | 110 | 20.99 [17.52, 25.18] | -1.97 [-4.23, 0.60] | 34 | 0 |
| all/pooled | markov_w05_dist_vs_fixed_g2 | 110 | 10.00 [7.27, 13.28] | 6.18 [5.16, 7.34] | 32 | 0 |
| all/pooled | pearl_vs_fixed_g2 | 110 | 10.94 [8.63, 13.50] | 1.45 [-0.41, 3.48] | 45 | 2 |
| all/pooled | picospec_vs_fixed_g2 | 110 | 12.55 [9.32, 16.29] | -9.30 [-13.04, -5.16] | 49 | 0 |
| all/pooled | pipesd_vs_fixed_g2 | 110 | -14.22 [-16.84, -11.10] | -29.57 [-32.81, -25.71] | 52 | 0 |
| all/pooled | hf_default_vs_fixed_g2 | 110 | -23.26 [-27.19, -20.09] | -26.77 [-33.59, -22.00] | 68 | 0 |
| all/pooled | sync_g4_vs_fixed_g8 | 110 | -19.54 [-24.75, -14.65] | 28.39 [22.78, 32.93] | 70 | 0 |
| all/pooled | fixed_g2_vs_fixed_g8 | 110 | -4.60 [-11.00, 1.31] | 33.02 [27.76, 37.25] | 88 | 2 |
| all/pooled | fixed_fast_vs_fixed_g8 | 110 | 4.47 [0.78, 7.85] | 26.14 [23.29, 28.54] | 68 | 0 |
| all/pooled | markov_w0_dist_vs_fixed_g8 | 110 | 15.42 [11.10, 19.32] | 31.70 [28.01, 34.77] | 82 | 2 |
| all/pooled | markov_w05_dist_vs_fixed_g8 | 110 | 4.95 [0.38, 9.29] | 37.15 [32.68, 40.84] | 82 | 1 |
| all/pooled | pearl_vs_fixed_g8 | 110 | 5.84 [0.88, 10.31] | 33.99 [30.17, 37.04] | 81 | 4 |
| all/pooled | picospec_vs_fixed_g8 | 110 | 7.37 [3.31, 11.05] | 26.79 [23.93, 29.17] | 68 | 0 |
| all/pooled | pipesd_vs_fixed_g8 | 110 | -18.16 [-21.28, -15.30] | 13.21 [8.75, 16.89] | 74 | 2 |
| all/pooled | hf_default_vs_fixed_g8 | 110 | -26.79 [-31.23, -22.29] | 15.09 [8.79, 20.56] | 74 | 2 |
| all/pooled | fixed_g2_vs_sync_g4 | 110 | 18.56 [17.68, 19.46] | 6.46 [5.91, 6.96] | 48 | 3 |
| all/pooled | fixed_fast_vs_sync_g4 | 110 | 29.84 [26.26, 34.11] | -3.15 [-6.55, 0.76] | 3 | 0 |
| all/pooled | fixed_g8_vs_sync_g4 | 110 | 24.28 [17.17, 32.90] | -39.65 [-49.10, -29.50] | 70 | 1 |
| all/pooled | markov_w0_dist_vs_sync_g4 | 110 | 43.45 [39.38, 48.19] | 4.61 [2.44, 7.14] | 49 | 3 |
| all/pooled | markov_w05_dist_vs_sync_g4 | 110 | 30.43 [27.31, 34.31] | 12.23 [11.04, 13.51] | 50 | 2 |
| all/pooled | pearl_vs_sync_g4 | 110 | 31.53 [28.99, 34.40] | 7.81 [5.99, 9.80] | 55 | 5 |
| all/pooled | picospec_vs_sync_g4 | 110 | 33.44 [29.91, 37.54] | -2.24 [-5.73, 1.65] | 3 | 0 |
| all/pooled | pipesd_vs_sync_g4 | 110 | 1.70 [-1.15, 5.26] | -21.20 [-24.36, -17.49] | 54 | 2 |
| all/pooled | hf_default_vs_sync_g4 | 110 | -9.01 [-13.59, -5.42] | -18.59 [-24.92, -14.08] | 61 | 3 |
| gsm8k/low | sync_g4 | 50 | -37.62 [-39.16, -35.86] | -0.51 [-3.30, 2.10] | 0 | 0 |
| gsm8k/low | fixed_g2 | 50 | -6.33 [-8.22, -3.90] | 18.38 [16.61, 20.19] | 4 | 1 |
| gsm8k/low | fixed_g8 | 50 | -16.17 [-18.42, -13.39] | -37.76 [-41.13, -34.26] | 10 | 0 |
| gsm8k/low | markov_w0_dist | 50 | -8.34 [-10.98, -5.14] | 15.06 [12.70, 17.20] | 3 | 1 |
| gsm8k/low | markov_w05_dist | 50 | -16.99 [-19.13, -14.42] | 14.86 [12.62, 17.12] | 4 | 1 |
| gsm8k/low | pearl | 50 | -17.62 [-20.17, -14.75] | 15.66 [12.68, 18.44] | 5 | 2 |
| gsm8k/low | picospec | 50 | 7.42 [5.98, 9.47] | 2.45 [1.88, 3.20] | 0 | 0 |
| gsm8k/low | pipesd | 50 | -42.71 [-44.18, -40.97] | -30.88 [-33.59, -28.00] | 11 | 1 |
| gsm8k/low | hf_default | 50 | -45.65 [-47.47, -43.80] | -25.34 [-29.70, -21.39] | 11 | 1 |
| gsm8k/low | sync_g4_vs_fixed_g2 | 50 | -33.40 [-34.29, -32.47] | -23.14 [-24.69, -21.76] | 4 | 0 |
| gsm8k/low | fixed_fast_vs_fixed_g2 | 50 | 6.75 [4.05, 8.96] | -22.51 [-25.30, -19.92] | 4 | 0 |
| gsm8k/low | fixed_g8_vs_fixed_g2 | 50 | -10.51 [-13.61, -7.16] | -68.78 [-75.84, -61.54] | 11 | 0 |
| gsm8k/low | markov_w0_dist_vs_fixed_g2 | 50 | -2.15 [-4.69, 0.47] | -4.07 [-5.63, -2.69] | 1 | 0 |
| gsm8k/low | markov_w05_dist_vs_fixed_g2 | 50 | -11.38 [-13.10, -9.38] | -4.30 [-5.49, -3.22] | 2 | 0 |
| gsm8k/low | pearl_vs_fixed_g2 | 50 | -12.05 [-13.62, -10.48] | -3.33 [-5.25, -1.54] | 3 | 1 |
| gsm8k/low | picospec_vs_fixed_g2 | 50 | 14.68 [12.92, 16.37] | -19.51 [-22.15, -16.93] | 4 | 0 |
| gsm8k/low | pipesd_vs_fixed_g2 | 50 | -38.84 [-40.54, -36.92] | -60.34 [-63.90, -56.77] | 11 | 0 |
| gsm8k/low | hf_default_vs_fixed_g2 | 50 | -41.98 [-43.57, -40.32] | -53.56 [-57.58, -49.69] | 11 | 0 |
| gsm8k/low | sync_g4_vs_fixed_g8 | 50 | -25.58 [-28.71, -22.56] | 27.04 [23.33, 30.40] | 10 | 0 |
| gsm8k/low | fixed_g2_vs_fixed_g8 | 50 | 11.74 [7.71, 15.75] | 40.75 [38.10, 43.13] | 11 | 1 |
| gsm8k/low | fixed_fast_vs_fixed_g8 | 50 | 19.29 [15.45, 22.59] | 27.41 [25.51, 29.14] | 10 | 0 |
| gsm8k/low | markov_w0_dist_vs_fixed_g8 | 50 | 9.34 [5.23, 13.40] | 38.34 [35.29, 41.02] | 11 | 1 |
| gsm8k/low | markov_w05_dist_vs_fixed_g8 | 50 | -0.97 [-4.74, 2.86] | 38.20 [35.19, 41.03] | 12 | 1 |
| gsm8k/low | pearl_vs_fixed_g8 | 50 | -1.73 [-6.38, 3.15] | 38.78 [35.23, 42.02] | 12 | 2 |
| gsm8k/low | picospec_vs_fixed_g8 | 50 | 28.14 [24.64, 31.47] | 29.19 [27.54, 30.69] | 10 | 0 |
| gsm8k/low | pipesd_vs_fixed_g8 | 50 | -31.66 [-33.42, -29.68] | 5.00 [1.67, 8.44] | 7 | 1 |
| gsm8k/low | hf_default_vs_fixed_g8 | 50 | -35.17 [-37.95, -32.48] | 9.02 [4.34, 12.89] | 10 | 1 |
| gsm8k/low | fixed_g2_vs_sync_g4 | 50 | 50.15 [48.09, 52.19] | 18.79 [17.87, 19.80] | 4 | 1 |
| gsm8k/low | fixed_fast_vs_sync_g4 | 50 | 60.30 [55.92, 64.36] | 0.51 [-2.14, 3.19] | 0 | 0 |
| gsm8k/low | fixed_g8_vs_sync_g4 | 50 | 34.38 [29.14, 40.28] | -37.07 [-43.67, -30.43] | 10 | 0 |
| gsm8k/low | markov_w0_dist_vs_sync_g4 | 50 | 46.93 [42.63, 51.51] | 15.49 [14.09, 16.78] | 3 | 1 |
| gsm8k/low | markov_w05_dist_vs_sync_g4 | 50 | 33.07 [29.97, 36.65] | 15.30 [14.29, 16.27] | 4 | 1 |
| gsm8k/low | pearl_vs_sync_g4 | 50 | 32.06 [29.82, 34.12] | 16.09 [14.91, 17.16] | 5 | 2 |
| gsm8k/low | picospec_vs_sync_g4 | 50 | 72.19 [68.59, 75.84] | 2.94 [0.32, 5.61] | 0 | 0 |
| gsm8k/low | pipesd_vs_sync_g4 | 50 | -8.17 [-10.94, -5.00] | -30.21 [-33.74, -26.67] | 11 | 1 |
| gsm8k/low | hf_default_vs_sync_g4 | 50 | -12.89 [-15.73, -9.95] | -24.71 [-28.49, -21.14] | 11 | 1 |
| gsm8k/high | sync_g4 | 50 | -24.20 [-25.34, -23.13] | -9.67 [-11.58, -7.94] | 0 | 0 |
| gsm8k/high | fixed_g2 | 50 | -23.30 [-24.74, -22.01] | -15.34 [-17.57, -13.40] | 6 | 0 |
| gsm8k/high | fixed_g8 | 50 | 18.20 [14.95, 21.62] | -14.67 [-17.95, -11.35] | 10 | 0 |
| gsm8k/high | markov_w0_dist | 50 | 20.26 [18.05, 22.69] | -6.24 [-8.24, -4.14] | 7 | 0 |
| gsm8k/high | markov_w05_dist | 50 | 2.94 [0.04, 6.02] | -0.69 [-2.13, 0.74] | 10 | 0 |
| gsm8k/high | pearl | 50 | 7.51 [5.60, 9.53] | -0.67 [-2.33, 1.03] | 7 | 0 |
| gsm8k/high | picospec | 50 | 0.02 [-0.46, 0.62] | -0.17 [-0.65, 0.39] | 0 | 0 |
| gsm8k/high | pipesd | 50 | -11.60 [-13.32, -9.72] | -20.43 [-22.48, -18.21] | 7 | 0 |
| gsm8k/high | hf_default | 50 | -25.52 [-26.74, -24.35] | -21.59 [-23.94, -19.46] | 7 | 0 |
| gsm8k/high | sync_g4_vs_fixed_g2 | 50 | -1.16 [-1.87, -0.36] | 4.91 [4.28, 5.57] | 6 | 0 |
| gsm8k/high | fixed_fast_vs_fixed_g2 | 50 | 30.39 [28.22, 32.88] | 13.30 [11.81, 14.94] | 6 | 0 |
| gsm8k/high | fixed_g8_vs_fixed_g2 | 50 | 54.11 [48.04, 60.72] | 0.58 [-3.76, 4.96] | 11 | 0 |
| gsm8k/high | markov_w0_dist_vs_fixed_g2 | 50 | 56.80 [51.79, 62.13] | 7.89 [4.80, 11.07] | 7 | 0 |
| gsm8k/high | markov_w05_dist_vs_fixed_g2 | 50 | 34.21 [29.05, 39.61] | 12.70 [10.70, 14.67] | 6 | 0 |
| gsm8k/high | pearl_vs_fixed_g2 | 50 | 40.18 [35.92, 44.58] | 12.72 [10.04, 15.43] | 7 | 0 |
| gsm8k/high | picospec_vs_fixed_g2 | 50 | 30.41 [28.23, 32.77] | 13.15 [11.58, 14.82] | 6 | 0 |
| gsm8k/high | pipesd_vs_fixed_g2 | 50 | 15.26 [11.82, 18.79] | -4.41 [-7.43, -1.34] | 7 | 0 |
| gsm8k/high | hf_default_vs_fixed_g2 | 50 | -2.89 [-4.89, -0.79] | -5.42 [-7.62, -3.23] | 7 | 0 |
| gsm8k/high | sync_g4_vs_fixed_g8 | 50 | -35.87 [-38.41, -33.26] | 4.36 [0.04, 8.41] | 10 | 0 |
| gsm8k/high | fixed_g2_vs_fixed_g8 | 50 | -35.11 [-37.78, -32.45] | -0.58 [-5.22, 3.62] | 11 | 0 |
| gsm8k/high | fixed_fast_vs_fixed_g8 | 50 | -15.39 [-17.78, -13.01] | 12.79 [10.19, 15.22] | 10 | 0 |
| gsm8k/high | markov_w0_dist_vs_fixed_g8 | 50 | 1.75 [0.04, 3.40] | 7.35 [5.65, 8.99] | 10 | 0 |
| gsm8k/high | markov_w05_dist_vs_fixed_g8 | 50 | -12.91 [-14.72, -11.06] | 12.19 [9.74, 14.59] | 5 | 0 |
| gsm8k/high | pearl_vs_fixed_g8 | 50 | -9.04 [-10.62, -7.42] | 12.21 [10.41, 13.91] | 7 | 0 |
| gsm8k/high | picospec_vs_fixed_g8 | 50 | -15.38 [-17.69, -13.00] | 12.65 [10.10, 15.11] | 10 | 0 |
| gsm8k/high | pipesd_vs_fixed_g8 | 50 | -25.21 [-27.08, -23.32] | -5.02 [-7.77, -2.39] | 9 | 0 |
| gsm8k/high | hf_default_vs_fixed_g8 | 50 | -36.99 [-39.00, -34.89] | -6.04 [-10.16, -2.12] | 10 | 0 |
| gsm8k/high | fixed_g2_vs_sync_g4 | 50 | 1.18 [0.36, 1.90] | -5.17 [-5.90, -4.47] | 6 | 0 |
| gsm8k/high | fixed_fast_vs_sync_g4 | 50 | 31.92 [30.10, 33.94] | 8.82 [7.35, 10.37] | 0 | 0 |
| gsm8k/high | fixed_g8_vs_sync_g4 | 50 | 55.92 [49.83, 62.37] | -4.56 [-9.18, -0.04] | 10 | 0 |
| gsm8k/high | markov_w0_dist_vs_sync_g4 | 50 | 58.65 [53.75, 63.84] | 3.13 [-0.11, 6.46] | 7 | 0 |
| gsm8k/high | markov_w05_dist_vs_sync_g4 | 50 | 35.79 [30.69, 41.27] | 8.19 [6.08, 10.35] | 10 | 0 |
| gsm8k/high | pearl_vs_sync_g4 | 50 | 41.83 [37.80, 46.12] | 8.21 [5.47, 11.02] | 7 | 0 |
| gsm8k/high | picospec_vs_sync_g4 | 50 | 31.95 [30.15, 33.83] | 8.67 [7.18, 10.20] | 0 | 0 |
| gsm8k/high | pipesd_vs_sync_g4 | 50 | 16.62 [13.20, 20.15] | -9.81 [-13.03, -6.54] | 7 | 0 |
| gsm8k/high | hf_default_vs_sync_g4 | 50 | -1.75 [-3.62, 0.23] | -10.87 [-13.14, -8.64] | 7 | 0 |
| gsm8k/dynamic | sync_g4 | 50 | -28.49 [-30.14, -26.80] | -4.66 [-7.07, -2.48] | 0 | 0 |
| gsm8k/dynamic | fixed_g2 | 50 | -10.25 [-12.14, -8.23] | 5.61 [3.07, 8.01] | 5 | 1 |
| gsm8k/dynamic | fixed_g8 | 50 | 2.81 [-0.67, 6.26] | -26.92 [-30.71, -23.16] | 8 | 0 |
| gsm8k/dynamic | markov_w0_dist | 50 | 4.50 [2.53, 6.55] | 2.04 [0.27, 3.95] | 5 | 1 |
| gsm8k/dynamic | markov_w05_dist | 50 | -6.54 [-9.08, -4.25] | 5.24 [3.10, 7.10] | 4 | 0 |
| gsm8k/dynamic | pearl | 50 | -5.39 [-6.80, -3.96] | 5.29 [3.38, 7.09] | 6 | 1 |
| gsm8k/dynamic | picospec | 50 | 3.60 [2.51, 4.80] | 1.20 [0.63, 1.72] | 0 | 0 |
| gsm8k/dynamic | pipesd | 50 | -26.32 [-29.00, -23.62] | -24.97 [-27.60, -22.63] | 5 | 1 |
| gsm8k/dynamic | hf_default | 50 | -37.24 [-39.46, -34.96] | -28.75 [-32.51, -25.25] | 5 | 1 |
| gsm8k/dynamic | sync_g4_vs_fixed_g2 | 50 | -20.33 [-22.44, -18.39] | -10.88 [-12.81, -9.03] | 5 | 0 |
| gsm8k/dynamic | fixed_fast_vs_fixed_g2 | 50 | 11.42 [8.97, 13.82] | -5.94 [-8.70, -3.17] | 5 | 0 |
| gsm8k/dynamic | fixed_g8_vs_fixed_g2 | 50 | 14.55 [9.12, 20.17] | -34.46 [-41.61, -27.64] | 10 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_fixed_g2 | 50 | 16.43 [12.68, 20.34] | -3.78 [-5.91, -1.60] | 7 | 0 |
| gsm8k/dynamic | markov_w05_dist_vs_fixed_g2 | 50 | 4.14 [0.43, 8.09] | -0.39 [-2.24, 1.41] | 6 | 0 |
| gsm8k/dynamic | pearl_vs_fixed_g2 | 50 | 5.41 [3.89, 6.94] | -0.34 [-1.58, 0.93] | 4 | 0 |
| gsm8k/dynamic | picospec_vs_fixed_g2 | 50 | 15.43 [13.08, 17.90] | -4.67 [-7.34, -2.04] | 5 | 0 |
| gsm8k/dynamic | pipesd_vs_fixed_g2 | 50 | -17.91 [-21.68, -14.21] | -32.39 [-37.06, -28.14] | 5 | 0 |
| gsm8k/dynamic | hf_default_vs_fixed_g2 | 50 | -30.07 [-32.98, -27.22] | -36.40 [-41.21, -32.07] | 4 | 0 |
| gsm8k/dynamic | sync_g4_vs_fixed_g8 | 50 | -30.45 [-33.07, -27.74] | 17.54 [13.47, 21.30] | 8 | 0 |
| gsm8k/dynamic | fixed_g2_vs_fixed_g8 | 50 | -12.70 [-16.79, -8.35] | 25.63 [21.65, 29.38] | 10 | 1 |
| gsm8k/dynamic | fixed_fast_vs_fixed_g8 | 50 | -2.74 [-5.89, 0.68] | 21.21 [18.80, 23.50] | 8 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_fixed_g8 | 50 | 1.64 [-0.91, 4.40] | 22.82 [19.52, 26.13] | 9 | 1 |
| gsm8k/dynamic | markov_w05_dist_vs_fixed_g8 | 50 | -9.09 [-11.92, -6.33] | 25.34 [21.72, 28.64] | 10 | 0 |
| gsm8k/dynamic | pearl_vs_fixed_g8 | 50 | -7.98 [-11.80, -3.74] | 25.38 [21.88, 28.77] | 10 | 1 |
| gsm8k/dynamic | picospec_vs_fixed_g8 | 50 | 0.76 [-3.06, 4.98] | 22.15 [19.71, 24.53] | 8 | 0 |
| gsm8k/dynamic | pipesd_vs_fixed_g8 | 50 | -28.34 [-30.55, -26.21] | 1.54 [-1.75, 4.77] | 9 | 1 |
| gsm8k/dynamic | hf_default_vs_fixed_g8 | 50 | -38.96 [-41.06, -36.87] | -1.44 [-6.00, 2.47] | 9 | 1 |
| gsm8k/dynamic | fixed_g2_vs_sync_g4 | 50 | 25.51 [22.53, 28.94] | 9.81 [8.28, 11.36] | 5 | 1 |
| gsm8k/dynamic | fixed_fast_vs_sync_g4 | 50 | 39.84 [36.61, 43.15] | 4.45 [2.42, 6.60] | 0 | 0 |
| gsm8k/dynamic | fixed_g8_vs_sync_g4 | 50 | 43.78 [38.39, 49.41] | -21.27 [-27.06, -15.56] | 8 | 0 |
| gsm8k/dynamic | markov_w0_dist_vs_sync_g4 | 50 | 46.13 [42.50, 49.81] | 6.40 [4.46, 8.33] | 5 | 1 |
| gsm8k/dynamic | markov_w05_dist_vs_sync_g4 | 50 | 30.70 [27.25, 34.25] | 9.46 [7.92, 10.91] | 4 | 0 |
| gsm8k/dynamic | pearl_vs_sync_g4 | 50 | 32.30 [29.16, 35.85] | 9.51 [8.12, 10.93] | 6 | 1 |
| gsm8k/dynamic | picospec_vs_sync_g4 | 50 | 44.88 [41.06, 49.06] | 5.60 [3.52, 7.73] | 0 | 0 |
| gsm8k/dynamic | pipesd_vs_sync_g4 | 50 | 3.04 [-0.05, 6.20] | -19.40 [-22.66, -16.33] | 5 | 1 |
| gsm8k/dynamic | hf_default_vs_sync_g4 | 50 | -12.23 [-14.54, -9.91] | -23.02 [-26.16, -20.00] | 5 | 1 |
| gsm8k/pooled | sync_g4 | 50 | -28.79 [-29.93, -27.64] | -5.52 [-7.67, -3.49] | 0 | 0 |
| gsm8k/pooled | fixed_g2 | 50 | -16.00 [-17.48, -14.59] | 0.93 [-1.09, 2.79] | 15 | 2 |
| gsm8k/pooled | fixed_g8 | 50 | 4.21 [1.51, 7.05] | -25.01 [-28.28, -21.76] | 28 | 0 |
| gsm8k/pooled | markov_w0_dist | 50 | 8.11 [6.82, 9.59] | 2.46 [1.57, 3.30] | 15 | 2 |
| gsm8k/pooled | markov_w05_dist | 50 | -4.80 [-6.37, -3.04] | 5.65 [4.32, 6.86] | 18 | 1 |
| gsm8k/pooled | pearl | 50 | -2.66 [-3.74, -1.46] | 6.05 [4.95, 7.08] | 18 | 3 |
| gsm8k/pooled | picospec | 50 | 2.64 [2.07, 3.25] | 1.00 [0.69, 1.31] | 0 | 0 |
| gsm8k/pooled | pipesd | 50 | -24.89 [-26.40, -23.33] | -24.68 [-26.46, -23.00] | 23 | 2 |
| gsm8k/pooled | hf_default | 50 | -34.44 [-35.89, -33.07] | -24.82 [-27.74, -22.19] | 23 | 2 |
| gsm8k/pooled | sync_g4_vs_fixed_g2 | 50 | -15.22 [-16.05, -14.34] | -6.51 [-7.27, -5.73] | 15 | 0 |
| gsm8k/pooled | fixed_fast_vs_fixed_g2 | 50 | 19.05 [17.08, 21.18] | -0.94 [-2.87, 1.07] | 15 | 0 |
| gsm8k/pooled | fixed_g8_vs_fixed_g2 | 50 | 24.06 [19.31, 29.11] | -26.18 [-31.75, -20.66] | 32 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_fixed_g2 | 50 | 28.70 [25.77, 32.01] | 1.55 [-0.22, 3.39] | 15 | 0 |
| gsm8k/pooled | markov_w05_dist_vs_fixed_g2 | 50 | 13.33 [10.43, 16.47] | 4.77 [3.59, 5.96] | 14 | 0 |
| gsm8k/pooled | pearl_vs_fixed_g2 | 50 | 15.88 [14.39, 17.47] | 5.17 [4.03, 6.34] | 14 | 1 |
| gsm8k/pooled | picospec_vs_fixed_g2 | 50 | 22.19 [20.42, 24.07] | 0.07 [-1.90, 2.14] | 15 | 0 |
| gsm8k/pooled | pipesd_vs_fixed_g2 | 50 | -10.58 [-13.26, -7.90] | -25.85 [-29.01, -22.77] | 23 | 0 |
| gsm8k/pooled | hf_default_vs_fixed_g2 | 50 | -21.96 [-23.84, -20.00] | -25.99 [-29.04, -23.25] | 22 | 0 |
| gsm8k/pooled | sync_g4_vs_fixed_g8 | 50 | -31.66 [-34.21, -29.09] | 15.59 [11.70, 19.13] | 28 | 0 |
| gsm8k/pooled | fixed_g2_vs_fixed_g8 | 50 | -19.39 [-22.54, -16.19] | 20.75 [17.12, 24.10] | 32 | 2 |
| gsm8k/pooled | fixed_fast_vs_fixed_g8 | 50 | -4.04 [-6.59, -1.49] | 20.01 [17.87, 22.05] | 28 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_fixed_g8 | 50 | 3.74 [1.63, 5.92] | 21.98 [19.69, 24.29] | 30 | 2 |
| gsm8k/pooled | markov_w05_dist_vs_fixed_g8 | 50 | -8.65 [-10.75, -6.63] | 24.53 [21.74, 27.23] | 27 | 1 |
| gsm8k/pooled | pearl_vs_fixed_g8 | 50 | -6.59 [-9.46, -3.60] | 24.84 [22.11, 27.44] | 29 | 3 |
| gsm8k/pooled | picospec_vs_fixed_g8 | 50 | -1.51 [-4.16, 1.31] | 20.80 [18.77, 22.78] | 28 | 0 |
| gsm8k/pooled | pipesd_vs_fixed_g8 | 50 | -27.92 [-29.68, -26.17] | 0.26 [-2.64, 3.19] | 25 | 2 |
| gsm8k/pooled | hf_default_vs_fixed_g8 | 50 | -37.09 [-39.11, -35.07] | 0.15 [-4.10, 3.78] | 29 | 2 |
| gsm8k/pooled | fixed_g2_vs_sync_g4 | 50 | 17.96 [16.74, 19.11] | 6.11 [5.42, 6.77] | 15 | 2 |
| gsm8k/pooled | fixed_fast_vs_sync_g4 | 50 | 40.43 [38.19, 42.72] | 5.23 [3.38, 7.12] | 0 | 0 |
| gsm8k/pooled | fixed_g8_vs_sync_g4 | 50 | 46.34 [41.02, 52.01] | -18.47 [-23.66, -13.25] | 28 | 0 |
| gsm8k/pooled | markov_w0_dist_vs_sync_g4 | 50 | 51.81 [48.70, 55.40] | 7.57 [5.78, 9.34] | 15 | 2 |
| gsm8k/pooled | markov_w05_dist_vs_sync_g4 | 50 | 33.68 [30.40, 37.27] | 10.59 [9.37, 11.87] | 18 | 1 |
| gsm8k/pooled | pearl_vs_sync_g4 | 50 | 36.69 [34.95, 38.58] | 10.97 [9.80, 12.22] | 18 | 3 |
| gsm8k/pooled | picospec_vs_sync_g4 | 50 | 44.13 [41.92, 46.36] | 6.18 [4.28, 8.12] | 0 | 0 |
| gsm8k/pooled | pipesd_vs_sync_g4 | 50 | 5.48 [2.73, 8.30] | -18.16 [-21.09, -15.27] | 23 | 2 |
| gsm8k/pooled | hf_default_vs_sync_g4 | 50 | -7.94 [-9.95, -5.92] | -18.29 [-20.93, -15.82] | 23 | 2 |
| mtbench/low | sync_g4 | 30 | -20.85 [-22.23, -19.20] | 23.92 [22.11, 25.29] | 2 | 0 |
| mtbench/low | fixed_g2 | 30 | 12.34 [9.57, 15.37] | 34.48 [32.78, 35.84] | 13 | 0 |
| mtbench/low | fixed_g8 | 30 | -30.52 [-32.42, -28.32] | -64.48 [-68.24, -60.11] | 13 | 0 |
| mtbench/low | markov_w0_dist | 30 | 12.28 [8.57, 16.29] | 40.03 [36.97, 42.61] | 11 | 0 |
| mtbench/low | markov_w05_dist | 30 | 11.80 [7.63, 16.24] | 41.90 [39.05, 44.25] | 10 | 0 |
| mtbench/low | pearl | 30 | 25.68 [20.72, 30.91] | 47.21 [44.31, 49.47] | 14 | 1 |
| mtbench/low | picospec | 30 | 9.64 [8.27, 11.44] | 1.96 [1.35, 2.61] | 0 | 0 |
| mtbench/low | pipesd | 30 | -32.19 [-33.95, -30.12] | -0.92 [-4.30, 2.03] | 10 | 0 |
| mtbench/low | hf_default | 30 | -33.47 [-39.26, -28.22] | 2.94 [-7.08, 10.07] | 11 | 0 |
| mtbench/low | sync_g4_vs_fixed_g2 | 30 | -29.54 [-30.96, -27.80] | -16.11 [-17.66, -14.20] | 12 | 0 |
| mtbench/low | fixed_fast_vs_fixed_g2 | 30 | -10.98 [-13.33, -8.73] | -52.62 [-55.87, -48.77] | 13 | 0 |
| mtbench/low | fixed_g8_vs_fixed_g2 | 30 | -38.15 [-40.69, -35.28] | -151.03 [-160.05, -140.65] | 18 | 0 |
| mtbench/low | markov_w0_dist_vs_fixed_g2 | 30 | -0.05 [-3.28, 3.38] | 8.47 [5.23, 11.60] | 4 | 0 |
| mtbench/low | markov_w05_dist_vs_fixed_g2 | 30 | -0.48 [-4.18, 3.29] | 11.33 [8.47, 14.01] | 5 | 0 |
| mtbench/low | pearl_vs_fixed_g2 | 30 | 11.88 [8.17, 16.16] | 19.43 [16.66, 22.03] | 6 | 1 |
| mtbench/low | picospec_vs_fixed_g2 | 30 | -2.40 [-5.38, 0.75] | -49.63 [-53.14, -45.39] | 13 | 0 |
| mtbench/low | pipesd_vs_fixed_g2 | 30 | -39.64 [-41.08, -37.72] | -54.02 [-57.38, -50.13] | 12 | 0 |
| mtbench/low | hf_default_vs_fixed_g2 | 30 | -40.78 [-45.90, -36.36] | -48.14 [-63.07, -37.54] | 14 | 0 |
| mtbench/low | sync_g4_vs_fixed_g8 | 30 | 13.92 [10.30, 17.26] | 53.74 [51.90, 55.19] | 14 | 0 |
| mtbench/low | fixed_g2_vs_fixed_g8 | 30 | 61.68 [54.52, 68.60] | 60.16 [58.45, 61.55] | 18 | 0 |
| mtbench/low | fixed_fast_vs_fixed_g8 | 30 | 43.93 [39.51, 47.98] | 39.20 [37.54, 40.56] | 13 | 0 |
| mtbench/low | markov_w0_dist_vs_fixed_g8 | 30 | 61.60 [53.63, 68.86] | 63.54 [61.30, 65.35] | 17 | 0 |
| mtbench/low | markov_w05_dist_vs_fixed_g8 | 30 | 60.91 [52.11, 68.67] | 64.68 [62.60, 66.32] | 17 | 0 |
| mtbench/low | pearl_vs_fixed_g8 | 30 | 80.89 [70.97, 89.92] | 67.90 [65.85, 69.53] | 19 | 1 |
| mtbench/low | picospec_vs_fixed_g8 | 30 | 57.80 [53.41, 61.52] | 40.39 [38.85, 41.68] | 13 | 0 |
| mtbench/low | pipesd_vs_fixed_g8 | 30 | -2.40 [-5.67, 1.01] | 38.64 [35.93, 40.95] | 16 | 0 |
| mtbench/low | hf_default_vs_fixed_g8 | 30 | -4.25 [-13.31, 4.65] | 40.99 [34.55, 45.99] | 14 | 0 |
| mtbench/low | fixed_g2_vs_sync_g4 | 30 | 41.93 [38.51, 44.85] | 13.88 [12.43, 15.01] | 12 | 0 |
| mtbench/low | fixed_fast_vs_sync_g4 | 30 | 26.34 [23.76, 28.59] | -31.44 [-33.85, -28.39] | 2 | 0 |
| mtbench/low | fixed_g8_vs_sync_g4 | 30 | -12.22 [-14.72, -9.34] | -116.19 [-123.18, -107.90] | 14 | 0 |
| mtbench/low | markov_w0_dist_vs_sync_g4 | 30 | 41.86 [37.27, 45.70] | 21.17 [18.40, 23.51] | 10 | 0 |
| mtbench/low | markov_w05_dist_vs_sync_g4 | 30 | 41.26 [36.28, 45.58] | 23.64 [21.18, 25.78] | 9 | 0 |
| mtbench/low | pearl_vs_sync_g4 | 30 | 58.79 [53.48, 63.64] | 30.61 [28.25, 32.63] | 13 | 1 |
| mtbench/low | picospec_vs_sync_g4 | 30 | 38.52 [35.55, 41.35] | -28.87 [-31.54, -25.63] | 2 | 0 |
| mtbench/low | pipesd_vs_sync_g4 | 30 | -14.33 [-15.74, -12.84] | -32.65 [-34.96, -30.48] | 9 | 0 |
| mtbench/low | hf_default_vs_sync_g4 | 30 | -15.95 [-23.57, -9.36] | -27.58 [-40.50, -18.52] | 11 | 0 |
| mtbench/high | sync_g4 | 30 | -8.35 [-9.68, -7.12] | 10.44 [9.00, 11.58] | 1 | 0 |
| mtbench/high | fixed_g2 | 30 | -1.58 [-4.04, 0.74] | 10.18 [7.92, 12.16] | 10 | 1 |
| mtbench/high | fixed_g8 | 30 | -5.68 [-7.48, -3.58] | -42.03 [-45.34, -38.01] | 15 | 1 |
| mtbench/high | markov_w0_dist | 30 | 7.95 [6.58, 9.21] | -15.43 [-17.07, -13.49] | 12 | 1 |
| mtbench/high | markov_w05_dist | 30 | -5.04 [-6.86, -3.16] | 7.93 [5.12, 10.41] | 10 | 1 |
| mtbench/high | pearl | 30 | -1.87 [-3.45, -0.18] | -8.33 [-10.11, -6.24] | 14 | 1 |
| mtbench/high | picospec | 30 | 0.05 [-0.24, 0.35] | -0.02 [-0.29, 0.28] | 0 | 0 |
| mtbench/high | pipesd | 30 | -15.90 [-17.19, -14.68] | -23.74 [-25.86, -21.67] | 11 | 0 |
| mtbench/high | hf_default | 30 | -20.08 [-27.60, -14.28] | -9.00 [-21.57, -0.76] | 13 | 1 |
| mtbench/high | sync_g4_vs_fixed_g2 | 30 | -6.88 [-7.92, -5.66] | 0.28 [-0.79, 1.44] | 10 | 0 |
| mtbench/high | fixed_fast_vs_fixed_g2 | 30 | 1.61 [-0.74, 4.21] | -11.34 [-13.84, -8.61] | 10 | 0 |
| mtbench/high | fixed_g8_vs_fixed_g2 | 30 | -4.17 [-7.38, -0.34] | -58.14 [-63.83, -51.61] | 19 | 0 |
| mtbench/high | markov_w0_dist_vs_fixed_g2 | 30 | 9.69 [7.20, 12.24] | -28.52 [-31.18, -25.76] | 9 | 0 |
| mtbench/high | markov_w05_dist_vs_fixed_g2 | 30 | -3.51 [-4.53, -2.40] | -2.51 [-3.65, -1.42] | 5 | 0 |
| mtbench/high | pearl_vs_fixed_g2 | 30 | -0.29 [-2.65, 2.35] | -20.61 [-23.49, -17.31] | 14 | 0 |
| mtbench/high | picospec_vs_fixed_g2 | 30 | 1.66 [-0.58, 4.22] | -11.36 [-13.74, -8.77] | 10 | 0 |
| mtbench/high | pipesd_vs_fixed_g2 | 30 | -14.55 [-16.43, -12.20] | -37.77 [-40.95, -33.98] | 6 | 0 |
| mtbench/high | hf_default_vs_fixed_g2 | 30 | -18.79 [-25.75, -13.09] | -21.36 [-34.28, -12.61] | 13 | 0 |
| mtbench/high | sync_g4_vs_fixed_g8 | 30 | -2.83 [-5.93, -0.24] | 36.94 [34.55, 38.79] | 16 | 0 |
| mtbench/high | fixed_g2_vs_fixed_g8 | 30 | 4.35 [0.34, 7.97] | 36.76 [34.04, 38.96] | 19 | 0 |
| mtbench/high | fixed_fast_vs_fixed_g8 | 30 | 6.03 [3.71, 8.08] | 29.59 [27.54, 31.20] | 15 | 0 |
| mtbench/high | markov_w0_dist_vs_fixed_g8 | 30 | 14.46 [11.79, 16.94] | 18.73 [16.49, 20.52] | 16 | 0 |
| mtbench/high | markov_w05_dist_vs_fixed_g8 | 30 | 0.68 [-2.52, 3.58] | 35.17 [32.30, 37.52] | 18 | 0 |
| mtbench/high | pearl_vs_fixed_g8 | 30 | 4.05 [1.92, 6.31] | 23.73 [22.05, 25.20] | 16 | 0 |
| mtbench/high | picospec_vs_fixed_g8 | 30 | 6.08 [3.61, 8.29] | 29.58 [27.53, 31.17] | 15 | 0 |
| mtbench/high | pipesd_vs_fixed_g8 | 30 | -10.83 [-12.98, -8.65] | 12.88 [10.67, 14.74] | 18 | 0 |
| mtbench/high | hf_default_vs_fixed_g8 | 30 | -15.26 [-23.47, -8.27] | 23.26 [14.28, 29.48] | 16 | 0 |
| mtbench/high | fixed_g2_vs_sync_g4 | 30 | 7.38 [6.00, 8.60] | -0.28 [-1.46, 0.79] | 10 | 1 |
| mtbench/high | fixed_fast_vs_sync_g4 | 30 | 9.11 [7.67, 10.72] | -11.65 [-13.09, -9.89] | 1 | 0 |
| mtbench/high | fixed_g8_vs_sync_g4 | 30 | 2.91 [0.24, 6.30] | -58.58 [-63.38, -52.79] | 16 | 1 |
| mtbench/high | markov_w0_dist_vs_sync_g4 | 30 | 17.78 [16.08, 19.45] | -28.88 [-30.87, -26.59] | 12 | 1 |
| mtbench/high | markov_w05_dist_vs_sync_g4 | 30 | 3.61 [2.47, 4.74] | -2.80 [-4.57, -1.04] | 10 | 1 |
| mtbench/high | pearl_vs_sync_g4 | 30 | 7.07 [5.13, 9.40] | -20.95 [-23.33, -17.96] | 14 | 1 |
| mtbench/high | picospec_vs_sync_g4 | 30 | 9.16 [7.78, 10.71] | -11.67 [-13.09, -9.93] | 1 | 0 |
| mtbench/high | pipesd_vs_sync_g4 | 30 | -8.24 [-9.91, -6.36] | -38.16 [-41.02, -35.03] | 11 | 0 |
| mtbench/high | hf_default_vs_sync_g4 | 30 | -12.79 [-20.75, -6.69] | -21.70 [-35.30, -12.89] | 13 | 1 |
| mtbench/dynamic | sync_g4 | 30 | -9.40 [-11.77, -7.14] | 18.52 [16.75, 20.05] | 0 | 0 |
| mtbench/dynamic | fixed_g2 | 30 | 10.95 [8.37, 13.39] | 24.79 [22.85, 26.44] | 11 | 0 |
| mtbench/dynamic | fixed_g8 | 30 | -15.75 [-18.45, -13.15] | -55.20 [-59.03, -50.78] | 11 | 0 |
| mtbench/dynamic | markov_w0_dist | 30 | 13.90 [11.26, 16.35] | 20.23 [16.76, 23.36] | 10 | 0 |
| mtbench/dynamic | markov_w05_dist | 30 | 13.08 [9.68, 16.39] | 30.12 [27.51, 32.35] | 11 | 0 |
| mtbench/dynamic | pearl | 30 | 8.59 [6.19, 11.07] | 19.06 [17.06, 21.12] | 9 | 0 |
| mtbench/dynamic | picospec | 30 | 4.72 [3.73, 5.60] | 0.61 [0.15, 1.08] | 0 | 0 |
| mtbench/dynamic | pipesd | 30 | -19.02 [-21.38, -16.71] | -9.43 [-11.67, -7.36] | 8 | 0 |
| mtbench/dynamic | hf_default | 30 | -26.62 [-35.21, -19.87] | -6.64 [-19.79, 2.12] | 10 | 0 |
| mtbench/dynamic | sync_g4_vs_fixed_g2 | 30 | -18.34 [-19.76, -16.80] | -8.34 [-9.62, -7.08] | 11 | 0 |
| mtbench/dynamic | fixed_fast_vs_fixed_g2 | 30 | -9.87 [-11.81, -7.72] | -32.97 [-35.95, -29.62] | 11 | 0 |
| mtbench/dynamic | fixed_g8_vs_fixed_g2 | 30 | -24.06 [-26.92, -20.81] | -106.37 [-114.64, -96.89] | 18 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_fixed_g2 | 30 | 2.67 [1.53, 3.85] | -6.07 [-8.46, -3.78] | 4 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_fixed_g2 | 30 | 1.93 [0.72, 3.21] | 7.08 [5.73, 8.42] | 6 | 0 |
| mtbench/dynamic | pearl_vs_fixed_g2 | 30 | -2.13 [-3.94, -0.37] | -7.63 [-9.58, -5.82] | 10 | 0 |
| mtbench/dynamic | picospec_vs_fixed_g2 | 30 | -5.61 [-7.84, -3.11] | -32.15 [-35.14, -28.95] | 11 | 0 |
| mtbench/dynamic | pipesd_vs_fixed_g2 | 30 | -27.01 [-28.86, -25.06] | -45.51 [-48.10, -42.83] | 8 | 0 |
| mtbench/dynamic | hf_default_vs_fixed_g2 | 30 | -33.86 [-41.32, -27.70] | -41.80 [-59.40, -29.97] | 15 | 0 |
| mtbench/dynamic | sync_g4_vs_fixed_g8 | 30 | 7.53 [3.59, 11.13] | 47.50 [45.17, 49.38] | 11 | 0 |
| mtbench/dynamic | fixed_g2_vs_fixed_g8 | 30 | 31.69 [26.28, 36.83] | 51.54 [49.21, 53.41] | 18 | 0 |
| mtbench/dynamic | fixed_fast_vs_fixed_g8 | 30 | 18.70 [15.14, 22.63] | 35.57 [33.68, 37.12] | 11 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_fixed_g8 | 30 | 35.20 [29.68, 40.31] | 48.60 [45.23, 51.33] | 16 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_fixed_g8 | 30 | 34.22 [28.19, 40.02] | 54.97 [52.33, 57.13] | 17 | 0 |
| mtbench/dynamic | pearl_vs_fixed_g8 | 30 | 28.89 [23.53, 34.49] | 47.85 [45.42, 49.84] | 15 | 0 |
| mtbench/dynamic | picospec_vs_fixed_g8 | 30 | 24.30 [20.28, 28.24] | 35.96 [34.06, 37.47] | 11 | 0 |
| mtbench/dynamic | pipesd_vs_fixed_g8 | 30 | -3.88 [-6.77, -1.20] | 29.49 [26.59, 31.90] | 13 | 0 |
| mtbench/dynamic | hf_default_vs_fixed_g8 | 30 | -12.91 [-21.86, -5.26] | 31.29 [23.04, 36.90] | 12 | 0 |
| mtbench/dynamic | fixed_g2_vs_sync_g4 | 30 | 22.46 [20.20, 24.63] | 7.70 [6.61, 8.77] | 11 | 0 |
| mtbench/dynamic | fixed_fast_vs_sync_g4 | 30 | 10.38 [7.69, 13.34] | -22.73 [-25.08, -20.12] | 0 | 0 |
| mtbench/dynamic | fixed_g8_vs_sync_g4 | 30 | -7.01 [-10.01, -3.47] | -90.47 [-97.55, -82.39] | 11 | 0 |
| mtbench/dynamic | markov_w0_dist_vs_sync_g4 | 30 | 25.73 [23.34, 28.30] | 2.09 [-0.57, 4.69] | 10 | 0 |
| mtbench/dynamic | markov_w05_dist_vs_sync_g4 | 30 | 24.82 [22.19, 27.58] | 14.23 [12.48, 15.97] | 11 | 0 |
| mtbench/dynamic | pearl_vs_sync_g4 | 30 | 19.86 [16.79, 23.14] | 0.66 [-1.33, 2.65] | 9 | 0 |
| mtbench/dynamic | picospec_vs_sync_g4 | 30 | 15.59 [12.50, 19.01] | -21.98 [-24.26, -19.20] | 0 | 0 |
| mtbench/dynamic | pipesd_vs_sync_g4 | 30 | -10.62 [-12.18, -9.15] | -34.30 [-36.33, -32.39] | 8 | 0 |
| mtbench/dynamic | hf_default_vs_sync_g4 | 30 | -19.01 [-27.85, -11.96] | -30.88 [-47.14, -20.14] | 10 | 0 |
| mtbench/pooled | sync_g4 | 30 | -11.74 [-13.13, -10.37] | 16.97 [15.38, 18.26] | 3 | 0 |
| mtbench/pooled | fixed_g2 | 30 | 5.03 [2.79, 7.14] | 21.93 [20.15, 23.41] | 34 | 1 |
| mtbench/pooled | fixed_g8 | 30 | -15.63 [-17.15, -13.84] | -52.86 [-55.88, -48.99] | 39 | 1 |
| mtbench/pooled | markov_w0_dist | 30 | 10.69 [9.12, 12.17] | 12.17 [10.25, 14.00] | 33 | 1 |
| mtbench/pooled | markov_w05_dist | 30 | 3.67 [1.27, 6.01] | 24.93 [22.45, 27.06] | 31 | 1 |
| mtbench/pooled | pearl | 30 | 6.33 [4.49, 8.20] | 16.49 [14.91, 18.03] | 37 | 2 |
| mtbench/pooled | picospec | 30 | 3.53 [3.14, 3.93] | 0.76 [0.54, 0.97] | 0 | 0 |
| mtbench/pooled | pipesd | 30 | -21.17 [-22.32, -20.08] | -12.65 [-14.32, -11.08] | 29 | 0 |
| mtbench/pooled | hf_default | 30 | -25.65 [-32.92, -19.94] | -4.91 [-16.62, 2.95] | 34 | 1 |
| mtbench/pooled | sync_g4_vs_fixed_g2 | 30 | -15.96 [-16.81, -14.91] | -6.35 [-7.20, -5.34] | 33 | 0 |
| mtbench/pooled | fixed_fast_vs_fixed_g2 | 30 | -4.78 [-6.66, -2.72] | -28.09 [-30.56, -25.23] | 34 | 0 |
| mtbench/pooled | fixed_g8_vs_fixed_g2 | 30 | -19.67 [-22.16, -16.63] | -95.81 [-102.34, -88.06] | 55 | 0 |
| mtbench/pooled | markov_w0_dist_vs_fixed_g2 | 30 | 5.39 [4.07, 6.67] | -12.50 [-13.82, -11.12] | 17 | 0 |
| mtbench/pooled | markov_w05_dist_vs_fixed_g2 | 30 | -1.29 [-2.10, -0.49] | 3.84 [2.65, 5.01] | 16 | 0 |
| mtbench/pooled | pearl_vs_fixed_g2 | 30 | 1.24 [-0.49, 2.99] | -6.97 [-8.65, -5.34] | 30 | 1 |
| mtbench/pooled | picospec_vs_fixed_g2 | 30 | -1.43 [-3.59, 1.00] | -27.12 [-29.69, -24.13] | 34 | 0 |
| mtbench/pooled | pipesd_vs_fixed_g2 | 30 | -24.94 [-26.15, -23.48] | -44.29 [-46.23, -41.98] | 26 | 0 |
| mtbench/pooled | hf_default_vs_fixed_g2 | 30 | -29.21 [-35.78, -23.79] | -34.39 [-49.07, -24.39] | 42 | 0 |
| mtbench/pooled | sync_g4_vs_fixed_g8 | 30 | 4.62 [1.35, 7.44] | 45.69 [43.53, 47.30] | 41 | 0 |
| mtbench/pooled | fixed_g2_vs_fixed_g8 | 30 | 24.49 [19.95, 28.47] | 48.93 [46.83, 50.58] | 55 | 0 |
| mtbench/pooled | fixed_fast_vs_fixed_g8 | 30 | 18.53 [16.06, 20.70] | 34.58 [32.88, 35.85] | 39 | 0 |
| mtbench/pooled | markov_w0_dist_vs_fixed_g8 | 30 | 31.20 [27.37, 34.75] | 42.55 [40.23, 44.40] | 49 | 0 |
| mtbench/pooled | markov_w05_dist_vs_fixed_g8 | 30 | 22.88 [18.43, 26.85] | 50.89 [48.52, 52.80] | 52 | 0 |
| mtbench/pooled | pearl_vs_fixed_g8 | 30 | 26.04 [22.47, 29.53] | 45.37 [43.56, 46.86] | 50 | 1 |
| mtbench/pooled | picospec_vs_fixed_g8 | 30 | 22.71 [20.16, 24.94] | 35.08 [33.38, 36.30] | 39 | 0 |
| mtbench/pooled | pipesd_vs_fixed_g8 | 30 | -6.56 [-8.93, -4.40] | 26.31 [23.92, 28.28] | 47 | 0 |
| mtbench/pooled | hf_default_vs_fixed_g8 | 30 | -11.87 [-20.37, -4.53] | 31.37 [23.53, 36.93] | 42 | 0 |
| mtbench/pooled | fixed_g2_vs_sync_g4 | 30 | 18.99 [17.52, 20.21] | 5.97 [5.07, 6.71] | 33 | 1 |
| mtbench/pooled | fixed_fast_vs_sync_g4 | 30 | 13.30 [11.58, 15.12] | -20.44 [-22.34, -18.17] | 3 | 0 |
| mtbench/pooled | fixed_g8_vs_sync_g4 | 30 | -4.42 [-6.92, -1.33] | -84.12 [-89.77, -77.08] | 41 | 1 |
| mtbench/pooled | markov_w0_dist_vs_sync_g4 | 30 | 25.40 [23.95, 26.73] | -5.78 [-6.88, -4.63] | 32 | 1 |
| mtbench/pooled | markov_w05_dist_vs_sync_g4 | 30 | 17.45 [16.08, 18.74] | 9.58 [7.99, 10.98] | 30 | 1 |
| mtbench/pooled | pearl_vs_sync_g4 | 30 | 20.47 [18.48, 22.35] | -0.58 [-2.01, 0.89] | 36 | 2 |
| mtbench/pooled | picospec_vs_sync_g4 | 30 | 17.29 [15.31, 19.41] | -19.53 [-21.53, -17.10] | 3 | 0 |
| mtbench/pooled | pipesd_vs_sync_g4 | 30 | -10.69 [-11.78, -9.54] | -35.68 [-37.18, -33.97] | 28 | 0 |
| mtbench/pooled | hf_default_vs_sync_g4 | 30 | -15.76 [-23.83, -9.44] | -26.36 [-40.31, -17.04] | 34 | 1 |
| humaneval/low | sync_g4 | 30 | -45.80 [-47.67, -43.80] | -33.45 [-37.30, -30.06] | 0 | 0 |
| humaneval/low | fixed_g2 | 30 | -16.24 [-18.23, -14.15] | -0.54 [-2.87, 1.70] | 0 | 0 |
| humaneval/low | fixed_g8 | 30 | 6.99 [4.27, 10.23] | -5.60 [-8.10, -2.60] | 0 | 0 |
| humaneval/low | markov_w0_dist | 30 | -3.39 [-8.04, 1.53] | -2.01 [-4.02, 0.09] | 0 | 0 |
| humaneval/low | markov_w05_dist | 30 | -13.31 [-16.55, -9.72] | -2.36 [-4.32, -0.38] | 1 | 0 |
| humaneval/low | pearl | 30 | -32.25 [-34.77, -29.81] | -18.09 [-21.84, -14.75] | 1 | 0 |
| humaneval/low | picospec | 30 | -1.07 [-2.70, 0.57] | 1.64 [0.94, 2.31] | 0 | 0 |
| humaneval/low | pipesd | 30 | -31.57 [-34.26, -28.50] | -31.33 [-33.79, -28.67] | 1 | 0 |
| humaneval/low | hf_default | 30 | -42.57 [-45.05, -40.25] | -36.27 [-40.69, -32.21] | 1 | 0 |
| humaneval/low | sync_g4_vs_fixed_g2 | 30 | -35.30 [-36.78, -33.74] | -32.73 [-34.86, -30.56] | 0 | 0 |
| humaneval/low | fixed_fast_vs_fixed_g2 | 30 | 19.38 [16.48, 22.29] | 0.54 [-1.72, 2.79] | 0 | 0 |
| humaneval/low | fixed_g8_vs_fixed_g2 | 30 | 27.72 [23.13, 32.99] | -5.03 [-9.40, -0.13] | 0 | 0 |
| humaneval/low | markov_w0_dist_vs_fixed_g2 | 30 | 15.33 [9.71, 21.18] | -1.46 [-3.53, 0.39] | 0 | 0 |
| humaneval/low | markov_w05_dist_vs_fixed_g2 | 30 | 3.49 [-0.31, 7.90] | -1.81 [-3.28, -0.44] | 1 | 0 |
| humaneval/low | pearl_vs_fixed_g2 | 30 | -19.12 [-20.77, -17.38] | -17.45 [-19.02, -15.90] | 1 | 0 |
| humaneval/low | picospec_vs_fixed_g2 | 30 | 18.10 [15.27, 21.11] | 2.17 [0.08, 4.32] | 0 | 0 |
| humaneval/low | pipesd_vs_fixed_g2 | 30 | -18.31 [-22.16, -13.96] | -30.62 [-35.42, -25.45] | 1 | 0 |
| humaneval/low | hf_default_vs_fixed_g2 | 30 | -31.44 [-33.27, -29.54] | -35.53 [-38.47, -32.79] | 1 | 0 |
| humaneval/low | sync_g4_vs_fixed_g8 | 30 | -49.34 [-51.56, -47.08] | -26.37 [-32.77, -20.91] | 0 | 0 |
| humaneval/low | fixed_g2_vs_fixed_g8 | 30 | -21.70 [-24.81, -18.79] | 4.79 [0.13, 8.60] | 0 | 0 |
| humaneval/low | fixed_fast_vs_fixed_g8 | 30 | -6.53 [-9.28, -4.10] | 5.30 [2.54, 7.50] | 0 | 0 |
| humaneval/low | markov_w0_dist_vs_fixed_g8 | 30 | -9.70 [-14.64, -4.57] | 3.40 [-0.51, 6.73] | 0 | 0 |
| humaneval/low | markov_w05_dist_vs_fixed_g8 | 30 | -18.97 [-22.75, -14.89] | 3.07 [-1.09, 6.60] | 1 | 0 |
| humaneval/low | pearl_vs_fixed_g8 | 30 | -36.68 [-39.79, -33.63] | -11.82 [-18.13, -6.61] | 1 | 0 |
| humaneval/low | picospec_vs_fixed_g8 | 30 | -7.53 [-10.42, -5.12] | 6.86 [4.10, 9.10] | 0 | 0 |
| humaneval/low | pipesd_vs_fixed_g8 | 30 | -36.04 [-38.21, -33.64] | -24.36 [-26.83, -22.15] | 1 | 0 |
| humaneval/low | hf_default_vs_fixed_g8 | 30 | -46.32 [-48.99, -43.72] | -29.04 [-35.46, -23.31] | 1 | 0 |
| humaneval/low | fixed_g2_vs_sync_g4 | 30 | 54.56 [50.92, 58.17] | 24.66 [23.41, 25.85] | 0 | 0 |
| humaneval/low | fixed_fast_vs_sync_g4 | 30 | 84.51 [77.95, 91.10] | 25.07 [23.11, 27.17] | 0 | 0 |
| humaneval/low | fixed_g8_vs_sync_g4 | 30 | 97.40 [88.97, 106.46] | 20.87 [17.29, 24.68] | 0 | 0 |
| humaneval/low | markov_w0_dist_vs_sync_g4 | 30 | 78.26 [67.96, 89.11] | 23.56 [21.50, 25.42] | 0 | 0 |
| humaneval/low | markov_w05_dist_vs_sync_g4 | 30 | 59.96 [52.71, 68.07] | 23.30 [21.84, 24.64] | 1 | 0 |
| humaneval/low | pearl_vs_sync_g4 | 30 | 25.00 [22.69, 27.84] | 11.51 [10.16, 12.89] | 1 | 0 |
| humaneval/low | picospec_vs_sync_g4 | 30 | 82.53 [76.14, 88.85] | 26.30 [24.39, 28.32] | 0 | 0 |
| humaneval/low | pipesd_vs_sync_g4 | 30 | 26.26 [20.05, 33.20] | 1.59 [-2.56, 5.91] | 1 | 0 |
| humaneval/low | hf_default_vs_sync_g4 | 30 | 5.96 [3.09, 9.14] | -2.11 [-4.46, 0.34] | 1 | 0 |
| humaneval/high | sync_g4 | 30 | -35.84 [-36.64, -35.06] | -31.93 [-33.81, -30.15] | 0 | 0 |
| humaneval/high | fixed_g2 | 30 | -35.32 [-36.20, -34.40] | -37.51 [-39.72, -35.35] | 0 | 0 |
| humaneval/high | fixed_g8 | 30 | 50.69 [46.95, 55.06] | 15.27 [12.76, 18.24] | 1 | 0 |
| humaneval/high | markov_w0_dist | 30 | 41.03 [35.03, 46.01] | 12.73 [9.99, 15.50] | 1 | 0 |
| humaneval/high | markov_w05_dist | 30 | 33.77 [30.63, 37.06] | 12.31 [10.36, 14.59] | 1 | 0 |
| humaneval/high | pearl | 30 | 25.57 [23.32, 28.27] | 13.76 [11.97, 15.68] | 0 | 0 |
| humaneval/high | picospec | 30 | 0.09 [-0.18, 0.40] | 0.74 [0.36, 1.19] | 0 | 0 |
| humaneval/high | pipesd | 30 | 11.91 [8.23, 16.29] | 1.94 [-0.88, 4.90] | 2 | 0 |
| humaneval/high | hf_default | 30 | -17.32 [-20.02, -14.37] | -13.26 [-16.85, -9.66] | 2 | 0 |
| humaneval/high | sync_g4_vs_fixed_g2 | 30 | -0.80 [-1.59, 0.03] | 4.06 [3.25, 4.86] | 0 | 0 |
| humaneval/high | fixed_fast_vs_fixed_g2 | 30 | 54.60 [52.44, 56.75] | 27.28 [26.12, 28.43] | 0 | 0 |
| humaneval/high | fixed_g8_vs_fixed_g2 | 30 | 132.97 [124.71, 142.44] | 38.39 [35.85, 41.23] | 1 | 0 |
| humaneval/high | markov_w0_dist_vs_fixed_g2 | 30 | 118.03 [106.84, 128.25] | 36.54 [33.76, 39.31] | 1 | 0 |
| humaneval/high | markov_w05_dist_vs_fixed_g2 | 30 | 106.81 [100.44, 113.55] | 36.23 [34.15, 38.50] | 1 | 0 |
| humaneval/high | pearl_vs_fixed_g2 | 30 | 94.13 [89.37, 99.55] | 37.29 [35.68, 39.12] | 0 | 0 |
| humaneval/high | picospec_vs_fixed_g2 | 30 | 54.74 [52.59, 56.95] | 27.82 [26.64, 28.96] | 0 | 0 |
| humaneval/high | pipesd_vs_fixed_g2 | 30 | 73.01 [65.88, 81.43] | 28.69 [26.05, 31.57] | 2 | 0 |
| humaneval/high | hf_default_vs_fixed_g2 | 30 | 27.82 [23.41, 32.82] | 17.64 [14.88, 20.48] | 2 | 0 |
| humaneval/high | sync_g4_vs_fixed_g8 | 30 | -57.42 [-59.01, -55.89] | -55.72 [-63.01, -49.69] | 1 | 0 |
| humaneval/high | fixed_g2_vs_fixed_g8 | 30 | -57.08 [-58.75, -55.50] | -62.30 [-70.15, -55.88] | 1 | 0 |
| humaneval/high | fixed_fast_vs_fixed_g8 | 30 | -33.64 [-35.51, -31.95] | -18.03 [-22.31, -14.63] | 1 | 0 |
| humaneval/high | markov_w0_dist_vs_fixed_g8 | 30 | -6.42 [-10.00, -3.40] | -3.00 [-6.18, -0.29] | 2 | 0 |
| humaneval/high | markov_w05_dist_vs_fixed_g8 | 30 | -11.23 [-13.15, -9.34] | -3.49 [-5.99, -1.31] | 2 | 0 |
| humaneval/high | pearl_vs_fixed_g8 | 30 | -16.67 [-18.53, -14.57] | -1.79 [-4.42, 0.86] | 1 | 0 |
| humaneval/high | picospec_vs_fixed_g8 | 30 | -33.58 [-35.41, -31.88] | -17.15 [-21.16, -13.84] | 1 | 0 |
| humaneval/high | pipesd_vs_fixed_g8 | 30 | -25.74 [-27.29, -24.05] | -15.74 [-17.87, -13.89] | 1 | 0 |
| humaneval/high | hf_default_vs_fixed_g8 | 30 | -45.13 [-46.87, -43.38] | -33.67 [-37.98, -29.22] | 1 | 0 |
| humaneval/high | fixed_g2_vs_sync_g4 | 30 | 0.81 [-0.03, 1.62] | -4.23 [-5.11, -3.36] | 0 | 0 |
| humaneval/high | fixed_fast_vs_sync_g4 | 30 | 55.85 [53.98, 57.82] | 24.20 [23.17, 25.27] | 0 | 0 |
| humaneval/high | fixed_g8_vs_sync_g4 | 30 | 134.86 [126.71, 143.99] | 35.78 [33.20, 38.65] | 1 | 0 |
| humaneval/high | markov_w0_dist_vs_sync_g4 | 30 | 119.79 [108.79, 129.79] | 33.85 [31.03, 36.66] | 1 | 0 |
| humaneval/high | markov_w05_dist_vs_sync_g4 | 30 | 108.48 [101.92, 115.67] | 33.54 [31.40, 35.89] | 1 | 0 |
| humaneval/high | pearl_vs_sync_g4 | 30 | 95.71 [90.49, 101.46] | 34.63 [32.82, 36.66] | 0 | 0 |
| humaneval/high | picospec_vs_sync_g4 | 30 | 56.00 [54.08, 57.96] | 24.77 [23.73, 25.83] | 0 | 0 |
| humaneval/high | pipesd_vs_sync_g4 | 30 | 74.41 [67.41, 82.56] | 25.68 [22.89, 28.64] | 2 | 0 |
| humaneval/high | hf_default_vs_sync_g4 | 30 | 28.86 [24.19, 34.02] | 14.16 [11.03, 17.20] | 2 | 0 |
| humaneval/dynamic | sync_g4 | 30 | -38.95 [-42.09, -35.78] | -31.86 [-37.19, -27.22] | 0 | 0 |
| humaneval/dynamic | fixed_g2 | 30 | -22.95 [-25.36, -20.21] | -16.07 [-19.67, -12.43] | 0 | 0 |
| humaneval/dynamic | fixed_g8 | 30 | 29.68 [23.58, 35.61] | 4.50 [0.99, 8.04] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist | 30 | 13.21 [7.58, 19.44] | 1.21 [-1.47, 3.86] | 1 | 0 |
| humaneval/dynamic | markov_w05_dist | 30 | 4.73 [-1.45, 11.15] | -0.09 [-3.71, 3.02] | 0 | 0 |
| humaneval/dynamic | pearl | 30 | -11.81 [-13.51, -9.95] | -5.97 [-7.93, -3.98] | 0 | 0 |
| humaneval/dynamic | picospec | 30 | -0.30 [-1.72, 0.99] | 0.52 [-0.67, 1.72] | 0 | 0 |
| humaneval/dynamic | pipesd | 30 | -10.61 [-16.40, -4.55] | -12.88 [-17.56, -8.27] | 0 | 0 |
| humaneval/dynamic | hf_default | 30 | -30.86 [-35.05, -26.01] | -26.56 [-31.88, -20.87] | 1 | 0 |
| humaneval/dynamic | sync_g4_vs_fixed_g2 | 30 | -20.77 [-25.08, -16.82] | -13.61 [-17.81, -9.75] | 0 | 0 |
| humaneval/dynamic | fixed_fast_vs_fixed_g2 | 30 | 29.78 [25.33, 33.98] | 13.84 [11.05, 16.43] | 0 | 0 |
| humaneval/dynamic | fixed_g8_vs_fixed_g2 | 30 | 68.29 [56.94, 78.76] | 17.72 [12.91, 22.46] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_fixed_g2 | 30 | 46.92 [37.30, 56.98] | 14.89 [10.33, 19.06] | 1 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_fixed_g2 | 30 | 35.92 [25.14, 46.09] | 13.77 [8.61, 18.15] | 0 | 0 |
| humaneval/dynamic | pearl_vs_fixed_g2 | 30 | 14.45 [11.83, 16.92] | 8.70 [6.85, 10.46] | 0 | 0 |
| humaneval/dynamic | picospec_vs_fixed_g2 | 30 | 29.39 [25.53, 32.82] | 14.29 [11.76, 16.74] | 0 | 0 |
| humaneval/dynamic | pipesd_vs_fixed_g2 | 30 | 16.01 [6.63, 25.37] | 2.75 [-3.25, 8.25] | 0 | 0 |
| humaneval/dynamic | hf_default_vs_fixed_g2 | 30 | -10.27 [-16.91, -3.24] | -9.04 [-15.46, -2.52] | 1 | 0 |
| humaneval/dynamic | sync_g4_vs_fixed_g8 | 30 | -52.92 [-55.35, -50.39] | -38.07 [-46.36, -31.06] | 0 | 0 |
| humaneval/dynamic | fixed_g2_vs_fixed_g8 | 30 | -40.58 [-44.06, -36.28] | -21.54 [-28.96, -14.83] | 0 | 0 |
| humaneval/dynamic | fixed_fast_vs_fixed_g8 | 30 | -22.89 [-26.26, -19.08] | -4.71 [-8.74, -1.00] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_fixed_g8 | 30 | -12.70 [-16.48, -9.22] | -3.44 [-6.41, -0.62] | 1 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_fixed_g8 | 30 | -19.24 [-22.61, -15.74] | -4.80 [-8.28, -1.29] | 0 | 0 |
| humaneval/dynamic | pearl_vs_fixed_g8 | 30 | -32.00 [-35.51, -28.00] | -10.96 [-16.44, -6.02] | 0 | 0 |
| humaneval/dynamic | picospec_vs_fixed_g8 | 30 | -23.11 [-26.72, -19.04] | -4.17 [-8.16, -0.35] | 0 | 0 |
| humaneval/dynamic | pipesd_vs_fixed_g8 | 30 | -31.07 [-33.94, -27.91] | -18.20 [-21.80, -14.96] | 0 | 0 |
| humaneval/dynamic | hf_default_vs_fixed_g8 | 30 | -46.68 [-49.26, -43.98] | -32.53 [-38.64, -27.05] | 1 | 0 |
| humaneval/dynamic | fixed_g2_vs_sync_g4 | 30 | 26.21 [20.23, 33.47] | 11.98 [8.88, 15.12] | 0 | 0 |
| humaneval/dynamic | fixed_fast_vs_sync_g4 | 30 | 63.79 [55.71, 72.69] | 24.16 [21.40, 27.11] | 0 | 0 |
| humaneval/dynamic | fixed_g8_vs_sync_g4 | 30 | 112.40 [101.55, 123.98] | 27.57 [23.70, 31.67] | 0 | 0 |
| humaneval/dynamic | markov_w0_dist_vs_sync_g4 | 30 | 85.43 [76.45, 94.40] | 25.08 [21.84, 28.23] | 1 | 0 |
| humaneval/dynamic | markov_w05_dist_vs_sync_g4 | 30 | 71.54 [62.35, 80.61] | 24.10 [20.39, 27.54] | 0 | 0 |
| humaneval/dynamic | pearl_vs_sync_g4 | 30 | 44.44 [37.45, 52.57] | 19.64 [16.77, 22.54] | 0 | 0 |
| humaneval/dynamic | picospec_vs_sync_g4 | 30 | 63.31 [55.94, 71.69] | 24.55 [21.94, 27.49] | 0 | 0 |
| humaneval/dynamic | pipesd_vs_sync_g4 | 30 | 46.42 [37.74, 55.31] | 14.39 [10.02, 18.41] | 0 | 0 |
| humaneval/dynamic | hf_default_vs_sync_g4 | 30 | 13.25 [9.04, 17.82] | 4.02 [0.68, 7.36] | 1 | 0 |
| humaneval/pooled | sync_g4 | 30 | -39.27 [-40.74, -37.74] | -32.31 [-35.26, -29.76] | 0 | 0 |
| humaneval/pooled | fixed_g2 | 30 | -27.93 [-28.95, -26.87] | -20.62 [-22.72, -18.75] | 0 | 0 |
| humaneval/pooled | fixed_g8 | 30 | 31.94 [28.41, 35.70] | 6.16 [3.59, 9.13] | 1 | 0 |
| humaneval/pooled | markov_w0_dist | 30 | 19.45 [16.23, 22.52] | 5.01 [3.50, 6.39] | 2 | 0 |
| humaneval/pooled | markov_w05_dist | 30 | 10.64 [7.79, 13.41] | 4.32 [2.93, 5.64] | 2 | 0 |
| humaneval/pooled | pearl | 30 | -5.21 [-6.18, -4.18] | -1.21 [-2.31, -0.10] | 1 | 0 |
| humaneval/pooled | picospec | 30 | -0.29 [-0.89, 0.33] | 0.90 [0.43, 1.40] | 0 | 0 |
| humaneval/pooled | pipesd | 30 | -8.32 [-11.23, -5.25] | -11.79 [-14.60, -9.07] | 3 | 0 |
| humaneval/pooled | hf_default | 30 | -28.73 [-31.26, -26.00] | -23.78 [-27.35, -20.08] | 4 | 0 |
| humaneval/pooled | sync_g4_vs_fixed_g2 | 30 | -15.73 [-17.26, -14.23] | -9.70 [-11.14, -8.27] | 0 | 0 |
| humaneval/pooled | fixed_fast_vs_fixed_g2 | 30 | 38.76 [36.75, 40.75] | 17.09 [15.79, 18.52] | 0 | 0 |
| humaneval/pooled | fixed_g8_vs_fixed_g2 | 30 | 83.07 [76.52, 90.19] | 22.20 [19.07, 25.66] | 1 | 0 |
| humaneval/pooled | markov_w0_dist_vs_fixed_g2 | 30 | 65.75 [60.40, 70.79] | 21.25 [19.15, 23.35] | 2 | 0 |
| humaneval/pooled | markov_w05_dist_vs_fixed_g2 | 30 | 53.52 [48.45, 58.04] | 20.67 [18.68, 22.58] | 2 | 0 |
| humaneval/pooled | pearl_vs_fixed_g2 | 30 | 31.53 [29.78, 33.52] | 16.09 [15.09, 17.18] | 1 | 0 |
| humaneval/pooled | picospec_vs_fixed_g2 | 30 | 38.35 [36.54, 40.17] | 17.84 [16.50, 19.23] | 0 | 0 |
| humaneval/pooled | pipesd_vs_fixed_g2 | 30 | 27.21 [22.10, 32.72] | 7.32 [3.86, 10.70] | 3 | 0 |
| humaneval/pooled | hf_default_vs_fixed_g2 | 30 | -1.11 [-4.67, 2.58] | -2.63 [-5.84, 0.60] | 4 | 0 |
| humaneval/pooled | sync_g4_vs_fixed_g8 | 30 | -53.97 [-55.85, -52.20] | -41.00 [-48.23, -35.33] | 1 | 0 |
| humaneval/pooled | fixed_g2_vs_fixed_g8 | 30 | -45.38 [-47.42, -43.35] | -28.54 [-34.51, -23.56] | 1 | 0 |
| humaneval/pooled | fixed_fast_vs_fixed_g8 | 30 | -24.21 [-26.31, -22.13] | -6.57 [-10.04, -3.73] | 1 | 0 |
| humaneval/pooled | markov_w0_dist_vs_fixed_g8 | 30 | -9.46 [-12.10, -7.13] | -1.22 [-3.86, 1.00] | 3 | 0 |
| humaneval/pooled | markov_w05_dist_vs_fixed_g8 | 30 | -16.14 [-18.31, -14.19] | -1.97 [-4.74, 0.42] | 3 | 0 |
| humaneval/pooled | pearl_vs_fixed_g8 | 30 | -28.15 [-30.32, -25.86] | -7.86 [-11.85, -4.34] | 2 | 0 |
| humaneval/pooled | picospec_vs_fixed_g8 | 30 | -24.43 [-26.68, -22.31] | -5.60 [-9.06, -2.81] | 1 | 0 |
| humaneval/pooled | pipesd_vs_fixed_g8 | 30 | -30.52 [-31.92, -28.90] | -19.13 [-21.37, -17.15] | 2 | 0 |
| humaneval/pooled | hf_default_vs_fixed_g8 | 30 | -45.98 [-47.90, -43.98] | -31.91 [-36.73, -27.30] | 3 | 0 |
| humaneval/pooled | fixed_g2_vs_sync_g4 | 30 | 18.66 [16.58, 20.87] | 8.84 [7.64, 10.02] | 0 | 0 |
| humaneval/pooled | fixed_fast_vs_sync_g4 | 30 | 64.65 [60.62, 68.75] | 24.42 [22.93, 26.07] | 0 | 0 |
| humaneval/pooled | fixed_g8_vs_sync_g4 | 30 | 117.24 [109.19, 126.52] | 29.08 [26.10, 32.54] | 1 | 0 |
| humaneval/pooled | markov_w0_dist_vs_sync_g4 | 30 | 96.69 [90.42, 103.41] | 28.21 [26.15, 30.32] | 2 | 0 |
| humaneval/pooled | markov_w05_dist_vs_sync_g4 | 30 | 82.17 [76.82, 87.55] | 27.68 [25.85, 29.59] | 2 | 0 |
| humaneval/pooled | pearl_vs_sync_g4 | 30 | 56.08 [52.47, 59.91] | 23.50 [22.13, 25.01] | 1 | 0 |
| humaneval/pooled | picospec_vs_sync_g4 | 30 | 64.18 [60.40, 68.10] | 25.10 [23.59, 26.78] | 0 | 0 |
| humaneval/pooled | pipesd_vs_sync_g4 | 30 | 50.95 [44.97, 57.47] | 15.51 [12.20, 18.69] | 3 | 0 |
| humaneval/pooled | hf_default_vs_sync_g4 | 30 | 17.35 [13.87, 21.00] | 6.44 [3.87, 9.02] | 4 | 0 |

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
