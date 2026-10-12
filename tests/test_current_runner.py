"""Exercise all current dispatch paths without model or power-sensor access."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from edge.experiment_live import LiveExperiment
from experiments.adaptive_research import METHODS, parser, run_phase


class FakeProfiler:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def record(self, tokens):
        return dict(available=True, source='unit-test', scope='jetson_board',
                    sample_hz=1, joules=5., joules_per_token=5. / max(1, tokens),
                    samples=[dict(t=0., power_w=5.), dict(t=1., power_w=5.)])


class FakeLive(LiveExperiment):
    def __init__(self):
        self.client = SimpleNamespace(draft_n_probs=1, token_only_parser=True,
                                      props=Mock(return_value={'n_vocab':128256}),
                                      _session=Mock())
        self.remote = SimpleNamespace(_session=Mock())
        self.info = {}
        self.model = {'eos_id':99, 'stop_strings':[]}
        self.reference_stops = {0:'eos'}
        self.observed = []
        self.reference = Mock(return_value=([7,99], 'Final answer: 7'))

    def energy_profiler(self):
        return FakeProfiler()

    def run(self, strategy, adaptive_window, gamma, k, example, index, scenario):
        self.observed.append((strategy, adaptive_window, gamma, k,
                              self.client.draft_n_probs, self.client.config['K_MAX']))
        self.client.last_lookahead = dict(backend_settings={
            kind:{'n_probs':self.client.draft_n_probs}
            for kind in ('foreground','background')})
        return dict(rounds=[], output_ids=[7,99], reference_ids=[7,99],
                    output_text='Final answer: 7', reference_text='Final answer: 7',
                    reference_quality=1., task_quality=1., truncated=False,
                    wall_time_s=1., output_tokens=2, energy=FakeProfiler().record(2))


class CurrentRunnerTests(unittest.TestCase):
    def test_defaults_select_only_current_methods(self):
        self.assertEqual(METHODS, ('fixed','fixed_fast','regime'))
        self.assertEqual(parser().parse_args([]).methods, list(METHODS))
        with contextlib.redirect_stderr(io.StringIO()):
            for retired in ('buffered','streaming','joint','original'):
                with self.assertRaises(SystemExit):
                    parser().parse_args(['--methods',retired])

    def test_all_current_methods_complete_and_preserve_probability_controls(self):
        with tempfile.TemporaryDirectory() as temp:
            dataset = Path(temp)/'dataset.jsonl'
            dataset.write_text(json.dumps({'question':'What is seven?', 'gold_answer':'7'})+'\n')
            args = parser().parse_args([
                '--phase','offline_dispatch_test','--indices','0',
                '--dataset',str(dataset),'--output-root',str(Path(temp)/'results'),
                '--compact-target-logprobs'])
            live = FakeLive()
            def construct(config):
                live.c = config
                return live
            with patch('edge.experiment_live.LiveExperiment',side_effect=construct), \
                 patch('experiments.adaptive_research.ServiceLocks'), \
                 patch('experiments.adaptive_research.hardware_snapshot',return_value={}), \
                 patch('experiments.adaptive_research.source_snapshot'), \
                 patch('experiments.adaptive_research.time.sleep'), \
                 contextlib.redirect_stdout(io.StringIO()):
                directory = run_phase(args)
            result = json.loads((directory/'results.json').read_text())
            self.assertTrue(result['complete'])
            self.assertEqual(result['completed_requests'],6)
            self.assertEqual(live.reference.call_count,1)
            self.assertEqual({item[:4] for item in live.observed}, {('strict',False,4,1)})
            self.assertEqual({item[4:] for item in live.observed}, {(1,4),(0,1)})
            raw = [json.loads(p.read_text()) for p in (directory/'raw').glob('*.json')]
            self.assertEqual({r['method'] for r in raw}, set(METHODS))
            self.assertTrue(all(r['energy_validation']['valid'] for r in raw))
            for r in raw:
                self.assertEqual(r['configured_draft_n_probs'],1 if r['method']=='fixed' else 0)
                self.assertEqual(r['configured_target_probability_cap'],4 if r['method']=='fixed' else 1)


if __name__ == '__main__':
    unittest.main()
