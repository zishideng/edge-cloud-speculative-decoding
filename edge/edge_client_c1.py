"""edge_client_c1.py — C1: Entropy-Aware Adaptive γ Controller.

Drop-in extension of EdgeClient from Day 4B. Override `generate()` to use
an AdaptiveGammaController that picks γ each round based on:
  - exponentially-moving-averaged acceptance rate
  - draft entropy (mean logprob magnitude)

Algorithm (training-free, ~20 lines of logic):

  init: γ ← γ_init,  ema_accept ← 0.7

  each round:
    α = (n_accepted_last_round) / γ_used_last_round
    ema_accept = β * ema_accept + (1-β) * α
    mean_lp   = mean of draft logprobs last round (negative; closer to 0 = more confident)

    # rule: confident & high acceptance → grow γ; uncertain or rejecting → shrink
    if ema_accept > thresh_hi and mean_lp > lp_thresh:
        γ ← min(γ + 1, γ_max)
    elif ema_accept < thresh_lo:
        γ ← max(γ - 1, γ_min)
    # else: keep γ

Defaults tuned for our B3 measurements (acceptance 73-81% on Llama-3.2-1B / 8B):
  γ_min=2, γ_max=8, γ_init=3
  thresh_hi=0.80, thresh_lo=0.55
  lp_thresh=-1.5 (token-level avg logprob)
  β=0.7

Keep `verifier.py` unchanged.
"""
from __future__ import annotations
import time
from dataclasses import dataclass
from typing import List, Optional, Dict, Tuple

from edge.edge_client import EdgeClient, GenerationMetrics
from edge.verifier import VerifierBase, VerifyResult


# --------------------------------------------------------------------------- #
@dataclass
class C1Config:
    gamma_init: int = 3
    gamma_min: int = 2
    gamma_max: int = 8
    thresh_hi: float = 0.80     # ema_accept above → consider growing
    thresh_lo: float = 0.55     # ema_accept below → shrink
    lp_thresh: float = -1.5     # require draft confidence (mean lp > this) to grow
    beta: float = 0.7           # EMA factor on acceptance


class AdaptiveGammaController:
    """Stateful controller. One instance per generate() call."""

    def __init__(self, cfg: C1Config):
        self.cfg = cfg
        self.gamma = cfg.gamma_init
        self.ema_accept = 0.7
        # log per-round for analysis
        self.trace: List[Dict] = []

    def next_gamma(self) -> int:
        return self.gamma

    def update(self, n_accepted: int, gamma_used: int,
               draft_logprobs: List[float]) -> None:
        """Called after each round with the verify result."""
        cfg = self.cfg
        alpha = n_accepted / max(1, gamma_used)
        self.ema_accept = cfg.beta * self.ema_accept + (1 - cfg.beta) * alpha
        mean_lp = sum(draft_logprobs) / len(draft_logprobs) if draft_logprobs else 0.0

        old = self.gamma
        if self.ema_accept > cfg.thresh_hi and mean_lp > cfg.lp_thresh:
            self.gamma = min(self.gamma + 1, cfg.gamma_max)
        elif self.ema_accept < cfg.thresh_lo:
            self.gamma = max(self.gamma - 1, cfg.gamma_min)

        self.trace.append({
            "gamma_before": old,
            "gamma_after": self.gamma,
            "n_accepted": n_accepted,
            "gamma_used": gamma_used,
            "alpha": alpha,
            "ema_accept": self.ema_accept,
            "mean_lp": mean_lp,
        })


# --------------------------------------------------------------------------- #
class EdgeClientC1(EdgeClient):
    """EdgeClient with C1 adaptive γ instead of fixed γ."""

    def __init__(self, draft_url: str = "http://localhost:8080",
                 c1_cfg: Optional[C1Config] = None):
        super().__init__(draft_url=draft_url)
        self.c1_cfg = c1_cfg or C1Config()

    def generate(
        self,
        messages,
        verifier: VerifierBase,
        gamma: int = 5,          # ignored — kept for interface compat
        max_tokens: int = 512,
        temperature: float = 0.0,
        eos_id: Optional[int] = None,
    ) -> Tuple[str, GenerationMetrics]:
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
        controller = AdaptiveGammaController(self.c1_cfg)
        t_start = time.perf_counter()

        ids = list(prompt_ids)
        while len(ids) - gen_start < max_tokens:
            g = controller.next_gamma()

            # Draft
            t0 = time.perf_counter()
            draft_ids, draft_lps = self.draft(ids, g, temperature)
            draft_ms = (time.perf_counter() - t0) * 1000.0

            if not draft_ids:
                break
            short_draft_stop = len(draft_ids) < g

            # Clip to budget
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

            # Update controller
            controller.update(vr.n_accepted, len(draft_ids), draft_lps)

            metrics.n_rounds += 1
            metrics.n_draft_proposed += len(draft_ids)
            metrics.n_accepted += vr.n_accepted
            metrics.n_bonus += (1 if vr.bonus_id is not None else 0)
            metrics.draft_time_ms += draft_ms
            metrics.verify_time_ms += vr.verify_time_ms
            metrics.network_time_ms += vr.network_time_ms
            metrics.rounds.append({
                "gamma": len(draft_ids),
                "n_accepted": vr.n_accepted,
                "draft_ms": draft_ms,
                "verify_ms": vr.verify_time_ms,
                "network_ms": vr.network_time_ms,
                "ema_accept_after": controller.ema_accept,
                "gamma_next": controller.gamma,
            })

            if vr.should_stop or short_draft_stop:
                break
            if vr.n_accepted == 0 and vr.bonus_id is None:
                break

        metrics.total_output_tokens = len(ids) - gen_start
        metrics.wall_time_s = time.perf_counter() - t_start

        gen_ids = ids[gen_start:]
        if eos_id is not None and gen_ids and gen_ids[-1] == eos_id:
            gen_ids = gen_ids[:-1]
        text = self.detokenize(gen_ids)

        # Attach controller trace to metrics for analysis
        metrics.rounds[0]["c1_config"] = self.c1_cfg.__dict__  # stash on round 0
        return text, metrics
