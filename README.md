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

## 一键实验：运行哪些任务、生成哪些结果

在 Jetson 的项目根目录运行：

```bash
# 连接已启动的边缘草稿服务和云端验证服务
bash run_all_experiments.sh --mode real

# 使用自己的实验配置
bash run_all_experiments.sh --mode real --config configs/my-experiment.json

# 不连接真实模型，使用合成模型与虚拟时间验证流程
bash run_all_experiments.sh --mode simulate
```

不指定 `--mode` 时默认是 `simulate`。Windows 入口为 `run_all_experiments.ps1`。
脚本连接现有服务，不负责启动云端或边缘模型。默认参数见
[experiment.defaults.json](configs/experiment.defaults.json)，详细算法和计时定义见
[实验系统说明](docs/EXPERIMENT_SYSTEM.md)。

### 1. 数据集任务

每次运行使用 `TASK` 和 `DATASET` 指定的一个任务；不会自动轮流运行全部数据集。

| 任务 | 本地数据文件 | 生成内容及当前评价方式 |
|---|---|---|
| `gsm8k`（默认） | `common/data/gsm8k_test_50.jsonl` | 数学解题文本；提取 `Final answer:` 或 `####` 后的数字，与标准答案比较 |
| `humaneval` | `common/data/humaneval_30.jsonl` | 代码续写；保存输出与参照的文本/token 差异，目前不执行代码测试，任务质量为 `null` |
| `mtbench` | `common/data/mtbench_30.jsonl` | 使用首轮问题生成回复；目前不运行多轮对话或外部裁判，任务质量为 `null` |

默认取 GSM8K 文件的 **50 题**（`N_REQUESTS=50`），每次最多生成 **512 个 token**
（`MAX_TOKENS=512`）。仍需检查截断率与答案提取率；未提取到最终数字时
GSM8K 得分为 0。`simulate` 不对这些自然语言题目做模型推理，其任务质量指标为 `null`。

### 2. 执行阶段与实验方案

脚本依次执行：记录配置与环境 → 静态检查 → 核心单元测试 → HTTP 整合测试 →
真实服务及模型词表/协议检查（仅 `real`）→ 批量推理 → 汇总表格 → 绘图与报告。
前置检查失败时不会开始推理。

`gamma` 表示一轮提出多少个草稿 token；`K` 表示目标模型允许接受的候选排名范围。
`K=1` 为严格接受，`K>1` 的接受仍受概率、置信度和累计质量预算限制。

| 实验类别 / 结果中的 `method` | 默认设置 | 要观察的问题 |
|---|---|---|
| 基线 A / `A` | 严格接受，固定 gamma=2 | 固定窗口的基础性能 |
| 基线 B / `B` | 严格接受，自适应 gamma（1–8，初值 2） | 只调整窗口能否改善吞吐与延迟 |
| 基线 C / `C` | 固定 K=2，固定 gamma=2；预算收紧时退回 K=1 | 受质量约束的宽松接受效果 |
| 联合控制 / `Proposed` | 自适应 K（1–4）及 gamma（1–8） | 联合调整接受范围和窗口的表现 |
| 窗口扫描 / `gamma_1`、`gamma_2`、`gamma_4`、`gamma_8` | 严格接受，分别固定窗口 | 哪个扫描窗口实测最好，数学估计是否接近 |
| K 扫描 / `k_1`、`k_2`、`k_3`、`k_4` | 固定 gamma=2，分别设置 K；仍受预算限制 | 接受率、速度与质量变化的关系 |

真实模式还会为每道题通过云端 `/generate` 生成一次严格贪心参照，并在本次运行中缓存复用。
参照的 token 和文本保存在每份对应的 `raw/*.json` 中，不单独计入下列 8400 组实验。

### 3. 网络情境与默认任务数量

每种实验方案都会在以下 7 种情境中运行。表中数值是**额外注入的延迟**，真实网络和服务耗时还会叠加；
真实模式使用应用层等待模拟网络条件，不是操作系统级流量整形。

| 情境 | 默认注入设置 |
|---|---|
| `low` | RTT 2 ms |
| `medium` | RTT 30 ms |
| `high` | RTT 100 ms |
| `jitter` | RTT 30 ms，抖动 ±25 ms |
| `bandwidth` | RTT 30 ms，按 1 Mbps 估算传输等待 |
| `burst` | RTT 5 ms；从轮次索引 4（第 5 轮）起额外增加 100 ms |
| `queue` | RTT 10 ms，服务端排队注入 20 ms、抖动 ±15 ms |

默认总数为：**7 种情境 × 2 次重复 ×（4 个基线 + 4 个 gamma 扫描 + 4 个 K 扫描）× 50 道题 = 8400 组**。
同一重复内方案顺序按固定种子打乱，所以终端不一定从 A 开始。修改 `N_REQUESTS`、`REPEATS`、
扫描列表或 `NETWORK_SCENARIOS` 会改变总数；`N_REQUESTS` 超过数据集长度时以实际题数为准。
这里的一组包含多轮 draft → verify HTTP 调用，并非一次 HTTP 请求。

### 4. 运行中怎样看进度

启动后会立即打印结果目录和检查阶段。每组请求开始与完成时打印进度，例如：

```text
Running 8400 requests. Mode=real
[1/8400] low_0_gamma_8_0: starting
[1/8400] low_0_gamma_8_0: OK 48 tokens, 7.61s, 6.31 tokens/s
```

`low_0_gamma_8_0` 表示 low 情境、第 0 次重复、gamma=8 扫描、第 0 道题（编号从 0 开始）。
失败时打印 `FAILED`，保存异常堆栈并继续其他请求。
加 `--verbose-rounds` 会在**每组请求完成后**打印该请求各轮的 K、gamma、通信估计和验证延迟；
逐轮原始数据本身始终保存，不需要开启此选项。

### 5. 结果目录与生成时间

每次运行创建独立的 `results/YYYYMMDD_HHMMSS_微秒_唯一后缀/`。
**不用全部跑完才有结果：每完成一组请求就写入一个 `raw/*.json`；表格和图表在批量推理结束后生成。**

| 路径 | 保存内容 | 生成时间 |
|---|---|---|
| `config/resolved.json` | 合并后的完整实验参数 | 启动时 |
| `config/environment.json` | Python、依赖版本、Git 状态及运行模式 | 启动时 |
| `config/service_info.json` | 云端模型、词表、上下文上限及协议版本；仅真实模式 | 服务检查通过后 |
| `config/requests.json`、`config/dataset.json` | 实际题目、数据路径与 SHA-256 摘要 | 推理开始前 |
| `logs/static.log`、`unit.log`、`integration.log` | 三个前置检查阶段的输出 | 各检查完成后 |
| `raw/<情境>_<重复>_<方案>_<题号>.json` | 生成文本/token、严格参照、请求指标、各轮时延、接受决策、控制器预测和质量预算 | 每组成功后立即写入 |
| `logs/<请求名>.log`、`logs/pipeline.log` | 请求失败或整条流程异常的堆栈 | 对应错误发生时 |
| `tables/requests.csv` | 每组请求一行：耗时、吞吐、TTFT、TPOT、接受率与质量差异等 | 批量推理结束后 |
| `tables/rounds.csv` | 每轮一行：草稿/验证/通信/排队耗时、K、gamma 和决策 | 批量推理结束后 |
| `tables/latency_summary.json`、`latency_summary.csv` | 延迟等指标的均值、P50/P95/P99、最小/最大值及样本数 | 汇总阶段 |
| `tables/comparison.csv` | 按实验类别、情境、方案分别汇总的性能与质量指标 | 汇总阶段 |
| `tables/window_estimates.json` | 数学估计窗口、实测扫描最佳窗口及两者差值 | 绘图阶段 |
| `figures/*.png`、`figures/*.svg` | 下节所列 11 组图，每组两种格式，共 22 个文件 | 绘图阶段 |
| `report/report.md`、`report/status.json` | 可阅读报告、检查退出码、成功数量、失败列表及中断标记 | 运行结束或捕获异常/中断时 |

TTFT 是首批验证通过 token 可用的时间；TPOT 是后续 token 可用间隔的平均值。
文本/token 差异使用序列比较，不等于语义准确率；质量预算限制的是 logprob regret，也不保证任务准确率不下降。
总体汇总用于了解运行情况，比较方案时应优先看按情境分组的 `comparison.csv`。

完整成功退出码为 0；出现失败为 1；Ctrl+C 中断为 130，并标记 `interrupted: true`。
中断保留已经写入的原始结果，但不会自动补齐汇总与图表。失败批次可能只有部分文件，
请先查看 `report/status.json`。运行期间不要清空该结果目录，否则后续写入与报告保存会失败。

### 6. 生成的 11 组图

以下文件名均同时提供 `.png` 和 `.svg`：

| 文件名 | 图的含义 |
|---|---|
| `gamma_throughput` | 固定 gamma 与吞吐量的关系 |
| `gamma_latency` | 固定 gamma 与整组请求耗时的关系 |
| `k_acceptance` | 固定 K 与接受率的关系 |
| `k_quality` | 固定 K 与任务质量下降的关系；缺少任务评分时使用 token 差异代理 |
| `scheme_comparison` | A、B、C、Proposed 在各网络情境中的吞吐比较 |
| `network_throughput` | 稳定延迟情境下，注入 RTT 与各方案吞吐的关系 |
| `rtt_best_gamma` | 数学预测窗口与扫描网格内实测最佳窗口的比较 |
| `window_error` | 预测窗口减去实测扫描最佳窗口的差值 |
| `latency_percentiles` | 各方案每请求轮次延迟的均值、P95、P99，再按请求平均 |
| `quality_speed_pareto` | 各情境内质量变化与吞吐的折中关系 |
| `controller_trace` | Proposed 第一题、第一次重复的 K、gamma、RTT、接受率和质量风险随时间变化 |

查看结果时，先读 `report/report.md`，再用 `tables/comparison.csv` 比较方案，
需要追查某次决策时打开对应的 `raw/*.json`。已有完整原始数据时可重新绘图：

```bash
python -m analysis.make_figures results/<本次运行目录>
```

云端单机 AR/本地投机/n-gram 基线、旧 C1、异步预取、能耗和 SLO 实验仍需通过各自入口单独运行，
不包含在此脚本的 8400 组中。


### P0 正确性与测量保护

真实运行前先更新并重启云端 `cloud.verify_server`，新客户端要求服务声明
`strict_diagnostics_available`。前 4 题在配置的每个固定 gamma 下进行完整严格序列检查，
与 `/generate` 贪心参照逐 token 比较；这些调用兼作暖机，不计入性能样本。
失败时停止套件，并将输出及首个分歧位置的同前缀 `/generate(max_tokens=1)`、
不同 gamma 的 `/verify` 候选分布保存在 `preflight/`。
正式测试的所有严格请求也检查一致性，失败记录保存在 `raw/`，并立即停止套件。
此机制检测差异，不会通过改用云端生成掩盖差异；后端数值问题仍需根据诊断定位。

`requests.csv` 和原始 JSON 增加 `stop_reason`、`truncated`、`answer_extracted`、
`quality_status` 与对应参照字段。报告同时列出绝对准确率、参照准确率、提取率与截断率。
缺少答案仍按 benchmark 错题计分，但与已完成的错误答案分开标记。
参照全错时报告明确提示质量比较缺乏鉴别力；不能将零下降解释为质量无损。

真实实验按每个服务地址获取主机本地进程锁，覆盖不同输出目录和项目副本；共享任一服务
即拒绝并发运行，退出或进程终止后操作系统释放锁。锁文件保留不代表仍被占用。
这不阻止其他主机或旧版客户端访问服务，远端仍须安排独占实验时段。
`config/hardware_start.json`、`hardware_end.json` 保存运行主机的负载、可用 GPU/功耗模式快照；
`service_info.json` 保存 target 运行库版本。快照不是全程监控，也不自动修改功耗或清空缓存；
重复实验须保持相同功耗、时钟、缓存策略与服务负载，并另行记录远端硬件负载。

完整默认套件现在为 8400 组，外加预检与参照请求。仅检查流程时显式使用：

```bash
bash run_all_experiments.sh --mode simulate --config configs/experiment.smoke.json
```

`tables/paired_comparison.csv` 将 Proposed 与 A/B/C/固定 gamma=4 按题目和重复次数配对，
先在每题内平均，再按题目 bootstrap 计算 95% 区间；不把重复运行当作独立题目。
吞吐指标为逐配对相对增益的均值，质量指标为准确率差；缺失配对被排除，表中记录样本数。
模拟模式或不足两道题时不输出置信区间，小样本区间仅供描述。
