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
        self.assertEqual(real['expected_requests'], 80)
        self.assertIn('Lookahead', real['methods'])
        self.assertNotIn('Proposed', real['methods'])
        self.assertNotIn('Proposed', self.plan('--mode', 'real', '--profile', 'full')['methods'])
        sim = self.plan('--mode', 'simulate', '--profile', 'smoke')
        self.assertEqual(sim['expected_requests'], 4)
        self.assertNotIn('Lookahead', sim['methods'])

    def test_explicit_size_overrides_profile(self):
        p = self.plan('--n', '3', '--repeats', '1', '--gamma', '6')
        self.assertEqual(p['expected_requests'], 24)
        self.assertEqual(p['gamma'], 6)

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

    def test_compaction_preserves_raw_lookahead_evidence(self):
        raw = {'rounds': [], 'lookahead': {'generated_tokens': 5, 'events': [{'prefix': [1]}]}}
        compact = compact_record(raw)
        self.assertEqual(compact['lookahead'], {'generated_tokens': 5})
        self.assertEqual(len(raw['lookahead']['events']), 1)


if __name__ == '__main__':
    unittest.main()
