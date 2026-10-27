# Progress probe: qwen_new_110

State: complete; 1320/1320 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | pearl | 110 | 30804 | 30.493 | 0.2659 | 6 | 0.00 |
| all/low | picospec | 110 | 30897 | 35.069 | 0.3599 | 7 | 46.36 |
| all/low | pipesd | 110 | 30833 | 32.025 | 0.3713 | 6 | 0.00 |
| all/low | hf_default | 110 | 30831 | 22.849 | 0.3699 | 6 | 0.00 |
| all/high | pearl | 110 | 30967 | 17.765 | 0.4833 | 6 | 0.00 |
| all/high | picospec | 110 | 30956 | 17.751 | 0.4677 | 7 | 35.41 |
| all/high | pipesd | 110 | 30905 | 18.446 | 0.6355 | 6 | 0.00 |
| all/high | hf_default | 110 | 30998 | 12.902 | 0.5058 | 6 | 0.00 |
| all/dynamic | pearl | 110 | 30814 | 24.858 | 0.3632 | 6 | 0.00 |
| all/dynamic | picospec | 110 | 30764 | 25.678 | 0.4022 | 6 | 41.73 |
| all/dynamic | pipesd | 110 | 30793 | 24.209 | 0.4899 | 6 | 0.00 |
| all/dynamic | hf_default | 110 | 31014 | 17.388 | 0.4198 | 7 | 0.00 |
| all/pooled | pearl | 330 | 92585 | 23.187 | 0.3710 | 18 | 0.00 |
| all/pooled | picospec | 330 | 92617 | 24.226 | 0.4100 | 20 | 40.68 |
| all/pooled | pipesd | 330 | 92531 | 23.664 | 0.4990 | 18 | 0.00 |
| all/pooled | hf_default | 330 | 92843 | 16.772 | 0.4319 | 19 | 0.00 |
| humaneval/low | pearl | 30 | 10320 | 30.751 | 0.2595 | 1 | 0.00 |
| humaneval/low | picospec | 30 | 10361 | 39.009 | 0.3215 | 2 | 51.63 |
| humaneval/low | pipesd | 30 | 10354 | 34.878 | 0.3398 | 1 | 0.00 |
| humaneval/low | hf_default | 30 | 10370 | 24.987 | 0.3320 | 1 | 0.00 |
| humaneval/high | pearl | 30 | 10338 | 20.157 | 0.4273 | 1 | 0.00 |
| humaneval/high | picospec | 30 | 10351 | 19.699 | 0.4184 | 1 | 41.56 |
| humaneval/high | pipesd | 30 | 10276 | 21.176 | 0.5564 | 1 | 0.00 |
| humaneval/high | hf_default | 30 | 10390 | 14.437 | 0.4553 | 1 | 0.00 |
| humaneval/dynamic | pearl | 30 | 10320 | 27.393 | 0.3325 | 1 | 0.00 |
| humaneval/dynamic | picospec | 30 | 10377 | 28.266 | 0.3607 | 1 | 47.69 |
| humaneval/dynamic | pipesd | 30 | 10307 | 26.827 | 0.4382 | 1 | 0.00 |
| humaneval/dynamic | hf_default | 30 | 10446 | 19.123 | 0.3796 | 2 | 0.00 |
| humaneval/pooled | pearl | 90 | 30978 | 25.284 | 0.3398 | 3 | 0.00 |
| humaneval/pooled | picospec | 90 | 31089 | 26.843 | 0.3668 | 4 | 46.61 |
| humaneval/pooled | pipesd | 90 | 30937 | 26.525 | 0.4445 | 3 | 0.00 |
| humaneval/pooled | hf_default | 90 | 31206 | 18.564 | 0.3889 | 4 | 0.00 |
| gsm8k/low | pearl | 50 | 13035 | 32.964 | 0.2468 | 0 | 0.00 |
| gsm8k/low | picospec | 50 | 13049 | 44.410 | 0.2813 | 0 | 59.04 |
| gsm8k/low | pipesd | 50 | 13051 | 39.130 | 0.2975 | 0 | 0.00 |
| gsm8k/low | hf_default | 50 | 13105 | 27.602 | 0.3108 | 0 | 0.00 |
| gsm8k/high | pearl | 50 | 13006 | 23.018 | 0.3755 | 0 | 0.00 |
| gsm8k/high | picospec | 50 | 13011 | 22.376 | 0.3665 | 0 | 50.24 |
| gsm8k/high | pipesd | 50 | 13016 | 25.101 | 0.4559 | 0 | 0.00 |
| gsm8k/high | hf_default | 50 | 13087 | 16.042 | 0.4140 | 0 | 0.00 |
| gsm8k/dynamic | pearl | 50 | 13018 | 29.468 | 0.3053 | 0 | 0.00 |
| gsm8k/dynamic | picospec | 50 | 13010 | 32.161 | 0.3162 | 0 | 55.30 |
| gsm8k/dynamic | pipesd | 50 | 13028 | 30.081 | 0.3881 | 0 | 0.00 |
| gsm8k/dynamic | hf_default | 50 | 13127 | 21.121 | 0.3529 | 0 | 0.00 |
| gsm8k/pooled | pearl | 150 | 39059 | 27.855 | 0.3092 | 0 | 0.00 |
| gsm8k/pooled | picospec | 150 | 39070 | 30.528 | 0.3213 | 0 | 54.62 |
| gsm8k/pooled | pipesd | 150 | 39095 | 30.420 | 0.3804 | 0 | 0.00 |
| gsm8k/pooled | hf_default | 150 | 39319 | 20.563 | 0.3592 | 0 | 0.00 |
| mtbench/low | pearl | 30 | 7449 | 26.684 | 0.3079 | 5 | 0.00 |
| mtbench/low | picospec | 30 | 7487 | 23.280 | 0.5499 | 5 | 21.29 |
| mtbench/low | pipesd | 30 | 7428 | 22.348 | 0.5448 | 5 | 0.00 |
| mtbench/low | hf_default | 30 | 7356 | 16.008 | 0.5287 | 5 | 0.00 |
| mtbench/high | pearl | 30 | 7623 | 11.459 | 0.7431 | 5 | 0.00 |
| mtbench/high | picospec | 30 | 7594 | 11.922 | 0.7085 | 6 | 13.20 |
| mtbench/high | pipesd | 30 | 7613 | 11.334 | 1.0495 | 5 | 0.00 |
| mtbench/high | hf_default | 30 | 7521 | 8.675 | 0.7353 | 5 | 0.00 |
| mtbench/dynamic | pearl | 30 | 7476 | 17.753 | 0.5066 | 5 | 0.00 |
| mtbench/dynamic | picospec | 30 | 7377 | 17.299 | 0.6123 | 5 | 17.31 |
| mtbench/dynamic | pipesd | 30 | 7458 | 16.403 | 0.7391 | 5 | 0.00 |
| mtbench/dynamic | hf_default | 30 | 7441 | 12.082 | 0.5944 | 5 | 0.00 |
| mtbench/pooled | pearl | 90 | 22548 | 16.512 | 0.5209 | 15 | 0.00 |
| mtbench/pooled | picospec | 90 | 22458 | 16.215 | 0.6240 | 16 | 16.66 |
| mtbench/pooled | pipesd | 90 | 22499 | 15.424 | 0.7800 | 15 | 0.00 |
| mtbench/pooled | hf_default | 90 | 22318 | 11.490 | 0.6202 | 15 | 0.00 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
