"""verifier_ext.py — add remote generate() to RemoteVerifier.

Import this AFTER verifier.py to monkeypatch the generate method onto
RemoteVerifier, OR just copy the generate() method into verifier.py's
RemoteVerifier class.

Provides:
    RemoteVerifier.generate(prompt_ids, max_tokens, temperature, eos_id)
      → (token_ids: List[int], should_stop: bool, ms: float)
"""
from __future__ import annotations
import time
from typing import List, Optional, Tuple

from edge.verifier import RemoteVerifier


def _remote_generate(self, prompt_ids: List[int], max_tokens: int = 1,
                     temperature: float = 0.0,
                     eos_id: Optional[int] = None) -> Tuple[List[int], bool, float]:
    body = {
        "prompt_ids": prompt_ids,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    if eos_id is not None:
        body["eos_id"] = eos_id
    t0 = time.perf_counter()
    r = self._session.post(f"{self.base}/generate", json=body, timeout=60)
    wall = (time.perf_counter() - t0) * 1000.0
    r.raise_for_status()
    d = r.json()
    return d["token_ids"], d.get("should_stop", False), wall


# Attach to the class
RemoteVerifier.generate = _remote_generate
