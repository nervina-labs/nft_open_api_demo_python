from utils.config import config
from default import create_token_class

key = config['default']['key']
secret = config['default']['secret']


def test_create_unlimited_token_class():
    name = 'Open API Unlimit Test'
    description = 'Open API Test Description'
    total = '0'
    renderer = 'https://example.com'
    r = create_token_class(key, secret, name, description, total, renderer)
    assert r.status_code == 201
    print(r.json())


def test_create_limited_token_class():
    name = 'Open API Limit Test'
    description = 'Open API Test Description'
    total = '7'
    renderer = 'https://example.com'
    r = create_token_class(key, secret, name, description, total, renderer)
    assert r.status_code == 201
    print(r.json())


def test_create_token_class_with_name_more_than_30_chars():
    name = 'c'*31
    description = 'Open API Test Description'
    total = '7'
    renderer = 'https://example.com'
    r = create_token_class(key, secret, name, description, total, renderer)
    assert r.status_code == 400
    assert r.json()['code'] == 1003
    assert r.json()['message'] == 'the token class name is too long'


def test_create_token_class_with_description_more_than_200_chars():
    name = 'Open API Test'
    description = 'c'*201
    total = '7'
    renderer = 'https://example.com'
    r = create_token_class(key, secret, name, description, total, renderer)
    assert r.status_code == 400
    assert r.json()['code'] == 1005
    assert r.json()['message'] == 'the token class description is too long'


def test_create_token_class_with_total_as_negative():
    name = 'Open API Test'
    description = 'Open API Test Description'
    total = '-1'
    renderer = 'https://example.com'
    r = create_token_class(key, secret, name, description, total, renderer)
    assert r.status_code == 400
    assert r.json()['code'] == 1011
    assert r.json()['message'] == 'the total is negative'


def test_create_token_class_with_total_as_decimal():
    name = 'Open API Test'
    description = 'Open API Test Description'
    total = '7.7'
    renderer = 'https://example.com'
    r = create_token_class(
        key, secret, name, description, total, renderer)
    assert r.status_code == 400
    assert r.json()['code'] == 1033
    assert r.json()['message'] == 'invalid total'


def test_create_token_class_with_renderer_format_error():
    name = 'Open API Test'
    description = 'Open API Test Description'
    total = '7'
    renderer = 'http://example.com'
    r = create_token_class(key, secret, name, description, total, renderer)
    assert r.status_code == 400
    assert r.json()['code'] == 1032
    assert r.json()['message'] == 'invalid URL format'


def test_create_token_class_with_renderer_more_than_255_chars():
    name = 'Open API Test'
    description = 'Open API Test Description'
    total = '7'
    renderer = 'https://' + 'c'*248
    r = create_token_class(key, secret, name, description, total, renderer)
    assert r.status_code == 400
    assert r.json()['code'] == 1014
    assert r.json()['message'] == 'the renderer is too long'
