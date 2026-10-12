"""Quality > stability > speed. Controller state is isolated per request."""
from collections import deque
from statistics import mean
from common.window_estimator import WindowController


class JointController:
    def __init__(self, c, strategy='strict', adaptive_window=False, fixed_k=None):
        if strategy not in ('strict', 'fixed', 'adaptive'):
            raise ValueError('Unknown acceptance strategy')
        self.c, self.strategy = c, strategy
        self.k = 1 if strategy == 'strict' else (fixed_k if strategy == 'fixed' else c['K_INITIAL'])
        if self.k is None or not c['K_MIN'] <= self.k <= c['K_MAX']:
            raise ValueError('Invalid fixed K')
        self.spent, self.rounds = 0.0, 0
        self.window = WindowController(c, adaptive_window)
        self.quality = deque(maxlen=c['QUALITY_WINDOW_SIZE'])
        self.quality_evaluation = None

    def observe(self, row, decisions, spent):
        if spent < self.spent or spent > self.c['QUALITY_BUDGET']:
            raise ValueError('Server returned invalid cumulative quality budget')
        self.spent = spent
        self.rounds += 1
        self.quality.extend(decisions)
        self.window.observe(row)
        before = self.k
        risk = mean(d['quality_risk'] for d in self.quality) if self.quality else 1.0
        confidence = mean(d['p_top1'] for d in self.quality) if self.quality else 0.0
        rate = mean(d['accepted'] for d in self.quality) if self.quality else 0.0
        if self.rounds % self.c['QUALITY_EVAL_INTERVAL'] == 0:
            self.quality_evaluation = dict(round=self.rounds, mean_risk=risk,
                                          mean_confidence=confidence, acceptance=rate)
        reason = 'strict baseline' if self.strategy == 'strict' else 'fixed/cooldown'
        if self.spent >= self.c['QUALITY_BUDGET'] * self.c['BUDGET_TIGHTEN_FRACTION']:
            self.k, reason = 1, 'quality budget near exhaustion'
        elif self.strategy == 'adaptive':
            if risk >= self.c['RISK_TIGHTEN_THRESHOLD'] or confidence < self.c['MIN_TOP1_CONFIDENCE']:
                self.k = max(1, self.k-self.c['K_CHANGE_STEP'])
                reason = 'quality risk or low confidence; tighten K'
            elif self.rounds % self.c['K_UPDATE_INTERVAL'] == 0:
                if row['network_rtt_ms'] >= self.c['RTT_HIGH_MS'] and rate < self.c['TARGET_ACCEPTANCE_RATE']:
                    self.k = min(self.c['K_MAX'], self.k+self.c['K_CHANGE_STEP'])
                    reason = 'high RTT, sufficient quality budget; increase K'
        window = self.window.choose(hold=self.k != before)
        def projected_risk(k):
            # Replay observed candidates under the next K, applying the same
            # per-token constraints. This is an empirical proxy, not task loss.
            regrets=[]
            for d in self.quality:
                eligible=(d['target_rank'] is not None and d['target_rank'] <= k
                          and d['p_top1'] >= self.c['MIN_TOP1_CONFIDENCE']
                          and d['probability_ratio'] >= self.c['MIN_PROBABILITY_RATIO']
                          and d['logprob_regret'] <= self.c['MAX_LOGPROB_REGRET']
                          and self.spent+d['logprob_regret'] <= self.c['QUALITY_BUDGET'])
                regrets.append(d['quality_risk'] if eligible else 0.0)
            return mean(regrets) if regrets else None
        previous_risk, next_risk = projected_risk(before), projected_risk(self.k)
        return dict(next_k=self.k, next_gamma=window['gamma'], reason=reason,
                    quality_evaluation=self.quality_evaluation,
                    quality_risk=risk, quality_spent=self.spent,
                    predicted_quality_risk_change=next_risk-previous_risk if next_risk is not None else None,
                    risk_prediction_note='Empirical replay of recent candidates; normalized regret proxy, not predicted task accuracy',
                    predicted_throughput_change=window['predicted_gain'], window=window)
