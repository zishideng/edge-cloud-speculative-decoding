import json
import math
import unittest
from concurrent.futures import Future
from unittest.mock import MagicMock, patch

from common.experiment_config import load_config
from common.pipeline_model import choose_windows
from edge.edge_client import EdgeClient
from edge.edge_client_adaedl import AdaEDLClient, entropy_lower_bound
from edge.edge_client_pipeline import MarkovPipelineClient
from experiments.progress_probe import METHODS, draft_n_probs


def result(n, sent):
    return type('R', (), dict(n_accepted=n, metadata=dict(n_draft=sent)))()


class PipelineModelTests(unittest.TestCase):
    def choose(self, alpha, verify, weight=0.):
        return choose_windows(alpha, alpha, verify, 10., 25., weight, 2.3, 8)

    def test_long_verification_uses_longer_lookahead(self):
        self.assertGreater(self.choose(.85, 400)['lookahead'], self.choose(.85, 60)['lookahead'])

    def test_energy_weight_shortens_low_acceptance_lookahead(self):
        self.assertLess(self.choose(.5, 300, 1.)['lookahead'], self.choose(.5, 300, 0.)['lookahead'])

    def test_high_acceptance_prefers_longer_fresh_window_when_verification_is_slow(self):
        self.assertGreater(self.choose(.95, 400)['fresh_gamma'], self.choose(.5, 60)['fresh_gamma'])

    def test_invalid_inputs_rejected(self):
        with self.assertRaises(ValueError):
            choose_windows(1., .5, 100, 10, 25, 0, 2.3, 8)


class MarkovClientTests(unittest.TestCase):
    def setUp(self):
        self.c = MarkovPipelineClient(config=load_config('configs/research.pilot.json'))
        self.c._lookahead_eos = 99
        self.c._remaining = 512
        self.addCleanup(self.c._session.close)

    def pending(self, prefix, tokens):
        future = Future()
        future.set_result((tokens, [0.]*len(tokens), 5.))
        event = dict(generated_tokens=0, reused_tokens=0, bridge_tokens=0,
                     discarded_tokens=0, unused_tokens=0, outcome='pending')
        self.c._pending = (prefix, future, event)

    def test_miss_drafts_fresh_window(self):
        self.c.fresh_gamma = 2
        with patch.object(EdgeClient, 'draft', return_value=([5, 6], [0., 0.])) as draft:
            self.assertEqual(self.c.draft([1, 2, 3], 8)[0], [5, 6])
            draft.assert_called_once_with([1, 2, 3], 2, 0.)

    def test_hit_sends_all_reusable_tokens_without_foreground_call(self):
        self.pending([1, 2], [3, 4, 5, 6, 7])
        with patch.object(EdgeClient, 'draft') as draft:
            self.assertEqual(self.c.draft([1, 2, 3], 8)[0], [4, 5, 6, 7])
            draft.assert_not_called()

    def test_short_hit_is_topped_up_to_fresh_window(self):
        self.c.fresh_gamma = 2
        self.pending([1, 2], [3, 4])
        with patch.object(EdgeClient, 'draft', return_value=([5], [0.])) as draft:
            self.assertEqual(self.c.draft([1, 2, 3], 8)[0], [4, 5])
            draft.assert_called_once_with([1, 2, 3, 4], 1, 0.)

    def test_acceptance_is_tracked_by_previous_round_state(self):
        self.c._verification_result(result(4, 4))   # after miss, full accept
        self.c._verification_result(result(1, 4))   # after full, one accepted then rejected
        self.assertAlmostEqual(self.c._alpha(False), (8+4)/(10+4))
        self.assertAlmostEqual(self.c._alpha(True), (8+1)/(10+2))

    def test_round_plan_sets_fresh_window_and_lookahead(self):
        self.c._verify_history.extend([400.]*3)
        self.assertEqual(self.c._choose_gamma(4, 512), self.c.config['GAMMA_MAX'])
        self.assertGreaterEqual(self.c._planned_h, 2)
        self.assertEqual(self.c._choose_h([1, 2]), self.c._planned_h)
        self.c._remaining = 3
        self.assertEqual(self.c._choose_h([1, 2]), 0)

    def test_estimates_use_recent_medians(self):
        self.c._verify_history.extend([100., 90., 1000., 80.])
        self.assertEqual(self.c._verify_estimate(), 90.)
        self.c._background_history.extend([(2, 10+2*30.), (4, 10+4*20.), (3, 10+3*25.)])
        self.assertEqual(self.c._token_cost(), 25.)


def stream(entries, stop_after=None):
    lines = []
    for token, logprobs in entries:
        top = [dict(id=token+i, logprob=lp) for i, lp in enumerate(logprobs)]
        lines.append(b'data: ' + json.dumps(dict(completion_probabilities=[
            dict(id=token, logprob=logprobs[0], top_logprobs=top)], stop=False)).encode())
    response = MagicMock()
    response.iter_lines.return_value = iter(lines)
    response.__enter__.return_value = response
    return response


class AdaEDLTests(unittest.TestCase):
    def setUp(self):
        self.c = AdaEDLClient(config=load_config('configs/research.pilot.json'))
        self.c._lambda, self.c._ar, self.c._rounds, self.c._last_sent = .5, None, [], 0
        self.addCleanup(self.c._session.close)

    def test_entropy_counts_residual_mass(self):
        self.assertAlmostEqual(entropy_lower_bound([math.log(.5), math.log(.5)]), math.log(2))
        self.assertAlmostEqual(entropy_lower_bound([math.log(.5)]), math.log(2))

    def test_stops_before_low_bound_token_and_keeps_first(self):
        sure, unsure = [math.log(.99)], [math.log(.3), math.log(.3), math.log(.3)]
        self.assertGreater(self.c.stop_bound(sure), .5)
        self.assertLess(self.c.stop_bound(unsure), .5)
        with patch.object(self.c._session, 'post', return_value=stream([(1, unsure), (2, sure)])):
            self.assertEqual(self.c._fresh_draft([0], 8, 0.)[0], [1, 2])
        with patch.object(self.c._session, 'post', return_value=stream([(1, sure), (2, sure), (3, unsure), (4, sure)])):
            self.assertEqual(self.c._fresh_draft([0], 8, 0.)[0], [1, 2])

    def test_threshold_follows_paper_update(self):
        self.c._rounds.append({})
        self.c._verification_result(result(1, 4))     # AR .25 < alpha: raise lambda
        self.assertAlmostEqual(self.c._lambda, .9*.5 + .1*(.5+.01))
        self.c._ar = .95
        self.c._rounds.append({})
        before = self.c._lambda
        self.c._verification_result(result(4, 4))     # AR >= alpha, n_acc != L(8): lower lambda
        self.assertAlmostEqual(self.c._lambda, .9*before + .1*(before-.01))


class RunnerTests(unittest.TestCase):
    def test_method_set_and_probability_settings(self):
        self.assertEqual(set(METHODS), {'fixed_fast', 'fixed_g2', 'fixed_g8', 'sync_g4', 'adaedl',
                                        'markov', 'markov_w0', 'markov_w05'})
        self.assertEqual(draft_n_probs('adaedl'), 20)
        self.assertEqual(draft_n_probs('markov'), 0)


if __name__ == '__main__':
    unittest.main()
