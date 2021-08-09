from utils.config import config
from api.default import get_holder_by_token_uuid
from api.indexer import get_token_by_nft_type_args

key = config['default']['key']
secret = config['default']['secret']


def test_get_holder_address_by_token_uuid():
    token_uuid = config['default']['token_uuid']
    r = get_holder_by_token_uuid(key, secret, token_uuid)
    assert r.status_code == 200
    assert r.json()['address'] == config['default']['address']


def test_get_holder_address_by_token_type_args():
    nft_type_args = config['default']['nft_type_args']
    r = get_token_by_nft_type_args(key, secret, nft_type_args)
    assert r.status_code == 200
    assert r.json()[
        'token']['holder_address'] == config['default']['short_address']
