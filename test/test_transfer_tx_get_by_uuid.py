from utils.config import config
from api.transfer_tx import get_tx_by_tx_uuid

key = config['default']['key']
secret = config['default']['secret']
issue_tx_uuid = '1c77933c-4c33-4995-8755-9f18ac707668'
transfer_tx_uuid = 'de84bde3-b745-4e1d-a8cf-f5e07e80d313'


def test_get_issue_tx_by_tx_uuid():
    r = get_tx_by_tx_uuid(key, secret, issue_tx_uuid)
    print(r.json())
    assert r.status_code == 200
    assert r.json()['tx_type'] == 'issue'


def test_get_transfer_tx_by_tx_uuid():
    r = get_tx_by_tx_uuid(key, secret, transfer_tx_uuid)
    assert r.status_code == 200
    assert r.json()['tx_type'] == 'transfer'


def test_get_tx_by_wrong_uuid():
    r = get_tx_by_tx_uuid(key, secret, 'wrong_tx_uuid')
    assert r.status_code == 404
    assert r.json()['code'] == 1002
    assert r.json()['message'] == 'token ckb transaction not found'
