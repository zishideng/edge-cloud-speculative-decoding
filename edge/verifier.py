"""Verifier interface + two implementations.

MockVerifier:  Jetson uses its own llama-server to also act as the target.
               No network. Useful for protocol validation when H200 is unavailable.

RemoteVerifier: HTTP POST to the verify_server running on H200.
"""
from __future__ import annotations

import time
import json
from common.metrics import latency_breakdown
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

import requests


# --------------------------------------------------------------------------- #
@dataclass
class VerifyResult:
    accepted_ids: List[int]
    n_accepted: int
    bonus_id: Optional[int]
    bonus_is_correction: bool
    should_stop: bool
    verify_time_ms: float           # server-side compute time only
    network_time_ms: float          # round-trip wall time minus server time
    metadata: Dict[str, Any] = field(default_factory=dict)


# --------------------------------------------------------------------------- #
class VerifierBase:
    """Contract: verify a draft chunk and report what target accepts."""

    def verify(
        self,
        prompt_ids: List[int],
        draft_ids: List[int],
        draft_logprobs: Optional[List[float]] = None,
        temperature: float = 0.0,
        eos_id: Optional[int] = None,
    ) -> VerifyResult:
        raise NotImplementedError


# --------------------------------------------------------------------------- #
class MockVerifier(VerifierBase):
    """Use the local llama.cpp server as the target too.

    This is *not* a real Edge-Cloud verifier — both models live on Jetson and
    they're identical. Acceptance rate will be ~100%. The point is to
    validate the rest of the protocol (tokenization, draft loop, accept
    logic, bonus token handling) without depending on the H200.

    Implementation: we ask llama-server to predict tokens at each draft
    position by sending `prompt + draft[:i]` and asking for `n_predict=1`
    greedy. If predicted token matches `draft[i]`, accept; otherwise stop.

    NOTE: this is O(γ) sequential calls per verify — slow but correct.
    A real verifier would batch this into one forward pass (which is what
    H200's vLLM-backed verify_server does).
    """

    def __init__(self, base_url: str = "http://localhost:8080", model_id: str = ""):
        self.base_url = base_url.rstrip("/")
        self.model_id = model_id
        self._session = requests.Session()

    def _greedy_next(self, token_ids: List[int]) -> int:
        """Ask llama-server for the next greedy token after these IDs."""
        r = self._session.post(
            f"{self.base_url}/completion",
            json={
                "prompt": token_ids,
                "n_predict": 1,
                "return_tokens": True,
                "samplers": ["top_k"],
                "top_k": 1,
                "temperature": 0.0,
                "seed": 42,
                "cache_prompt": True,
                "stop": ["<|eot_id|>", "<|end_of_text|>"],
            },
            timeout=30,
        )
        r.raise_for_status()
        data = r.json()
        # Different llama.cpp versions name this differently
        tokens = (
            data.get("tokens")
            or data.get("output_tokens")
            or []
        )
        if tokens:
            return int(tokens[0])
        # Alternative: detokenize from content (slow path)
        content = data.get("content", "")
        if content:
            # /tokenize endpoint to get IDs back
            tr = self._session.post(
                f"{self.base_url}/tokenize",
                json={"content": content},
                timeout=10,
            )
            tids = tr.json().get("tokens", [])
            if tids:
                return int(tids[0])
        raise RuntimeError(f"could not extract token ID from llama-server: {data}")

    def verify(
        self,
        prompt_ids: List[int],
        draft_ids: List[int],
        draft_logprobs: Optional[List[float]] = None,
        temperature: float = 0.0,
        eos_id: Optional[int] = None,
    ) -> VerifyResult:
        t0 = time.perf_counter()
        accepted = []
        bonus = None
        bonus_is_corr = False

        cur = list(prompt_ids)
        for i, draft_tok in enumerate(draft_ids):
            try:
                target_tok = self._greedy_next(cur)
            except Exception as e:
                # Network glitch or server error — treat as reject at this position
                target_tok = -1
            if target_tok == draft_tok:
                accepted.append(draft_tok)
                cur.append(draft_tok)
            else:
                bonus = target_tok if target_tok >= 0 else None
                bonus_is_corr = True
                break

        # If all draft accepted, generate one bonus
        if len(accepted) == len(draft_ids):
            try:
                bonus = self._greedy_next(cur)
            except Exception:
                bonus = None

        should_stop = (
            eos_id is not None and bonus is not None and bonus == eos_id
        )

        verify_ms = (time.perf_counter() - t0) * 1000.0
        return VerifyResult(
            accepted_ids=accepted,
            n_accepted=len(accepted),
            bonus_id=bonus,
            bonus_is_correction=bonus_is_corr,
            should_stop=should_stop,
            verify_time_ms=verify_ms,
            network_time_ms=0.0,  # mock = no real network
            metadata={"mode": "mock"},
        )


# --------------------------------------------------------------------------- #
class RemoteVerifier(VerifierBase):
    """HTTP POST to /verify on the H200 verify_server."""

    def __init__(self, url: str, timeout: float = 60):
        # url like "http://foscsmlprd03.its.auckland.ac.nz:9090"
        self.base = url.rstrip("/")
        self.timeout = timeout
        self.policy = None
        self._session = requests.Session()
        # Long-running connection keeps TCP alive between rounds.
        self._session.headers.update({"Connection": "keep-alive"})

    def verify(
        self,
        prompt_ids: List[int],
        draft_ids: List[int],
        draft_logprobs: Optional[List[float]] = None,
        temperature: float = 0.0,
        eos_id: Optional[int] = None,
    ) -> VerifyResult:
        body = {
            "prompt_ids": prompt_ids,
            "draft_ids": draft_ids,
            "temperature": temperature,
        }
        if draft_logprobs is not None:
            body["draft_logprobs"] = draft_logprobs
        if eos_id is not None:
            body["eos_id"] = eos_id

        if self.policy is not None:
            body['policy'] = self.policy
        body['experiment_queue_ms'] = getattr(self, 'experiment_queue_ms', 0.0)
        t0 = time.perf_counter()
        wire = json.dumps(body, allow_nan=False).encode('utf-8')
        serialize_ms = (time.perf_counter() - t0) * 1000
        t0 = time.perf_counter()
        r = self._session.post(f"{self.base}/verify", data=wire,
                               headers={'Content-Type': 'application/json'}, timeout=self.timeout)
        wall_ms = (time.perf_counter() - t0) * 1000.0
        r.raise_for_status()
        t0 = time.perf_counter()
        data = json.loads(r.content)
        deserialize_ms = (time.perf_counter() - t0) * 1000

        server_ms = data['cloud_verify_ms']
        timing = latency_breakdown(wall_ms, serialize_ms, deserialize_ms,
                                   data['cloud_queue_ms'], server_ms, len(wire), len(r.content))
        return VerifyResult(
            accepted_ids=data["accepted_ids"],
            n_accepted=data["n_accepted"],
            bonus_id=data.get("bonus_id"),
            bonus_is_correction=data.get("bonus_is_correction", False),
            should_stop=data.get("should_stop", False),
            verify_time_ms=server_ms,
            network_time_ms=timing['network_rtt_ms'],
            metadata=data.get("metadata", {}) | {"mode": "remote", "wall_ms": wall_ms, 'timing': timing},
        )

    def health(self) -> Dict[str, Any]:
        r = self._session.get(f"{self.base}/health", timeout=5)
        r.raise_for_status()
        return r.json()

    def info(self) -> Dict[str, Any]:
        r = self._session.get(f"{self.base}/info", timeout=5)
        r.raise_for_status()
        return r.json()
