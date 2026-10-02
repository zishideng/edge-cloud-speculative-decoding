"""Regression coverage for suite planning and honest completion reporting."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from experiments.suite import main
from experiments.run import create_output, write_json
from analysis.suite_report import report
from common.model_config import _find_yaml
from common.result_storage import compact_record


class SuiteTests(unittest.TestCase):
    def plan(self, *args):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(main(['--plan', *args]), 0)
        return json.loads(output.getvalue())

    def test_real_quick_and_simulation_scope(self):
        real = self.plan('--mode', 'real')
        self.assertEqual(real['expected_requests'], 48)
        self.assertEqual(real['methods'], ['A', 'B', 'Lookahead'])
        full = self.plan('--mode', 'real', '--profile', 'full')['methods']
        self.assertTrue(all(m in ['A', 'B', 'Lookahead'] or m.startswith('gamma_') for m in full))
        self.assertNotIn('Proposed', real['methods'])
        self.assertNotIn('Proposed', self.plan('--mode', 'real', '--profile', 'full')['methods'])
        sim = self.plan('--mode', 'simulate', '--profile', 'smoke')
        self.assertEqual(sim['expected_requests'], 2)
        self.assertNotIn('Lookahead', sim['methods'])

    def test_explicit_size_overrides_profile(self):
        p = self.plan('--n', '3', '--repeats', '1', '--gamma', '6')
        self.assertEqual(p['expected_requests'], 12)
        self.assertEqual(p['gamma'], 6)

    def test_paired_gamma_lookahead_sweep(self):
        plan = self.plan('--mode', 'real', '--gamma-lookahead-sweep', '2', '4', '6', '--repeats', '1')
        self.assertEqual(plan['expected_requests'], 48)
        self.assertEqual(plan['methods'], ['gamma_2', 'gamma_4', 'gamma_6', 'Lookahead_g2', 'Lookahead_g4', 'Lookahead_g6'])
        self.assertEqual(plan['lookahead_by_method'], {'Lookahead_g2': 3, 'Lookahead_g4': 5, 'Lookahead_g6': 7})

    def test_missing_registry_does_not_fall_back(self):
        with self.assertRaises(FileNotFoundError):
            _find_yaml('/nonexistent/model_registry.yaml')

    def test_failed_run_has_bilingual_incomplete_summary(self):
        with tempfile.TemporaryDirectory() as temp:
            root = create_output(temp)
            write_json(root/'config/plan.json', dict(mode='real', profile='quick',
                model_pair='test', scenarios=['low'], expected_requests=6))
            write_json(root/'report/suite_status.json', {'exit_code': 1})
            report(root)
            summary = (root/'SUMMARY.md').read_text()
            self.assertLess(summary.index('# 中文'), summary.index('# English'))
            self.assertIn('INCOMPLETE', summary)
            self.assertIn('不作真实加速结论', summary)
            self.assertFalse(json.loads((root/'report/summary.json').read_text())['complete'])

    def test_sweep_report_pairs_same_gamma(self):
        with tempfile.TemporaryDirectory() as temp:
            root = create_output(temp)
            methods = ['gamma_2', 'Lookahead_g2']
            write_json(root/'config/plan.json', dict(mode='real', profile='quick',
                model_pair='test', scenarios=['high'], expected_requests=4,
                methods=methods, lookahead_by_method={'Lookahead_g2': 3}))
            write_json(root/'report/suite_status.json', {'exit_code': 0})
            raw = root/'runs/test/raw'
            raw.mkdir(parents=True)
            for i in range(2):
                for method, speed in zip(methods, [10, 12]):
                    write_json(raw/f'{method}_{i}.json', dict(method=method, scenario='high',
                        request_index=i, repeat=0, tokens_per_second=speed, wall_time_s=10,
                        task_quality=1, truncated=False))
            report(root)
            result=json.loads((root/'report/summary.json').read_text())
            self.assertTrue(result['complete'])
            self.assertEqual(len(result['comparisons']), 1)
            self.assertAlmostEqual(result['comparisons'][0]['gain'], .2)
            self.assertEqual(result['comparisons'][0]['control'], 'gamma_2')
            self.assertIn('h=3', (root/'SUMMARY.md').read_text())
            self.assertTrue((root/'figures/throughput.png').exists())

    def test_compaction_preserves_raw_lookahead_evidence(self):
        raw = {'rounds': [], 'lookahead': {'generated_tokens': 5, 'events': [{'prefix': [1]}]}}
        compact = compact_record(raw)
        self.assertEqual(compact['lookahead'], {'generated_tokens': 5})
        self.assertEqual(len(raw['lookahead']['events']), 1)


if __name__ == '__main__':
    unittest.main()
