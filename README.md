# Edge-Cloud Speculative Decoding

Acceptance-aware edge-cloud speculative decoding: a quantized draft model runs on an
edge device (Jetson Orin Nano, llama.cpp), a target model (currently AWQ INT4 for `llama3_awq`) verifies in the
cloud (vLLM).

Top-k 策略：边缘端贪心解码及本地模拟验证器已显式使用 `top_k=1`；详细范围与检查记录见 [Top-k 策略检查记录](docs/TOP_K_AUDIT.md)。

上述记录保留改造前的检查结论；当前新增的 Top-K 宽松接受与联合控制见 [实验系统说明](docs/EXPERIMENT_SYSTEM.md)。

The repo is split by **where the code runs**:

```
edge-cloud-speculative-decoding/
├── common/     两侧都要:模型对配置、数据集
├── cloud/      只在 GPU 服务器上跑:vLLM verify server + 单机 baseline
├── edge/       只在 Jetson 上跑:draft 客户端 + benchmark
├── configs/    models.yaml —— 模型对注册表
├── analysis/   离线分析,不需要 GPU
├── docs/       各实验的 RUNBOOK
└── results/    实验输出
```

---

## 目录职责

### `common/` — 两侧都需要

| 文件 | 作用 |
|---|---|
| `model_config.py` | 读 `configs/models.yaml`,**校验 draft 与 target 的 vocab 是否一致**(不一致直接中止) |
| `fetch_datasets.py` | 下载 GSM8K / HumanEval / MT-Bench |
| `data/*.jsonl` | 已下载好的评测集(3 个任务) |

> 数据集放在 `common/` 而非 `edge/`,因为云端的 `bench_baseline.py` 同样要读。

### `cloud/` — GPU 服务器

| 文件 | 作用 |
|---|---|
| `verify_server.py` | FastAPI + vLLM,暴露 `POST /verify` 与 `POST /generate` |
| `bench_baseline.py` | 云端单机 baseline:纯自回归 / 本地投机解码 / n-gram |
| `summarize.py` | 汇总云端结果 |
| `scripts/serve_slurm.sbatch` | SLURM 集群启动 |
| `scripts/run_slurm.sh` | SLURM 批量跑 baseline |
| `scripts/setup.sh`, `scripts/env.sh` | 环境准备 |
| `tools/smoke_test.py` | verify server 自检 |
| `tools/gpu_power_logger.py` | GPU 功耗采样(nvidia-smi,10 Hz) |

### `edge/` — Jetson

| 文件 | 作用 |
|---|---|
| `edge_client.py` | 投机解码主循环(基线实现) |
| `edge_client_smart.py` | Quality-constrained Top-K and mathematical window control |
| `edge_client_prefetch.py` | 异步预取(**负面结果**,−25%) |
| `edge_client_warmup.py` | warmup γ 调度(**弱结果**,+1%) |
| `edge_client_c1.py` | 熵自适应 γ(**负面结果**,−4%) |
| `edge_client_b5.py` | SLO 路由 |
| `verifier.py` | Cloud verification HTTP client and latency measurements |
| `energy_profiler.py` | Jetson 功耗采样(jtop / INA3221) |
| `bench_*.py` | 每个实验一个 benchmark 入口 |
| `scripts/start_draft_server.sh` | 启动 llama.cpp draft server |
| `scripts/setup_jetson.sh`, `download_model.sh`, `power_mode.sh` | 环境准备 |

---

## 运行方式

**所有 Python 入口都从仓库根目录以模块方式运行**,这样 `edge` / `cloud` / `common`
三个包才能互相导入:

```bash
cd <repo-root>
python -m edge.bench_edge_cloud --help      # ✅
python -m cloud.verify_server --help        # ✅

cd edge && python bench_edge_cloud.py       # ❌ 会 ImportError
```

### 1. 云端

```bash
pip install -r cloud/requirements.txt
export HF_TOKEN=hf_xxxx

# 直接跑(无 SLURM)
python -m cloud.verify_server \
    --target hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4 \
    --host 0.0.0.0 --port 9090 --max-model-len 4096

# 或提交到 SLURM
MODEL_CONFIG=llama3 sbatch cloud/scripts/serve_slurm.sbatch

# 自检
python -m cloud.tools.smoke_test --host 172.23.119.64 --port 9090
```

云端单机 baseline(需先停掉 verify server,它占着显存):

```bash
python -m cloud.bench_baseline --method ar    --data common/data/gsm8k_test_50.jsonl \
    --out results/B1_AR.json --tag B1_AR
python -m cloud.bench_baseline --method draft --gamma 3 --data common/data/gsm8k_test_50.jsonl \
    --out results/B2_SD_g3.json --tag B2_SD_g3
python -m cloud.bench_baseline --method ngram --gamma 5 --data common/data/gsm8k_test_50.jsonl \
    --out results/B4_ngram_g5.json --tag B4_ngram_g5
```

同时记录 GPU 功耗:

```bash
python -m cloud.tools.gpu_power_logger --out results/B1_AR_power.csv
```

### 2. 边缘

```bash
pip install -r edge/requirements.txt          # requests tqdm pyyaml jetson-stats
bash edge/scripts/setup_jetson.sh             # 首次:编译 llama.cpp (CUDA, sm_87)
bash edge/scripts/download_model.sh
sudo nvpmodel -m 0 && sudo jetson_clocks      # 15W 模式

nohup bash edge/scripts/start_draft_server.sh llama > ~/draft.log 2>&1 &
curl -s localhost:8080/health
```

连到云端(同局域网直接用 IP,跨网段才需要 SSH 隧道):
出现问题修复1.sudo ip route add 172.23.64.0/19 via 172.23.127.254 dev wlp37s0 src 172.23.119.64
2.sudo ufw allow 9090/tcp
```bash
export CLOUD_URL=http://172.23.119.64:9090
curl -s $CLOUD_URL/health
```

跑实验:

```bash
# 边云 SD 基线
python -m edge.bench_edge_cloud --verifier remote --remote-url $CLOUD_URL \
    --model-config llama3 --gamma 3 --n 50 \
    --data common/data/gsm8k_test_50.jsonl --out results/B3_remote_g3.json

# New baseline / joint controller suite
python -m edge.bench_smart --mode simulate
# Real services: --mode real --config configs/my-experiment.json
```

### 3. 分析

不需要 GPU,只读 `results/`:

```bash
python -m analysis.make_figures results/<timestamp>
python -m analysis.make_results_index results --out-md results/RESULTS_INDEX.md
```

---

## 加一个新的模型对

```bash
# 1. 确认 draft 与 target 的 vocab_size 一致(不一致会带来显著开销,见 docs/add_model.md)
# 2. 在 configs/models.yaml 加一条
# 3. 云端: MODEL_CONFIG=<name> sbatch cloud/scripts/serve_slurm.sbatch
#    边缘: bash edge/scripts/start_draft_server.sh <name>
# 4. 跑: python -m edge.bench_edge_cloud --model-config <name> --verifier remote ...
```

`common/model_config.py` 会在启动时比对两侧 vocab,**不一致直接中止**。
完整说明见 `docs/add_model.md`。

---

## 硬件

- **Edge**:Jetson Orin Nano 8GB,JetPack 6,llama.cpp b5050 (sm_87)
- **Cloud**:H200 / RTX 3080,vLLM
- 模型对见 `configs/models.yaml`

## 一键实验与最终汇报

```bash
# 查看计划，不调用模型
bash run_all_experiments.sh --mode real --plan
# 推荐：精简完整实验，默认 80 次计时请求
bash run_all_experiments.sh --mode real
# 连通性和输出检查：5 次请求，输出上限 64 token
bash run_all_experiments.sh --mode real --profile smoke
# 保留参数扫描的完整套件
bash run_all_experiments.sh --mode real --profile full
```

默认 quick 使用 4 道题、2 次重复、2 个网络条件（额外注入 2/100 ms 延迟），
比较 A（严格接受、固定 γ）、B（严格接受、自适应 γ）、C（固定 K/γ）、
D（固定 K、自适应 γ）、Lookahead（A 加固定提前草拟 h）。
Proposed 暂时不参与一键套件，底层实现和历史结果保留。
默认 γ=4、h=5、输出上限 512 token。只比较推测解码方案；质量参照请求不作为云端速度基线。
full 额外扫描配置中的 γ/K。快速检查仍保留必要的代码与协议测试。

脚本自动完成检查、服务校验、实验、统计、图表和最终汇报；失败也会生成标注未完成的汇报，
并返回非零退出码。服务需要事先部署并保持独占；脚本不负责下载或启动模型。

```text
results/suites/<运行编号>/
  SUMMARY.md             中文总结在前，英文在后，优先看这个文件
  tables/                方法指标、配对吞吐比较
  figures/               吞吐图 PNG/SVG
  logs/run.log           执行日志
  config/                计划、配置、模型注册表、代码快照
  report/                完成状态与机器可读总结
  runs/<编号>/raw/        逐请求原始证据及底层实验输出
```

每次运行创建独立目录，历史研究结果不覆盖。按题目聚类计算配对增益及 bootstrap 区间；
4 道题只适合探索，不足以证明泛化或质量非劣性。报告列出任务正确率和截断数；
没有已实现评分器的任务显示 N/A。smoke 和 simulate 不输出真实加速结论。
提前草拟计时包含后台任务收尾。模拟流程可用 `--mode simulate --profile smoke`，不包含 Lookahead。

### 更换模型对

在 `configs/models.yaml` 或自己的 YAML 注册表添加模型对，然后运行：

```bash
bash run_all_experiments.sh --mode real \
  --models-yaml configs/models.yaml --model-pair qwen3 \
  --draft-url http://EDGE_HOST:8080 --cloud-url http://CLOUD_HOST:9090
```

注册项必需字段为 `target`、`draft_gguf`、`eos_id`、`vocab_size`；可选 `stop_strings`
控制文本停止标记，未设置则使用服务自身 EOS 行为。聊天模板由草拟服务提供。
两端须部署匹配的模型并共享 token ID 语义。脚本检查目标模型标识和词表大小，
但词表大小一致本身不能证明 tokenizer 一致；词表大小不同的模型对目前会被拒绝。
每次运行选择一个模型对，其他模型对仍需实际验证。

通过 `--n 8 --repeats 2 --gamma 4 --lookahead 5 --max-tokens 512 --request-offset 0`
调整规模与参数。配置优先级为 profile 默认值 < `--config` JSON < 显式命令行参数；
建议先用 `--plan` 确认实际请求数。`--output-root` 可指定输出父目录。
底层 `python -m experiments.run` 保留原接口，一键入口使用 `experiments.suite`。
Windows 对应入口为 `run_all_experiments.ps1 -Mode real -Profile quick -ModelPair llama3_awq`。
