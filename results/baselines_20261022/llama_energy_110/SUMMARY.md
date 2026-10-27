# Progress probe: llama_energy_110

State: complete; 990/990 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | markov_w025_pre | 110 | 28125 | 26.745 | 0.5374 | 12 | 44.12 |
| all/low | markov_w1_pre | 110 | 27825 | 27.098 | 0.5216 | 12 | 42.62 |
| all/low | markov_w2_pre | 110 | 27872 | 27.228 | 0.5176 | 12 | 42.18 |
| all/high | markov_w025_pre | 110 | 27206 | 18.083 | 0.7645 | 8 | 46.69 |
| all/high | markov_w1_pre | 110 | 27073 | 16.377 | 0.7139 | 7 | 47.70 |
| all/high | markov_w2_pre | 110 | 27243 | 15.754 | 0.7076 | 8 | 46.86 |
| all/dynamic | markov_w025_pre | 110 | 27751 | 21.872 | 0.6381 | 11 | 46.29 |
| all/dynamic | markov_w1_pre | 110 | 27771 | 21.063 | 0.6126 | 10 | 45.03 |
| all/dynamic | markov_w2_pre | 110 | 27774 | 20.863 | 0.6038 | 11 | 44.39 |
| all/pooled | markov_w025_pre | 330 | 83082 | 21.721 | 0.6454 | 31 | 45.77 |
| all/pooled | markov_w1_pre | 330 | 82669 | 20.676 | 0.6151 | 29 | 45.12 |
| all/pooled | markov_w2_pre | 330 | 82889 | 20.295 | 0.6090 | 31 | 44.44 |
| mtbench/low | markov_w025_pre | 30 | 8341 | 23.223 | 0.6063 | 6 | 33.29 |
| mtbench/low | markov_w1_pre | 30 | 8354 | 24.286 | 0.5753 | 6 | 33.17 |
| mtbench/low | markov_w2_pre | 30 | 8348 | 23.898 | 0.5793 | 7 | 33.29 |
| mtbench/high | markov_w025_pre | 30 | 8474 | 13.784 | 0.9483 | 7 | 34.39 |
| mtbench/high | markov_w1_pre | 30 | 8334 | 12.463 | 0.8380 | 6 | 32.58 |
| mtbench/high | markov_w2_pre | 30 | 8513 | 12.002 | 0.8261 | 7 | 32.17 |
| mtbench/dynamic | markov_w025_pre | 30 | 8316 | 18.275 | 0.7322 | 6 | 34.73 |
| mtbench/dynamic | markov_w1_pre | 30 | 8464 | 17.992 | 0.6840 | 6 | 32.96 |
| mtbench/dynamic | markov_w2_pre | 30 | 8342 | 17.860 | 0.6719 | 6 | 32.63 |
| mtbench/pooled | markov_w025_pre | 90 | 25131 | 17.587 | 0.7633 | 19 | 34.17 |
| mtbench/pooled | markov_w1_pre | 90 | 25152 | 16.959 | 0.6990 | 18 | 32.91 |
| mtbench/pooled | markov_w2_pre | 90 | 25203 | 16.519 | 0.6933 | 20 | 32.72 |
| gsm8k/low | markov_w025_pre | 50 | 10062 | 27.469 | 0.5218 | 5 | 45.44 |
| gsm8k/low | markov_w1_pre | 50 | 9967 | 27.393 | 0.5126 | 5 | 43.52 |
| gsm8k/low | markov_w2_pre | 50 | 9764 | 27.788 | 0.5055 | 4 | 42.94 |
| gsm8k/high | markov_w025_pre | 50 | 8984 | 18.778 | 0.7437 | 0 | 46.90 |
| gsm8k/high | markov_w1_pre | 50 | 9015 | 16.357 | 0.7107 | 0 | 47.05 |
| gsm8k/high | markov_w2_pre | 50 | 9033 | 15.937 | 0.6974 | 0 | 45.92 |
| gsm8k/dynamic | markov_w025_pre | 50 | 9833 | 22.087 | 0.6338 | 4 | 46.79 |
| gsm8k/dynamic | markov_w1_pre | 50 | 9599 | 20.727 | 0.6120 | 3 | 44.59 |
| gsm8k/dynamic | markov_w2_pre | 50 | 9778 | 20.785 | 0.5999 | 4 | 44.37 |
| gsm8k/pooled | markov_w025_pre | 150 | 28879 | 22.388 | 0.6290 | 9 | 46.40 |
| gsm8k/pooled | markov_w1_pre | 150 | 28581 | 20.739 | 0.6084 | 8 | 44.99 |
| gsm8k/pooled | markov_w2_pre | 150 | 28575 | 20.578 | 0.5985 | 8 | 44.32 |
| humaneval/low | markov_w025_pre | 30 | 9722 | 29.812 | 0.4942 | 1 | 53.07 |
| humaneval/low | markov_w1_pre | 30 | 9504 | 29.795 | 0.4839 | 1 | 50.73 |
| humaneval/low | markov_w2_pre | 30 | 9760 | 30.219 | 0.4770 | 1 | 49.79 |
| humaneval/high | markov_w025_pre | 30 | 9748 | 23.701 | 0.6240 | 1 | 58.62 |
| humaneval/high | markov_w1_pre | 30 | 9724 | 22.445 | 0.6104 | 1 | 59.05 |
| humaneval/high | markov_w2_pre | 30 | 9697 | 21.397 | 0.6132 | 1 | 58.42 |
| humaneval/dynamic | markov_w025_pre | 30 | 9602 | 26.051 | 0.5611 | 1 | 56.30 |
| humaneval/dynamic | markov_w1_pre | 30 | 9708 | 25.222 | 0.5509 | 1 | 55.28 |
| humaneval/dynamic | markov_w2_pre | 30 | 9654 | 24.520 | 0.5489 | 1 | 53.86 |
| humaneval/pooled | markov_w025_pre | 90 | 29072 | 26.286 | 0.5598 | 3 | 56.20 |
| humaneval/pooled | markov_w1_pre | 90 | 28936 | 25.447 | 0.5489 | 3 | 55.29 |
| humaneval/pooled | markov_w2_pre | 90 | 29111 | 24.884 | 0.5462 | 3 | 54.22 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
