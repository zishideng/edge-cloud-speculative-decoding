import json
import math
import unittest
from statistics import median
from concurrent.futures import Future
from unittest.mock import MagicMock, patch

from common.experiment_config import load_config
from common.pipeline_model import choose_windows
from edge.edge_client import EdgeClient
from edge.edge_client_adaedl import AdaEDLClient, entropy_lower_bound
from edge.edge_client_pipeline import POSITION_HISTORY, MarkovPipelineClient, position_curve
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
        with self.assertRaises(ValueError):
            choose_windows([1., .9, .95] + [.5] * 8, .8, 100, 10, 25, 0, 2.3, 8)

    def test_geometric_curve_matches_rate(self):
        curve = [.8 ** i for i in range(11)]
        self.assertEqual(choose_windows(curve, curve, 250, 10, 25, 0, 2.3, 8),
                         choose_windows(.8, .8, 250, 10, 25, 0, 2.3, 8))

    def test_rising_position_acceptance_prefers_longer_windows(self):
        rising, curve = [.72, .74, .77, .79, .84, .84, .87, .87, .87, .87], [1.]
        for rate in rising:
            curve.append(curve[-1] * rate)
        alpha = sum(curve[1:9]) / sum(curve[:8])  # same per-token acceptance
        flat = choose_windows(alpha, alpha, 215, 10, 12.7, 0, 2.3, 8)
        shaped = choose_windows(curve, curve, 215, 10, 12.7, 0, 2.3, 8)
        self.assertGreater(shaped['fresh_gamma'] + shaped['lookahead'],
                           flat['fresh_gamma'] + flat['lookahead'])


class PositionCurveTests(unittest.TestCase):
    def test_empty_history_is_geometric(self):
        curve = position_curve([], .7, .8, 6)
        for k, value in enumerate(curve):
            self.assertAlmostEqual(value, .7 ** k)

    def test_shape_follows_history_and_level_follows_local_rate(self):
        # first position accepted half the time, later positions always
        history = [(4, 0), (4, 4)] * 200
        curve = position_curve(history, .8, .8, 5)
        rates = [b / a for a, b in zip(curve, curve[1:])]
        self.assertLess(rates[0], rates[1])
        self.assertTrue(all(0 < v < 1 for v in curve[1:]))

    def test_unseen_positions_keep_last_rate(self):
        curve = position_curve([(2, 2)] * 100 + [(2, 0)] * 100, .6, .8, 7)
        rates = [b / a for a, b in zip(curve, curve[1:])]
        self.assertAlmostEqual(rates[-1], rates[-2], places=6)


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

    def test_uncapped_lookahead_follows_round_trip(self):
        c = MarkovPipelineClient(config=dict(self.c.config, GAMMA_MAX=32), energy_weight=0.,
                                 fresh_max=8, lookahead_max=32)
        self.addCleanup(c._session.close)
        c._verify_history.extend([220.]*3)
        c._background_history.extend([(9, 10+9*13.8)]*3)
        c._choose_gamma(4, 512)
        self.assertGreater(c._planned_h, 9)          # beyond the old cap
        self.assertLess(c._planned_h, 32)            # bounded by the round trip, not the search range
        self.assertLessEqual(c.fresh_gamma, 8)

    def test_position_model_records_history_across_requests(self):
        POSITION_HISTORY.pop('unit', None)
        c = MarkovPipelineClient(config=self.c.config, acceptance_model='position', history_key='unit')
        c._prev_full = False
        c._verification_result(result(2, 4))
        again = MarkovPipelineClient(config=self.c.config, acceptance_model='position', history_key='unit')
        self.assertEqual(list(again._position_history[False]), [(4, 2)])
        again._choose_gamma(8, 100)
        self.assertEqual(len(again._choice['survival_miss']), self.c.config['GAMMA_MAX'] + 2)
        POSITION_HISTORY.pop('unit', None)

    def test_fit_cost_model_recovers_intercept_and_uses_mean_round_trip(self):
        c = MarkovPipelineClient(config=self.c.config, cost_model='fit')
        for n in (2, 3, 5, 9, 2, 9):
            c._consumed(dict(generated_tokens=n, service_ms=14 + 10 * n))
        call, token = c._draft_cost()
        self.assertAlmostEqual(call, 14, places=6)
        self.assertAlmostEqual(token, 10, places=6)
        for ms in (30, 30, 30, 90):
            c._verified(ms)
        self.assertEqual(c._verify_estimate(), 45)

    def test_mean_cost_model_keeps_rare_stalls(self):
        c = MarkovPipelineClient(config=self.c.config, cost_model='mean')
        for ms in [30] * 60 + [300] * 4:
            c._verified(ms)
        self.assertAlmostEqual(c._verify_estimate(), (30 * 60 + 300 * 4) / 64)
        self.assertEqual(c._draft_cost(), (c.call_overhead_ms, c.token_ms))

    def test_robust_cost_model_tracks_level_and_keeps_tail(self):
        c = MarkovPipelineClient(config=self.c.config, cost_model='robust')
        for ms in [30, 30, 30, 30, 30, 130] * 10:       # level 30 ms, one 100 ms stall in six
            c._verified(ms)
        self.assertAlmostEqual(c._verify_estimate(), 30 + 100 / 6, delta=2)
        for ms in [200] * 5:                            # delay jumps: level follows within 5 rounds
            c._verified(ms)
        self.assertGreater(c._verify_estimate(), 200)

    def test_robust_estimate_stays_positive_after_delay_drop(self):
        c = MarkovPipelineClient(config=self.c.config, cost_model='robust')
        for ms in [120] * 6 + [20] * 3:
            c._verified(ms)
        self.assertGreaterEqual(c._verify_estimate(), 20)

    def test_fresh_min_floor_excludes_single_token_rounds(self):
        free = MarkovPipelineClient(config=self.c.config, cost_model='robust')
        floor = MarkovPipelineClient(config=self.c.config, cost_model='robust', fresh_min=2)
        for c in (free, floor):
            for ms in [35] * 10:                        # low delay: the free model picks one-token rounds
                c._verified(ms)
            c._background_history.extend([(2, 49.0)] * 8)
            c._choose_gamma(4, 512)
        self.assertEqual((free.fresh_gamma, free._planned_h), (1, 2))
        self.assertGreaterEqual(floor.fresh_gamma, 2)
        self.assertGreaterEqual(floor._planned_h, 3)
        with self.assertRaises(ValueError):
            MarkovPipelineClient(config=self.c.config, fresh_min=0)

    def test_distribution_overlap_prices_heavy_tail(self):
        from common.pipeline_model import choose_windows
        samples = [35.0] * 9 + [200.0]                  # median 35 ms, mean 51.5 ms
        point = choose_windows(.87, .87, sum(samples) / len(samples), 10, 20, 0, 2.3, 8)
        dist = choose_windows(.87, .87, samples, 10, 20, 0, 2.3, 8)
        self.assertEqual((point['fresh_gamma'], point['lookahead']), (1, 2))
        self.assertNotEqual((dist['fresh_gamma'], dist['lookahead']), (1, 2))
        self.assertEqual(choose_windows(.87, .87, [50.0], 10, 20, 0, 2.3, 8),
                         choose_windows(.87, .87, 50.0, 10, 20, 0, 2.3, 8))

    def test_dist_cost_model_shifts_samples_to_current_level(self):
        c = MarkovPipelineClient(config=self.c.config, cost_model='dist')
        self.assertEqual(c._verify_estimate(), c.verify_prior_ms)
        for ms in [30, 30, 30, 30, 30, 130] * 10:
            c._verified(ms)
        est = c._verify_estimate()
        self.assertEqual(len(est), 55)
        self.assertEqual(median(est), 30)
        for ms in [200] * 5:                            # delay jump: the whole distribution moves up
            c._verified(ms)
        self.assertGreaterEqual(min(c._verify_estimate()), 100)
        for ms in [20] * 5:                             # delay drop: samples stay nonnegative
            c._verified(ms)
        self.assertGreaterEqual(min(c._verify_estimate()), 0)
        c._background_history.extend([(2, 49.0)] * 8)
        c._choose_gamma(4, 512)
        self.assertIsInstance(c.pipeline_decisions, list)

    def test_pipesd_nav_trigger_uses_cumulative_and_single_thresholds(self):
        from edge.edge_client_baselines import PipeSDClient
        c = PipeSDClient(config=dict(self.c.config, GAMMA_MAX=16), r1=0.5, r2=0.3)
        lp = math.log
        self.assertIsNone(c._nav_trigger([lp(.9), lp(.9), lp(.9)]))      # cumulative .73
        self.assertEqual(c._nav_trigger([lp(.9), lp(.8), lp(.6)]), 2)     # .9*.8*.6 = .43 <= .5
        self.assertEqual(c._nav_trigger([lp(.95), lp(.2)]), 1)            # single token <= .3
        with self.assertRaises(ValueError):
            PipeSDClient(config=self.c.config, r1=0, r2=.5)

    def test_pipesd_continues_one_stream_across_verification(self):
        import threading
        from edge.edge_client_baselines import PipeSDClient
        c = PipeSDClient(config=dict(self.c.config, GAMMA_MAX=16), r1=0.1, r2=0.3)
        lp = math.log
        tokens = [(10, lp(.9)), (11, lp(.2)), (12, lp(.9)), (13, lp(.9)), (14, lp(.25))]

        class Stream:
            prefix, cancel, closed = [1, 2], threading.Event(), False
            def get(self, i): return tokens[i] if i < len(tokens) else None
            def available(self): return len(tokens)
            def close(self): self.closed = True

        stream = Stream()
        c._stream, c._windows, c._budget, c._produced, c._lookahead_eos = stream, [], 100, 0, 99
        self.assertEqual(c.draft([1, 2], 16)[0], [10, 11])              # NAV fires on p=.2
        self.assertEqual(c.draft([1, 2, 10, 11, 12], 16)[0], [13, 14])  # bonus 12 matched: continue
        self.assertFalse(stream.closed)
        self.assertEqual([w['restarted'] for w in c._windows], [False, False])
        self.assertIsNone(c._follows(stream, [1, 2, 10, 7]))              # rejection: restart

    def test_hf_default_confidence_threshold_refit(self):
        from types import SimpleNamespace
        from edge.edge_client_baselines import HFDefaultClient, roc_threshold
        self.assertEqual(roc_threshold([.9, .8, .3, .2], [1, 1, 0, 0]), .8)
        self.assertEqual(roc_threshold([.9, .2], [0, 1]), .2)
        c = HFDefaultClient(config=dict(self.c.config, GAMMA_MAX=20))
        self.assertEqual(c._choose_gamma(4, 512), 20)
        c._threshold, c._probs, c._matches, c._trace, c._sent = .4, [.9, .95, .8, .3], [], [], 4
        c._verification_result(SimpleNamespace(n_accepted=2))
        self.assertEqual((c._probs, c._matches), ([.9, .95, .8], [1, 1, 0]))
        c._probs += [.99, .7, .6]; c._sent = 3
        c._verification_result(SimpleNamespace(n_accepted=3))
        self.assertEqual(c._matches, [1, 1, 0, 1, 1, 1])
        self.assertEqual(c._threshold, .6)                                # cost fpr 1 + fnr 0

    def test_pearl_is_lossless_and_switches_modes(self):
        from types import SimpleNamespace
        from unittest import mock
        import edge.edge_client_baselines as baselines
        prompt = [1, 2, 3]
        target = list(range(100, 140))                      # the target's greedy continuation
        wrong = {105, 112, 113, 120}                         # positions where the draft disagrees

        def draft_from(prefix, count, _t=0.0):
            start = len(prefix) - len(prompt)
            seq = prefix[len(prompt):]
            if seq != target[:start]:
                return [7] * count, [0.0] * count             # off the target path: all wrong
            return [target[i] if target[i] not in wrong else 7 for i in range(start, start+count)], [0.0]*count

        class Worker:
            def __init__(self, *_): self._session = mock.Mock()
            def draft(self, prefix, count, t=0.0): return draft_from(prefix, count)

        flips = []

        def verify(prompt_ids, draft_ids, *_a, **_k):
            truth = (prompt + target)[len(prompt_ids):len(prompt_ids)+len(draft_ids)+1]
            if len(draft_ids) == 1 and not flips and len(prompt_ids) > 15:
                flips.append(1)                               # one near-tie flip of the anchor
                truth = [-1] + truth[1:]
            n = 0
            while n < len(draft_ids) and draft_ids[n] == truth[n]:
                n += 1
            dec = [dict(strict_accepted=i < n, relaxed_only=False, accepted=i < n, quality_risk=0.0, p_top1=1.0,
                        target_rank=1 if i < n else 2, probability_ratio=1.0, logprob_regret=0.0)
                   for i in range(min(n+1, len(draft_ids)))]
            return SimpleNamespace(accepted_ids=draft_ids[:n], n_accepted=n, bonus_id=truth[n], should_stop=False,
                                   verify_time_ms=1.0, network_time_ms=0.0,
                                   metadata=dict(timing={}, decisions=dec, quality_spent=0.0))

        c = baselines.PEARLClient(config=self.c.config, gamma=3)
        c.tokenize = lambda *a, **k: list(prompt)
        c.apply_chat_template = lambda m: ''
        c.detokenize = lambda ids: ''
        c.draft = lambda ids, n, t=0.0: draft_from(list(ids), n)
        with mock.patch.object(baselines, 'EdgeClient', Worker):
            _, m = c.generate([], SimpleNamespace(verify=verify, policy=None), max_tokens=30, eos_id=999)
        self.assertEqual(m.output_ids, target[:30])
        modes = [s['mode'] for s in m.lookahead['steps']]
        self.assertEqual(modes[0], 'post')
        self.assertIn('pre', modes)
        self.assertTrue(any(s['continued'] for s in m.lookahead['steps']))
        self.assertTrue(all(r['n_proposed'] == 0 for r in m.rounds if r['pearl_mode'] == 'pre'))
        self.assertEqual(sum(r['pearl_anchor_rejected'] for r in m.rounds), 1)

    def test_pre_verify_sends_anchor_and_returns_only_the_next_token(self):
        from edge.edge_client_pipeline import MarkovPipelineClient
        from edge.verifier import VerifyResult
        c = MarkovPipelineClient(config=self.c.config, cost_model='dist', pre_verify=True)
        c._anchor, c._anchor_rejections, calls = True, 0, []

        class Remote:
            def verify(self, prompt, draft, *a, **k):
                calls.append((list(prompt), list(draft)))
                ok = draft == [9]
                return VerifyResult(accepted_ids=draft[:ok], n_accepted=int(ok), bonus_id=42, bonus_is_correction=not ok,
                                    should_stop=False, verify_time_ms=1.0, network_time_ms=1.0,
                                    metadata=dict(timing={}, decisions=[{}], n_draft=1, quality_spent=0.0))

        r = c._remote_verify(Remote(), [1, 2, 9], [9], [0.0], temperature=0.0, eos_id=5)
        self.assertEqual(calls, [([1, 2], [9])])             # the last verified token is the anchor
        self.assertEqual((r.accepted_ids, r.n_accepted, r.bonus_id), ([], 0, 42))
        self.assertEqual((r.metadata['n_draft'], r.metadata['decisions']), (0, []))
        self.assertTrue(r.metadata['timing']['pre_verify'] and not c._anchor)
        c._anchor = True
        c._fresh_draft = lambda prompt, n, t: ([7], [0.0])
        Remote.verify = lambda self, prompt, draft, *a, **k: VerifyResult(
            accepted_ids=[], n_accepted=0, bonus_id=13, bonus_is_correction=True, should_stop=False,
            verify_time_ms=1.0, network_time_ms=1.0, metadata=dict(timing={}, decisions=[{}], quality_spent=0.0))
        r = c._remote_verify(Remote(), [1, 2, 9], [9], [0.0], temperature=0.0, eos_id=5)
        self.assertEqual((r.bonus_id, c._anchor_rejections), (13, 1))   # fallback: one normal token
        self.assertEqual(choose_windows(.7, .8, 40, 10, 20, 0, 2.3, 8, fresh_options=range(0, 9))['fresh_gamma'], 0)

    def test_hf_heuristic_schedule(self):
        from types import SimpleNamespace
        from edge.edge_client_baselines import HFHeuristicClient
        c = HFHeuristicClient(config=dict(self.c.config, GAMMA_MAX=16))
        c._n, c._trace = 5, []
        result = lambda sent, acc: SimpleNamespace(metadata={'n_draft': sent}, n_accepted=acc)
        c._verification_result(result(5, 5)); self.assertEqual(c._n, 7)
        c._verification_result(result(7, 3)); self.assertEqual(c._n, 6)
        c._n = 1; c._verification_result(result(1, 0)); self.assertEqual(c._n, 1)
        c._n = 30; self.assertEqual(c._choose_gamma(4, 512), 16)

    def test_picospec_interrupts_background_draft_on_rejection(self):
        import threading
        from edge.edge_client_baselines import PicoSpecClient
        c = PicoSpecClient(config=self.c.config)
        c.lookahead_events = []
        for prompt, interrupted in (([1, 2, 3, 9, 9], True), ([1, 2, 3, 4, 5, 6], False)):
            future = Future(); future.set_result(([6, 7], [0.0, 0.0], 5.0))
            event = dict(outcome='pending', interrupted=False)
            c._cancel = threading.Event()
            c._pending = ([1, 2, 3, 4, 5], future, event)       # context [1,2,3] + draft [4,5]
            c._take(prompt, 4)
            self.assertEqual(c._cancel.is_set(), interrupted)
            self.assertEqual(event['interrupted'], interrupted)

    def test_dynamic_delay_schedule_is_deterministic(self):
        from experiments.progress_probe import dynamic_segments
        spec = dict(levels=[2, 100], mean_dwell_ms=1500, horizon_ms=20000)
        a, b = dynamic_segments(spec, 'k'), dynamic_segments(spec, 'k')
        self.assertEqual(a, b)
        self.assertTrue(all(d in (2, 100) for _, d in a))
        self.assertTrue(all(x[1] != y[1] for x, y in zip(a, a[1:])))
        self.assertGreaterEqual(a[-1][0], 20000)

    def test_fit_cost_model_falls_back_without_length_variation(self):
        c = MarkovPipelineClient(config=self.c.config, cost_model='fit')
        for _ in range(5):
            c._consumed(dict(generated_tokens=2, service_ms=40))
        self.assertEqual(c._draft_cost(), (c.call_overhead_ms, 15.0))

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
                                        'markov', 'markov_w0', 'markov_w05',
                                        'markov_w0_nocap', 'markov_w05_nocap',
                                        'markov_w0_pos', 'markov_w05_pos', 'markov_w0_fit', 'markov_w05_fit',
                                        'markov_w0_mean', 'markov_w05_mean',
                                        'markov_w0_robust', 'markov_w05_robust',
                                        'markov_w0_floor2', 'markov_w05_floor2',
                                        'markov_w0_dist', 'markov_w05_dist', 'markov_w0_fresh4', 'markov_w0_pre', 'markov_w05_pre', 'markov_w025_pre', 'markov_w1_pre', 'markov_w2_pre',
                                        'picospec', 'pipesd', 'hf_heuristic', 'hf_default', 'pearl'})
        self.assertEqual(draft_n_probs('adaedl'), 20)
        self.assertEqual(draft_n_probs('markov'), 0)
        self.assertEqual(draft_n_probs('hf_default'), 1)


if __name__ == '__main__':
    unittest.main()
