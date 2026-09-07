"""verify_server.py — H200-side verify worker for Edge-Cloud SD.

Loads Llama-3.1-8B once, exposes a FastAPI app on a TCP port. The Jetson
hits POST /verify with (context, draft tokens) and gets back accept/reject
strict or quality-constrained relaxed prefix decisions.

Design notes:
- Single-worker, single-request-at-a-time. SD is inherently sequential
  per stream; concurrency comes from batching multiple streams, which
  we don't need for Day 4A.
- vLLM is held in this process; no IPC. The server stays up for the
  duration of the Slurm job (8h).
- We compute target logprobs by sending [context + draft] as a single
  prompt with max_tokens=1 and prompt_logprobs=K. vLLM returns the
  top-K logprobs at every prompt position; we look at positions
  len(context) .. len(context)+len(draft)-1.
"""
import argparse
import logging
import math
import os
import asyncio
from fastapi.concurrency import run_in_threadpool
from common.acceptance import accept_prefix
from common.experiment_config import load_config, validate
import socket
import sys
import time
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# We import vLLM lazily inside startup to make import errors visible in logs
# instead of dying before FastAPI can announce anything.

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger("verify_server")


# --------------------------------------------------------------------------- #
# Request / response schemas
# --------------------------------------------------------------------------- #
class VerifyRequest(BaseModel):
    prompt_ids: List[int]          # full context: system+user+assistant-so-far
    draft_ids: List[int]           # γ draft tokens proposed by Jetson
    draft_logprobs: Optional[List[float]] = None  # compatibility telemetry; strict/relaxed verification uses target probabilities
    temperature: float = 0.0
    eos_id: Optional[int] = None   # accepting this stops chain
    policy: Optional[dict] = None
    experiment_queue_ms: float = 0.0


class VerifyResponse(BaseModel):
    accepted_ids: List[int]        # initial run of accepted draft tokens
    n_accepted: int                # = len(accepted_ids)
    bonus_id: Optional[int]        # bonus token if all γ accepted; else correction token at reject point
    bonus_is_correction: bool      # True = bonus came from rejection re-sample
    should_stop: bool              # if EOS produced
    verify_time_ms: float
    cloud_queue_ms: float = 0.0
    cloud_verify_ms: float
    metadata: dict                 # extra info for the controller


class GenerateRequest(BaseModel):
    prompt_ids: List[int]
    max_tokens: int = 1            # how many tokens H200 should AR-generate
    temperature: float = 0.0
    eos_id: Optional[int] = None


class GenerateResponse(BaseModel):
    token_ids: List[int]           # generated token IDs
    should_stop: bool              # hit EOS
    generate_time_ms: float


class InfoResponse(BaseModel):
    target_model: str
    vocab_size: int
    n_layers: int
    max_model_len: int
    hostname: str
    port: int
    uptime_s: float


# --------------------------------------------------------------------------- #
# Globals populated at startup
# --------------------------------------------------------------------------- #
STATE = {
    "llm": None,
    "tokenizer": None,
    "args": None,
    "start_time": time.time(),
}


# --------------------------------------------------------------------------- #
# Core verify algorithm
# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
# App
# --------------------------------------------------------------------------- #
app = FastAPI(title="EdgeCloud SD verify server")
MODEL_LOCK = asyncio.Lock()
DEFAULT_CONFIG = load_config()



@app.get("/health")
def health():
    return {"status": "ok", "uptime_s": time.time() - STATE["start_time"]}


@app.get("/info", response_model=InfoResponse)
def info():
    llm = STATE["llm"]
    if llm is None:
        raise HTTPException(503, "model not loaded yet")
    cfg = llm.llm_engine.model_config
    return InfoResponse(
        target_model=cfg.model,
        vocab_size=cfg.get_vocab_size(),
        n_layers=getattr(cfg.hf_config, "num_hidden_layers", -1),
        max_model_len=cfg.max_model_len,
        hostname=socket.gethostname(),
        port=STATE["args"].port,
        uptime_s=time.time() - STATE["start_time"],
    )


@app.post("/verify", response_model=VerifyResponse)
async def verify(req: VerifyRequest):
    if not math.isfinite(req.experiment_queue_ms) or not 0 <= req.experiment_queue_ms <= 60000:
        raise HTTPException(400, 'Invalid injected experiment queue delay')
    queued = time.perf_counter()
    async with MODEL_LOCK:
        if req.experiment_queue_ms:
            deadline = time.perf_counter() + req.experiment_queue_ms / 1000
            # Windows event-loop timers may wake before a perf_counter deadline.
            while (remaining := deadline - time.perf_counter()) > 0:
                await asyncio.sleep(remaining)
        queue_ms = (time.perf_counter() - queued) * 1000
        result = await run_in_threadpool(_verify, req)
        result.cloud_queue_ms = queue_ms
        return result


def _verify(req: VerifyRequest):
    """Run verify on a single draft chunk."""
    t0 = time.perf_counter()
    llm = STATE["llm"]
    if llm is None:
        raise HTTPException(503, "model not loaded yet")

    # vLLM is imported at startup; SamplingParams now in scope
    from vllm import SamplingParams

    n_ctx = len(req.prompt_ids)
    n_draft = len(req.draft_ids)
    if n_draft == 0 or n_ctx == 0:
        raise HTTPException(400, "draft_ids must be non-empty")

    full = req.prompt_ids + req.draft_ids
    if len(full) >= llm.llm_engine.model_config.max_model_len:
        raise HTTPException(400, "prompt + draft exceeds max_model_len")

    # Ask vLLM for logprobs at every prompt position + one more sampled token
    # NOTE: prompt_logprobs returns logprobs over the *given* prompt;
    # since the prompt includes draft_ids, we get target's view of those.
    if req.temperature != 0:
        raise HTTPException(400, "Only temperature=0 is supported; relaxed acceptance is lossy")
    policy = req.policy or {'strategy': 'strict', 'k': 1, 'spent': 0.0}
    try:
        config = validate(dict(DEFAULT_CONFIG, **policy.get('config', {})))
        if config['K_MAX'] > DEFAULT_CONFIG['K_MAX']:
            raise ValueError('Requested K_MAX exceeds server startup configuration; restart with matching --experiment-config')
        if config['SEED'] != DEFAULT_CONFIG['SEED']:
            raise ValueError('Client/server SEED mismatch; use the same experiment configuration')
        strategy = policy['strategy']
        if strategy not in ('strict', 'fixed', 'adaptive'):
            raise ValueError('Invalid acceptance strategy')
        k = 1 if strategy == 'strict' else policy['k']
        if type(k) is not int or not config['K_MIN'] <= k <= config['K_MAX']:
            raise ValueError('Invalid K')
    except (ValueError, KeyError, TypeError) as exc:
        raise HTTPException(400, str(exc)) from exc
    K = config['K_MAX']
    sp = SamplingParams(
        temperature=req.temperature,
        max_tokens=1,
        prompt_logprobs=K,
        logprobs=K,
        seed=DEFAULT_CONFIG['SEED'],
    )
    out = llm.generate(
        prompts=[{"prompt_token_ids": full}],
        sampling_params=sp,
        use_tqdm=False,
    )
    o = out[0]
    # o.prompt_logprobs is a list[Optional[dict[token_id, Logprob]]] of length len(full).
    # Position i corresponds to the token AT prompt position i; logprob is over
    # the distribution that token was sampled from. Position 0 is None (no
    # preceding context). For verify, we want logprobs at positions
    # n_ctx .. n_ctx + n_draft - 1 → these are the distributions BEFORE
    # the draft tokens were placed, which is exactly what we want to compare
    # against.
    prompt_lp = o.prompt_logprobs or []

    # Convert vLLM's Logprob objects to plain dicts
    target_topk_per_pos = []
    for i in range(n_ctx, n_ctx + n_draft):
        if i < len(prompt_lp) and prompt_lp[i]:
            target_topk_per_pos.append(
                {tid: {'logprob': lp.logprob, 'rank': lp.rank} for tid, lp in prompt_lp[i].items()}
            )
        else:
            target_topk_per_pos.append({})

    try:
        accepted_ids, correction, decisions, spent = accept_prefix(
            target_topk_per_pos, req.draft_ids, k=k, config=config,
            spent=policy.get('spent', 0.0), eos_id=req.eos_id)
    except (ValueError, TypeError) as exc:
        raise HTTPException(400, str(exc)) from exc
    n_acc = len(accepted_ids)
    stopped_in_prefix = req.eos_id is not None and req.eos_id in accepted_ids
    if stopped_in_prefix:
        bonus_id = None
    elif n_acc == n_draft:
        sampled = o.outputs[0].token_ids
        if not sampled:
            raise HTTPException(500, 'Target produced no bonus token')
        bonus_id = sampled[0]
    else:
        bonus_id = correction
    bonus_is_correction = correction is not None
    should_stop = stopped_in_prefix or (req.eos_id is not None and bonus_id == req.eos_id)
    md = {'decisions': decisions, 'quality_spent': spent, 'n_draft': n_draft,
          'n_ctx': n_ctx, 'queue_scope': 'application model lock; excludes HTTP ingress',
          'draft_logprobs_target': [d.get(t, {}).get('logprob') for d,t in zip(target_topk_per_pos, req.draft_ids)]}
    elapsed = (time.perf_counter() - t0) * 1000.0

    return VerifyResponse(
        accepted_ids=accepted_ids,
        n_accepted=n_acc,
        bonus_id=bonus_id,
        bonus_is_correction=bonus_is_correction,
        should_stop=should_stop,
        verify_time_ms=elapsed,
        cloud_verify_ms=elapsed,
        metadata=md,
    )


# --------------------------------------------------------------------------- #
# Lifespan: load model on startup, write a "ready" marker so slurm_serve.sh
# can let user know.
# --------------------------------------------------------------------------- #
@app.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    # Explicit quality-reference endpoint, never selected by SD error handling.
    async with MODEL_LOCK:
        return await run_in_threadpool(_generate, req)


def _generate(req: GenerateRequest):
    """H200 autoregressively generates up to max_tokens from prompt_ids.

    Explicit strict cloud quality reference; never invoked by the SD loop.
    """
    import time as _t
    from vllm import SamplingParams
    t0 = _t.perf_counter()
    llm = STATE["llm"]
    if llm is None:
        raise HTTPException(503, "model not loaded yet")

    if req.temperature != 0 or req.max_tokens < 1 or not req.prompt_ids:
        raise HTTPException(400, 'Strict reference requires nonempty prompt, positive max_tokens, temperature=0')
    sp = SamplingParams(
        temperature=0.0,
        max_tokens=req.max_tokens,
        seed=DEFAULT_CONFIG['SEED'],
    )
    if req.eos_id is not None:
        sp.stop_token_ids = [req.eos_id]

    out = llm.generate(
        prompts=[{"prompt_token_ids": req.prompt_ids}],
        sampling_params=sp,
        use_tqdm=False,
    )
    gen = out[0].outputs[0]
    tok_ids = list(gen.token_ids)
    should_stop = bool(
        req.eos_id is not None and tok_ids and tok_ids[-1] == req.eos_id
    )
    return GenerateResponse(
        token_ids=tok_ids,
        should_stop=should_stop,
        generate_time_ms=(_t.perf_counter() - t0) * 1000.0,
    )


@app.on_event("startup")
def _startup():
    args = STATE["args"]
    log.info("Loading target model: %s (tp=%d, dtype=%s, quant=%s, gpu_util=%.2f)",
             args.target, args.tensor_parallel_size, args.dtype,
             args.quantization, args.gpu_memory_utilization)
    from vllm import LLM
    llm_kwargs = dict(
        model=args.target,
        dtype=args.dtype,
        gpu_memory_utilization=args.gpu_memory_utilization,
        max_model_len=args.max_model_len,
        tensor_parallel_size=args.tensor_parallel_size,
        max_logprobs=DEFAULT_CONFIG['K_MAX'],
        seed=DEFAULT_CONFIG['SEED'],
    )
    # Only pass quantization when set; None means "use the checkpoint as-is".
    if args.quantization and args.quantization.lower() != "none":
        llm_kwargs["quantization"] = args.quantization
    llm = LLM(**llm_kwargs)
    STATE["llm"] = llm
    STATE["tokenizer"] = llm.get_tokenizer()
    log.info("Model ready: vocab=%d, max_len=%d",
             llm.llm_engine.model_config.get_vocab_size(),
             llm.llm_engine.model_config.max_model_len)

    # Write a ready marker so slurm_serve.sh can echo "ready at X:Y"
    ready_path = args.ready_file
    if ready_path:
        with open(ready_path, "w") as f:
            f.write(f"{socket.gethostname()}\t{args.port}\n")
        log.info("Wrote ready marker → %s", ready_path)


# --------------------------------------------------------------------------- #
# Entry
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", default="meta-llama/Llama-3.1-8B-Instruct")
    ap.add_argument("--host", default="0.0.0.0")
    ap.add_argument("--port", type=int, default=9090)
    ap.add_argument("--max-model-len", type=int, default=4096)
    # Large-target support (e.g. Llama-3.3-70B, Qwen3-32B).
    ap.add_argument("--tensor-parallel-size", type=int, default=1,
                    help="number of GPUs to shard the target across (TP). "
                         "70B bf16 needs >=2 H200; 32B bf16 fits on 1.")
    ap.add_argument("--dtype", default="bfloat16",
                    help="vLLM dtype: bfloat16 (default), float16, auto.")
    ap.add_argument("--quantization", default=None,
                    help="vLLM quantization, e.g. fp8, awq, gptq. "
                         "Lets a 70B target fit on a single H200. "
                         "Omit/None to load the checkpoint as-is.")
    ap.add_argument("--gpu-memory-utilization", type=float, default=0.85,
                    help="fraction of GPU memory vLLM may use (raise to ~0.92 "
                         "for large targets that are tight on KV-cache room).")
    ap.add_argument("--ready-file", default=None,
                    help="if given, write hostname\\tport here when model is loaded")
    ap.add_argument("--experiment-config", default=None)
    args = ap.parse_args()
    global DEFAULT_CONFIG
    DEFAULT_CONFIG = load_config(args.experiment_config)
    STATE["args"] = args

    log.info("Starting verify server on %s:%d", args.host, args.port)
    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
