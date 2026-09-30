import unittest
from concurrent.futures import Future, ThreadPoolExecutor
from threading import Event
from types import SimpleNamespace
from unittest.mock import Mock, patch

from edge.edge_client import EdgeClient
from edge.edge_client_lookahead import FixedLookaheadClient, _OverlappedVerifier


class LookaheadTests(unittest.TestCase):
    def setUp(self):
        self.client = FixedLookaheadClient()
        self.client._lookahead_eos = 99
        self.addCleanup(self.client._session.close)

    def pending(self, prefix, tokens):
        future = Future()
        future.set_result((tokens,[0.]*len(tokens),5.))
        event=dict(generated_tokens=0,reused_tokens=0,bridge_tokens=0,
                   discarded_tokens=0,unused_tokens=0,outcome='pending')
        self.client._pending=(prefix,future,event)
        return event

    def test_matching_bonus_reuses_only_continuation(self):
        event=self.pending([1,2,3],[4,5,6])
        self.assertEqual(self.client._take([1,2,3,4],2)[0],[5,6])
        self.assertEqual((event['bridge_tokens'],event['reused_tokens']),(1,2))

    def test_bonus_mismatch_discards_even_if_original_draft_matches(self):
        event=self.pending([1,2,3],[4,5,6])
        self.assertEqual(self.client._take([1,2,3,8],2)[0],[])
        self.assertEqual(event['discarded_tokens'],3)

    def test_rejection_inside_original_draft_invalidates_prefetch(self):
        event=self.pending([1,2,3],[4,5,6])
        self.assertEqual(self.client._take([1,8],2)[0],[])
        self.assertEqual(event['outcome'],'prefix_mismatch')

    def test_cached_eos_never_requests_more_tokens(self):
        self.pending([1,2],[3,99])
        with patch.object(EdgeClient,'draft') as draft:
            self.assertEqual(self.client.draft([1,2,3],4)[0],[99])
            draft.assert_not_called()

    def test_partial_reuse_fills_from_correct_extended_prefix(self):
        self.pending([1,2],[3,4])
        with patch.object(EdgeClient,'draft',return_value=([5,6],[0.,0.])) as draft:
            self.assertEqual(self.client.draft([1,2,3],3)[0],[4,5,6])
            draft.assert_called_once_with([1,2,3,4],2,0.)

    def test_terminal_drain_accounts_for_unused_work(self):
        event=self.pending([1,2],[3,4])
        self.client._take()
        self.assertEqual(event['unused_tokens'],2)
        self.assertIsNone(self.client._pending)

    def test_end_to_end_commits_only_verified_output_and_drains(self):
        self.client.tokenize=Mock(side_effect=lambda *args,**kwargs:[1])
        self.client.apply_chat_template=Mock(return_value='prompt')
        self.client.detokenize=Mock(return_value='verified output')
        def next_ids(prefix,count):
            result=[]
            for token in range(prefix[-1]+1,prefix[-1]+1+count):
                result.append(token if token < 7 else 99)
                if result[-1]==99:break
            return result
        def draft(client,prefix,count,temperature):
            ids=next_ids(prefix,count)
            return ids,[0.]*len(ids)
        def verify(prefix,ids,lps,**kwargs):
            self.assertEqual(ids,next_ids(prefix,len(ids)))
            decisions=[dict(accepted=True,strict_accepted=True,relaxed_only=False,
                quality_risk=0.,p_top1=1.,target_rank=1,probability_ratio=1.,logprob_regret=0.) for _ in ids]
            bonus=next_ids(prefix+ids,1)[0]
            return SimpleNamespace(accepted_ids=ids,n_accepted=len(ids),bonus_id=bonus,
                should_stop=bonus==99,verify_time_ms=1.,network_time_ms=1.,
                metadata=dict(quality_spent=0.,decisions=decisions,
                    timing=dict(network_rtt_ms=1.,cloud_verify_ms=1.,serialize_ms=0.,
                                deserialize_ms=0.,cloud_queue_ms=0.)))
        remote=Mock();remote.verify.side_effect=verify
        with patch.object(EdgeClient,'draft',draft):
            for h in (0,3):
                self.client.lookahead_tokens=h
                _,metrics=self.client.generate([],remote,gamma=2,max_tokens=20,
                    eos_id=99,strategy='strict',adaptive_window=False,fixed_k=1)
                self.assertEqual(metrics.output_ids,[2,3,4,5,6,99])
                self.assertIsNone(self.client._pending)
                self.assertIsNone(self.client._pool)
                if h:
                    self.assertEqual(metrics.lookahead['reused_tokens'],2)
                    self.assertEqual(metrics.lookahead['unused_tokens'],1)

    def test_verify_overlaps_outstanding_draft_and_forwards_policy(self):
        started,release=Event(),Event()
        def draft(prefix,count,temperature):
            started.set()
            if not release.wait(2):raise RuntimeError('Verifier did not run concurrently')
            return [4,5],[0.,0.]
        self.client._worker=Mock()
        self.client._worker.draft.side_effect=draft
        remote=Mock()
        def verify(*args,**kwargs):
            self.assertTrue(started.wait(2))
            release.set()
            return 'verified'
        remote.verify.side_effect=verify
        with ThreadPoolExecutor(max_workers=1) as pool:
            self.client._pool=pool
            proxy=_OverlappedVerifier(remote,self.client)
            proxy.policy={'strategy':'strict'}
            self.assertEqual(remote.policy,{'strategy':'strict'})
            self.assertEqual(proxy.verify([1],[2,3],[],eos_id=99),'verified')
            self.assertEqual(self.client._take([1,2,3,4],1)[0],[5])


if __name__=='__main__':
    unittest.main()
