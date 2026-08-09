"""edge_client_prefetch.py — Single-stage prefetch async SD (clean).

The real cost we hide is the forward pass over the long shared prefix.
llama.cpp caches KV for prefixes (cache_prompt=True). So the prefetch's
job is to WARM the KV cache for the likely-next context while H200
verifies the current batch.

Per round:
  1. Hold current draft (cur_draft, cur_lps) for context `ids`.
  2. Background thread: draft from spec_ctx = ids + cur_draft (assume full
     accept) — discarded, but warms llama.cpp KV cache for that prefix.
  3. Main thread: verify cur_draft on H200 (parallel with step 2).
  4. Join prefetch.
  5. Re-draft from true next context (ids + accepted + bonus). On a full
     accept this lands on a warm cache (off by 1 bonus token) → fast draft.

Threading works because: requests releases GIL during network I/O, and
llama.cpp runs as a separate process (HTTP), so prefetch-draft (to :8080)
and verify (to :9090) run genuinely in parallel.

Set enable_prefetch=False to get the synchronous baseline with identical
code paths (clean ablation).
"""
from __future__ import annotations
import threading
import time
from dataclasses import dataclass
from typing import List, Optional, Tuple, Dict, Any

from edge.edge_client import EdgeClient, GenerationMetrics
from edge.verifier import VerifierBase, VerifyResult


@dataclass
class PrefetchMetrics(GenerationMetrics):
    n_prefetch_hits: int = 0
    n_prefetch_miss: int = 0


class PrefetchEdgeClient(EdgeClient):
    def __init__(self, draft_url: str = "http://localhost:8080",
                 enable_prefetch: bool = True):
        super().__init__(draft_url=draft_url)
        self.enable_prefetch = enable_prefetch

    def _warm_cache_async(self, ctx_ids: List[int], gamma: int,
                          temperature: float, box: Dict[str, Any]):
        t0 = time.perf_counter()
        try:
            self.draft(ctx_ids, gamma, temperature)  # discard; warms cache
            box["ok"] = True
        except Exception as e:
            box["ok"] = False
            box["error"] = str(e)
        box["ms"] = (time.perf_counter() - t0) * 1000.0

    def generate(self, messages, verifier: VerifierBase, gamma: int = 3,
                 max_tokens: int = 512, temperature: float = 0.0,
                 eos_id: Optional[int] = None) -> Tuple[str, PrefetchMetrics]:
        prompt_text = self.apply_chat_template(messages, add_generation_prompt=True)
        prompt_ids = self.tokenize(prompt_text, add_special=False)
        if eos_id is None:
            props = self.props()
            eos_id = (props.get("default_generation_settings", {}).get("eos_token_id")
                      or props.get("eos_token_id") or 128009)

        gen_start = len(prompt_ids)
        m = PrefetchMetrics()
        t_start = time.perf_counter()
        ids = list(prompt_ids)

        t0 = time.perf_counter()
        cur_draft, cur_lps = self.draft(ids, gamma, temperature)
        m.draft_time_ms += (time.perf_counter() - t0) * 1000.0

        while len(ids) - gen_start < max_tokens:
            if not cur_draft:
                break
            short_draft_stop = len(cur_draft) < gamma
            remaining = max_tokens - (len(ids) - gen_start)
            if len(cur_draft) > remaining:
                cur_draft = cur_draft[:remaining]
                cur_lps = cur_lps[:remaining]
            n_proposed = len(cur_draft)

            box: Dict[str, Any] = {}
            pf = None
            if self.enable_prefetch:
                spec_ctx = ids + cur_draft
                pf = threading.Thread(target=self._warm_cache_async,
                                      args=(spec_ctx, gamma, temperature, box),
                                      daemon=True)
                pf.start()

            vr: VerifyResult = verifier.verify(
                prompt_ids=ids, draft_ids=cur_draft,
                draft_logprobs=cur_lps, temperature=temperature, eos_id=eos_id,
            )

            if pf:
                pf.join()

            n_acc = vr.n_accepted
            ids.extend(vr.accepted_ids)
            if vr.bonus_id is not None:
                ids.append(vr.bonus_id)
            full_accept = (n_acc == n_proposed)
            if full_accept and not vr.should_stop:
                m.n_prefetch_hits += 1
            else:
                m.n_prefetch_miss += 1

            if vr.should_stop or short_draft_stop:
                cur_draft = []
            else:
                t0 = time.perf_counter()
                cur_draft, cur_lps = self.draft(ids, gamma, temperature)
                m.draft_time_ms += (time.perf_counter() - t0) * 1000.0

            m.n_rounds += 1
            m.n_draft_proposed += n_proposed
            m.n_accepted += n_acc
            m.n_bonus += (1 if vr.bonus_id is not None else 0)
            m.verify_time_ms += vr.verify_time_ms
            m.network_time_ms += vr.network_time_ms
            m.rounds.append({
                "n_proposed": n_proposed, "n_accepted": n_acc,
                "verify_ms": vr.verify_time_ms, "network_ms": vr.network_time_ms,
                "prefetch_ms": box.get("ms", 0.0), "full_accept": full_accept,
            })

            if not cur_draft:
                break

        m.total_output_tokens = len(ids) - gen_start
        m.wall_time_s = time.perf_counter() - t_start
        gen_ids = ids[gen_start:]
        if eos_id is not None and gen_ids and gen_ids[-1] == eos_id:
            gen_ids = gen_ids[:-1]
        text = self.detokenize(gen_ids)
        return text, m
