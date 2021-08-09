import pytest
from utils.config import config
from api.default import distribute_token

key = config['default']['key']
secret = config['default']['secret']

token_class_uuid = config['default']['token_class_uuid']
address = config['default']['address']


def test_distribute_to_single_address():
    r = distribute_token(key, secret, token_class_uuid, address)
    assert r.status_code == 201


@pytest.mark.test
def test_distribute_to_multi_addresses():
    r = distribute_token(key, secret, token_class_uuid,
                         *[address] * 1000)
    print(r.json())
    assert r.status_code == 201


def test_distribute_to_multi_same_addresses():
    r = distribute_token(key, secret, token_class_uuid, address, address)
    assert r.status_code == 201


def test_distribute_without_address():
    r = distribute_token(key, secret, token_class_uuid)
    assert r.status_code == 400
    assert r.json()['code'] == 1017
    assert r.json()['message'] == 'the addresses is missing'


def test_distribute_with_invalid_token_class_uuid():
    r = distribute_token(key, secret, 'invalid_token_class_uuid', address)
    assert r.status_code == 404
    assert r.json()['code'] == 1015
    assert r.json()['message'] == 'token class not found'


def test_distribute_not_owned_token_class():
    not_owned_token_class_uuid = config['default']['not_owned_token_class_uuid']
    r = distribute_token(key, secret, not_owned_token_class_uuid, address)
    assert r.status_code == 404
    assert r.json()['code'] == 1015
    assert r.json()['message'] == 'token class not found'


def test_distribute_to_invalid_address():
    r = distribute_token(key, secret, token_class_uuid, 'invalid_ckb_address')
    assert r.status_code == 400
    assert r.json()['code'] == 1018
    assert r.json()['message'] == 'the address is invalid'


def test_distribute_to_multi_addresses_with_one_invalid():
    r = distribute_token(key, secret, token_class_uuid,
                         address, 'invalid_ckb_address')
    assert r.status_code == 400
    assert r.json()['code'] == 1018
    assert r.json()['message'] == 'the address is invalid'


def test_distribute_to_short_address():
    short_address = config['default']['short_address']
    r = distribute_token(key, secret, token_class_uuid, short_address)
    assert r.status_code == 400
    assert r.json()['code'] == 1022
    assert r.json()['message'] == 'only support full address'


def test_distribute_out_of_limited():
    limited_class_uuid = config['default']['limited_token_class_uuid']
    r = distribute_token(key, secret, limited_class_uuid, * [address] * 8)
    assert r.status_code == 400
    assert r.json()['code'] == 1021
    assert r.json()['message'] == 'exceed total'


def test_distribute_out_of_stock():
    out_of_stock_class_uuid = config['default']['out_of_stock_token_class_uuid']
    r = distribute_token(key, secret, out_of_stock_class_uuid, address)
    assert r.status_code == 400
    assert r.json()['code'] == 1021
    assert r.json()['message'] == 'exceed total'
