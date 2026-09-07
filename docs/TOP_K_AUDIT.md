# Top-k 策略检查记录

检查日期：2026-09-07。

## 结论

项目已经显式使用 top-k，但目前主要用于 `k=1` 的贪心解码，尚未提供统一、可配置的 `k>1` 随机采样参数。因此，本次按“若未使用则添加”的条件，不重复添加采样实现。

## 代码依据

- `edge/edge_client.py` 的 `EdgeClient.draft()`：当 `temperature == 0.0` 时，发送 `samplers: ["top_k"]`、`top_k: 1`，并设置 `top_p: 1.0`、`min_p: 0.0`。即只保留概率最大的一个候选 token。
- `edge/verifier.py` 的 `MockVerifier._greedy_next()`：同样显式发送 `samplers: ["top_k"]` 和 `top_k: 1`。
- `cloud/verify_server.py` 的 `/verify` 路径：设置 `K = 20`，传入 `prompt_logprobs=K` 和 `logprobs=K`；这是候选概率的返回数量，不是 `SamplingParams(top_k=20)` 的生成采样配置。`verify_sampling()` 的拒绝分支使用返回的候选集合进行重采样。
- 边缘端 `temperature > 0` 时未显式发送 `top_k`，实际采样行为取决于 llama-server 配置；云端 `SamplingParams` 也未显式指定 `top_k`。不能据此认定全链路采用了统一的 top-k 随机采样策略。

## 本次更改与验证

- 新增本检查记录，并在 README 中添加入口，保留 Git 可查看的更改痕迹。
- 未修改运行时代码或已有采样行为。
- 验证方式：检索项目中的 `top_k`、`topk`、`SamplingParams` 和温度相关配置，核对请求构造与验证逻辑；检查文档差异格式。未运行模型推理测试，本次变更仅涉及文档。
