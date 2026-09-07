# Edge-Cloud Speculative Decoding

Acceptance-aware edge-cloud speculative decoding: a quantized draft model runs on an
edge device (Jetson Orin Nano, llama.cpp), a full-precision target model verifies in the
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
    --target meta-llama/Llama-3.1-8B-Instruct \
    --host 0.0.0.0 --port 9090 --max-model-len 4096

# 或提交到 SLURM
MODEL_CONFIG=llama3 sbatch cloud/scripts/serve_slurm.sbatch

# 自检
python -m cloud.tools.smoke_test --host localhost --port 9090
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

```bash
export CLOUD_URL=http://<cloud-ip>:9090
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

## Quality-constrained experiments

Run `./run_all_experiments.ps1` (Windows) or `bash run_all_experiments.sh` (Linux). Default mode is synthetic simulation. See [experiment system](docs/EXPERIMENT_SYSTEM.md) for real services, configuration and limitations. Legacy C1, prefetch, energy and SLO experiments remain independent of the new synchronous controller.
