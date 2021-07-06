from utils.config import config
from default import get_token

key = config['default']['key']
secret = config['default']['secret']
token_class_uuid = '4867853a-bceb-42a2-8105-c23cb77f9cba'
token_uuid = '09fac672-cb8b-423d-b919-3671336f8c7f'


def test_get_token_by_token_uuid():
    r = get_token(key, secret, token_class_uuid, token_uuid)
    assert r.status_code == 200


def test_get_token_with_wrong_token_uuid():
    r = get_token(key, secret, token_class_uuid, 'wrong_token_uuid')
    assert r.status_code == 404
    assert r.json()['code'] == 1004
    assert r.json()['message'] == 'token not found'


def test_get_token_with_wrong_token_class_uuid():
    r = get_token(key, secret, 'wrong_token_class_uuid', token_uuid)
    assert r.status_code == 404
    assert r.json()['code'] == 1015
    assert r.json()['message'] == 'token class not found'
