# Progress probe: gemma_new_110

State: complete; 1320/1320 requests.

Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. Pooled weights reflect this declared sample; they are not population estimates. Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.

Reported scenarios: low, high, dynamic; pooled = low+high+dynamic.

| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |
|---|---|---:|---:|---:|---:|---:|---:|
| all/low | pearl | 110 | 24655 | 16.671 | 0.9482 | 7 | 0.00 |
| all/low | picospec | 110 | 24631 | 13.798 | 1.2169 | 7 | 67.78 |
| all/low | pipesd | 110 | 24618 | 13.818 | 1.1547 | 7 | 0.00 |
| all/low | hf_default | 110 | 24642 | 12.662 | 1.2209 | 8 | 0.00 |
| all/high | pearl | 110 | 24854 | 13.823 | 1.1061 | 10 | 0.00 |
| all/high | picospec | 110 | 24822 | 12.559 | 1.3342 | 10 | 52.88 |
| all/high | pipesd | 110 | 24593 | 11.546 | 1.3746 | 10 | 0.00 |
| all/high | hf_default | 110 | 24779 | 10.829 | 1.3057 | 10 | 0.00 |
| all/dynamic | pearl | 110 | 24722 | 13.485 | 1.0346 | 10 | 0.00 |
| all/dynamic | picospec | 110 | 24727 | 13.191 | 1.2711 | 10 | 59.59 |
| all/dynamic | pipesd | 110 | 24719 | 12.718 | 1.2516 | 10 | 0.00 |
| all/dynamic | hf_default | 110 | 24680 | 11.671 | 1.2659 | 10 | 0.00 |
| all/pooled | pearl | 330 | 74231 | 14.526 | 1.0298 | 27 | 0.00 |
| all/pooled | picospec | 330 | 74180 | 13.161 | 1.2742 | 27 | 59.46 |
| all/pooled | pipesd | 330 | 73930 | 12.627 | 1.2602 | 27 | 0.00 |
| all/pooled | hf_default | 330 | 74101 | 11.671 | 1.2643 | 28 | 0.00 |
| gsm8k/low | pearl | 50 | 7151 | 17.118 | 0.9194 | 0 | 0.00 |
| gsm8k/low | picospec | 50 | 7148 | 15.062 | 1.1118 | 0 | 70.90 |
| gsm8k/low | pipesd | 50 | 7149 | 13.968 | 1.1356 | 0 | 0.00 |
| gsm8k/low | hf_default | 50 | 7166 | 13.229 | 1.1604 | 0 | 0.00 |
| gsm8k/high | pearl | 50 | 7173 | 14.591 | 1.0473 | 0 | 0.00 |
| gsm8k/high | picospec | 50 | 7151 | 13.860 | 1.1996 | 0 | 58.73 |
| gsm8k/high | pipesd | 50 | 7151 | 12.074 | 1.3049 | 0 | 0.00 |
| gsm8k/high | hf_default | 50 | 7151 | 11.563 | 1.2272 | 0 | 0.00 |
| gsm8k/dynamic | pearl | 50 | 7152 | 13.864 | 1.0016 | 0 | 0.00 |
| gsm8k/dynamic | picospec | 50 | 7148 | 14.395 | 1.1547 | 0 | 63.90 |
| gsm8k/dynamic | pipesd | 50 | 7152 | 13.122 | 1.2042 | 0 | 0.00 |
| gsm8k/dynamic | hf_default | 50 | 7152 | 12.355 | 1.1911 | 0 | 0.00 |
| gsm8k/pooled | pearl | 150 | 21476 | 15.069 | 0.9895 | 0 | 0.00 |
| gsm8k/pooled | picospec | 150 | 21447 | 14.422 | 1.1554 | 0 | 64.13 |
| gsm8k/pooled | pipesd | 150 | 21452 | 13.008 | 1.2149 | 0 | 0.00 |
| gsm8k/pooled | hf_default | 150 | 21469 | 12.346 | 1.1929 | 0 | 0.00 |
| mtbench/low | pearl | 30 | 5723 | 14.709 | 1.0730 | 1 | 0.00 |
| mtbench/low | picospec | 30 | 5705 | 10.054 | 1.6735 | 1 | 52.06 |
| mtbench/low | pipesd | 30 | 5687 | 11.101 | 1.4353 | 1 | 0.00 |
| mtbench/low | hf_default | 30 | 5739 | 9.358 | 1.6640 | 2 | 0.00 |
| mtbench/high | pearl | 30 | 5793 | 11.195 | 1.3681 | 2 | 0.00 |
| mtbench/high | picospec | 30 | 5775 | 8.774 | 1.9149 | 2 | 30.78 |
| mtbench/high | pipesd | 30 | 5559 | 8.436 | 1.8859 | 2 | 0.00 |
| mtbench/high | hf_default | 30 | 5744 | 7.951 | 1.7849 | 2 | 0.00 |
| mtbench/dynamic | pearl | 30 | 5739 | 12.026 | 1.1620 | 2 | 0.00 |
| mtbench/dynamic | picospec | 30 | 5752 | 9.543 | 1.7608 | 2 | 39.80 |
| mtbench/dynamic | pipesd | 30 | 5741 | 9.799 | 1.6243 | 2 | 0.00 |
| mtbench/dynamic | hf_default | 30 | 5703 | 8.568 | 1.7300 | 2 | 0.00 |
| mtbench/pooled | pearl | 90 | 17255 | 12.470 | 1.2017 | 5 | 0.00 |
| mtbench/pooled | picospec | 90 | 17232 | 9.425 | 1.7835 | 5 | 39.08 |
| mtbench/pooled | pipesd | 90 | 16987 | 9.668 | 1.6467 | 5 | 0.00 |
| mtbench/pooled | hf_default | 90 | 17186 | 8.587 | 1.7263 | 6 | 0.00 |
| humaneval/low | pearl | 30 | 11781 | 17.530 | 0.9050 | 6 | 0.00 |
| humaneval/low | picospec | 30 | 11778 | 15.849 | 1.0595 | 6 | 72.09 |
| humaneval/low | pipesd | 30 | 11782 | 15.555 | 1.0308 | 6 | 0.00 |
| humaneval/low | hf_default | 30 | 11737 | 14.834 | 1.0412 | 6 | 0.00 |
| humaneval/high | pearl | 30 | 11888 | 15.068 | 1.0139 | 8 | 0.00 |
| humaneval/high | picospec | 30 | 11896 | 14.827 | 1.1333 | 8 | 61.68 |
| humaneval/high | pipesd | 30 | 11883 | 13.523 | 1.1773 | 8 | 0.00 |
| humaneval/high | hf_default | 30 | 11884 | 12.543 | 1.1213 | 8 | 0.00 |
| humaneval/dynamic | pearl | 30 | 11831 | 14.080 | 0.9928 | 8 | 0.00 |
| humaneval/dynamic | picospec | 30 | 11827 | 15.256 | 1.1034 | 8 | 66.52 |
| humaneval/dynamic | pipesd | 30 | 11826 | 14.552 | 1.0994 | 8 | 0.00 |
| humaneval/dynamic | hf_default | 30 | 11825 | 13.589 | 1.0873 | 8 | 0.00 |
| humaneval/pooled | pearl | 90 | 35500 | 15.426 | 0.9707 | 22 | 0.00 |
| humaneval/pooled | picospec | 90 | 35501 | 15.298 | 1.0988 | 22 | 66.48 |
| humaneval/pooled | pipesd | 90 | 35491 | 14.493 | 1.1027 | 22 | 0.00 |
| humaneval/pooled | hf_default | 90 | 35446 | 13.587 | 1.0835 | 22 | 0.00 |

Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.

| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |
|---|---|---:|---|---|---:|---:|

No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. Background service overlaps verification; it is not an additive latency component.
