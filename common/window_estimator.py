"""Explainable synchronous throughput model; milliseconds in, tokens/s out."""
import math
from collections import deque
from statistics import mean


def expected_tokens(alpha, gamma):
    if not math.isfinite(alpha) or not 0 <= alpha <= 1 or type(gamma) is not int or gamma < 1:
        raise ValueError('alpha in [0,1], integer gamma >= 1 required')
    # Geometric sum avoids cancellation near alpha=1 and division by zero.
    return sum(alpha ** i for i in range(gamma + 1))


def estimate(alpha, draft_token_ms, rtt_ms, verify_fixed_ms, verify_token_ms, gamma_min, gamma_max):
    if gamma_min < 1 or gamma_max < gamma_min:
        raise ValueError('Invalid gamma range')
    values = (draft_token_ms, rtt_ms, verify_fixed_ms, verify_token_ms)
    if any(not math.isfinite(v) or v < 0 for v in values) or sum(values) == 0:
        raise ValueError('Invalid latency model')
    candidates = []
    for g in range(gamma_min, gamma_max + 1):
        ms = rtt_ms + verify_fixed_ms + (draft_token_ms + verify_token_ms) * g
        candidates.append(dict(gamma=g, predicted_tokens_per_second=1000 * expected_tokens(alpha, g) / ms,
                               predicted_round_ms=ms))
    return max(candidates, key=lambda x: x['predicted_tokens_per_second'])['gamma'], candidates


class WindowController:
    def __init__(self, config, adaptive=True):
        self.c, self.adaptive = config, adaptive
        self.gamma = config['GAMMA_INITIAL']
        self.rows = deque(maxlen=config['ESTIMATION_WINDOW_SIZE'])
        self.count = 0

    def observe(self, row):
        self.rows.append(row)
        self.count += 1

    def choose(self, hold=False):
        result = dict(gamma=self.gamma, candidates=[], reason='fixed window', predicted_gain=0.0)
        if not self.adaptive:
            return result
        if len(self.rows) < self.c['MIN_ESTIMATION_SAMPLES']:
            return result | {'reason': 'insufficient observations; initial window'}
        xs = [r['gamma'] for r in self.rows]
        ys = [r['cloud_verify_ms'] for r in self.rows]
        mx, my = mean(xs), mean(ys)
        variance = sum((x-mx)**2 for x in xs)
        # An unidentifiable slope is NOT fabricated from a single window.
        slope = max(0.0, sum((x-mx)*(y-my) for x,y in zip(xs,ys))/variance) if variance else 0.0
        intercept = max(0.0, my - slope * mx)
        n = sum(r['n_examined'] for r in self.rows)
        alpha = sum(r['n_accepted'] for r in self.rows) / max(1, n)
        rtts = [r['network_rtt_ms'] for r in self.rows]
        jump = len(rtts) > 1 and max(rtts[-1], mean(rtts[:-1])) > self.c['LATENCY_JUMP_RATIO'] * max(1e-6, min(rtts[-1], mean(rtts[:-1])))
        overhead = mean(r.get('serialize_ms',0)+r.get('deserialize_ms',0)+r.get('cloud_queue_ms',0) for r in self.rows)
        best, candidates = estimate(alpha, mean(r['draft_token_ms'] for r in self.rows),
                                    rtts[-1] if jump else mean(rtts), intercept + overhead, slope,
                                    self.c['GAMMA_MIN'], self.c['GAMMA_MAX'])
        old = next(v['predicted_tokens_per_second'] for v in candidates if v['gamma'] == self.gamma)
        peak = max(v['predicted_tokens_per_second'] for v in candidates)
        gain = peak / old - 1
        reason = 'hysteresis: predicted improvement too small'
        if hold:
            reason = 'K changed; hold window for stability'
        elif self.count % self.c['WINDOW_UPDATE_INTERVAL'] and not jump:
            reason = 'window update cooldown'
        elif gain > self.c['WINDOW_HYSTERESIS']:
            step = self.c['WINDOW_CHANGE_STEP']
            self.gamma += max(-step, min(step, best - self.gamma))
            reason = 'latency jump' if jump else 'maximum predicted throughput with step limit'
        chosen = next(v['predicted_tokens_per_second'] for v in candidates if v['gamma'] == self.gamma)
        return dict(gamma=self.gamma, estimated_best_gamma=best, candidates=candidates, reason=reason,
                    predicted_gain=chosen/old-1, alpha=alpha, verify_fixed_ms=intercept,
                    verify_token_ms=slope, fit_identifiable=bool(variance), model='synchronous; queue/codec in fixed overhead')
