from utils.config import config
from api.default import get_token, get_token_class_by_uuid

key = config['default']['key']
secret = config['default']['secret']


def test_get_token_class_by_uuid():
    token_class_uuid = config['default']['token_class_uuid']
    r = get_token_class_by_uuid(key, secret, token_class_uuid)
    print(r.json())
    assert r.status_code == 200
    assert r.json()['uuid'] == token_class_uuid


def test_get_token_class_with_invalid_uuid():
    r = get_token_class_by_uuid(key, secret, 'invalid_class_uuid')
    assert r.status_code == 404
    assert r.json()['code'] == 1015
    assert r.json()['message'] == 'token class not found'


def test_get_not_owned_token_class():
    not_owned_token_class_uuid = config['default']['not_owned_token_class_uuid']
    r = get_token_class_by_uuid(key, secret, not_owned_token_class_uuid)
    assert r.status_code == 200
    assert r.json()['uuid'] == not_owned_token_class_uuid
