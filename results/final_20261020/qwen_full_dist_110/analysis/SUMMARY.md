# Cross-pair results against the best fixed window

fixed_g4 is the raw arm fixed_fast. best_fixed is, per delay, the fixed window (g2/g4/g8) with the highest throughput; pooled combines those per-delay choices. It is chosen after the measurement, so it is an oracle baseline.

alpha = strict accepted / examined draft tokens; tau = accepted draft tokens per verification round; util = accepted / proposed draft tokens. sync_g4 and fixed_g4 use the same window, so their acceptance differs only through prefetch reuse.

## results/final_20261020/qwen_full_dist_110

results/final_20261020/qwen_full_dist_110: 1980/1980 requests. Best fixed window: low: fixed_g2, high: fixed_g8, dynamic: fixed_g4.

| Delay | Method | Requests | tokens/s | J/token | alpha % | tau | util % |
|---|---|---:|---:|---:|---:|---:|---:|
| low | sync_g4 | 110 | 26.46 | 0.2806 | 83.9 | 2.56 | 64.4 |
| low | fixed_g2 | 110 | 37.46 | 0.2934 | 83.7 | 1.53 | 76.5 |
| low | fixed_g4 | 110 | 36.11 | 0.3549 | 84.0 | 2.56 | 64.4 |
| low | fixed_g8 | 110 | 27.22 | 0.5085 | 84.2 | 3.74 | 47.4 |
| low | **best_fixed** (fixed_g2) | 110 | 37.46 | 0.2934 | 83.7 | 1.53 | 76.5 |
| low | CAPE-S dist (w=0) | 110 | 36.30 | 0.3082 | 85.0 | 1.83 | 72.0 |
| low | CAPE-E dist (w=0.5) | 110 | 36.16 | 0.2856 | 85.1 | 1.53 | 75.3 |
| high | sync_g4 | 110 | 13.35 | 0.4480 | 83.8 | 2.56 | 64.4 |
| high | fixed_g2 | 110 | 14.38 | 0.4591 | 83.8 | 1.53 | 76.5 |
| high | fixed_g4 | 110 | 18.36 | 0.4564 | 83.7 | 2.55 | 64.2 |
| high | fixed_g8 | 110 | 20.32 | 0.5836 | 84.0 | 3.68 | 46.7 |
| high | **best_fixed** (fixed_g8) | 110 | 20.32 | 0.5836 | 84.0 | 3.68 | 46.7 |
| high | CAPE-S dist (w=0) | 110 | 20.74 | 0.5144 | 84.7 | 2.88 | 60.1 |
| high | CAPE-E dist (w=0.5) | 110 | 18.55 | 0.4414 | 84.8 | 2.77 | 63.3 |
| dynamic | sync_g4 | 110 | 19.20 | 0.3456 | 83.8 | 2.55 | 64.1 |
| dynamic | fixed_g2 | 110 | 24.35 | 0.3422 | 83.7 | 1.52 | 76.3 |
| dynamic | fixed_g4 | 110 | 26.28 | 0.3989 | 83.7 | 2.55 | 64.1 |
| dynamic | fixed_g8 | 110 | 23.47 | 0.5462 | 84.0 | 3.68 | 46.7 |
| dynamic | **best_fixed** (fixed_g4) | 110 | 26.28 | 0.3989 | 83.7 | 2.55 | 64.1 |
| dynamic | CAPE-S dist (w=0) | 110 | 27.67 | 0.3898 | 84.9 | 2.32 | 66.1 |
| dynamic | CAPE-E dist (w=0.5) | 110 | 26.04 | 0.3459 | 84.8 | 1.99 | 68.9 |
| pooled | sync_g4 | 330 | 18.18 | 0.3584 | 83.8 | 2.56 | 64.3 |
| pooled | fixed_g2 | 330 | 21.81 | 0.3652 | 83.7 | 1.53 | 76.4 |
| pooled | fixed_g4 | 330 | 24.93 | 0.4036 | 83.8 | 2.55 | 64.2 |
| pooled | fixed_g8 | 330 | 23.33 | 0.5462 | 84.1 | 3.70 | 46.9 |
| pooled | **best_fixed** | 330 | 26.30 | 0.4259 | 83.8 | 2.37 | 58.6 |
| pooled | CAPE-S dist (w=0) | 330 | 26.78 | 0.4045 | 84.9 | 2.29 | 65.4 |
| pooled | CAPE-E dist (w=0.5) | 330 | 24.97 | 0.3579 | 84.9 | 2.02 | 68.4 |

Paired effects versus best_fixed (prompt-cluster bootstrap, 2000 draws). Positive energy saving means lower J/token.

| Delay | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences |
|---|---|---:|---|---|---:|
| low | sync_g4 | 110 | -29.37 [-30.60, -28.19] | 4.36 [3.14, 5.52] | 16 |
| low | CAPE-S dist (w=0) | 110 | -3.11 [-4.27, -1.91] | -5.06 [-6.88, -3.29] | 14 |
| low | CAPE-E dist (w=0.5) | 110 | -3.47 [-4.65, -2.28] | 2.67 [0.43, 4.83] | 8 |
| high | sync_g4 | 110 | -34.29 [-38.16, -30.40] | 23.24 [18.16, 27.78] | 23 |
| high | CAPE-S dist (w=0) | 110 | 2.07 [-2.27, 5.33] | 11.86 [8.64, 14.74] | 25 |
| high | CAPE-E dist (w=0.5) | 110 | -8.72 [-10.59, -6.94] | 24.36 [20.33, 27.92] | 27 |
| dynamic | sync_g4 | 110 | -26.94 [-29.57, -24.31] | 13.38 [10.20, 16.38] | 0 |
| dynamic | CAPE-S dist (w=0) | 110 | 5.29 [3.59, 7.21] | 2.29 [-0.52, 5.14] | 19 |
| dynamic | CAPE-E dist (w=0.5) | 110 | -0.93 [-3.04, 1.06] | 13.29 [9.57, 16.94] | 18 |
| pooled | sync_g4 | 110 | -30.85 [-33.56, -28.06] | 15.85 [12.21, 19.25] | 39 |
| pooled | CAPE-S dist (w=0) | 110 | 1.84 [-0.20, 3.59] | 5.01 [2.38, 7.52] | 58 |
| pooled | CAPE-E dist (w=0.5) | 110 | -5.03 [-6.45, -3.64] | 15.95 [12.27, 19.34] | 53 |
