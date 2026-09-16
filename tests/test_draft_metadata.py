import unittest
from types import SimpleNamespace
from unittest.mock import Mock
import requests
from common.model_config import get_draft_vocab


class DraftMetadataTests(unittest.TestCase):
    def client(self, props):
        return SimpleNamespace(draft_url='http://edge:8080', props=Mock(return_value=props))

    def test_supported_layouts(self):
        for props in ({'n_vocab':128256}, {'model_meta':{'n_vocab':128256}},
                      {'model':{'n_vocab':128256}}, {'default_generation_settings':{'n_vocab':128256}}):
            self.assertEqual(get_draft_vocab(self.client(props),required=True),128256)

    def test_v1_models_layout(self):
        client = self.client({'endpoint_props': False})
        client.models = Mock(return_value={
            'data': [{'meta': {'n_vocab': 128256}}],
        })
        self.assertEqual(get_draft_vocab(client, required=True), 128256)

    def test_connection_error_preserves_cause(self):
        client=self.client({})
        client.props.side_effect=requests.ConnectionError('connection refused')
        with self.assertRaisesRegex(RuntimeError, 'http://edge:8080/props') as caught:
            get_draft_vocab(client,required=True)
        self.assertIsInstance(caught.exception.__cause__,requests.ConnectionError)

    def test_missing_metadata_is_not_loading_failure(self):
        with self.assertRaisesRegex(RuntimeError,'metadata compatibility'):
            get_draft_vocab(self.client({'chat_template':'template'}),required=True)

    def test_missing_or_invalid_vocab_never_uses_config_value(self):
        for value in (None,0,-1,True,'128256'):
            self.assertIsNone(get_draft_vocab(self.client({'n_vocab':value})))


if __name__ == '__main__': unittest.main()
