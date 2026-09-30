# 2026-09-28 研究进展与复现入口

当前阶段是 baseline、任务质量和性能实验，尚未达到论文整理条件。2026-09-30 研究者进一步明确：只比较相对推测解码的速度；直接云端生成不作为目标或验收基线。研究者明确要求
不以严格 token 一致作为目标；算法操作正确性、任务质量、延迟和吞吐量是主要标准。
token 差异仅作为描述性诊断。所有正结果、负结果和启动失败均保留。

## 已完成的证据

- 保留会话开始时的代码、未提交差异、SHA-256 清单；没有清理原有实验或提交用户的其他改动。
- 审计历史 672 组真实请求：只有 4 道独立题目；A 的 56 次请求全部答对，
  但没有一次与保存的 AR 参照逐 token 一致。C 答对 42/56，Proposed 答对 55/56。
  网络情境与重复次数不能扩大独立的质量样本量。
- 完成 NGL=0 配置下的 16 次严格解码诊断，并逐一保存请求、完整 token、
  首个差异位置和三次重放。gamma=2 有 5/8 次完全一致，gamma=8 有 4/8 次；
  1/4 道题的 AR 参照自身在重复间变化。NGL=0 数据不是全 GPU 性能 baseline。
- 完成三种工作负载、12 道题、1,149 次固定前缀检查。预先指定的稀疏位置全部一致。
  这轮没有支持普遍路径差异；其位置集合也没有覆盖先前已知的差异位置。
- 修复本地 K=1 在 global rank 并列时误入宽松接受的问题。48 组非并列模拟
  回归结果保持不变且与合成目标一致；历史真实数据没有触发这个缺陷，不能用它
  解释历史差异。云端尚未部署此修复。
- 全 GPU 草稿服务的启动已恢复。停止本次启动的 NGL=0 服务后，对该 GGUF
  执行 `POSIX_FADV_DONTNEED` 释放可回收文件缓存，原始 NGL=99 启动成功。
  未修改模型文件、未使用 sudo、未终止用户桌面应用。这是一次成功的恢复，
  还不是关于所有 Jetson 内存分配失败的通用结论。

实时追加的实验结论见 [research_log.md](../research_log.md)。原始证据根目录：
`results/research_20260928_135549/`。子目录含 `strict_audit`、`gpu_strict_audit`、
`target_path_audit`、`target_low_margin`，报告与源数据分开保存。`initial.patch`、
`snapshot/` 和 `manifest.json` 保留会话开始状态；`environment.json` 包含软件版本、
Jetson 信息、llama.cpp commit、GGUF SHA-256。所有结果仍保存在本地；部分 JSON/CSV/log
沿用仓库 `.gitignore` 规则，不会仅因代码提交而上传或进入 Git。

## 复现命令

从仓库根目录运行。默认连接配置来自 `configs/experiment.defaults.json`，
也可通过 `--config` 指向覆盖文件。真实实验需要运行中的 draft 和 target；
诊断脚本会持有同一套服务锁，不应并行运行。

```bash
python -m unittest discover -s tests -v

# 真实严格解码、AR 参照、首差异前缀重放；硬件标签应填写实际配置
python -m experiments.strict_diagnostic --n 4 --repeats 2 --max-tokens 512 \
  --gammas 2 8 --hardware-label 'Jetson NGL=99; remote AWQ target'

# 预先指定位置：原始的零差异结果应保留
python -m experiments.target_path_audit --n 4 --repeats 3

# 独立新实验：筛选低 margin / 已分歧位置进行定向确认
python -m experiments.target_path_audit --n 4 --repeats 3 \
  --position-selection low_margin

# 每次分析也创建独立目录，不覆盖源实验
python -m analysis.research_audit results/20260922_165127_613688_bbf68018 --sd-only
python -m analysis.strict_report results/<strict_diagnostic_run>
python -m analysis.target_path_report results/<target_path_run>

# 当前优先实验：8 道题、两次重复、两种 RTT，四种 SD 方案（128 组；历史完整运行另含 AR 对照）
python -m experiments.run --mode real --config configs/research.pilot.json \
  --methods A B C Proposed
```

生成器保存实际模板和 token IDs；模板可能包含日期，复现旧前缀应使用保存的 IDs，
不能仅在另一天重新生成模板并认定输入相同。种子是 42；重复实验不把相同题目当作
新的独立样本。低 margin 筛选故意富集可疑位置，其差异比例不代表总体错误率。
teacher-forcing 使用目标输出充当待评分序列，只用于诊断，不能宣称是可部署的草稿策略。

## 云端后续实验

现有 HTTP 服务可访问，任务质量/性能实验可以继续；SSH 不是当前研究的阻塞条件。
尚未提供可用于检查部署配置、修改并重启服务的 SSH 入口。
本地已准备可选概率诊断以及启动时源码 SHA-256、精度/量化/复现设置字段，
但本地测试通过不等于部署中的云端实现已经修复。需要用同一模型、同一工作负载、
同一提示模板进行单变量干预，才能把已观察到的路径差异归因到具体因素。

如果后续需要进一步解释数值路径差异，一项可选干预是保持现有启动参数不变，只在进程启动前设置
`VLLM_BATCH_INVARIANT=1`，再完整重复保存的前缀审计与 AR/SD 比较。该设置是候选实验，
不是已经验证的修复。vLLM 官方将其标为 beta，当前文档列出的 NVIDIA 硬件要求是
compute capability ≥ 8.0；需核对实际部署版本、GPU 和 AWQ 模型是否兼容。
来源：[vLLM batch invariance](https://docs.vllm.ai/en/stable/features/batch_invariance/)、
[可复现性说明](https://docs.vllm.ai/en/stable/usage/reproducibility/)。

该干预若无效，分别检查 prefix caching、prefill/decode kernel 和精度，不能一次
更换精度、缓存、模型与版本后把变化归因于某一项。保留原始配置的输出、耗时和质量结果。
这些诊断不作为性能实验准入条件。质量保持须由任务评分支持，不能由本地 regret 预算推断。

论文所需的更大独立样本、质量非劣性验证、不同模型对、资源/能耗
和部署环境控制仍待完成。当前没有把这份阶段性诊断包装成论文级结果。

## 2026-09-30 续研结果

160 请求的历史 pilot 已全部完成，结果已另生成只比较 SD 的报告，保留原报告。
Proposed 对 A 的配对吞吐提升：低额外延迟约 4.9%，高额外延迟约 22.8%；
对 B 的提升区间均跨零，尚不能证明联合 K 控制优于单独自适应窗口。
这里的 low/high 是额外注入 2/100 ms，并非测得的物理 RTT。

关闭未使用草稿概率返回的微基准有 440 对，草稿调用缩短约 7.36%。
正在进行同日配对的端到端验证：两组均为 Proposed，仅改变 DRAFT_N_PROBS。
历史默认值保持 1，候选值为 0。原始请求、配置及源码保存在 draft_payload_e2e 子目录。


后续消融中，B 是严格接受＋自适应窗口，D 是固定 K=2＋自适应窗口，
Proposed 是联合自适应。新题使用 `--request-offset 8` 排除前轮的 8 道题。
`results/research_20260928_135549/followup_r009.py` 保存串行执行计划，
`followup_r009_status.json` 保存实时状态。R009 未达到预设标准时，
后续各组统一使用原设置；达到时才统一使用候选设置。不会把两种草稿
设置分别分配给基线和 Proposed 来放大算法收益。
