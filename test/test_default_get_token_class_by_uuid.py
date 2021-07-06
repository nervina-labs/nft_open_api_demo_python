from utils.config import config
# from default import create_token_class
from default import get_token_class_by_uuid

key = config['default']['key']
secret = config['default']['secret']

# r = create_token_class(key, secret, 'OpenAPITest',
#                        'OpenAPI description', '0', 'https://example.com')
# token_class_uuid = r.json()['uuid']
token_class_uuid = '4867853a-bceb-42a2-8105-c23cb77f9cba'


def test_get_token_class_by_uuid():
    r = get_token_class_by_uuid(key, secret, token_class_uuid)
    assert r.status_code == 200
    assert r.json()['uuid'] == token_class_uuid


def test_get_token_class_with_wrong_uuid():
    r = get_token_class_by_uuid(key, secret, 'wrong_class_uuid')
    assert r.status_code == 404
    assert r.json()['code'] == 1015
    assert r.json()['message'] == 'token class not found'
