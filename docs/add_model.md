# Adding a new draft / target model pair

The system is config-driven via `models.yaml`. Adding a pair = one yaml entry
+ launching the two servers with that config + running the validation test.

## Hard requirement
**Draft and target MUST share the same tokenizer / vocab_size.** Speculative
decoding compares draft tokens against target logprobs by token id; mismatched
vocabularies produce garbage (or near-zero acceptance). The bench scripts
validate this automatically when you pass `--model-config`, and abort on a
confirmed mismatch.

## Step 1 — verify vocab match BEFORE anything else
```bash
python3 -c "
from transformers import AutoTokenizer
d = AutoTokenizer.from_pretrained('<DRAFT_HF_REPO_OR_BASE>')
t = AutoTokenizer.from_pretrained('<TARGET_HF_REPO>')
print('draft', len(d), 'target', len(t),
      'MATCH' if len(d)==len(t) else 'MISMATCH -> do not use')
"
```
Same family (both Llama-3, both Qwen2.5, ...) almost always matches. Crossing
families usually does not.

## Step 2 — add an entry to `models.yaml`
```yaml
mypair:
  description: "<one line>"
  target: org/Target-Model            # HF id for vLLM
  draft_hf_repo: org/Draft-GGUF        # GGUF repo
  draft_gguf: draft-q4_k_m.gguf        # filename inside that repo
  eos_id: <int>                        # see Step 3
  vocab_size: <int>                    # from Step 1
  max_model_len: 4096
```

## Step 3 — find the EOS token id
```bash
python3 -c "
from transformers import AutoTokenizer
t = AutoTokenizer.from_pretrained('<TARGET_HF_REPO>')
print('eos_token', t.eos_token, 'id', t.eos_token_id)
# chat models often stop on a chat-end token, not the raw eos:
print('special', t.special_tokens_map)
"
```
Common values: Llama-3 `<|eot_id|>` = 128009; Qwen2.5 `<|im_end|>` = 151645.
Use the token the chat template actually ends turns with.

## Step 4 — launch servers with the config

Cloud (H200):
```bash
# slurm_serve.sh reads MODEL_CONFIG to pick --target from models.yaml
MODEL_CONFIG=mypair sbatch cloud/slurm_serve.sh
# (or directly:)
python cloud/verify_server.py --target org/Target-Model --port 9090 --max-model-len 4096
```

Edge (Jetson):
```bash
# download the draft GGUF
huggingface-cli download org/Draft-GGUF draft-q4_k_m.gguf \
    --local-dir ~/specdecode/models
# launch llama-server pointing at it
MODEL=~/specdecode/models/draft-q4_k_m.gguf bash edge/start_server.sh
```

## Step 5 — validate + baseline (the test ladder)
Run from `src/`. Stop at the first failure.

```bash
cd ~/specdecode/src

# (1) tiny remote run WITH validation — aborts on vocab mismatch
python bench_edge_cloud.py --verifier remote --remote-url http://localhost:9090 \
    --model-config mypair --gamma 2 --n 5 \
    --data ../edge/data/gsm8k_test_50.jsonl --out /tmp/newpair_smoke.json
#   watch for: "[model_config] vocab OK"  and  acceptance > 0

# (2) full baseline — record new pair's acceptance / tok/s
python bench_edge_cloud.py --verifier remote --remote-url http://localhost:9090 \
    --model-config mypair --gamma 2 --n 50 \
    --data ../edge/data/gsm8k_test_50.jsonl \
    --out ../results/B3_mypair_g2.json

# (3) fallback experiment (if baseline acceptance is reasonable)
python bench_smart.py --model-config mypair \
    --fallback-k 3 --fallback-thresh 0.65 --gamma 2 --task gsm8k \
    --data ../edge/data/gsm8k_test_50.jsonl --n 30 --profile-energy \
    --out ../results/S_fb_mypair_gsm8k.json
```

## Diagnosing a bad pair
- **Validation aborts with VOCAB MISMATCH** → tokenizers differ; pick a draft
  from the same family as the target.
- **Acceptance ≈ 0 but vocab matched** → wrong `eos_id` (chain stops wrong), or
  the draft is too weak / wrong instruction format. Check the chat template.
- **"could not read vocab"** warning → llama.cpp `/props` or vLLM `/info` didn't
  expose `n_vocab`; validation is skipped (not fatal). Confirm manually via Step 1.
- **Garbage text** → almost always tokenizer mismatch that slipped past
  validation; re-run Step 1.

## Which bench scripts support --model-config
`bench_edge_cloud.py` and `bench_smart.py` are wired (validation + eos_id).
For `bench_warmup.py`, `bench_prefetch.py`, `bench_c1.py`, `bench_b5.py`,
`bench_c3_energy.py`: they default to the Llama-3 eos (128009). To use them with
a non-Llama pair, either add the same three lines (see the diff in bench_smart.py:
load_model_config -> eos_id -> pass eos_id into generate), or pass the right data
and rely on llama.cpp /props auto-detection of eos.
