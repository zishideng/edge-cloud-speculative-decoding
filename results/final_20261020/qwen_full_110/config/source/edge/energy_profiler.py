"""Sample Jetson board input power; integrate watts over monotonic time.

Prefer the INA3221 VDD_IN rail (mV * mA / 1e6 -> W), then jtop's
explicit total. Never sum overlapping rails. Missing measurements are null.
This is gross board energy, including idle power, not cloud or wall energy.
"""
from __future__ import annotations

import math
from pathlib import Path
import socket
import threading
import time
from urllib.parse import urlsplit


def local_draft_url(url):
    """Only attribute runner power to a draft service on this host."""
    try:
        addresses = socket.getaddrinfo(urlsplit(url).hostname, None, type=socket.SOCK_STREAM)
        for family, kind, protocol, _, address in addresses:
            try:
                with socket.socket(family, kind, protocol) as probe:
                    probe.bind(address)
                return True
            except OSError:
                continue
    except (OSError, ValueError, TypeError):
        pass
    return False


class EnergyProfiler:
    def __init__(self, sample_hz=10.0, label='', disabled_reason=None):
        if not math.isfinite(sample_hz) or sample_hz <= 0:
            raise ValueError('sample_hz must be positive and finite')
        self.dt = 1.0 / sample_hz
        self.label = label
        self.disabled_reason = disabled_reason
        self.samples = []
        self._stop = threading.Event()
        self._thr = None
        self._jtop = None
        self._reader = None
        self._t_start = self._t_end = 0.0
        self.started_at_unix = None
        self.source = None
        self.reason = disabled_reason
        self.read_errors = 0

    def _select_reader(self):
        for label in sorted(Path('/sys/bus/i2c/drivers/ina3221').glob('*/hwmon/hwmon*/in*_label')):
            if label.read_text().strip() != 'VDD_IN':
                continue
            channel = label.name[2:-6]
            voltage = label.with_name(f'in{channel}_input')
            current = label.with_name(f'curr{channel}_input')
            def read(voltage=voltage, current=current):
                return float(voltage.read_text()) * float(current.read_text()) / 1e6
            read()  # Check access before starting the measured interval.
            self.source = f'ina3221:{label.parent}:VDD_IN'
            return read
        from jtop import jtop
        self._jtop = jtop(interval=self.dt)
        self._jtop.start()
        def read():
            power = self._jtop.power
            total = power.get('tot', power.get('Total', {}))
            value = total.get('power')  # Instantaneous mW; never substitute an average.
            if value is None:
                raise ValueError('jtop total board power unavailable')
            return float(value) / 1000.0
        read()
        self.source = 'jtop:total_board_power'
        return read

    def _sample(self, timestamp=None):
        try:
            watts = self._reader()
            if not math.isfinite(watts) or watts <= 0:
                raise ValueError('Invalid board input power')
            self.samples.append(dict(t=time.perf_counter()-self._t_start if timestamp is None else timestamp,
                                     power_w=watts))
        except Exception as exc:
            self.read_errors += 1
            self.reason = f'Power read failed: {exc}'

    def __enter__(self):
        if self.disabled_reason:
            return self
        self.samples = []
        self._stop.clear()
        self.read_errors = 0
        self.reason = None
        try:
            self._reader = self._select_reader()
            self.started_at_unix = time.time()
            self._t_start = time.perf_counter()
            self._sample(0.0)
            self._thr = threading.Thread(target=self._loop, daemon=True)
            self._thr.start()
        except Exception as exc:
            self.reason = f'Board power unavailable: {exc}'
            self._close()
        return self

    def _loop(self):
        while not self._stop.wait(self.dt):
            self._sample()

    def _close(self):
        if self._jtop is not None:
            try:
                self._jtop.close()
            except Exception:
                pass
            self._jtop = None

    def __exit__(self, *exc):
        self._stop.set()
        if self._thr is not None:
            self._thr.join()
            self._sample()
            self._t_end = time.perf_counter()
        self._close()
        return False

    def summary(self):
        result = dict(available=False, label=self.label, scope='jetson_board', source=self.source,
                      started_at_unix=self.started_at_unix,
                      reason=self.reason, duration_s=None, joules=None, avg_watts=None,
                      peak_watts=None, min_watts=None, n_samples=len(self.samples),
                      read_errors=self.read_errors, sample_hz=1/self.dt)
        if len(self.samples) < 2 or self.read_errors or self.reason:
            result['reason'] = self.reason or 'Insufficient power samples'
            return result
        duration = self.samples[-1]['t'] - self.samples[0]['t']
        gaps = [b['t']-a['t'] for a,b in zip(self.samples, self.samples[1:])]
        if duration <= 0 or max(gaps) > max(1.0, 5*self.dt):
            result['reason'] = 'Incomplete power sampling coverage'
            return result
        joules = sum((a['power_w']+b['power_w'])*0.5*(b['t']-a['t'])
                     for a,b in zip(self.samples, self.samples[1:]))
        watts = [s['power_w'] for s in self.samples]
        result.update(available=True, reason=None, duration_s=duration, joules=joules,
                      avg_watts=joules/duration, peak_watts=max(watts), min_watts=min(watts))
        return result

    def record(self, output_tokens):
        result = self.summary()
        result['joules_per_token'] = (result['joules']/output_tokens
                                     if result['available'] and output_tokens > 0 else None)
        result['samples'] = list(self.samples)
        return result
