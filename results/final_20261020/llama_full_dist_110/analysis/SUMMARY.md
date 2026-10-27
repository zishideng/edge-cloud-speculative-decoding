# Cross-pair results against the best fixed window

fixed_g4 is the raw arm fixed_fast. best_fixed is, per delay, the fixed window (g2/g4/g8) with the highest throughput; pooled combines those per-delay choices. It is chosen after the measurement, so it is an oracle baseline.

alpha = strict accepted / examined draft tokens; tau = accepted draft tokens per verification round; util = accepted / proposed draft tokens. sync_g4 and fixed_g4 use the same window, so their acceptance differs only through prefetch reuse.

## results/final_20261020/llama_full_dist_110

results/final_20261020/llama_full_dist_110: 2310/2310 requests. Best fixed window: low: fixed_g2, high: fixed_g4, dynamic: fixed_g4.

| Delay | Method | Requests | tokens/s | J/token | alpha % | tau | util % |
|---|---|---:|---:|---:|---:|---:|---:|
| low | sync_g4 | 110 | 23.60 | 0.4985 | 86.2 | 2.74 | 68.9 |
| low | fixed_g2 | 110 | 26.77 | 0.5559 | 86.0 | 1.59 | 79.7 |
| low | fixed_g4 | 110 | 23.55 | 0.6868 | 86.2 | 2.74 | 68.9 |
| low | fixed_g8 | 110 | 16.69 | 1.0023 | 86.3 | 4.16 | 52.7 |
| low | **best_fixed** (fixed_g2) | 110 | 26.77 | 0.5559 | 86.0 | 1.59 | 79.7 |
| low | adaedl | 110 | 20.36 | 0.6325 | 90.0 | 3.41 | 70.2 |
| low | CAPE-S dist (w=0) | 110 | 26.30 | 0.5562 | 86.7 | 1.43 | 80.1 |
| low | CAPE-E dist (w=0.5) | 110 | 26.69 | 0.5341 | 86.4 | 1.20 | 82.2 |
| high | sync_g4 | 110 | 12.73 | 0.6159 | 85.9 | 2.72 | 68.3 |
| high | fixed_g2 | 110 | 14.22 | 0.6910 | 85.6 | 1.58 | 79.1 |
| high | fixed_g4 | 110 | 18.15 | 0.7699 | 85.9 | 2.72 | 68.3 |
| high | fixed_g8 | 110 | 15.68 | 1.0388 | 85.9 | 4.09 | 51.8 |
| high | **best_fixed** (fixed_g4) | 110 | 18.15 | 0.7699 | 85.9 | 2.72 | 68.3 |
| high | adaedl | 110 | 12.09 | 0.7323 | 89.6 | 3.40 | 69.1 |
| high | CAPE-S dist (w=0) | 110 | 18.74 | 0.7839 | 86.5 | 2.62 | 68.9 |
| high | CAPE-E dist (w=0.5) | 110 | 17.27 | 0.7197 | 86.4 | 2.35 | 72.0 |
| dynamic | sync_g4 | 110 | 17.60 | 0.5381 | 86.1 | 2.73 | 68.6 |
| dynamic | fixed_g2 | 110 | 20.01 | 0.6195 | 85.6 | 1.58 | 79.2 |
| dynamic | fixed_g4 | 110 | 20.68 | 0.7251 | 86.1 | 2.73 | 68.6 |
| dynamic | fixed_g8 | 110 | 16.26 | 1.0144 | 86.1 | 4.14 | 52.4 |
| dynamic | **best_fixed** (fixed_g4) | 110 | 20.68 | 0.7251 | 86.1 | 2.73 | 68.6 |
| dynamic | adaedl | 110 | 15.80 | 0.6735 | 89.9 | 3.45 | 69.8 |
| dynamic | CAPE-S dist (w=0) | 110 | 21.68 | 0.6700 | 86.4 | 1.98 | 73.0 |
| dynamic | CAPE-E dist (w=0.5) | 110 | 21.18 | 0.6235 | 86.4 | 1.70 | 75.1 |
| pooled | sync_g4 | 330 | 16.89 | 0.5507 | 86.1 | 2.73 | 68.6 |
| pooled | fixed_g2 | 330 | 19.02 | 0.6222 | 85.8 | 1.58 | 79.3 |
| pooled | fixed_g4 | 330 | 20.56 | 0.7272 | 86.1 | 2.73 | 68.6 |
| pooled | fixed_g8 | 330 | 16.20 | 1.0184 | 86.1 | 4.13 | 52.3 |
| pooled | **best_fixed** | 330 | 21.29 | 0.6840 | 86.0 | 2.25 | 71.4 |
| pooled | adaedl | 330 | 15.39 | 0.6792 | 89.8 | 3.42 | 69.7 |
| pooled | CAPE-S dist (w=0) | 330 | 21.83 | 0.6695 | 86.5 | 1.93 | 73.4 |
| pooled | CAPE-E dist (w=0.5) | 330 | 21.05 | 0.6255 | 86.4 | 1.67 | 75.8 |

Paired effects versus best_fixed (prompt-cluster bootstrap, 2000 draws). Positive energy saving means lower J/token.

| Delay | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences |
|---|---|---:|---|---|---:|
| low | sync_g4 | 110 | -11.82 [-12.87, -10.65] | 10.33 [9.47, 11.21] | 18 |
| low | adaedl | 110 | -23.94 [-24.94, -22.90] | -13.77 [-14.90, -12.62] | 22 |
| low | CAPE-S dist (w=0) | 110 | -1.74 [-2.68, -0.71] | -0.05 [-1.20, 1.16] | 7 |
| low | CAPE-E dist (w=0.5) | 110 | -0.29 [-1.47, 0.90] | 3.94 [2.70, 5.18] | 10 |
| high | sync_g4 | 110 | -29.86 [-31.29, -28.42] | 20.00 [18.11, 21.78] | 1 |
| high | adaedl | 110 | -33.36 [-34.47, -32.32] | 4.89 [3.22, 6.49] | 24 |
| high | CAPE-S dist (w=0) | 110 | 3.25 [1.98, 4.70] | -1.81 [-2.99, -0.45] | 18 |
| high | CAPE-E dist (w=0.5) | 110 | -4.82 [-6.38, -3.20] | 6.53 [4.75, 8.19] | 17 |
| dynamic | sync_g4 | 110 | -14.90 [-17.22, -12.61] | 25.79 [23.86, 27.56] | 0 |
| dynamic | adaedl | 110 | -23.56 [-25.49, -21.61] | 7.12 [5.24, 8.88] | 19 |
| dynamic | CAPE-S dist (w=0) | 110 | 4.88 [3.08, 6.80] | 7.60 [5.54, 9.68] | 17 |
| dynamic | CAPE-E dist (w=0.5) | 110 | 2.42 [0.65, 4.47] | 14.01 [11.58, 16.26] | 15 |
| pooled | sync_g4 | 110 | -20.69 [-22.17, -19.23] | 19.48 [17.95, 20.95] | 19 |
| pooled | adaedl | 110 | -27.69 [-28.82, -26.56] | 0.70 [-0.62, 1.99] | 65 |
| pooled | CAPE-S dist (w=0) | 110 | 2.55 [1.71, 3.42] | 2.12 [1.01, 3.25] | 42 |
| pooled | CAPE-E dist (w=0.5) | 110 | -1.12 [-1.92, -0.26] | 8.55 [6.78, 10.26] | 42 |
