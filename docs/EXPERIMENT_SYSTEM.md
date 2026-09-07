# 云端—边缘推测解码实验系统

## 改造范围与原始实现

Python 3.10+；边缘端为 requests + llama.cpp `/completion`，云端为 FastAPI + vLLM。
保留现有模型注册表 `configs/models.yaml`、数据下载模块、三个数据集、能耗与 SLO 实验。
`edge/edge_client.py` 负责模板、分词、草稿和普通同步循环；`edge/verifier.py` 负责 HTTP；
`cloud/verify_server.py` 负责目标概率、修正与 bonus；新接受判定位于 `common/acceptance.py`。
旧固定 gamma、C1 熵窗口、warmup 和预取分别保留在原客户端文件；新数学模型仅用于同步链路。
原有图表读取旧实验字段，已改造成新体系的绘图器；新增 unittest 测试，无需 GPU。

开始时工作区只有 README 的未提交修改与未跟踪 `docs/TOP_K_AUDIT.md`。
前者原有检查入口保留，后者内容不变，作为改造前的历史记录。
未提交、推送代码，也未删除数据集、模型、用户原始结果。

## 已移除的推理切换路径

旧 smart 客户端在指定轮数处检测累计接受率，低于阈值时调用目标模型生成剩余文本。
该分支、参数、状态、统计以及启动时先生成目标 token 的分支均已删除。
`SmartEdgeClient` 现在每轮只执行 draft → verify → 接受前缀/修正；错误直接向调用方抛出。
`/generate` 仅供实验器显式建立严格云端质量参照，SD 客户端没有调用它的路径。
被拒绝后的 top-1 修正和全接受后的 bonus 保留，属于正常推测解码。

删除清单（执行前已说明原因）：

| 文件 | 原因 |
|---|---|
| `edge/verifier_ext.py` | 仅给旧切换客户端挂接 generate 的猴子补丁 |
| `edge/scripts/run_sweep_humaneval.sh` | 扫描已删除的切换阈值，无法与新参数兼容 |
| `docs/RUNBOOK_STEP12.md` | 专用的旧启动/切换消融说明，与当前行为冲突 |

`edge_client_smart.py`、`bench_smart.py`、`analysis/make_figures.py` 原位改造。
README、模型说明和结果索引仅移除失效段落/字段。功耗的备用采集方式仍保留，和推理切换无关。
静态检查会扫描 Python AST 中已删除的标识符/参数，并限制 SD 客户端调用链。

## 一键执行

在仓库根目录创建 Python 环境并安装实验依赖：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-experiments.txt
powershell -NoProfile -ExecutionPolicy Bypass -File .\run_all_experiments.ps1
```

`ExecutionPolicy Bypass` 只作用于本次进程，适用于禁止直接运行 PS1 的 Windows 设置。
可以用 `-Python C:\path\python.exe` 指定解释器；`-VerboseTokens` 开启逐 Token 决策日志。
`-VerboseRounds` 开启终端每轮延迟显示，Python/Linux 对应 `--verbose-rounds`；默认每轮数据写入 JSON/CSV，终端仅显示汇总。

Linux：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-experiments.txt
bash run_all_experiments.sh --mode simulate
```

默认 simulate 是**合成模型 + 虚拟时间**：不是 Llama、不是 GSM8K 推理准确率。
使用集中配置的概率分布、草稿命中率及延迟系数；请求索引映射到合成上下文。
数据文件的摘要和请求集合仍保存，但自然语言内容不参与合成模型计算。
单位测试另外启动本机 HTTP 服务，验证实际 requests/FastAPI 协议；此服务使用假模型。

真实实验先在 GPU 主机安装适合其 CUDA 环境的 vLLM、项目云端依赖并启动目标服务：

```bash
python -m cloud.verify_server --target <models.yaml中的目标模型> \
  --experiment-config configs/my-experiment.json
```

边缘端启动 `edge/scripts/start_draft_server.sh`，需支持 `/apply-template`、`/tokenize`、
`/detokenize`、`/completion` 的 llama-server。缺少模板或生成 token ID 时明确报错。
然后从边缘端运行：

```bash
bash run_all_experiments.sh --mode real --config configs/my-experiment.json
```

Windows 对应 `-Mode real -Config configs/my-experiment.json`。
一键脚本连接现有服务，不创建远程资源、不自动提交集群任务。
需要填写 `DRAFT_URL`、`CLOUD_URL`、`MODEL_PAIR`；云边使用相同 `SEED` 和兼容的 `K_MAX`。
核验词表大小、目标模型名称；词表相等不是 tokenizer 完全一致的数学证明，还需模型对本身正确。
脚本依次记录环境、校验配置、静态检查、单元测试、HTTP 集成测试，再进行实验与绘图。
检查不通过时不运行实验；个别请求失败继续其他请求并保存错误，最终退出码为 1。
完全成功退出码为 0。每次运行保存到 `results/YYYYMMDD_HHMMSS_ffffff_<唯一后缀>/`，避免并发运行覆盖：

```text
config/   完整解析配置、Python/包版本、Git状态、数据摘要、请求、真实服务信息
raw/      每请求输出、严格参照、每轮计时、逐Token质量决策、窗口候选预测
logs/     静态/单元/集成日志和各失败项堆栈
tables/   请求CSV、轮次CSV、延迟JSON/CSV、分方案比较、窗口误差
figures/  11组 PNG + SVG
report/   Markdown报告（含表格与图）和机器可读 status.json
```

重新绘图：`python -m analysis.make_figures results/<timestamp>`。不写死目录，缺数据报错。

## 集中参数与占位符

`configs/experiment.template.json` 用 null 留出所有要求的占位符；复制后填写，
直接使用未填写模板会列出缺失字段并返回失败。
`configs/experiment.defaults.json` 是完整的**保守实验默认值**，每次加载明确警告，不代表最终取值。
自定义 JSON 覆盖默认配置，未知字段、非法范围和非有限数值报错。

| 参数 | 含义/单位 |
|---|---|
| K_MIN / K_MAX / K_INITIAL | 接受候选排名边界/初值；K_MIN 必须为 1 |
| QUALITY_BUDGET | 单请求累计被宽松接受 token 的 logprob regret 上限，nats |
| MAX_LOGPROB_REGRET | 每个宽松接受 token 的 regret 上限，nats |
| MIN_PROBABILITY_RATIO | 候选概率 / top-1 概率下限 |
| TARGET_ACCEPTANCE_RATE | 网络条件允许时，提高 K 的接受率目标 |
| QUALITY_EVAL_INTERVAL | 每多少轮输出一次滑窗质量评估；每 token 的硬约束始终生效 |
| QUALITY_WINDOW_SIZE | 质量统计保存的最近决策 token 数量 |
| GAMMA_MIN / GAMMA_MAX / GAMMA_INITIAL | 整数窗口搜索范围/初值 |
| ESTIMATION_WINDOW_SIZE | 延迟与接受率滑窗的轮数 |
| WINDOW_UPDATE_INTERVAL | 窗口更新间隔，轮 |
| WINDOW_CHANGE_STEP | 每次窗口最大变化 token 数 |
| WINDOW_HYSTERESIS | 预测吞吐量相对收益最低阈值 |
| MIN_ESTIMATION_SAMPLES | 开始估算需要的最少轮数 |
| K_UPDATE_INTERVAL / K_CHANGE_STEP | K 调整冷却/步长 |
| MIN_TOP1_CONFIDENCE | top-1 的绝对概率下限，防止平坦分布下宽松接受 |
| BUDGET_TIGHTEN_FRACTION | 累计预算到此比例立即收紧为 K=1 |
| RISK_TIGHTEN_THRESHOLD | 滑窗平均归一化 regret 风险收紧阈值 |
| RTT_HIGH_MS / LATENCY_JUMP_RATIO | 高网络开销阈值/突变倍数 |
| REQUEST_TIMEOUT_S / SEED | HTTP 超时秒数/固定随机种子 |
| DRAFT_URL / CLOUD_URL / MODEL_PAIR | 实际服务及现有模型注册表键 |
| TASK / DATASET / N_REQUESTS / MAX_TOKENS | 任务、JSONL、请求数量、输出长度上限 |
| FIXED_K / GAMMA_SWEEP / K_SWEEP / REPEATS | 固定基线、扫描集合、重复次数 |
| VERBOSE_TOKENS | 终端逐 Token 日志开关；原始文件仍保留决策 |
| VERBOSE_ROUNDS | 终端逐轮 K、gamma、RTT、排队、验证及总延迟开关 |
| SIM_* | 合成模型概率与草稿/固定验证/增量验证毫秒数，仅模拟使用 |
| NETWORK_SCENARIOS | 每场景 rtt_ms、jitter_ms、bandwidth_mbps、burst_at、burst_ms、queue_ms、queue_jitter_ms |

七类默认场景为低延迟、中延迟、高延迟、高抖动、限带宽、突发延迟、队列变化。
模拟场景使用相同种子、按轮编号生成网络扰动；不同窗口会改变请求次数与时间轨迹。
真实模式通过应用层 sleep 注入额外通信延迟和按字节数估算的带宽时间；服务端显式注入排队延迟。
它不是 tc/netem，不模拟 TCP 拥塞、丢包、真实包队列，也不能消除环境本身的网络抖动。

## 接受策略与联合控制

严格策略仅接受目标 top-1，遇拒绝使用目标 top-1 修正。
宽松策略同时要求 global rank ≤ K、足够的 top-1 置信度、概率比、单 token regret 和剩余预算。
目标 token 的 rank 使用 vLLM 返回的全词表排名，不能把返回字典中的位置当作全局排名；
因为 vLLM 会额外返回观测 prompt token 的 logprob，即使它不在请求的候选数之内。
协议含义参考 [vLLM SamplingParams](https://docs.vllm.ai/en/stable/api/vllm/sampling_params/)。

每个实际考察 token 记录 K、rank、p_draft、p_top1、ratio、regret、risk、严格/宽松结果和累计预算。
缺失候选概率用 null，不虚构概率或输出非标准 JSON Infinity。
风险定义为 `min(1, regret / MAX_LOGPROB_REGRET)`；预算不是准确率下降预算，不能保证任务质量无损。
自适应 K 依据近期风险、top-1 置信度、接受率及网络通信估算调整。
高风险/低置信度减 K，预算临界强制 K=1；高 RTT 且预算充足/接受率未达标时有限增 K。
联合控制器在 K 改变的轮次保持窗口不动，否则窗口按自己的间隔、步长和迟滞更新。
输出下一轮 K/gamma、原因、吞吐预测变化与历史候选重放得到的风险变化估算。
该风险预测仅为近期候选的经验代理，不是任务准确率预测。

四组比较：A 严格+固定窗口，B 严格+自适应窗口，C 固定 K+固定窗口，Proposed 联合自适应。
C 仍受每 token 门限和硬预算约束，耗尽后 K=1；“固定”不豁免质量约束。
任务准确率在请求结束后与显式云端参照比较；当前 GSM8K 支持最终数字匹配。
HumanEval 未执行生成代码，MT-Bench 未调用外部 judge，二者任务质量为 null，不能当作零下降。
文本差异使用 `1 - SequenceMatcher.ratio()`，token 差异对 token ID 序列计算，均不等同于语义质量。
严格接受率与宽松接受率分母为实际考察的 token；另记录接受数/全部提出数，不能混用。

当前新链路明确限制 `temperature=0`。宽松接受会改变严格目标输出；用于随机采样同样会改变原始分布。
旧近似随机拒绝重采样已移除，不声称无损分布。

## 数学窗口模型

所有输入延迟单位为 ms：

```text
F = T_RTT + t_v0
c = t_d + t_v1
E(gamma) = sum(alpha**i, i=0..gamma)
T(gamma) = F + c*gamma
tokens_per_second = 1000 * E(gamma) / T(gamma)
```

等比求和等价于 `(1-alpha**(gamma+1))/(1-alpha)`，同时稳定处理 alpha=0、1 和接近 1。
在完整整数边界内枚举并选最大吞吐；当前窗口到最佳窗口按步长变化，收益不足则保持。
经验 alpha 为滑窗接受数/实际考察数，基于条件位置共享接受概率的简化假设。
验证固定/增量开销通过不同 gamma 的非负线性拟合估算。
只有一个 gamma 时无法辨识斜率，使用零斜率近似并明确 `fit_identifiable=false`；数据不足保留初值。
实际控制还将排队、序列化与反序列化的平均时间计入固定开销。
网络延迟突变时触发重估；上下文长度、KV cache、批处理、接受相关性和有限输出边界可能造成偏差。
保留的异步预取/流水线客户端不使用这一同步公式，不提供未经验证的流水线修正预测。
图中“实际最佳”仅是在实验扫描网格中测得的最佳，不代表所有可能整数窗口的真实全局最优。

## 计时口径与误差

全部新增本地耗时使用 `time.perf_counter()`，不跨机器相减绝对时钟。
服务端 async 入口等待模型锁，阻塞 vLLM 调用在线程中运行，避免阻塞事件循环；
该运行方式遵循 [FastAPI 并发说明](https://fastapi.tiangolo.com/async/)。
`cloud_queue_ms` 为应用模型锁及显式队列注入等待；`cloud_verify_ms` 为工作线程内目标推理和接受判定。
它不包含应用入口前的反向代理/OS 队列，也不是纯 GPU kernel 时间。

`http_round_trip_ms` 包括请求发送到响应体接收完毕。
`network_rtt_ms = max(0, http_round_trip_ms - cloud_queue_ms - cloud_verify_ms)`，是通信开销估算；
其中仍含服务端 codec、线程调度和入口外排队，不能称作纯链路 ping RTT。
负残差保留并标记 `timing_inconsistent`，不会隐瞒不一致。
`serialize_ms`/`deserialize_ms` 在客户端 JSON 编解码前后独立测量；
`upload_ms`/`download_ms` 按请求与响应字节比例分摊通信残差，并明确标记估算。
真实实验注入部分额外单独记录，表中的网络估算包含注入；`http_round_trip_ms` 保留底层实际 HTTP 耗时。
`round_total_ms` 从草稿生成开始到验证响应应用完成，包含草稿、编解码、通信、排队与验证。
`draft_token_ms` 含本地 llama-server 调用开销、prompt 处理，不是纯 decode kernel 单 token 时间。

TTFT 从开始构造模板/分词到第一批验证 token 可用；TPOT 按每个 token 可用时刻之差平均。
同一验证批次的多个 token 同时可用，间隔为零；这里不是云端逐 token 流式生成速率。
吞吐量用实际输出 token（含 EOS）/请求总时间，最终反分词也计入请求总时间。
合成模式 codec 未建模，用零且标记 synthetic_virtual_time，不能与实测 codec 相提并论。
汇总输出均值、线性插值 P50/P95/P99、最小值、最大值、样本数，并按方案/场景分组。

## 验证与限制

`python -m unittest discover -s tests -v` 覆盖严格/宽松边界、预算耗尽、K 边界、数学公式、
突变重估、延迟统计、配置错误、固定/自适应比较、EOS、空输出、超时、500/503、真实本机 HTTP、
严格输出与合成目标参照一致性、可复现性、联合稳定性、已删除调用链静态回归。
真实模型、GPU、服务地址未提供，不能报告真实性能改善或真实任务质量结论。
真实服务额外需要可用的 vLLM/CUDA、目标权重、边缘 GGUF、兼容 tokenizer、网络可达及填写的实验配置。
硬件负载、缓存热身、不同 vLLM/llama.cpp 版本还需在部署现场固定；环境清单记录 Python/包版本与云端信息。
预算由每个请求的客户端状态持续携带，适用于受信任实验客户端，不是防恶意客户端的服务端配额系统。
