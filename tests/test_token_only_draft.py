import json,unittest
from unittest.mock import Mock
from edge.edge_client import EdgeClient,TOKEN_ONLY_CHAT_PARSER

class TokenOnlyTests(unittest.TestCase):
 def test_fragment_content_cannot_replace_generated_ids(self):
  c=EdgeClient();self.addCleanup(c._session.close)
  c.token_only_parser=True
  response=Mock(ok=True)
  response.json.return_value={'content':'\ufffd 4','tokens':[115,220,19],'completion_probabilities':[{'id':115,'logprob':-.2},{'id':220,'logprob':-.1},{'id':19,'logprob':-.3}]}
  c._session.post=Mock(return_value=response)
  c.tokenize=Mock(side_effect=AssertionError('Generated tokens must not be retokenized'))
  ids,lps=c.draft([28,1717],3)
  self.assertEqual(ids,[115,220,19]);self.assertEqual(lps,[-.2,-.1,-.3])
  parser=json.loads(c._session.post.call_args.kwargs['json']['chat_parser'])
  self.assertEqual(parser['parsers'],[{'type':'epsilon'}])
  self.assertEqual(parser['root'],0)

 def test_formatting_flag_does_not_change_sampling_or_ids(self):
  c=EdgeClient();self.addCleanup(c._session.close)
  r=Mock(ok=True);r.json.return_value={'tokens':[11,12]};c._session.post=Mock(return_value=r)
  c.draft([1,2],2);ordinary=c._session.post.call_args.kwargs['json'].copy()
  c.token_only_parser=True;c.draft([1,2],2)
  token_only=c._session.post.call_args.kwargs['json'].copy()
  self.assertEqual(token_only.pop('chat_parser'),TOKEN_ONLY_CHAT_PARSER)
  self.assertEqual(token_only,ordinary)

if __name__=='__main__':unittest.main()
