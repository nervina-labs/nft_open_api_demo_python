import pytest
from utils.config import config
from api.transfer_tx import generate_new_transfer_tx

key = config['default']['key']
secret = config['default']['secret']
token_uuid = 'b309dbe5-265c-4cf4-9741-20ed90f6b805'
from_address = 'ckt1qyq85e3trex8ll5tycsvxrumxugaeu4k9zzsjctw4z'
to_address = 'ckt1qyqdrjrj7zxt5f9j4kh76s4g0uxld6vkyw7s5ntu0r'
nft_type_args = '0xf90f9c38b0ea0815156bbc340c910d0a21ee57cf0000003500000007'


@pytest.mark.test
def test_generate_new_transfer_tx_by_token_uuid():
    r = generate_new_transfer_tx(
        key, secret, from_address, to_address, token_uuid=token_uuid)
    print(r.request.headers)
    print(r.request.url)
    print(r.json())
    assert r.status_code == 200
    # assert r.json()[
    # 'unsigned_tx']['inputs'][0]['type']['args'] == nft_type_args


# @pytest.mark.test
# def test_generate_new_transfer_tx_by_nft_type_args():
#     r = generate_new_transfer_tx(
#         key, secret, from_address, to_address, nft_type_args=nft_type_args)
#     print(r.json())
#     assert r.status_code == 200
#     assert r.json()[
#         'unsigned_tx']['inputs'][0]['type']['args'] == nft_type_args


def test_generate_new_transfer_tx_with_wrong_token_uuid():
    r = generate_new_transfer_tx(
        key, secret, from_address, to_address, token_uuid='wrong_token_uuid')
    assert r.status_code == 404
    assert r.json()['code'] == 1004
    assert r.json()['message'] == 'token not found'


def test_generate_new_transfer_tx_with_wrong_nft_type_args():
    r = generate_new_transfer_tx(
        key, secret, from_address, to_address, nft_type_args='wrong_nft_type_args')
    assert r.status_code == 500


def test_generate_new_transfer_tx_with_wrong_from_address():
    r = generate_new_transfer_tx(
        key, secret, 'wrong_from_address', to_address, token_uuid=token_uuid)
    assert r.status_code == 500


def test_generate_new_transfer_tx_with_wrong_to_address():
    r = generate_new_transfer_tx(
        key, secret, from_address, 'wrong_to_address', token_uuid=token_uuid)
    assert r.status_code == 500


def test_generate_new_transfer_tx_with_to_address_same_as_from():
    r = generate_new_transfer_tx(
        key, secret, from_address, from_address, token_uuid=token_uuid)
    assert r.status_code == 500
