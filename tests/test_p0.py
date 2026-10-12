import tempfile
import unittest

from common.quality import evaluate_quality
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


if __name__ == '__main__':
    unittest.main()
