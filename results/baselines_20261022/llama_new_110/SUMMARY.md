# Progress probe: llama_new_110

State: complete; 1980/1980 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | markov_w0_pre | 110 | 27071 | 26.402 | 0.5569 | 9 | 45.12 |
| all/low | markov_w05_pre | 110 | 27248 | 26.942 | 0.5330 | 9 | 43.37 |
| all/low | pearl | 110 | 27329 | 27.666 | 0.5000 | 9 | 0.00 |
| all/low | picospec | 110 | 26914 | 24.340 | 0.6666 | 9 | 54.71 |
| all/low | pipesd | 110 | 27357 | 24.905 | 0.6292 | 9 | 0.00 |
| all/low | hf_default | 110 | 27651 | 21.972 | 0.6607 | 10 | 0.00 |
| all/high | markov_w0_pre | 110 | 27882 | 18.774 | 0.8003 | 11 | 45.49 |
| all/high | markov_w05_pre | 110 | 27765 | 17.648 | 0.7339 | 13 | 48.03 |
| all/high | pearl | 110 | 27628 | 18.187 | 0.7580 | 12 | 0.00 |
| all/high | picospec | 110 | 27407 | 17.997 | 0.7806 | 12 | 38.92 |
| all/high | pipesd | 110 | 27702 | 15.544 | 0.9951 | 13 | 0.00 |
| all/high | hf_default | 110 | 27934 | 13.379 | 0.7518 | 11 | 0.00 |
| all/dynamic | markov_w0_pre | 110 | 27633 | 21.604 | 0.6786 | 11 | 45.93 |
| all/dynamic | markov_w05_pre | 110 | 27668 | 21.360 | 0.6293 | 10 | 45.78 |
| all/dynamic | pearl | 110 | 27572 | 20.005 | 0.6173 | 9 | 0.00 |
| all/dynamic | picospec | 110 | 27316 | 21.160 | 0.7125 | 10 | 46.40 |
| all/dynamic | pipesd | 110 | 27598 | 20.274 | 0.7682 | 10 | 0.00 |
| all/dynamic | hf_default | 110 | 27755 | 17.373 | 0.7045 | 9 | 0.00 |
| all/pooled | markov_w0_pre | 330 | 82586 | 21.793 | 0.6798 | 31 | 45.54 |
| all/pooled | markov_w05_pre | 330 | 82681 | 21.310 | 0.6327 | 32 | 45.85 |
| all/pooled | pearl | 330 | 82529 | 21.242 | 0.6256 | 30 | 0.00 |
| all/pooled | picospec | 330 | 81637 | 20.828 | 0.7202 | 31 | 45.73 |
| all/pooled | pipesd | 330 | 82657 | 19.486 | 0.7982 | 32 | 0.00 |
| all/pooled | hf_default | 330 | 83340 | 16.857 | 0.7058 | 30 | 0.00 |
| mtbench/low | markov_w0_pre | 30 | 8353 | 22.753 | 0.6311 | 6 | 33.88 |
| mtbench/low | markov_w05_pre | 30 | 8266 | 23.915 | 0.5879 | 6 | 33.77 |
| mtbench/low | pearl | 30 | 8275 | 25.073 | 0.5509 | 6 | 0.00 |
| mtbench/low | picospec | 30 | 8375 | 19.010 | 0.8564 | 6 | 38.69 |
| mtbench/low | pipesd | 30 | 8271 | 20.331 | 0.7721 | 6 | 0.00 |
| mtbench/low | hf_default | 30 | 8391 | 18.605 | 0.7835 | 6 | 0.00 |
| mtbench/high | markov_w0_pre | 30 | 8475 | 14.279 | 1.0431 | 5 | 33.39 |
| mtbench/high | markov_w05_pre | 30 | 8476 | 13.134 | 0.8898 | 7 | 35.10 |
| mtbench/high | pearl | 30 | 8485 | 14.292 | 0.9668 | 6 | 0.00 |
| mtbench/high | picospec | 30 | 8503 | 13.939 | 1.0203 | 6 | 22.97 |
| mtbench/high | pipesd | 30 | 8351 | 11.460 | 1.3591 | 7 | 0.00 |
| mtbench/high | hf_default | 30 | 8419 | 10.714 | 0.9056 | 5 | 0.00 |
| mtbench/dynamic | markov_w0_pre | 30 | 8188 | 18.100 | 0.7967 | 6 | 34.24 |
| mtbench/dynamic | markov_w05_pre | 30 | 8293 | 18.080 | 0.7090 | 6 | 34.09 |
| mtbench/dynamic | pearl | 30 | 8164 | 17.492 | 0.7153 | 6 | 0.00 |
| mtbench/dynamic | picospec | 30 | 8309 | 16.810 | 0.9060 | 6 | 31.44 |
| mtbench/dynamic | pipesd | 30 | 8177 | 16.170 | 0.9667 | 6 | 0.00 |
| mtbench/dynamic | hf_default | 30 | 8349 | 14.537 | 0.8412 | 6 | 0.00 |
| mtbench/pooled | markov_w0_pre | 90 | 25016 | 17.704 | 0.8249 | 17 | 33.78 |
| mtbench/pooled | markov_w05_pre | 90 | 25035 | 17.270 | 0.7302 | 19 | 34.36 |
| mtbench/pooled | pearl | 90 | 24924 | 17.925 | 0.7463 | 18 | 0.00 |
| mtbench/pooled | picospec | 90 | 25187 | 16.304 | 0.9281 | 18 | 29.60 |
| mtbench/pooled | pipesd | 90 | 24799 | 15.110 | 1.0339 | 19 | 0.00 |
| mtbench/pooled | hf_default | 90 | 25159 | 13.891 | 0.8435 | 17 | 0.00 |
| gsm8k/low | markov_w0_pre | 50 | 9333 | 26.837 | 0.5476 | 1 | 45.36 |
| gsm8k/low | markov_w05_pre | 50 | 9539 | 27.266 | 0.5266 | 1 | 43.09 |
| gsm8k/low | pearl | 50 | 9458 | 28.289 | 0.4913 | 1 | 0.00 |
| gsm8k/low | picospec | 50 | 9126 | 25.452 | 0.6341 | 1 | 57.21 |
| gsm8k/low | pipesd | 50 | 9371 | 25.588 | 0.6111 | 1 | 0.00 |
| gsm8k/low | hf_default | 50 | 9467 | 21.892 | 0.6627 | 2 | 0.00 |
| gsm8k/high | markov_w0_pre | 50 | 9629 | 19.876 | 0.7556 | 4 | 47.13 |
| gsm8k/high | markov_w05_pre | 50 | 9597 | 18.497 | 0.7185 | 4 | 48.03 |
| gsm8k/high | pearl | 50 | 9746 | 19.187 | 0.7189 | 4 | 0.00 |
| gsm8k/high | picospec | 50 | 9473 | 19.017 | 0.7340 | 4 | 42.42 |
| gsm8k/high | pipesd | 50 | 9627 | 16.363 | 0.9380 | 4 | 0.00 |
| gsm8k/high | hf_default | 50 | 9716 | 13.629 | 0.7465 | 4 | 0.00 |
| gsm8k/dynamic | markov_w0_pre | 50 | 9752 | 21.600 | 0.6788 | 4 | 46.04 |
| gsm8k/dynamic | markov_w05_pre | 50 | 9939 | 21.109 | 0.6325 | 3 | 45.29 |
| gsm8k/dynamic | pearl | 50 | 9700 | 19.947 | 0.6083 | 2 | 0.00 |
| gsm8k/dynamic | picospec | 50 | 9469 | 21.770 | 0.6860 | 3 | 47.63 |
| gsm8k/dynamic | pipesd | 50 | 9859 | 20.597 | 0.7523 | 3 | 0.00 |
| gsm8k/dynamic | hf_default | 50 | 9682 | 17.033 | 0.7079 | 2 | 0.00 |
| gsm8k/pooled | markov_w0_pre | 150 | 28714 | 22.368 | 0.6619 | 9 | 46.27 |
| gsm8k/pooled | markov_w05_pre | 150 | 29075 | 21.705 | 0.6261 | 8 | 45.57 |
| gsm8k/pooled | pearl | 150 | 28904 | 21.756 | 0.6073 | 7 | 0.00 |
| gsm8k/pooled | picospec | 150 | 28068 | 21.730 | 0.6853 | 8 | 48.23 |
| gsm8k/pooled | pipesd | 150 | 28857 | 20.134 | 0.7684 | 8 | 0.00 |
| gsm8k/pooled | hf_default | 150 | 28865 | 16.843 | 0.7061 | 8 | 0.00 |
| humaneval/low | markov_w0_pre | 30 | 9385 | 30.230 | 0.5002 | 2 | 55.90 |
| humaneval/low | markov_w05_pre | 30 | 9443 | 29.895 | 0.4915 | 2 | 52.76 |
| humaneval/low | pearl | 30 | 9596 | 29.667 | 0.4647 | 2 | 0.00 |
| humaneval/low | picospec | 30 | 9413 | 30.697 | 0.5293 | 2 | 66.29 |
| humaneval/low | pipesd | 30 | 9715 | 29.854 | 0.5249 | 2 | 0.00 |
| humaneval/low | hf_default | 30 | 9793 | 26.115 | 0.5535 | 2 | 0.00 |
| humaneval/high | markov_w0_pre | 30 | 9778 | 24.017 | 0.6339 | 2 | 58.36 |
| humaneval/high | markov_w05_pre | 30 | 9692 | 23.691 | 0.6127 | 2 | 59.40 |
| humaneval/high | pearl | 30 | 9397 | 22.508 | 0.6101 | 2 | 0.00 |
| humaneval/high | picospec | 30 | 9431 | 22.743 | 0.6112 | 2 | 54.67 |
| humaneval/high | pipesd | 30 | 9724 | 20.904 | 0.7390 | 2 | 0.00 |
| humaneval/high | hf_default | 30 | 9799 | 16.630 | 0.6249 | 2 | 0.00 |
| humaneval/dynamic | markov_w0_pre | 30 | 9693 | 25.834 | 0.5786 | 1 | 57.16 |
| humaneval/dynamic | markov_w05_pre | 30 | 9436 | 25.796 | 0.5558 | 1 | 56.42 |
| humaneval/dynamic | pearl | 30 | 9708 | 22.828 | 0.5439 | 1 | 0.00 |
| humaneval/dynamic | picospec | 30 | 9538 | 26.369 | 0.5703 | 1 | 59.62 |
| humaneval/dynamic | pipesd | 30 | 9562 | 25.370 | 0.6150 | 1 | 0.00 |
| humaneval/dynamic | hf_default | 30 | 9724 | 21.380 | 0.5838 | 1 | 0.00 |
| humaneval/pooled | markov_w0_pre | 90 | 28856 | 26.406 | 0.5718 | 5 | 57.25 |
| humaneval/pooled | markov_w05_pre | 90 | 28571 | 26.194 | 0.5539 | 5 | 56.44 |
| humaneval/pooled | pearl | 90 | 28701 | 24.610 | 0.5391 | 5 | 0.00 |
| humaneval/pooled | picospec | 90 | 28382 | 26.206 | 0.5703 | 5 | 59.82 |
| humaneval/pooled | pipesd | 90 | 29001 | 24.841 | 0.6264 | 5 | 0.00 |
| humaneval/pooled | hf_default | 90 | 29316 | 20.659 | 0.5874 | 5 | 0.00 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
