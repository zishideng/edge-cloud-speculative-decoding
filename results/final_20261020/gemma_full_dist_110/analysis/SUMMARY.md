# Cross-pair results against the best fixed window

fixed_g4 is the raw arm fixed_fast. best_fixed is, per delay, the fixed window (g2/g4/g8) with the highest throughput; pooled combines those per-delay choices. It is chosen after the measurement, so it is an oracle baseline.

alpha = strict accepted / examined draft tokens; tau = accepted draft tokens per verification round; util = accepted / proposed draft tokens. sync_g4 and fixed_g4 use the same window, so their acceptance differs only through prefetch reuse.

## results/final_20261020/gemma_full_dist_110

results/final_20261020/gemma_full_dist_110: 1980/1980 requests. Best fixed window: low: fixed_g2, high: fixed_g2, dynamic: fixed_g2.

| Delay | Method | Requests | tokens/s | J/token | alpha % | tau | util % |
|---|---|---:|---:|---:|---:|---:|---:|
| low | sync_g4 | 110 | 14.07 | 0.9537 | 88.8 | 2.95 | 74.1 |
| low | fixed_g2 | 110 | 15.18 | 1.0677 | 88.6 | 1.66 | 83.2 |
| low | fixed_g4 | 110 | 12.57 | 1.3215 | 88.8 | 2.94 | 74.1 |
| low | fixed_g8 | 110 | 9.09 | 1.8594 | 88.9 | 4.65 | 59.1 |
| low | **best_fixed** (fixed_g2) | 110 | 15.18 | 1.0677 | 88.6 | 1.66 | 83.2 |
| low | CAPE-S dist (w=0) | 110 | 16.07 | 0.9841 | 89.2 | 1.15 | 87.8 |
| low | CAPE-E dist (w=0.5) | 110 | 16.14 | 0.9720 | 88.8 | 1.01 | 88.2 |
| high | sync_g4 | 110 | 9.71 | 1.0665 | 88.8 | 2.94 | 74.0 |
| high | fixed_g2 | 110 | 13.15 | 1.1347 | 88.6 | 1.66 | 83.1 |
| high | fixed_g4 | 110 | 12.45 | 1.3223 | 88.8 | 2.95 | 74.1 |
| high | fixed_g8 | 110 | 9.04 | 1.8614 | 88.9 | 4.64 | 59.0 |
| high | **best_fixed** (fixed_g2) | 110 | 13.15 | 1.1347 | 88.6 | 1.66 | 83.1 |
| high | CAPE-S dist (w=0) | 110 | 13.40 | 1.1664 | 89.2 | 1.99 | 82.4 |
| high | CAPE-E dist (w=0.5) | 110 | 13.26 | 1.1305 | 89.4 | 1.73 | 84.6 |
| dynamic | sync_g4 | 110 | 11.82 | 1.0116 | 88.7 | 2.94 | 73.9 |
| dynamic | fixed_g2 | 110 | 14.17 | 1.0989 | 88.6 | 1.66 | 83.2 |
| dynamic | fixed_g4 | 110 | 12.52 | 1.3227 | 88.8 | 2.94 | 74.0 |
| dynamic | fixed_g8 | 110 | 9.08 | 1.8589 | 88.9 | 4.64 | 59.1 |
| dynamic | **best_fixed** (fixed_g2) | 110 | 14.17 | 1.0989 | 88.6 | 1.66 | 83.2 |
| dynamic | CAPE-S dist (w=0) | 110 | 14.35 | 1.0899 | 89.3 | 1.59 | 84.4 |
| dynamic | CAPE-E dist (w=0.5) | 110 | 14.43 | 1.0564 | 89.3 | 1.37 | 86.2 |
| pooled | sync_g4 | 330 | 11.60 | 1.0106 | 88.8 | 2.94 | 74.0 |
| pooled | fixed_g2 | 330 | 14.12 | 1.1005 | 88.6 | 1.66 | 83.2 |
| pooled | fixed_g4 | 330 | 12.51 | 1.3222 | 88.8 | 2.94 | 74.0 |
| pooled | fixed_g8 | 330 | 9.07 | 1.8599 | 88.9 | 4.65 | 59.1 |
| pooled | **best_fixed** | 330 | 14.12 | 1.1005 | 88.6 | 1.66 | 83.2 |
| pooled | CAPE-S dist (w=0) | 330 | 14.53 | 1.0801 | 89.2 | 1.53 | 84.6 |
| pooled | CAPE-E dist (w=0.5) | 330 | 14.51 | 1.0532 | 89.2 | 1.33 | 86.2 |

Paired effects versus best_fixed (prompt-cluster bootstrap, 2000 draws). Positive energy saving means lower J/token.

| Delay | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences |
|---|---|---:|---|---|---:|
| low | sync_g4 | 110 | -7.27 [-9.70, -4.83] | 10.68 [9.72, 11.67] | 12 |
| low | CAPE-S dist (w=0) | 110 | 5.90 [4.23, 7.65] | 7.83 [6.39, 9.31] | 7 |
| low | CAPE-E dist (w=0.5) | 110 | 6.34 [4.56, 8.17] | 8.96 [7.52, 10.42] | 7 |
| high | sync_g4 | 110 | -26.12 [-26.86, -25.33] | 6.01 [5.30, 6.72] | 7 |
| high | CAPE-S dist (w=0) | 110 | 1.94 [0.85, 3.03] | -2.79 [-3.51, -2.13] | 7 |
| high | CAPE-E dist (w=0.5) | 110 | 0.89 [-0.13, 1.91] | 0.37 [-0.36, 1.12] | 5 |
| dynamic | sync_g4 | 110 | -16.57 [-17.61, -15.54] | 7.94 [7.22, 8.67] | 6 |
| dynamic | CAPE-S dist (w=0) | 110 | 1.28 [0.28, 2.25] | 0.81 [-0.27, 1.91] | 3 |
| dynamic | CAPE-E dist (w=0.5) | 110 | 1.80 [0.64, 3.09] | 3.87 [2.62, 5.19] | 2 |
| pooled | sync_g4 | 110 | -17.80 [-18.68, -16.84] | 8.17 [7.50, 8.86] | 25 |
| pooled | CAPE-S dist (w=0) | 110 | 2.92 [2.28, 3.56] | 1.85 [1.08, 2.64] | 17 |
| pooled | CAPE-E dist (w=0.5) | 110 | 2.80 [2.11, 3.54] | 4.29 [3.30, 5.32] | 14 |
