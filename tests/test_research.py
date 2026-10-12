import math
import unittest
from unittest.mock import Mock

from common.acceptance import accept_prefix
from common.experiment_config import load_config


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


if __name__ == '__main__':
    unittest.main()
