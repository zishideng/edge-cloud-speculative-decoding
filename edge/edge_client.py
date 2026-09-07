"""edge_client.py — Jetson-side SD control loop.

Public entrypoint: `generate(prompt_text, gamma, max_tokens, ...)` returns
the full assistant response plus a dict of per-round metrics.

Key methods:
- `tokenize(text)`       use llama.cpp's /tokenize so token IDs exactly match
                          what /completion will operate on
- `detokenize(ids)`      reverse, for final text
- `draft(ctx, gamma)`    ask the local llama-server for γ greedy tokens +
                          their logprobs; returns (token_ids, logprobs)
- `generate(...)`        the full SD loop using a Verifier
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple

import requests

from edge.verifier import VerifierBase, VerifyResult


# --------------------------------------------------------------------------- #
@dataclass
class GenerationMetrics:
    """Per-request metrics, exported to JSON."""
    n_rounds: int = 0
    n_draft_proposed: int = 0
    n_accepted: int = 0
    n_bonus: int = 0
    total_output_tokens: int = 0
    wall_time_s: float = 0.0
    draft_time_ms: float = 0.0      # cumulative
    verify_time_ms: float = 0.0     # cumulative server-side
    network_time_ms: float = 0.0    # cumulative network-only
    rounds: List[Dict[str, Any]] = field(default_factory=list)

    @property
    def acceptance_rate(self) -> float:
        return self.n_accepted / max(1, self.n_draft_proposed)

    @property
    def tokens_per_second(self) -> float:
        return self.total_output_tokens / max(1e-9, self.wall_time_s)


# --------------------------------------------------------------------------- #
class EdgeClient:
    """Jetson side of the SD protocol.

    Uses llama.cpp's native /completion endpoint to get token IDs and
    logprobs in one call. Chat templating is done by passing through the
    /v1/chat/completions endpoint once at the start to format the prompt,
    then we tokenize the formatted prompt and own everything in IDs.
    """

    def __init__(self, draft_url: str = "http://localhost:8080"):
        self.draft_url = draft_url.rstrip("/")
        self._session = requests.Session()
        self._session.headers.update({"Connection": "keep-alive"})
        # Cache the EOS / chat template tokens
        self._props = None

    # -------- low-level llama-server helpers ------------------------------- #
    def props(self) -> Dict[str, Any]:
        """llama.cpp exposes /props with chat template and special tokens."""
        if self._props is None:
            r = self._session.get(f"{self.draft_url}/props", timeout=10)
            r.raise_for_status()
            self._props = r.json()
        return self._props

    def draft_n_vocab(self) -> Optional[int]:
        """Best-effort read of the draft model's vocab size from /props."""
        try:
            p = self.props()
        except Exception:
            return None
        for path in (("default_generation_settings", "n_vocab"),
                     ("n_vocab",), ("model", "n_vocab")):
            d = p
            ok = True
            for k in path:
                if isinstance(d, dict) and k in d:
                    d = d[k]
                else:
                    ok = False
                    break
            if ok and isinstance(d, int):
                return d
        return None

    def _diagnose_bad_completion(self, prompt_ids: List[int], r) -> None:
        """Print why llama.cpp rejected a /completion prompt (HTTP 4xx).

        The usual cause in edge--cloud SD is a bonus/correction token returned
        by the cloud verifier whose id is invalid for the *draft* model:
        either out of range (vocab mismatch) or a special/control token.
        """
        nv = self.draft_n_vocab()
        oob = [t for t in prompt_ids if t < 0 or (nv is not None and t >= nv)]
        print(f"[draft][ERR] HTTP {r.status_code}: {r.text[:300]}")
        print(f"[draft][ERR] draft n_vocab={nv}  prompt_len={len(prompt_ids)}  "
              f"max_id_in_prompt={max(prompt_ids) if prompt_ids else None}  "
              f"out_of_range={oob[:10]}")
        # Show the suspect tokens (out-of-range first, else the last few) + text.
        suspects = oob[:6] or prompt_ids[-6:]
        for t in suspects:
            try:
                txt = self.detokenize([t])
            except Exception as e:
                txt = f"<detok failed: {e}>"
            print(f"   id={t} -> {txt!r}")

    def tokenize(self, text: str, add_special: bool = True) -> List[int]:
        r = self._session.post(
            f"{self.draft_url}/tokenize",
            json={"content": text, "add_special": add_special},
            timeout=10,
        )
        r.raise_for_status()
        return list(map(int, r.json().get("tokens", [])))

    def detokenize(self, ids: List[int]) -> str:
        r = self._session.post(
            f"{self.draft_url}/detokenize",
            json={"tokens": ids},
            timeout=10,
        )
        r.raise_for_status()
        return r.json().get("content", "")

    def apply_chat_template(
        self,
        messages: List[Dict[str, str]],
        add_generation_prompt: bool = True,
    ) -> str:
        """Use llama-server's chat template by hitting /apply-template."""
        r = self._session.post(
            f"{self.draft_url}/apply-template",
            json={"messages": messages, "add_generation_prompt": add_generation_prompt},
            timeout=10,
        )
        r.raise_for_status()
        prompt = r.json().get("prompt")
        if not prompt:
            raise RuntimeError("llama-server returned no chat template prompt")
        return prompt

    # -------- draft step ---------------------------------------------------- #
    def draft(
        self,
        prompt_ids: List[int],
        gamma: int,
        temperature: float = 0.0,
    ) -> Tuple[List[int], List[float]]:
        """Generate γ tokens via llama-server, return (ids, logprobs).

        We pass token IDs directly (not text) so the draft tokens are
        exactly what /tokenize produced — no tokenizer round-trip ambiguity.
        """
        payload = {
            "prompt": prompt_ids,
            "n_predict": gamma,
            "temperature": float(temperature),
            "return_tokens": True,
            "cache_prompt": True,
            "n_probs": 1,
            "seed": getattr(self, 'seed', 42),
            # Stop at Llama-3 turn boundaries so we don't keep generating
            # extra assistant turns after the first complete answer.
            "stop": ["<|eot_id|>", "<|end_of_text|>"],
        }
        if temperature == 0.0:
            payload.update({
                "samplers": ["top_k"],
                "top_k": 1,
                "top_p": 1.0,
                "min_p": 0.0,
            })
        r = self._session.post(
            f"{self.draft_url}/completion",
            json=payload,
            timeout=120,
        )
        if not r.ok:
            self._diagnose_bad_completion(prompt_ids, r)
        r.raise_for_status()
        data = r.json()

        # Field names vary by llama.cpp version. Try several.
        token_ids = (
            data.get("tokens")
            or data.get("output_tokens")
            or [t.get("id") for t in data.get("completion_probabilities", []) if "id" in t]
        )
        if not token_ids:
            raise RuntimeError("Draft response has no token IDs; tokenization cannot substitute for generated IDs")

        # Logprobs (optional for greedy, kept for T>0 mode)
        logprobs = []
        for entry in data.get("completion_probabilities", []) or []:
            # entry = {"id": int, "logprob": float, ...}
            if "logprob" in entry:
                logprobs.append(float(entry["logprob"]))
            elif "prob" in entry:
                import math
                logprobs.append(math.log(max(1e-30, float(entry["prob"]))))

        # If logprobs absent, fill with zeros (only used in T>0; benign for greedy)
        if len(logprobs) != len(token_ids):
            logprobs = [0.0] * len(token_ids)

        return [int(t) for t in token_ids], logprobs

    # -------- top-level generate ------------------------------------------- #
    def generate(
        self,
        messages: List[Dict[str, str]],
        verifier: VerifierBase,
        gamma: int = 5,
        max_tokens: int = 512,
        temperature: float = 0.0,
        eos_id: Optional[int] = None,
        no_think: bool = False,
    ) -> Tuple[str, GenerationMetrics]:
        """Full SD loop. Returns (assistant_text, metrics)."""
        if temperature != 0 or gamma < 1 or max_tokens < 1:
            raise ValueError("Require temperature=0 and positive gamma/max_tokens")
        # 1. Build prompt and tokenize once.
        # Qwen3 defaults to "thinking" mode; appending /no_think to the last user
        # turn disables it. (DeepSeek-R1 distills ignore this and always reason.)
        if no_think:
            messages = [dict(m) for m in messages]
            for m in reversed(messages):
                if m.get("role") == "user":
                    m["content"] = m.get("content", "").rstrip() + " /no_think"
                    break
        prompt_text = self.apply_chat_template(messages, add_generation_prompt=True)
        prompt_ids = self.tokenize(prompt_text, add_special=False)
        # apply_chat_template usually inserts <|begin_of_text|> already, so
        # add_special=False avoids doubling

        # If caller didn't pass eos_id, try to find it in /props, else
        # fall back to Llama-3's <|eot_id|> = 128009 (verified by tokenizing
        # the special string on this exact model).
        if eos_id is None:
            props = self.props()
            eos_id = (
                props.get("default_generation_settings", {}).get("eos_token_id")
                or props.get("eos_token_id")
            )
            if eos_id is None:
                raise ValueError("Model EOS ID unavailable; supply eos_id explicitly")

        gen_start = len(prompt_ids)   # everything after this is "generated"
        metrics = GenerationMetrics()
        t_start = time.perf_counter()

        ids = list(prompt_ids)
        while len(ids) - gen_start < max_tokens:
            # ---- 1. Draft on Jetson ---------------------------------------
            t0 = time.perf_counter()
            draft_ids, draft_lps = self.draft(ids, gamma, temperature)
            draft_ms = (time.perf_counter() - t0) * 1000.0

            if not draft_ids:
                raise RuntimeError("Draft backend returned no tokens")

            # If server returned fewer than requested, it hit a stop string
            # (e.g. <|eot_id|>). Mark a stop so we exit after applying.
            short_draft_stop = len(draft_ids) < gamma

            # Clip if draft overshoots max_tokens budget
            remaining = max_tokens - (len(ids) - gen_start)
            if len(draft_ids) > remaining:
                draft_ids = draft_ids[:remaining]
                draft_lps = draft_lps[:remaining]

            # ---- 2. Verify (mock or remote) -------------------------------
            vr: VerifyResult = verifier.verify(
                prompt_ids=ids,
                draft_ids=draft_ids,
                draft_logprobs=draft_lps,
                temperature=temperature,
                eos_id=eos_id,
            )

            # ---- 3. Apply accepted + bonus --------------------------------
            produced = vr.accepted_ids + ([] if vr.bonus_id is None else [vr.bonus_id])
            produced = produced[:remaining]
            if eos_id in produced:
                produced = produced[:produced.index(eos_id)+1]
            ids.extend(produced)

            # ---- 4. Update metrics ----------------------------------------
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
                "bonus_is_correction": vr.bonus_is_correction,
            })

            # ---- 5. Stop conditions ---------------------------------------
            if vr.should_stop or eos_id in produced:
                break
            # Safety: if 0 accepted and no bonus, we're stuck — break
            if vr.n_accepted == 0 and vr.bonus_id is None:
                raise RuntimeError("Verifier returned neither accepted nor correction token")

        metrics.total_output_tokens = len(ids) - gen_start
        metrics.wall_time_s = time.perf_counter() - t_start

        # 6. Detokenize generated portion
        gen_ids = ids[gen_start:]
        # Strip a trailing EOS for cleanliness
        if eos_id is not None and gen_ids and gen_ids[-1] == eos_id:
            gen_ids = gen_ids[:-1]
        text = self.detokenize(gen_ids)

        return text, metrics


# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    # quick sanity if you run `python edge_client.py`
    from verifier import MockVerifier
    client = EdgeClient()
    verifier = MockVerifier(base_url="http://localhost:8080")
    text, m = client.generate(
        messages=[
            {"role": "system", "content": "You are a helpful math tutor."},
            {"role": "user", "content": "What is 12 * 7? Just the number."},
        ],
        verifier=verifier,
        gamma=3,
        max_tokens=32,
    )
    print("=== Output ===")
    print(text)
    print("=== Metrics ===")
    print(json.dumps({
        "n_rounds": m.n_rounds,
        "n_accepted": m.n_accepted,
        "n_proposed": m.n_draft_proposed,
        "accept_rate": m.acceptance_rate,
        "tokens_per_sec": m.tokens_per_second,
        "wall_s": m.wall_time_s,
    }, indent=2))
