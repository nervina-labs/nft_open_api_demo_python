from utils.config import config
from api.default import get_token

key = config['default']['key']
secret = config['default']['secret']
token_uuid = config['default']['token_uuid']


def test_get_token_by_token_uuid():
    token_uuid = 'e11e6623-67c8-4202-888a-4f84daaec52c'
    r = get_token(key, secret, token_class_uuid, token_uuid)
    print(r.json())
    assert r.status_code == 200
    assert r.json()['uuid'] == token_uuid


# def test_get_token_with_invalid_token_uuid():
#     r = get_token(key, secret, token_class_uuid, 'invalid_token_uuid')
#     assert r.status_code == 404
#     assert r.json()['code'] == 1004
#     assert r.json()['message'] == 'token not found'


# def test_get_token_with_wrong_token_class_uuid():
#     r = get_token(key, secret, 'invalid_token_class_uuid', token_uuid)
#     print(r.json())
#     assert r.status_code == 404
#     assert r.json()['code'] == 1015
#     assert r.json()['message'] == 'token class not found'
