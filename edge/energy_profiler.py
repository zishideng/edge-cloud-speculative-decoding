"""energy_profiler.py — context manager that samples Jetson power via jtop.

Usage:
    with EnergyProfiler() as ep:
        # ... run bench ...
        ...
    print(ep.summary())   # joules, avg watts, samples, duration

Backed by jetson-stats (jtop). Samples at ~10 Hz in a background thread.

If jtop is unavailable, the profiler degrades to a no-op and reports
zeros — so the rest of the bench still runs on dev machines.
"""
from __future__ import annotations
import threading, time, json
from typing import Optional, List, Dict


class EnergyProfiler:
    def __init__(self, sample_hz: float = 10.0, label: str = ""):
        self.dt = 1.0 / sample_hz
        self.label = label
        self.samples: List[Dict] = []
        self._stop = threading.Event()
        self._thr: Optional[threading.Thread] = None
        self._t_start = 0.0
        self._t_end = 0.0
        self._jtop = None
        self._available = False

    def __enter__(self):
        try:
            from jtop import jtop
            self._jtop = jtop()
            self._jtop.start()
            self._available = True
        except Exception as e:
            print(f"[EnergyProfiler] jtop unavailable ({e}); profiler is a no-op")
            return self
        self._t_start = time.perf_counter()
        self._thr = threading.Thread(target=self._loop, daemon=True)
        self._thr.start()
        return self

    def _loop(self):
        while not self._stop.is_set():
            try:
                p = self._jtop.power     # dict-like in newer jtop
                # Total board power in mW; try the common keys
                tot_mw = None
                if isinstance(p, dict):
                    tot = p.get("tot") or p.get("Total") or {}
                    if isinstance(tot, dict):
                        tot_mw = tot.get("power") or tot.get("avg")
                if tot_mw is None:
                    # Fallback: sum rail entries
                    rails = p.get("rail", p) if isinstance(p, dict) else {}
                    tot_mw = sum(
                        (r.get("power", 0) if isinstance(r, dict) else 0)
                        for r in (rails.values() if isinstance(rails, dict) else [])
                    )
                self.samples.append({
                    "t": time.perf_counter() - self._t_start,
                    "power_w": (tot_mw or 0) / 1000.0,
                })
            except Exception:
                pass
            time.sleep(self.dt)

    def __exit__(self, *a):
        if not self._available:
            return
        self._stop.set()
        if self._thr:
            self._thr.join(timeout=2)
        self._t_end = time.perf_counter()
        try:
            self._jtop.close()
        except Exception:
            pass

    def summary(self) -> Dict:
        if not self.samples:
            return {"available": False, "duration_s": 0, "joules": 0,
                    "avg_watts": 0, "peak_watts": 0, "n_samples": 0}
        ws = [s["power_w"] for s in self.samples]
        duration = self.samples[-1]["t"] - self.samples[0]["t"]
        # Trapezoidal integration for joules
        joules = 0.0
        for i in range(1, len(self.samples)):
            dt = self.samples[i]["t"] - self.samples[i-1]["t"]
            joules += 0.5 * (self.samples[i]["power_w"] + self.samples[i-1]["power_w"]) * dt
        return {
            "available": True,
            "label": self.label,
            "duration_s": duration,
            "joules": joules,
            "avg_watts": sum(ws) / len(ws),
            "peak_watts": max(ws),
            "min_watts": min(ws),
            "n_samples": len(ws),
        }
