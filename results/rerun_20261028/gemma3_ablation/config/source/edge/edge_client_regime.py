"""Latency-regime policy with complete-block reuse and strict verification.

Short verification intervals retain gamma4; long intervals may amortize
verification with gamma6/8. Partial prefetch blocks are deliberately excluded.
The backend probability-output ablation is configured by the experiment runner.
"""
from statistics import median
from collections import deque
import time

from common.window_estimator import expected_tokens
from edge.edge_client_lookahead import FixedLookaheadClient


class LatencyRegimeLookaheadClient(FixedLookaheadClient):
    def __init__(self, draft_url='http://localhost:8080', config=None, max_lookahead=10):
        super().__init__(draft_url, config, lookahead_tokens=0)
        if type(max_lookahead) is not int or max_lookahead < 5:
            raise ValueError('max_lookahead must be an integer >=5')
        self.max_lookahead = max_lookahead
        self._verify_history = deque(maxlen=16)
        self._outcomes = deque(maxlen=24)
        self._foreground_history = deque(maxlen=32)
        self._background_history = deque(maxlen=32)
        self._match_history = deque(maxlen=16)
        self._joint_current = (4,5)
        self._joint_round = 0
        self.joint_decisions = []
        self.lookahead_decisions = []

    def _fresh_draft(self, prompt, count, temperature):
        initial = not getattr(self, '_initial_prefill_seen', False)
        started = time.perf_counter()
        ids, lps = super()._fresh_draft(prompt, count, temperature)
        if not initial:
            self._foreground_history.append((len(ids),(time.perf_counter()-started)*1000))
        self._initial_prefill_seen = True
        return ids, lps

    def _verified(self, elapsed_ms):
        self._verify_history.append(elapsed_ms)

    def _consumed(self, event):
        if event['generated_tokens']:
            self._background_history.append((event['generated_tokens'],event['service_ms']))
        if event['outcome'] in ('reused','bridge_only','prefix_mismatch'):
            self._match_history.append(event['outcome']!='prefix_mismatch')

    def _verification_result(self, result):
        self._outcomes.append(dict(accepted=result.n_accepted,
            examined=len(result.metadata.get('decisions',[])),
            gamma=self._active_gamma,verify_ms=self._verify_history[-1]))

    def _choose_h(self, draft):
        h=min(self._selected_h,len(draft)+1,self.max_lookahead)
        self.lookahead_decisions.append(dict(round=len(self.lookahead_decisions),h=h,
            gamma=len(draft),reason=self.joint_decisions[-1]['reason']))
        return h

    def _choose_gamma(self, default, remaining):
        self._joint_round += 1
        candidates = []
        v = median(self._verify_history) if self._verify_history else None
        alpha = None
        if len(self._verify_history) < 4 or not self._background_history:
            selected, reason, regime = (min(4, remaining), 5), 'warmup with gamma4/h5', 'warmup'
        else:
            # Initial prompt prefill is compulsory in every arm and should not
            # be extrapolated as the marginal cost of later draft windows.
            warm_fg = list(self._foreground_history)
            bg_unit = median(t/n for n, t in self._background_history if n)
            fg_unit = median(t/n for n, t in warm_fg if n) if warm_fg else bg_unit
            b5 = 5*bg_unit
            regime = 'long' if v >= 1.75*b5 else 'short_or_medium'
            accepted = sum(x['accepted'] for x in self._outcomes)
            examined = sum(x['examined'] for x in self._outcomes)
            alpha = (accepted+8)/(examined+10)
            observed_p = (2+sum(self._match_history))/(4+len(self._match_history))
            base_g = median(x['gamma'] for x in self._outcomes)
            calibration = max(.75, min(1.25, observed_p/max(.01, alpha**(base_g+1))))
            windows = (4, 6, 8) if regime == 'long' else (4,)
            for g in windows:
                if g > remaining or g > self.config['GAMMA_MAX'] or g+1 > self.max_lookahead:
                    continue
                # Extra work is only justified with measured overlap headroom.
                # Reserve20% for cost-model error/cache-state variation.
                if g>4 and bg_unit*(g+1)>.8*v:
                    continue
                fg = fg_unit*g
                p = min(.99, alpha**(g+1)*calibration)
                # User constraint: keep drafting/prefetch enabled for every
                # useful nonterminal round, including very short intervals.
                for h in (g+1,):
                    bg = bg_unit*h
                    saving = p*fg if h else 0.
                    cycle = v+fg-saving+max(0., bg-v)
                    produced = expected_tokens(alpha, g)
                    candidates.append(dict(gamma=g, h=h,
                        predicted_tokens_per_second=1000*produced/cycle,
                        predicted_round_ms=cycle,
                        work_per_token_proxy=(cycle+.65*(fg+bg-saving))/produced,
                        predicted_full_prefix_match=p))
            if not candidates:
                selected, reason = (min(4, remaining), 0), 'terminal capacity'
            else:
                base = next(x for x in candidates if (x['gamma'], x['h']) == (4, 5))
                feasible = [x for x in candidates if x['work_per_token_proxy'] <= base['work_per_token_proxy']]
                best = max(feasible, key=lambda x:x['predicted_tokens_per_second'])
                old = next((x for x in candidates if (x['gamma'], x['h']) == self._joint_current), None)
                update = self._joint_round % 3 == 2 or old is None
                if update and (old is None or best['predicted_tokens_per_second'] > 1.03*old['predicted_tokens_per_second']):
                    selected, reason = (best['gamma'], best['h']), 'latency-regime complete-block cost selection'
                else:
                    selected, reason = self._joint_current, 'three-round cooldown and3% hysteresis'
        g, h = selected
        if remaining <= g+1:
            h = 0
        self._active_gamma = g
        self._selected_h = h
        self._joint_current = (g, h)
        self.joint_decisions.append(dict(round=self._joint_round-1, gamma=g, h=h,
            reason=reason, regime=regime, verify_ms=v, alpha=alpha, candidates=candidates))
        return g

    def generate(self, messages, verifier, **kwargs):
        if (kwargs.get('strategy')!='strict' or kwargs.get('adaptive_window',True)
                or kwargs.get('fixed_k')!=1):
            raise ValueError('Latency regimes require strictK1 without the legacy gamma controller')
        self._initial_prefill_seen = False
        for history in (self._verify_history,self._outcomes,self._foreground_history,
                        self._background_history,self._match_history):
            history.clear()
        self._joint_current=(4,5)
        self._joint_round=0
        self.joint_decisions=[]
        self.lookahead_decisions=[]
        text, metrics = super().generate(messages, verifier, **kwargs)
        metrics.lookahead.update(variant='latency_regime_complete_block',
            tokens=None,
            adaptive=True,adaptive_gamma=True,acceptance_k=1,
            decisions=self.lookahead_decisions,joint_decisions=self.joint_decisions,
            energy_model='fixed-weight work proxy; actual board energy measured separately',
            draft_probability_output=self.draft_n_probs,
            regime_note='Measured verification interval; no scenario-name or answer access')
        return text, metrics
