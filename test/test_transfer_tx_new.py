from utils.config import config
from transfer_tx import generate_new_transfer_tx

key = config['default']['key']
secret = config['default']['secret']
token_uuid = '4730fe70-c46f-4ec9-a029-039909dcc6c2'
from_address = 'ckt1q3vvtay34wndv9nckl8hah6fzzcltcqwcrx79apwp2a5lkd07fdxxqycw877rwy0uuwspsh9cteaf8kqp8nzjl0dxfp'
to_address = 'ckt1q3vvtay34wndv9nckl8hah6fzzcltcqwcrx79apwp2a5lkd07fdx83pmv9wj80kf0w5zfym9am9eply253tuu8v5lsn'
nft_type_args = '0xf90f9c38b0ea0815156bbc340c910d0a21ee57cf000000200000000b'


def test_generate_new_transfer_tx_by_token_uuid():
    r = generate_new_transfer_tx(
        key, secret, from_address, to_address, token_uuid=token_uuid)
    assert r.status_code == 200
    assert r.json()[
        'unsigned_tx']['inputs'][0]['type']['args'] == nft_type_args


def test_generate_new_transfer_tx_by_nft_type_args():
    r = generate_new_transfer_tx(
        key, secret, from_address, to_address, nft_type_args=nft_type_args)
    assert r.status_code == 200
    assert r.json()[
        'unsigned_tx']['inputs'][0]['type']['args'] == nft_type_args


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
