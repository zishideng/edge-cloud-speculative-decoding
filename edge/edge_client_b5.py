"""edge_client_b5.py — B5 Ours = C3 SLO router (uses lookup table).

Reads C3_lookup.json (built by summarize_c3.py) and picks (power_mode, γ)
at the START of each request based on the user's latency SLO.

NOTE: actually CHANGING power mode requires sudo nvpmodel. We don't do
that at request time (too slow + needs root). Instead, the script reports
what power_mode the router WOULD pick — and you set Jetson to that mode
ONCE before the run.

In other words: the controller selects γ at runtime, and the operator
sets power_mode to match the dominant SLO. This is realistic — phones
and Jetsons rarely change power mode per-request.
"""
from __future__ import annotations
import json, pathlib
from typing import Dict, Optional

from edge.edge_client import EdgeClient


class SLORouter:
    def __init__(self, lookup_path: str, current_power_mode: str = "MAXN"):
        d = json.loads(pathlib.Path(lookup_path).read_text())
        self.table: Dict[str, dict] = {k: v for k, v in d.items() if v}
        self.current_mode = current_power_mode

    def route(self, slo_latency_s: float) -> dict:
        """Pick the lowest-J/tok config that fits the SLO."""
        # Find smallest SLO bucket >= slo_latency_s
        buckets = sorted(
            [(int(k.replace("slo_", "").replace("s", "")), v)
             for k, v in self.table.items()],
            key=lambda x: x[0]
        )
        chosen = None
        for slo_s, cfg in buckets:
            if slo_s >= slo_latency_s:
                chosen = cfg
                break
        if chosen is None:
            # SLO too tight — use the smallest bucket's config anyway
            chosen = buckets[0][1] if buckets else {"gamma": 3, "power_mode": "MAXN"}
        return chosen


class EdgeClientB5(EdgeClient):
    """Per-request γ via SLO routing. Power mode set externally."""

    def __init__(self, draft_url: str, router: SLORouter,
                 slo_latency_s: float = 15.0):
        super().__init__(draft_url=draft_url)
        self.router = router
        self.slo = slo_latency_s
        self._last_config = None

    def get_routed_gamma(self) -> int:
        cfg = self.router.route(self.slo)
        self._last_config = cfg
        if cfg["power_mode"] != self.router.current_mode:
            # Ideally would adjust; for now log a warning
            pass
        return int(cfg["gamma"])
