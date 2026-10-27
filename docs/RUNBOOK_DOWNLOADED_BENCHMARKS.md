# Experiments on the user's downloaded datasets

Use the existing files in `common/data/` only. This entrypoint does not fetch data or use the full official GSM8K file from the earlier research campaign.

| Dataset | Local file | Questions | Timed requests |
|---|---|---:|---:|
| GSM8K | `common/data/gsm8k_test_50.jsonl` | 50 | 450 |
| HumanEval | `common/data/humaneval_30.jsonl` | 30 | 270 |
| MT-Bench | `common/data/mtbench_30.jsonl` | 30 | 270 |

The current files contain 110 questions in total. Three methods (`fixed`, `fixed_fast`, `regime`) run at three added delays (2, 100, 300 ms), once per condition: **990 timed requests**. The runner also generates one untimed cloud reference per question. All available rows in each local file are selected automatically.

```bash
cd /home/jetson/zishi_edge-cloud-speculative-decoding
bash run_downloaded_benchmarks.sh
```

Both Llama model services must already be running. The default draft endpoint is `http://127.0.0.1:8080`; the cloud endpoint is `http://172.23.123.195:9090`. Override `DRAFT_URL` and `CLOUD_URL` as environment variables if necessary. `PYTHON` can select an interpreter; otherwise the script uses `.venv/bin/python` when available, then `python3`.

Inspect the resolved protocols without contacting models:

```bash
bash run_downloaded_benchmarks.sh --plan
```

Each dataset gets a separate phase directory and `SUMMARY.md` under `results/downloaded_benchmarks/`. The script stops on a failed phase and does not silently retry or start a duplicate draft service. It does not provide resume support; restarting the command creates new runs.

The 512-token output cap, strict K=1, model pair, fixed controls and adaptive controller match the prior comparison. Task configurations are separate: HumanEval and MT-Bench do not receive the GSM8K numeric-answer instruction. The local MT-Bench file contains only the first turn of each selected question.

The existing evaluator scores GSM8K numeric answers. It does **not** calculate HumanEval pass@1 or MT-Bench judge scores. For those datasets, `task_quality`/aggregate `quality` are null and the report's `Correct` column shows N/A. Use their speed, energy, truncation and token-sequence diagnostics only. Task-quality preservation is not established for these two datasets.

Energy sampling measures gross Jetson board input, excluding cloud and network energy. The research objective is acceleration without a substantial energy increase. The existing phase report retains the earlier strict energy-reduction target; no acceptable numerical overhead tolerance has yet been specified. These runs use previously downloaded/exposed samples and are labelled development rather than new held-out confirmation.
