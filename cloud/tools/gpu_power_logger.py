#!/usr/bin/env python3
"""gpu_power_logger.py — 采样 RTX 3080 的功耗,补上 H200 版缺失的云端能耗测量。

原项目的 `src/energy_profiler.py` 只采 Jetson(jtop / INA3221),云端能耗从未
测过。要回答"系统级 J/token",必须同时拿到两侧的数据。本脚本是云端那一半。

两种用法:

1) CLI —— 边跑实验边记录,Ctrl-C 结束后打印汇总
       python gpu_power_logger.py --out results_3080/B_edge_power.csv

2) 上下文管理器 —— 嵌进 cloud/bench_one.py 之类的脚本里
       from gpu_power_logger import GpuPowerLogger
       with GpuPowerLogger(out_csv="A1_power.csv") as p:
           ...跑 benchmark...
       print(p.summary())

采样走 `nvidia-smi --query-gpu=...`,不依赖 NVML 的 Python 绑定。
消费级卡上报的是**整卡功耗**(不含主机其余部分),这一点在解读
"系统级 J/token" 时要记住 —— 主机功耗需要另外用插座式功率计测。
"""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import threading
import time
from typing import Dict, List, Optional

_QUERY = "power.draw,utilization.gpu,memory.used,temperature.gpu,clocks.sm"


class GpuPowerLogger:
    def __init__(self, sample_hz: float = 10.0, gpu_index: int = 0,
                 out_csv: Optional[str] = None, label: str = ""):
        self.dt = 1.0 / sample_hz
        self.gpu_index = gpu_index
        self.out_csv = out_csv
        self.label = label
        self.samples: List[Dict] = []
        self._stop = threading.Event()
        self._thr: Optional[threading.Thread] = None
        self._t0 = 0.0
        self._t1 = 0.0
        self._available = False

    # ------------------------------------------------------------------ #
    def _read_once(self) -> Optional[Dict]:
        try:
            out = subprocess.check_output(
                ["nvidia-smi", f"--id={self.gpu_index}",
                 f"--query-gpu={_QUERY}",
                 "--format=csv,noheader,nounits"],
                stderr=subprocess.DEVNULL, timeout=2.0,
            ).decode().strip()
        except Exception:
            return None
        parts = [p.strip() for p in out.split(",")]
        if len(parts) < 5:
            return None
        try:
            return {
                "t": time.perf_counter() - self._t0,
                "power_w": float(parts[0]),
                "util_pct": float(parts[1]),
                "mem_used_mib": float(parts[2]),
                "temp_c": float(parts[3]),
                "sm_clock_mhz": float(parts[4]),
            }
        except ValueError:
            return None

    def _loop(self):
        while not self._stop.is_set():
            s = self._read_once()
            if s is not None:
                self.samples.append(s)
            time.sleep(self.dt)

    # ------------------------------------------------------------------ #
    def __enter__(self):
        self._t0 = time.perf_counter()
        probe = self._read_once()
        if probe is None:
            print("[GpuPowerLogger] nvidia-smi 不可用,退化为 no-op")
            return self
        self._available = True
        self.samples.append(probe)
        self._thr = threading.Thread(target=self._loop, daemon=True)
        self._thr.start()
        return self

    def __exit__(self, *exc):
        self._stop.set()
        if self._thr is not None:
            self._thr.join(timeout=2.0)
        self._t1 = time.perf_counter()
        if self.out_csv and self.samples:
            self.write_csv(self.out_csv)
        return False

    # ------------------------------------------------------------------ #
    def write_csv(self, path: str):
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(self.samples[0].keys()))
            w.writeheader()
            w.writerows(self.samples)

    def summary(self) -> Dict:
        """梯形积分求总能量。"""
        if not self._available or len(self.samples) < 2:
            return {"available": False, "joules": 0.0, "avg_watts": 0.0,
                    "duration_s": 0.0, "n_samples": len(self.samples)}
        j = 0.0
        for a, b in zip(self.samples, self.samples[1:]):
            j += 0.5 * (a["power_w"] + b["power_w"]) * (b["t"] - a["t"])
        dur = self.samples[-1]["t"] - self.samples[0]["t"]
        pw = [s["power_w"] for s in self.samples]
        ut = [s["util_pct"] for s in self.samples]
        # 占空比:GPU 利用率 > 5% 的采样点占比。边云 SD 下 3080 大部分时间在等
        # Jetson 的草稿,这个数字直接说明"云端被 offload 了多少"。
        duty = sum(1 for u in ut if u > 5.0) / len(ut)
        return {
            "available": True,
            "label": self.label,
            "joules": round(j, 2),
            "avg_watts": round(j / dur, 2) if dur > 0 else 0.0,
            "peak_watts": round(max(pw), 2),
            "idle_watts_p10": round(sorted(pw)[len(pw) // 10], 2),
            "avg_util_pct": round(sum(ut) / len(ut), 1),
            "busy_duty_cycle": round(duty, 3),
            "duration_s": round(dur, 2),
            "n_samples": len(self.samples),
        }


# ---------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="记录 GPU 功耗直到 Ctrl-C")
    ap.add_argument("--out", required=True, help="输出 CSV 路径")
    ap.add_argument("--hz", type=float, default=10.0)
    ap.add_argument("--gpu", type=int, default=0)
    ap.add_argument("--label", default="")
    ap.add_argument("--duration", type=float, default=None,
                    help="秒;不给则一直记录到 Ctrl-C")
    args = ap.parse_args()

    print(f"采样 GPU {args.gpu} @ {args.hz} Hz → {args.out}")
    print("Ctrl-C 结束\n")
    with GpuPowerLogger(args.hz, args.gpu, args.out, args.label) as p:
        try:
            if args.duration:
                time.sleep(args.duration)
            else:
                while True:
                    time.sleep(1.0)
                    if len(p.samples) % 100 < 10 and p.samples:
                        s = p.samples[-1]
                        print(f"\r  {s['t']:7.1f}s  {s['power_w']:6.1f} W  "
                              f"util {s['util_pct']:5.1f}%  {s['temp_c']:.0f}°C",
                              end="", flush=True)
        except KeyboardInterrupt:
            print("\n停止采样")

    s = p.summary()
    print("\n" + json.dumps(s, indent=2, ensure_ascii=False))
    side = args.out.rsplit(".", 1)[0] + "_summary.json"
    with open(side, "w") as f:
        json.dump(s, f, indent=2)
    print(f"\n汇总 → {side}")
    if s.get("available"):
        print(f"\n提示:busy_duty_cycle={s['busy_duty_cycle']} "
              f"表示 3080 只有这么大比例的时间在真正干活。")
        print("     边云 SD 下这个值应该很低(约 0.25),它就是'云端被 offload'的直接证据。")


if __name__ == "__main__":
    main()
