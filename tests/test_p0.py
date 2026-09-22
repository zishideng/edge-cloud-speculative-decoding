import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from common.quality import evaluate_quality, first_divergence
from edge.experiment_live import LiveExperiment
from experiments.isolation import ServiceLocks


class QualityTests(unittest.TestCase):
    def test_quality_diagnostics(self):
        gold = {'gold_answer': '42'}
        for text, stop, status, score in [
            ('working...', 'length', 'incomplete', 0),
            ('answer is forty two', 'eos', 'answer_not_extracted', 0),
            ('Final answer: 41', 'eos', 'incorrect', 0),
            ('Final answer: 42', 'length', 'correct', 1),
        ]:
            result = evaluate_quality('gsm8k', text, gold, stop)
            self.assertEqual(result['quality_status'], status)
            self.assertEqual(result['task_quality'], score)
            self.assertEqual(result['truncated'], stop == 'length')
        self.assertIsNone(evaluate_quality('humaneval', 'code', {}, 'eos')['task_quality'])

    def test_first_divergence_including_length(self):
        self.assertIsNone(first_divergence([1, 2], [1, 2]))
        self.assertEqual(first_divergence([1, 2], [1, 3]), 1)
        self.assertEqual(first_divergence([1, 2], [1]), 1)
        self.assertEqual(first_divergence([], [1]), 0)


class LockTests(unittest.TestCase):
    def test_shared_endpoint_and_release(self):
        with tempfile.TemporaryDirectory() as directory:
            first = ServiceLocks(['http://127.0.0.1:8080', 'http://127.0.0.1:9090'], 'one', directory).acquire()
            second = ServiceLocks(['http://localhost:8080/', 'http://127.0.0.1:9091'], 'two', directory)
            try:
                with self.assertRaisesRegex(RuntimeError, 'already used'):
                    second.acquire()
                self.assertFalse(second.handles)
            finally:
                first.close()
            second.acquire(); second.close()
            # Files intentionally persist; stale metadata must not block a run.
            first.acquire(); first.close()

    def test_disjoint_services_can_run(self):
        with tempfile.TemporaryDirectory() as directory:
            first = ServiceLocks(['http://127.0.0.1:8080'], 'one', directory).acquire()
            second = ServiceLocks(['http://127.0.0.1:8081'], 'two', directory).acquire()
            first.close(); second.close()


class PreflightTests(unittest.TestCase):
    def live(self):
        live = object.__new__(LiveExperiment)
        live.c = {'GAMMA_SWEEP': [1, 2, 4, 8], 'GAMMA_INITIAL': 2}
        return live

    def test_mismatch_persists_evidence_and_stops(self):
        live = self.live()
        live.run = Mock(return_value=dict(strict_consistent=False, output_ids=[2], reference_ids=[1]))
        live.diagnose = Mock(return_value={'position': 0, 'windows': []})
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RuntimeError, 'differs'):
                live.preflight([{'question': 'q'}], directory)
            self.assertEqual(live.run.call_count, 1)
            self.assertEqual(json.loads((Path(directory)/'strict_0_gamma_1.diagnostic.json').read_text())['position'], 0)

    def test_diagnostic_failure_does_not_erase_sequence(self):
        live = self.live()
        live.run = Mock(return_value=dict(strict_consistent=False, output_ids=[2], reference_ids=[1]))
        live.diagnose = Mock(side_effect=RuntimeError('network error'))
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RuntimeError, 'differs'):
                live.preflight([{}], directory)
            self.assertTrue((Path(directory)/'strict_0_gamma_1.json').exists())
            self.assertIn('network error', (Path(directory)/'strict_0_gamma_1.diagnostic.json').read_text())

    def test_pass_checks_all_windows_and_caps_prompts(self):
        live = self.live()
        live.run = Mock(return_value=dict(strict_consistent=True, output_ids=[1], reference_ids=[1]))
        with tempfile.TemporaryDirectory() as directory:
            result = live.preflight([{}]*5, directory)
            self.assertEqual(result['prompts'], 4)
            self.assertEqual(live.run.call_count, 16)

    def test_diagnosis_uses_identical_prefix_for_both_endpoints(self):
        live = self.live()
        live.c['REQUEST_TIMEOUT_S'] = 1
        live.c['TASK'] = 'gsm8k'
        live.model = {'eos_id': 99}
        live.client = Mock()
        live.client.tokenize.return_value = [10]
        live.client.draft.return_value = ([7], [])
        response = Mock()
        response.json.return_value = {'token_ids': [2]}
        live.remote = SimpleNamespace(base='http://cloud', _session=Mock())
        live.remote._session.post.return_value = response
        result = live.diagnose({'question': 'q'}, [1, 2], [1, 3])
        self.assertEqual(result['position'], 1)
        for call in live.remote._session.post.call_args_list:
            self.assertEqual(call.kwargs['json']['prompt_ids'], [10, 1])


class PairedTests(unittest.TestCase):
    def test_repeats_are_clustered_and_missing_pairs_excluded(self):
        from analysis.paired import paired_comparisons
        rows=[]
        for prompt in (0, 1):
            for repeat in (0, 1):
                for method, speed in [('A', 10), ('Proposed', 12)]:
                    rows.append(dict(scenario='low', request_index=prompt, repeat=repeat,
                                     method=method, tokens_per_second=speed, task_quality=1, mode='real'))
        rows.append(dict(rows[-1], request_index=99))
        comparison = paired_comparisons(rows, draws=100)[0]
        self.assertEqual(comparison['prompt_count'], 2)
        self.assertEqual(comparison['pair_count'], 4)
        self.assertAlmostEqual(comparison['ci95_low'], .2)
        for row in rows:
            row['mode'] = 'simulate'
        self.assertIsNone(paired_comparisons(rows, draws=100)[0]['ci95_low'])


class PipelineTests(unittest.TestCase):
    def run_fake_suite(self, directory, consistent):
        import copy
        from experiments.run import main
        from common.experiment_config import load_config
        from common.simulation import run_simulation
        overrides = dict(N_REQUESTS=1, MAX_TOKENS=8, REPEATS=1,
                         GAMMA_SWEEP=[1], K_SWEEP=[1], NETWORK_SCENARIOS={'low':{'rtt_ms':0}})
        path = Path(directory)/'config.json'
        path.write_text(json.dumps(overrides))
        config = load_config(path)
        record = run_simulation(config, 'strict', False, 2, 1, 0, {'rtt_ms':0})
        record.update(evaluate_quality('gsm8k', 'unfinished', {'gold_answer':'1'}, 'length'))
        record.update(reference_quality=0, reference_truncated=True, reference_answer_extracted=False,
                      strict_consistent=consistent)
        live = Mock()
        live.info = {}; live.preflight.return_value = {'passed':True}
        live.run.side_effect = lambda *args: copy.deepcopy(record)
        with patch('edge.experiment_live.LiveExperiment', return_value=live), \
             patch('experiments.run.ServiceLocks'), \
             patch('experiments.run.environment_snapshot', return_value={}), \
             patch('experiments.run.subprocess.run', return_value=SimpleNamespace(returncode=0, stdout='', stderr='')), \
             patch.dict('sys.modules', {'analysis.make_figures': SimpleNamespace(make_figures=Mock())}):
            result = main(['--mode','real','--config',str(path),'--output-root',directory])
        return result, live

    def test_timed_mismatch_stops_and_preserves_raw(self):
        with tempfile.TemporaryDirectory() as directory:
            result, live = self.run_fake_suite(directory, False)
            self.assertEqual(result, 1)
            self.assertEqual(live.run.call_count, 1)
            self.assertEqual(len(list(Path(directory).glob('*/raw/*.json'))), 1)
            status = json.loads(next(Path(directory).glob('*/report/status.json')).read_text())
            self.assertEqual(status['successful_requests'], 0)

    def test_quality_report_exposes_zero_reference_and_truncation(self):
        with tempfile.TemporaryDirectory() as directory:
            result, live = self.run_fake_suite(directory, True)
            self.assertEqual(result, 0)
            report = next(Path(directory).glob('*/report/report.md')).read_text()
            self.assertIn('参照未取得任何正确答案', report)
            self.assertIn('答案提取率', report)
            csv = next(Path(directory).glob('*/tables/requests.csv')).read_text()
            self.assertIn('quality_status', csv)
            self.assertIn('reference_truncated', csv)


    def test_preflight_failure_prevents_timed_jobs(self):
        from experiments.run import main
        live = Mock()
        live.info = {'target_model': 'fake'}
        live.preflight.side_effect = RuntimeError('strict mismatch')
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory)/'config.json'
            config.write_text(json.dumps({'N_REQUESTS':1, 'MAX_TOKENS':16}))
            with patch('edge.experiment_live.LiveExperiment', return_value=live), \
                 patch('experiments.run.ServiceLocks'), \
                 patch('experiments.run.environment_snapshot', return_value={}), \
                 patch('experiments.run.subprocess.run', return_value=SimpleNamespace(returncode=0, stdout='', stderr='')):
                self.assertEqual(main(['--mode','real','--config',str(config),'--output-root',directory]), 1)
            live.run.assert_not_called()
            status = json.loads(next(Path(directory).glob('*/report/status.json')).read_text())
            self.assertEqual(status['successful_requests'], 0)
            self.assertIn({'stage':'strict_consistency','exit_code':1}, status['checks'])


if __name__ == '__main__':
    unittest.main()
