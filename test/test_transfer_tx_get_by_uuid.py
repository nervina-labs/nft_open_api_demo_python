from utils.config import config
from transfer_tx import get_tx_by_tx_uuid

key = config['default']['key']
secret = config['default']['secret']
issue_tx_uuid = 'f68c78a2-4396-4559-ba47-16a52cadf5cf'
transfer_tx_uuid = '37ae9eab-21fb-4a46-a4aa-5450f7931009'


def test_get_issue_tx_by_tx_uuid():
    r = get_tx_by_tx_uuid(key, secret, issue_tx_uuid)
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
