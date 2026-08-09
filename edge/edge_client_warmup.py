"""edge_client_warmup.py — Warmup-Aware γ schedule.

Round 0 acceptance is ~0.25 (vs steady ~0.80), so spending γ=5 on round 0
wastes most of the draft. Solution: ramp γ from 1 → steady over the first
few rounds.

Schedule (default):
    round 0: γ = 1
    round 1: γ = 2
    round 2: γ = min(3, gamma_steady)
    round 3+: γ = gamma_steady

Configurable via --warmup-rounds and --warmup-step.
"""
from __future__ import annotations
import time
from dataclasses import dataclass
from typing import List, Optional, Tuple

from edge.edge_client import EdgeClient, GenerationMetrics
from edge.verifier import VerifierBase, VerifyResult


@dataclass
class WarmupConfig:
    gamma_steady: int = 3       # γ used after warmup phase
    warmup_rounds: int = 3      # how many rounds to ramp γ
    warmup_step: int = 1        # γ increment per round during warmup
    gamma_init: int = 1         # γ at round 0


def warmup_gamma(round_idx: int, cfg: WarmupConfig) -> int:
    """γ schedule. round 0 → gamma_init; ramps up; saturates at gamma_steady."""
    if round_idx >= cfg.warmup_rounds:
        return cfg.gamma_steady
    g = cfg.gamma_init + round_idx * cfg.warmup_step
    return min(g, cfg.gamma_steady)


class WarmupAwareEdgeClient(EdgeClient):
    """EdgeClient using warmup-aware γ schedule instead of fixed γ."""

    def __init__(self, draft_url: str = "http://localhost:8080",
                 wcfg: Optional[WarmupConfig] = None):
        super().__init__(draft_url=draft_url)
        self.wcfg = wcfg or WarmupConfig()

    def generate(
        self,
        messages,
        verifier: VerifierBase,
        gamma: int = 3,         # interpreted as gamma_steady
        max_tokens: int = 512,
        temperature: float = 0.0,
        eos_id: Optional[int] = None,
    ) -> Tuple[str, GenerationMetrics]:
        # Override steady γ from arg
        wcfg = WarmupConfig(
            gamma_steady=gamma,
            warmup_rounds=self.wcfg.warmup_rounds,
            warmup_step=self.wcfg.warmup_step,
            gamma_init=self.wcfg.gamma_init,
        )

        # Build prompt
        prompt_text = self.apply_chat_template(messages, add_generation_prompt=True)
        prompt_ids = self.tokenize(prompt_text, add_special=False)

        if eos_id is None:
            props = self.props()
            eos_id = (
                props.get("default_generation_settings", {}).get("eos_token_id")
                or props.get("eos_token_id")
                or 128009  # Llama-3 fallback
            )

        gen_start = len(prompt_ids)
        metrics = GenerationMetrics()
        t_start = time.perf_counter()
        ids = list(prompt_ids)
        round_idx = 0

        while len(ids) - gen_start < max_tokens:
            g = warmup_gamma(round_idx, wcfg)

            # Draft
            t0 = time.perf_counter()
            draft_ids, draft_lps = self.draft(ids, g, temperature)
            draft_ms = (time.perf_counter() - t0) * 1000.0

            if not draft_ids:
                break
            short_draft_stop = len(draft_ids) < g

            # Clip
            remaining = max_tokens - (len(ids) - gen_start)
            if len(draft_ids) > remaining:
                draft_ids = draft_ids[:remaining]
                draft_lps = draft_lps[:remaining]

            # Verify
            vr: VerifyResult = verifier.verify(
                prompt_ids=ids,
                draft_ids=draft_ids,
                draft_logprobs=draft_lps,
                temperature=temperature,
                eos_id=eos_id,
            )

            ids.extend(vr.accepted_ids)
            if vr.bonus_id is not None:
                ids.append(vr.bonus_id)

            metrics.n_rounds += 1
            metrics.n_draft_proposed += len(draft_ids)
            metrics.n_accepted += vr.n_accepted
            metrics.n_bonus += (1 if vr.bonus_id is not None else 0)
            metrics.draft_time_ms += draft_ms
            metrics.verify_time_ms += vr.verify_time_ms
            metrics.network_time_ms += vr.network_time_ms
            metrics.rounds.append({
                "round_idx": round_idx,
                "gamma": len(draft_ids),
                "gamma_scheduled": g,
                "n_accepted": vr.n_accepted,
                "draft_ms": draft_ms,
                "verify_ms": vr.verify_time_ms,
                "network_ms": vr.network_time_ms,
            })

            if vr.should_stop or short_draft_stop:
                break
            if vr.n_accepted == 0 and vr.bonus_id is None:
                break
            round_idx += 1

        metrics.total_output_tokens = len(ids) - gen_start
        metrics.wall_time_s = time.perf_counter() - t_start

        gen_ids = ids[gen_start:]
        if eos_id is not None and gen_ids and gen_ids[-1] == eos_id:
            gen_ids = gen_ids[:-1]
        text = self.detokenize(gen_ids)
        return text, metrics
