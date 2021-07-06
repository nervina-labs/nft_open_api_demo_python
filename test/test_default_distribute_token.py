from utils.config import config
from default import distribute_token

key = config['default']['key']
secret = config['default']['secret']
token_class_uuid = '4867853a-bceb-42a2-8105-c23cb77f9cba'
limited_class_uuid = '15fc9e0f-bfd2-465f-98e5-34e8179788fc'
out_of_stock_class_uuid = '0a5683f5-559d-4e1b-9e4e-5fe35e71f103'
address = 'ckt1q3vvtay34wndv9nckl8hah6fzzcltcqwcrx79apwp2a5lkd07fdxxqycw877rwy0uuwspsh9cteaf8kqp8nzjl0dxfp'
another_address = 'ckt1q3vvtay34wndv9nckl8hah6fzzcltcqwcrx79apwp2a5lkd07fdx83pmv9wj80kf0w5zfym9am9eply253tuu8v5lsn'


def test_distribute_token_to_single_address():
    r = distribute_token(key, secret, token_class_uuid, address)
    assert r.status_code == 201


def test_distribute_token_to_multi_addresses():
    r = distribute_token(key, secret, token_class_uuid,
                         address, another_address)
    assert r.status_code == 201


def test_distribute_token_to_multi_same_addresses():
    r = distribute_token(key, secret, token_class_uuid, address, address)
    assert r.status_code == 201


def test_distribute_token_to_empty_address():
    r = distribute_token(key, secret, token_class_uuid)
    assert r.status_code == 400
    assert r.json()['code'] == 1017
    assert r.json()['message'] == 'the addresses is missing'


def test_distribute_token_with_wrong_token_uuid():
    r = distribute_token(key, secret, 'wrong_token_uuid', address)
    assert r.status_code == 404
    assert r.json()['code'] == 1015
    assert r.json()['message'] == 'token class not found'


def test_distribute_token_to_wrong_address():
    r = distribute_token(key, secret, token_class_uuid, 'wrong_ckb_address')
    assert r.status_code == 400
    assert r.json()['code'] == 1018
    assert r.json()['message'] == 'the address is invalid'


def test_distribute_token_to_multi_addresses_with_one_invalid():
    r = distribute_token(key, secret, token_class_uuid,
                         address, 'wrong_ckb_address')
    assert r.status_code == 400
    assert r.json()['code'] == 1018
    assert r.json()['message'] == 'the address is invalid'


def test_distribute_token_out_of_limited():
    r = distribute_token(key, secret, limited_class_uuid, address,
                         address, address, address, address, address, address, address)
    assert r.status_code == 400
    assert r.json()['code'] == 1021
    assert r.json()['message'] == 'exceed total'


def test_distribute_out_of_stock_token():
    r = distribute_token(key, secret, out_of_stock_class_uuid, address)
    assert r.status_code == 400
    assert r.json()['code'] == 1021
    assert r.json()['message'] == 'exceed total'
