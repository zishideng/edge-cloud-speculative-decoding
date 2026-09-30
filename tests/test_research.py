import math
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

from common.acceptance import accept_prefix
from common.experiment_config import load_config
from experiments.strict_diagnostic import first_difference


class StrictTieTests(unittest.TestCase):
    def test_k1_rejects_noncanonical_tied_rank_one(self):
        c = load_config()
        dist = {20: {'rank': 1, 'logprob': math.log(.4)},
                10: {'rank': 1, 'logprob': math.log(.4)}}
        accepted, correction, decisions, spent = accept_prefix([dist], [20], k=1, config=c)
        self.assertEqual(accepted, [])
        self.assertEqual(correction, 10)
        self.assertFalse(decisions[0]['accepted'])
        self.assertEqual(spent, 0)
        # Relaxed K=2 can accept the tied alternative, with truthful telemetry.
        accepted, _, decisions, _ = accept_prefix([dist], [20], k=2, config=c)
        self.assertEqual(accepted, [20])
        self.assertTrue(decisions[0]['relaxed_only'])
        # Budget tightening to K=1 must obey exactly the same strict semantics.
        accepted, correction, _, _ = accept_prefix([dist], [20], k=2, config=c,
                                                  spent=c['QUALITY_BUDGET'])
        self.assertEqual((accepted, correction), ([], 10))


class DifferentialTests(unittest.TestCase):
    def test_greedy_draft_without_probability_telemetry(self):
        from edge.edge_client_smart import SmartEdgeClient
        from common.experiment_config import validate
        c = load_config()
        c['DRAFT_N_PROBS'] = 0
        client = SmartEdgeClient(config=validate(c))
        response = Mock(ok=True)
        response.json.return_value = {'tokens':[10,20]}
        client._session = Mock()
        client._session.post.return_value = response
        ids, logprobs = client.draft([1,2],2,0.0)
        self.assertEqual(ids,[10,20])
        self.assertEqual(logprobs,[0.0,0.0])
        payload = client._session.post.call_args.kwargs['json']
        self.assertEqual(payload['n_probs'],0)
        self.assertEqual(payload['samplers'],['top_k'])
        self.assertEqual(payload['top_k'],1)
        for invalid in (True,-1,2,'0'):
            with self.assertRaisesRegex(ValueError,'DRAFT_N_PROBS'):
                validate(dict(c,DRAFT_N_PROBS=invalid))

    def test_difference_includes_length_and_eos(self):
        self.assertIsNone(first_difference([1, 2], [1, 2]))
        self.assertEqual(first_difference([1, 2], [1, 3]), 1)
        self.assertEqual(first_difference([1, 2], [1, 2, 9]), 2)
        self.assertEqual(first_difference([], [1]), 0)


class CloudARBaselineTests(unittest.TestCase):
    def test_paired_latency_reduction_sign_and_cloud_control(self):
        from analysis.paired import paired_comparisons
        records=[]
        for prompt in [0,1]:
            for method,wall in [('cloud_AR',2),('Proposed',1)]:
                records.append(dict(mode='real',scenario='low',method=method,request_index=prompt,
                                    repeat=0,wall_time_s=wall,tokens_per_second=10/wall,task_quality=1))
        rows=paired_comparisons(records,draws=100)
        latency=next(r for r in rows if r['metric']=='wall_time_s')
        self.assertEqual(latency['baseline'],'cloud_AR')
        self.assertEqual(latency['mean'],.5)
        self.assertEqual(latency['effect'],'relative_latency_reduction')

    def test_ar_is_fresh_and_nonstreaming_metrics_are_missing(self):
        from edge.experiment_live import LiveExperiment
        from experiments.run import enrich
        live = LiveExperiment.__new__(LiveExperiment)
        live.c = load_config()
        live.model = {'eos_id': 99}
        live.reference = Mock(return_value=([10,99], 'Final answer: 18'))
        live.reference_stops = {0:'eos'}
        live.client = Mock()
        live.client.apply_chat_template.return_value = 'template'
        live.client.tokenize.return_value = [1,2]
        live.client.detokenize.return_value = 'Final answer: 18'
        response = Mock(content=b'{"token_ids":[10,99]}')
        response.json.return_value = {'token_ids':[10,99], 'stop_reason':'eos', 'generate_time_ms':1.0}
        session = Mock()
        session.post.return_value = response
        live.remote = SimpleNamespace(base='http://target', _session=session)
        with patch('edge.experiment_live.time.sleep') as sleep:
            for _ in range(2):
                r = enrich(live.run_cloud_ar({'question':'6*3', 'gold_answer':'18'},0,{'rtt_ms':100}))
                self.assertEqual(r['task_quality'],1)
                self.assertIsNone(r['ttft_ms'])
                self.assertIsNone(r['tpot_ms'])
                self.assertIsNone(r['strict_acceptance_rate'])
                self.assertEqual(r['ar_timing']['injected_network_ms'],100)
            self.assertEqual(session.post.call_count,2)
            self.assertEqual(sleep.call_args_list[0].args,(.1,))
        with self.assertRaisesRegex(ValueError,'queue injection'):
            live.run_cloud_ar({},0,{'rtt_ms':0,'queue_ms':20})


if __name__ == '__main__':
    unittest.main()
