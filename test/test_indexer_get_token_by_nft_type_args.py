from utils.config import config
from indexer import get_token_by_nft_type_args

key = config['default']['key']
secret = config['default']['secret']
nft_type_args = '0xf90f9c38b0ea0815156bbc340c910d0a21ee57cf0000002900000000'
token_uuid = 'db144551-e65f-4dc4-9037-fc017734ef7b'


def test_get_token_by_nft_type_args():
    r = get_token_by_nft_type_args(key, secret, nft_type_args)
    assert r.status_code == 200
    assert r.json()['token']['uuid'] == token_uuid


def test_get_token_by_nft_type_args_with_wrong_args():
    r = get_token_by_nft_type_args(key, secret, 'wroing_nft_type_args')
    assert r.status_code == 500
