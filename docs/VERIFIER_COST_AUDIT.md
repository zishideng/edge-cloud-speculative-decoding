# Verifier cost: a deployment-specific limitation

The current local `cloud/verify_server.py` sends the full context plus draft to
`LLM.generate`, requesting prompt logprobs at every position and one output
token. It then keeps only the draft-position scores. This is not a persistent
native speculative-decoding session that evaluates only the new draft suffix.

Source inspection of upstream vLLM **v0.26.0** found two relevant paths:

- [`SamplingParams.__post_init__`](https://github.com/vllm-project/vllm/blob/v0.26.0/vllm/sampling_params.py)
  defaults to skipping prefix-cache reads when prompt logprobs are requested.
- [`KVCacheManager.get_computed_blocks`](https://github.com/vllm-project/vllm/blob/v0.26.0/vllm/v1/core/kv_cache_manager.py)
  returns no cached blocks for such requests.

The inspected source files are retained under
`results/research_20260928_135549/source_audit/`. The remote `/info` reports this
package version, but its installed source and engine configuration have not
been independently inspected. Thus full-context recomputation is a strong
source-based explanation to test, not a measured kernel attribution.

Consequences for interpretation:

1. The pilot compares the deployed HTTP verifier against the deployed cloud AR
   path. It does not establish a limit for every implementation of edge–cloud SD.
2. Raising acceptance cannot remove work requested for old context positions.
3. Simply overriding `skip_reading_prefix_cache=False` is not a validated fix:
   previously cached blocks may include draft positions whose scores are needed.
   Missing scores must not be treated as accepted tokens.
4. A suffix-scoring implementation must preserve access to the distribution
   before the first draft token, correctly index all draft scores, and handle
   cached rejected suffixes. Validate acceptance mechanics, EOS, and task
   quality; exact output-token equality is not a research gate.
5. A causal intervention requires access to the running cloud implementation.
   Until then, local draft optimization and the current measured baselines
   remain useful; do not label an untested cloud patch as a speedup.

The application also holds a single model lock around each generation call.
Consequently, issuing concurrent HTTP requests against this server would not
constitute an experiment with an efficiently batched multi-client verifier.
