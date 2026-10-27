"""Critical-path-aware lookahead with a two-state window controller.

Freshly drafted tokens delay the verification request; lookahead tokens are
drafted while the previous verification is in flight. Each round the client
chooses the fresh window and the lookahead length from a two-state (prefetch
hit/miss) model (common.pipeline_model) using online estimates of
state-dependent acceptance, verification round trip and draft token cost.
On a prefetch hit every reusable token is sent. Strict K=1 verification and
complete-prefix reuse checks are unchanged.
"""
from collections import deque
from statistics import median

from common.pipeline_model import choose_windows
from edge.edge_client_lookahead import FixedLookaheadClient


class MarkovPipelineClient(FixedLookaheadClient):
    """energy_weight trades time against Jetson board energy (0 = speed only);
    energy_ratio is draft-active power over base board power (about
    10.0 W / 4.3 W on the Orin Nano 25 W mode, fitted from measured requests).
    """

    def __init__(self, draft_url='http://localhost:8080', config=None, energy_weight=0.25,
                 energy_ratio=2.3, call_overhead_ms=10.0, token_ms=24.5, verify_prior_ms=150.0,
                 acceptance_prior=(8, 10)):
        super().__init__(draft_url, config, lookahead_tokens=0)
        if energy_weight < 0 or energy_ratio < 0:
            raise ValueError('Energy weight and ratio must be nonnegative')
        self.energy_weight = energy_weight
        self.energy_ratio = energy_ratio
        self.call_overhead_ms = call_overhead_ms
        self.token_ms = token_ms
        self.verify_prior_ms = verify_prior_ms
        self.acceptance_prior = acceptance_prior
        self.fresh_gamma = 2
        self._verify_history = deque(maxlen=3)
        self._background_history = deque(maxlen=16)
        self._rounds = deque(maxlen=32)
        self._prev_full = False
        self._planned_h = 0
        self._last_sent = 0
        self.pipeline_decisions = []

    def _alpha(self, after_full):
        accepted, examined = self.acceptance_prior
        for state, gamma, n in self._rounds:
            if state == after_full:
                accepted += n
                examined += n + (n < gamma)
        return min(.99, accepted / examined)

    def _verify_estimate(self):
        return median(self._verify_history) if self._verify_history else self.verify_prior_ms

    def _token_cost(self):
        samples = [(t-self.call_overhead_ms)/n for n, t in self._background_history if n]
        return max(5.0, median(samples)) if samples else self.token_ms

    def _choose_gamma(self, default, remaining):
        # The returned gamma is only an upper bound: draft() sends all
        # reusable prefetched tokens or a fresh window of self.fresh_gamma.
        self._remaining = remaining
        verify = self._verify_estimate()
        alphas = self._alpha(False), self._alpha(True)
        choice = choose_windows(*alphas, verify, self.call_overhead_ms, self._token_cost(),
                                self.energy_weight, self.energy_ratio, self.config['GAMMA_MAX'])
        self.fresh_gamma = choice['fresh_gamma']
        self._planned_h = choice['lookahead']
        self._choice = dict(choice, alpha_miss=alphas[0], alpha_hit=alphas[1], verify_ms=verify,
                            token_ms=self._token_cost(), after_full=self._prev_full)
        return min(self.config['GAMMA_MAX'], remaining)

    def draft(self, prompt_ids, gamma, temperature=0.0):
        cached, lps = self._take(prompt_ids, gamma)
        if self._lookahead_eos in cached:
            end = cached.index(self._lookahead_eos)+1
            cached, lps = cached[:end], lps[:end]
        else:
            target = max(len(cached), min(self.fresh_gamma, gamma))
            if len(cached) < target:
                rest, rest_lps = self._fresh_draft(list(prompt_ids)+cached, target-len(cached), temperature)
                cached += rest
                lps += rest_lps
        self._last_sent = len(cached)
        return cached, lps

    def _verified(self, elapsed_ms):
        self._verify_history.append(elapsed_ms)

    def _consumed(self, event):
        if event['generated_tokens']:
            self._background_history.append((event['generated_tokens'], event['service_ms']))

    def _choose_h(self, draft):
        after = self._remaining - len(draft) - 1
        h = 0 if after <= 0 else min(self._planned_h, after+1)
        self.pipeline_decisions.append(dict(self._choice, round=len(self.pipeline_decisions),
                                            gamma=len(draft), h=h))
        return h

    def _verification_result(self, result):
        sent = result.metadata.get('n_draft', self._last_sent)
        self._rounds.append((self._prev_full, sent, result.n_accepted))
        self._prev_full = result.n_accepted == sent

    def generate(self, messages, verifier, **kwargs):
        if (kwargs.get('strategy') != 'strict' or kwargs.get('adaptive_window', True)
                or kwargs.get('fixed_k') != 1):
            raise ValueError('Pipeline lookahead requires strictK1 without the legacy gamma controller')
        for history in (self._verify_history, self._background_history, self._rounds):
            history.clear()
        self._prev_full = False
        self.pipeline_decisions = []
        self._remaining = kwargs.get('max_tokens', 512)
        text, metrics = super().generate(messages, verifier, **kwargs)
        metrics.lookahead.update(variant='markov_pipeline', tokens=None, adaptive=True,
                                 adaptive_gamma=True, acceptance_k=1, decisions=self.pipeline_decisions,
                                 energy_weight=self.energy_weight, energy_ratio=self.energy_ratio,
                                 draft_probability_output=self.draft_n_probs)
        return text, metrics
