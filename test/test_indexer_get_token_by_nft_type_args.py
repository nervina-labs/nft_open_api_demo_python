from utils.config import config
from api.indexer import get_token_by_nft_type_args

key = config['default']['key']
secret = config['default']['secret']
nft_type_args = '0x520adc2e6a1211b822f866e13b1009a1862225a10000000400000009'
token_uuid = '4a719f0f-d23d-4164-8a00-bee1a3619069'


def test_get_token_by_nft_type_args():
    r = get_token_by_nft_type_args(key, secret, nft_type_args)
    assert r.status_code == 200
    print(r.request.url)
    print(r.request.headers)
    print(r.json())
    # assert r.json()['token']['uuid'] == token_uuid


# def test_get_token_by_nft_type_args_with_wrong_args():
#     r = get_token_by_nft_type_args(key, secret, 'wroing_nft_type_args')
#     assert r.status_code == 500
