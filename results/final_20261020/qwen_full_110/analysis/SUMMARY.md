# Cross-pair results against the best fixed window

fixed_g4 is the raw arm fixed_fast. best_fixed is, per delay, the fixed window (g2/g4/g8) with the highest throughput; pooled combines those per-delay choices. It is chosen after the measurement, so it is an oracle baseline.

alpha = strict accepted / examined draft tokens; tau = accepted draft tokens per verification round; util = accepted / proposed draft tokens. sync_g4 and fixed_g4 use the same window, so their acceptance differs only through prefetch reuse.

## results/final_20261020/qwen_full_110

results/final_20261020/qwen_full_110: 2310/2310 requests. Best fixed window: low: fixed_g2, high: fixed_g8, dynamic: fixed_g4.

| Delay | Method | Requests | tokens/s | J/token | alpha % | tau | util % |
|---|---|---:|---:|---:|---:|---:|---:|
| low | sync_g4 | 110 | 25.11 | 0.2901 | 83.8 | 2.56 | 64.3 |
| low | fixed_g2 | 110 | 34.10 | 0.2965 | 83.9 | 1.53 | 76.6 |
| low | fixed_g4 | 110 | 33.72 | 0.3651 | 83.9 | 2.56 | 64.4 |
| low | fixed_g8 | 110 | 26.14 | 0.5196 | 84.0 | 3.69 | 46.9 |
| low | **best_fixed** (fixed_g2) | 110 | 34.10 | 0.2965 | 83.9 | 1.53 | 76.6 |
| low | adaedl | 110 | 21.43 | 0.3576 | 88.6 | 2.99 | 71.3 |
| low | CAPE-S (w=0) | 110 | 32.63 | 0.3184 | 84.6 | 1.44 | 73.7 |
| low | CAPE-E (w=0.5) | 110 | 33.38 | 0.2924 | 84.7 | 1.31 | 77.2 |
| high | sync_g4 | 110 | 13.15 | 0.4543 | 84.1 | 2.58 | 64.9 |
| high | fixed_g2 | 110 | 13.95 | 0.4690 | 84.0 | 1.53 | 76.8 |
| high | fixed_g4 | 110 | 17.96 | 0.4622 | 84.0 | 2.57 | 64.7 |
| high | fixed_g8 | 110 | 20.22 | 0.5787 | 84.4 | 3.75 | 47.6 |
| high | **best_fixed** (fixed_g8) | 110 | 20.22 | 0.5787 | 84.4 | 3.75 | 47.6 |
| high | adaedl | 110 | 12.30 | 0.5091 | 88.9 | 3.03 | 71.7 |
| high | CAPE-S (w=0) | 110 | 20.76 | 0.5299 | 84.8 | 2.95 | 59.6 |
| high | CAPE-E (w=0.5) | 110 | 17.96 | 0.4527 | 84.7 | 2.75 | 63.0 |
| dynamic | sync_g4 | 110 | 17.79 | 0.3659 | 83.8 | 2.55 | 64.0 |
| dynamic | fixed_g2 | 110 | 22.95 | 0.3495 | 83.7 | 1.52 | 76.3 |
| dynamic | fixed_g4 | 110 | 25.56 | 0.4065 | 83.8 | 2.55 | 64.1 |
| dynamic | fixed_g8 | 110 | 23.08 | 0.5497 | 84.0 | 3.70 | 46.9 |
| dynamic | **best_fixed** (fixed_g4) | 110 | 25.56 | 0.4065 | 83.8 | 2.55 | 64.1 |
| dynamic | adaedl | 110 | 15.78 | 0.4315 | 88.5 | 2.97 | 71.2 |
| dynamic | CAPE-S (w=0) | 110 | 25.14 | 0.4204 | 84.6 | 1.97 | 65.2 |
| dynamic | CAPE-E (w=0.5) | 110 | 25.26 | 0.3557 | 84.7 | 1.76 | 69.7 |
| pooled | sync_g4 | 330 | 17.43 | 0.3701 | 83.9 | 2.56 | 64.4 |
| pooled | fixed_g2 | 330 | 20.75 | 0.3716 | 83.8 | 1.53 | 76.6 |
| pooled | fixed_g4 | 330 | 24.11 | 0.4113 | 83.9 | 2.56 | 64.4 |
| pooled | fixed_g8 | 330 | 22.90 | 0.5493 | 84.1 | 3.71 | 47.1 |
| pooled | **best_fixed** | 330 | 25.45 | 0.4273 | 84.0 | 2.38 | 59.2 |
| pooled | adaedl | 330 | 15.68 | 0.4327 | 88.7 | 3.00 | 71.4 |
| pooled | CAPE-S (w=0) | 330 | 25.29 | 0.4230 | 84.7 | 2.00 | 65.1 |
| pooled | CAPE-E (w=0.5) | 330 | 23.97 | 0.3667 | 84.7 | 1.82 | 68.9 |

Paired effects versus best_fixed (prompt-cluster bootstrap, 2000 draws). Positive energy saving means lower J/token.

| Delay | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences |
|---|---|---:|---|---|---:|
| low | sync_g4 | 110 | -26.38 [-28.72, -23.49] | 2.15 [0.74, 3.59] | 17 |
| low | adaedl | 110 | -37.16 [-40.13, -33.21] | -20.60 [-23.28, -17.67] | 19 |
| low | CAPE-S (w=0) | 110 | -4.31 [-7.87, 0.26] | -7.39 [-10.25, -4.67] | 14 |
| low | CAPE-E (w=0.5) | 110 | -2.13 [-5.78, 2.31] | 1.39 [-1.49, 4.28] | 13 |
| high | sync_g4 | 110 | -34.99 [-38.52, -31.24] | 21.50 [16.59, 26.11] | 23 |
| high | adaedl | 110 | -39.18 [-41.49, -36.75] | 12.02 [8.01, 15.82] | 19 |
| high | CAPE-S (w=0) | 110 | 2.63 [0.08, 5.09] | 8.43 [6.40, 10.37] | 30 |
| high | CAPE-E (w=0.5) | 110 | -11.22 [-14.24, -8.67] | 21.78 [17.37, 25.67] | 30 |
| dynamic | sync_g4 | 110 | -30.42 [-35.28, -26.37] | 10.01 [5.25, 13.96] | 0 |
| dynamic | adaedl | 110 | -38.27 [-40.73, -35.72] | -6.13 [-9.44, -2.98] | 15 |
| dynamic | CAPE-S (w=0) | 110 | -1.64 [-5.91, 2.01] | -3.42 [-6.73, -0.47] | 17 |
| dynamic | CAPE-E (w=0.5) | 110 | -1.19 [-3.38, 0.89] | 12.52 [8.97, 15.83] | 19 |
| pooled | sync_g4 | 110 | -31.50 [-34.14, -28.76] | 13.38 [9.83, 16.87] | 40 |
| pooled | adaedl | 110 | -38.37 [-40.30, -36.35] | -1.27 [-4.47, 1.91] | 53 |
| pooled | CAPE-S (w=0) | 110 | -0.62 [-2.75, 1.58] | 0.99 [-0.80, 2.77] | 61 |
| pooled | CAPE-E (w=0.5) | 110 | -5.81 [-7.82, -3.79] | 14.16 [10.50, 17.59] | 62 |
