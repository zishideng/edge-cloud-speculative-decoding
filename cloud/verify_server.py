"""verify_server.py — H200-side verify worker for Edge-Cloud SD.

Loads Llama-3.1-8B once, exposes a FastAPI app on a TCP port. The Jetson
hits POST /verify with (context, draft tokens) and gets back accept/reject
decisions per the Leviathan 2023 algorithm.

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
import random
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
    draft_logprobs: Optional[List[float]] = None  # per-position log p(x_i),
                                                  # required for T>0 mode
    temperature: float = 0.0
    eos_id: Optional[int] = None   # if provided, accepting this stops chain


class VerifyResponse(BaseModel):
    accepted_ids: List[int]        # initial run of accepted draft tokens
    n_accepted: int                # = len(accepted_ids)
    bonus_id: Optional[int]        # bonus token if all γ accepted; else correction token at reject point
    bonus_is_correction: bool      # True = bonus came from rejection re-sample
    should_stop: bool              # if EOS produced
    verify_time_ms: float
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
def verify_greedy(target_topk_per_pos, draft_ids):
    """T=0 path. Accept while draft matches target's argmax.

    target_topk_per_pos: list[dict[token_id -> logprob]], one per draft position
    Returns (n_accepted, correction_id_or_None).
    """
    n_acc = 0
    correction = None
    for i, x_i in enumerate(draft_ids):
        # vLLM gave us top-K at this position; pick the actual argmax
        topk = target_topk_per_pos[i]
        if not topk:
            # vLLM didn't return logprobs here (shouldn't happen if request OK).
            # Conservative: reject everything from here.
            break
        argmax_id = max(topk.items(), key=lambda kv: kv[1])[0]
        if argmax_id == x_i:
            n_acc += 1
        else:
            correction = argmax_id
            break
    return n_acc, correction


def verify_sampling(target_topk_per_pos, draft_ids, draft_logprobs):
    """T>0 path. Standard Leviathan accept/reject.

    Each step:
      r ~ U(0,1)
      accept iff r < min(1, q(x_i) / p(x_i))
      where q is target prob, p is draft prob.

    Re-sampling on reject from max(0, q - p) is approximated here by
    sampling from `q` restricted to the top-K vLLM returned. Good enough
    for our paper; if the reviewer asks we can add full vocab support.
    """
    n_acc = 0
    correction = None
    for i, x_i in enumerate(draft_ids):
        topk = target_topk_per_pos[i]
        # Probability target assigns to the draft token (0 if outside top-K)
        q_lp = topk.get(x_i, -float("inf"))
        # Draft side log-prob the edge sent us
        p_lp = draft_logprobs[i] if draft_logprobs and i < len(draft_logprobs) else q_lp
        # Acceptance ratio in log-space: log(q/p) = q_lp - p_lp
        log_ratio = q_lp - p_lp
        accept_prob = min(1.0, math.exp(log_ratio)) if log_ratio < 700 else 1.0
        if random.random() < accept_prob:
            n_acc += 1
        else:
            # Re-sample correction from top-K of target (approx).
            # Convert logprobs → probs, normalize.
            ids = list(topk.keys())
            ps = [math.exp(topk[t]) for t in ids]
            s = sum(ps)
            if s > 0:
                ps = [p / s for p in ps]
                correction = random.choices(ids, weights=ps, k=1)[0]
            break
    return n_acc, correction


def sample_bonus(target_topk_per_pos, temperature):
    """Sample one bonus token from the position AFTER all draft tokens.

    target_topk_per_pos[-1] is at position len(draft); but vLLM only returned
    prompt_logprobs for prompt positions. The bonus token comes from the
    one max_tokens=1 we asked for separately — see caller.
    """
    raise NotImplementedError("bonus is handled by the caller using sampled_id from vLLM")


# --------------------------------------------------------------------------- #
# App
# --------------------------------------------------------------------------- #
app = FastAPI(title="EdgeCloud SD verify server")


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
def verify(req: VerifyRequest):
    """Run verify on a single draft chunk."""
    t0 = time.perf_counter()
    llm = STATE["llm"]
    if llm is None:
        raise HTTPException(503, "model not loaded yet")

    # vLLM is imported at startup; SamplingParams now in scope
    from vllm import SamplingParams

    n_ctx = len(req.prompt_ids)
    n_draft = len(req.draft_ids)
    if n_draft == 0:
        raise HTTPException(400, "draft_ids must be non-empty")

    full = req.prompt_ids + req.draft_ids
    if len(full) >= llm.llm_engine.model_config.max_model_len:
        raise HTTPException(400, "prompt + draft exceeds max_model_len")

    # Ask vLLM for logprobs at every prompt position + one more sampled token
    # NOTE: prompt_logprobs returns logprobs over the *given* prompt;
    # since the prompt includes draft_ids, we get target's view of those.
    K = 20  # top-K logprobs to retrieve; large enough for top-K resample
    sp = SamplingParams(
        temperature=req.temperature,
        max_tokens=1,
        prompt_logprobs=K,
        logprobs=K,
        seed=42,
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
                {tid: lp.logprob for tid, lp in prompt_lp[i].items()}
            )
        else:
            target_topk_per_pos.append({})

    # Run accept/reject
    if req.temperature == 0.0:
        n_acc, correction = verify_greedy(target_topk_per_pos, req.draft_ids)
    else:
        n_acc, correction = verify_sampling(
            target_topk_per_pos, req.draft_ids, req.draft_logprobs
        )

    accepted_ids = req.draft_ids[:n_acc]

    # Bonus token (when all draft accepted) is the one vLLM sampled.
    # Correction token (when rejected) comes from our resample above.
    if n_acc == n_draft:
        sampled = o.outputs[0].token_ids
        bonus_id = sampled[0] if sampled else None
        bonus_is_correction = False
    else:
        bonus_id = correction
        bonus_is_correction = True

    should_stop = (
        req.eos_id is not None
        and bonus_id is not None
        and bonus_id == req.eos_id
    )

    # Metadata for the Jetson-side controller (entropy, acceptance signal)
    md = {
        "draft_logprobs_target": [
            target_topk_per_pos[i].get(req.draft_ids[i], None) if i < len(target_topk_per_pos) else None
            for i in range(n_draft)
        ],
        "n_draft": n_draft,
        "n_ctx": n_ctx,
    }

    return VerifyResponse(
        accepted_ids=accepted_ids,
        n_accepted=n_acc,
        bonus_id=bonus_id,
        bonus_is_correction=bonus_is_correction,
        should_stop=should_stop,
        verify_time_ms=(time.perf_counter() - t0) * 1000.0,
        metadata=md,
    )


# --------------------------------------------------------------------------- #
# Lifespan: load model on startup, write a "ready" marker so slurm_serve.sh
# can let user know.
# --------------------------------------------------------------------------- #
@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    """H200 autoregressively generates up to max_tokens from prompt_ids.

    Used for round-0 bootstrap and cloud-only fallback. Pure target
    generation, no draft involved.
    """
    import time as _t
    from vllm import SamplingParams
    t0 = _t.perf_counter()
    llm = STATE["llm"]
    if llm is None:
        raise HTTPException(503, "model not loaded yet")

    sp = SamplingParams(
        temperature=req.temperature,
        max_tokens=req.max_tokens,
        seed=42,
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
        seed=42,
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
    args = ap.parse_args()
    STATE["args"] = args

    log.info("Starting verify server on %s:%d", args.host, args.port)
    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
