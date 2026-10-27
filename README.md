# Edge–Cloud Speculative Decoding

当前研究目标：**在不大量增加能耗的前提下提升解码速度**。
Jetson Orin Nano 上的 Llama-3.2-1B 草稿模型通过校园 Wi-Fi 为 RTX 3080 服务器上的
Llama-3.1-8B（AWQ）目标模型提供草稿，严格接受 K=1。当前方法为 **CAPE**：
关键路径感知的预取控制器（两状态 Markov 模型），每轮选择新起草窗口 γ_f 和预取长度 h，
权重 w 在速度与 Jetson 能耗之间折中（`edge/edge_client_pipeline.py`、`common/pipeline_model.py`）。

## 论文

[CAPE 论文初稿](paper/cape_20261010/)：[PDF](paper/cape_20261010/main.pdf)、
[LaTeX 包](paper/cape_20261010/cape_20261010_latex.zip)。文中所有数字由
`paper/cape_20261010/scripts/` 从原始记录生成。后续修改遵循[论文写作说明](docs/WRITING_GUIDELINES.md)。

## 主要实验

| 实验 | 目录 | 内容 |
|---|---|---|
| 主评测 | `results/compare_20261010/full_110` | 110 题 × 7 方法 × 2 个附加延迟（2/100 ms），1540 个请求 |
| 留出集 1、2 | `results/pipeline_research_20261009/confirm_markov`、`final_markov_v2` | CAPE 默认设置（w=0.25）与 Fixed-4、Regime 对比 |

中文汇总见[研究报告](results/pipeline_research_20261009/REPORT.md)，过程记录见 `research_log.md`。
原始逐请求记录和功率采样（`*.json`）只保存在本机，不上传 GitHub。

运行一组对比（计划文件写明方法、题目、延迟、种子，运行前冻结）：

```bash
python3 -u -m experiments.progress_probe --plan results/compare_20261010/full_110_plan.json
python3 -u -m experiments.progress_probe --plan <plan.json> --resume        # 中断后续跑
python3 -m experiments.progress_probe --report <campaign>/<phase>          # 只重算报告
```

方法：`sync_g4`（无预取）、`fixed_g2`/`fixed_fast`/`fixed_g8`（固定 γ 与 h=γ+1）、
`adaedl`（AdaEDL 基线）、`markov`/`markov_w0`/`markov_w05`（CAPE，w=0.25/0/0.5）。
详见[运行手册](docs/RUNBOOK_PROGRESS_PROBES.md)。

## 模型服务

已有服务正常运行时直接复用。默认地址为本地 `127.0.0.1:8080` 和服务器 `172.23.123.195:9090`。

```bash
LLAMA_ARG_MMAP=0 HOST=127.0.0.1 PORT=8080 NGL=99 CTX=4096 CACHE_RAM=256 \
  bash edge/scripts/start_draft_server.sh llama3_awq

# GPU 服务器（conda 环境 vllm）
python3 -m cloud.verify_server \
  --target hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4 \
  --host 0.0.0.0 --port 9090 --max-model-len 4096
```

Qwen2.5 模型对 `qwen25_05b_7b_awq`（0.5B-Instruct Q4_K_M 草稿 + 7B-Instruct AWQ 目标）使用相同端口，
切换模型对前先停掉旧服务：

```bash
# Jetson：下载并启动草稿
REPO=Qwen/Qwen2.5-0.5B-Instruct-GGUF MODEL_FILE=qwen2.5-0.5b-instruct-q4_k_m.gguf \
  MINSIZE=400000000 bash edge/scripts/download_model.sh
LLAMA_ARG_MMAP=0 HOST=127.0.0.1 PORT=8080 NGL=99 CTX=4096 CACHE_RAM=256 \
  bash edge/scripts/start_draft_server.sh qwen25_05b_7b_awq

# GPU 服务器（conda 环境 vllm）
python3 -m cloud.verify_server \
  --target Qwen/Qwen2.5-7B-Instruct-AWQ \
  --host 0.0.0.0 --port 9090 --max-model-len 4096
```

7B 的嵌入层填充到 152064 行，草稿 GGUF 为 151936 行，前 151665 个 token 逐一相同、其余均为填充。
`models.yaml` 用 `target_vocab_size` 声明这一差异，校验仍要求两端与声明值完全一致。实验通过配置项
`MODEL_PAIR` 选择模型对（`progress_probe` 读取 `configs/research.downloaded.gsm8k.json`，当前为 `llama3_awq`）。

模型注册表为 `configs/models.yaml`。环境依赖见 `edge/requirements.txt`、
`cloud/requirements.txt` 和 `requirements-experiments.txt`。

## 指标

- 速度为总输出 tokens / 总请求时间，包含后台草稿收尾。
- 能耗为 Jetson 整板输入功率积分（J/token）；不含服务器和网络能耗。
- 只报告 2/100 ms 附加延迟及其合并（pooled）；附加延迟叠加在真实 Wi-Fi 链路之上。
- 成对效应使用按题目聚类的 bootstrap 95% 区间（2000 次）。

## 早期基准（regime 方法）

`run_downloaded_benchmarks.sh` 用 50/30/30 本地题目比较 `fixed`、`fixed_fast`、`regime`
（[运行手册](docs/RUNBOOK_DOWNLOADED_BENCHMARKS.md)）。其 10 月 7–8 日的结果和旧论文已于
2026-10-12 删除，摘要保留在 `research_log.md`。

## 离线验证

```bash
python3 -m unittest discover -s tests
python3 -m experiments.static_check
```

测试使用模拟服务或本地假服务，不执行真实 GPU 实验。
