from utils.config import config
from api.indexer import get_tokens_by_token_class

key = config['default']['key']
secret = config['default']['secret']


def test_get_tokens_by_token_class_uuid():
    token_class_uuid = '632c3c98-3804-4473-974b-202a9bdf0e54'
    r = get_tokens_by_token_class(
        key, secret, token_class_uuid)
    print(r.request.url)
    print(r.request.headers)
    print(r.json())
