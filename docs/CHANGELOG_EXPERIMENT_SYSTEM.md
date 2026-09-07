# 实验系统改造记录（2026-09-07）

本次直接修改仓库，未 commit、push 或创建远程资源。保留修改前未提交的 README 检查入口，
`docs/TOP_K_AUDIT.md` 原文未变；数据集与既有原始实验结果未删除。

## 文件清单

| 范围 | 文件及变化 |
|---|---|
| 质量策略 | 新增 `common/acceptance.py`、`common/controller.py`、`common/quality.py` |
| 数学与计时 | 新增 `common/window_estimator.py`、`common/metrics.py` |
| 配置 | 新增 `common/experiment_config.py`、`configs/experiment.defaults.json`、`configs/experiment.template.json` |
| 云端协议 | 修改 `cloud/verify_server.py`，加入质量决策、服务端排队/验证计时；`cloud/scripts/serve_slurm.sbatch` 使用模块入口 |
| 边缘执行 | 原位改造 `edge/edge_client_smart.py` 与 `edge/bench_smart.py`；修改 `edge/verifier.py` 编解码计时和策略协议 |
| 基础正确性 | `edge/edge_client.py` 去掉模板异常吞噬和生成 token 重新分词替代，限制严格温度、显式无进展错误、输出上限与 EOS 截断 |
| 实验适配 | 新增 `common/simulation.py`、`edge/experiment_live.py`，区分虚拟时间合成模型与真实服务 |
| 一键管线 | 新增 `experiments/__init__.py`、`experiments/run.py`、`experiments/static_check.py`、两个 `run_all_experiments` 脚本和 `requirements-experiments.txt` |
| 图表与索引 | 改造 `analysis/make_figures.py`，清理 `analysis/make_results_index.py` 的失效字段 |
| 测试 | 新增 `tests/test_core.py`、`tests/test_integration.py` |
| 文档 | 更新 README、`docs/add_model.md`、`docs/RUNBOOK_MODELPAIRS.md`；新增本记录与 `docs/EXPERIMENT_SYSTEM.md` |
| 澄清术语 | `edge/energy_profiler.py`、`edge/verifier.py`、`edge/edge_client_c1.py`、`edge/edge_client_warmup.py`、`docs/RUNBOOK_C3.md` 的备用采集/兼容说明，避免与已删除的推理切换混淆 |

删除前已列出并说明：`edge/verifier_ext.py`（旧 generate 猴子补丁）、
`edge/scripts/run_sweep_humaneval.sh`（旧阈值扫描）、`docs/RUNBOOK_STEP12.md`（失效实验说明）。
生成的 `results/` 新目录均为本次运行产物，包含原始决策、配置、日志、图表和报告。

## 实现摘要

- 每轮固定走 draft → verify → 接受/修正，无接受率触发的推理路径切换；严格参照显式独立请求。
- 十二项指标分别记录；HTTP 总时间扣除服务端队列和验证得到通信残差估算，上传/下载明确标记分摊估算。
- Top-K 宽松接受有置信度、概率比、单 token regret 和累计 regret 预算门限；风险或预算升高收紧 K。
- 同步窗口模型枚举所有候选整数；滑窗估算、线性拟合、初值、迟滞、步长和延迟突变重估独立可测。
- 联合控制器优先质量，K 变化时保持窗口；输出候选预测、收益/风险代理变化与原因。
- A/B/C/Proposed、gamma/K 扫描、七类网络场景全部使用同一配置和种子；真实模式外部硬件负载仍需控制。

## 验证记录

- 37 项 unittest：28 个核心/回归测试、9 个协议/集成测试；本机真实 HTTP 服务使用假模型。
- 全流程模拟：7 场景 × 12 方案/扫描配置 × 4 请求 × 2 重复 = 672 请求，成功运行产生 11 组 PNG/SVG。
- 缺少真实服务配置与未填写模板均经过实际 CLI 调用验证：退出码 1，原因与日志保存在独立报告目录。
- Windows 定时器提前唤醒通过 perf_counter 截止时间循环处理；输出目录添加唯一后缀，避免同一时钟刻度启动时覆盖日志。
- `git diff --check` 与已删除路由的 AST 检查通过；图表经过图像查看，检查单位、标题、图例与模拟标记。

## 实验结果的解释边界

合成严格策略输出与合成目标参照一致；自适应 Top-K 能在高 RTT 下增大 K，预算紧张后收紧。
合成宽松输出可能与严格参照产生很大的序列差异，即使局部 regret 预算未超限。
这说明局部概率约束不能替代任务质量评测，不能据本次模拟得出真实模型“质量无损”或性能提升结论。
真实实验尚缺 `DRAFT_URL`、`CLOUD_URL`、`MODEL_PAIR`，以及用户选择的最终质量/窗口参数和实际推理服务。
当前真实任务评分支持 GSM8K 数值结果；HumanEval 安全执行器和 MT-Bench judge 尚未接入，评分字段为 null。
Linux shell 入口已提供，本机运行验证使用 Windows PowerShell；GPU/vLLM 推理本身未在此环境验证。

详细启动方式、全部参数解释、计时误差和数学模型见 [实验系统说明](EXPERIMENT_SYSTEM.md)。
