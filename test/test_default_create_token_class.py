import pytest
from utils.config import config
from api.default import create_token_class

key = config['default']['key']
secret = config['default']['secret']

valid_img_url = 'https://alifei02.cfp.cn/creative/vcg/400/new/VCG41N1001984424.jpg'
invalid_img_url_with_incorrect_prefix = 'http://alifei02.cfp.cn/creative/VCG41N1001984424.jpg'
invalid_img_url_with_incorrect_suffix = 'https://example.com'
invalid_img_url_with_forbidden_content = 'https://5b0988e595225.cdn.sohucs.com/images/20171128/eae4d64998924156950f9385999149ed.jpeg'

description = 'Open API Test Description'
total = '7'

forbidden_content = '本校小额贷款，安全、快捷、方便、无抵押，随机随贷，当天放款'


@pytest.mark.test
def test_create_unlimited_token_class():
    name = 'Open API Unlimit Test'
    total = '0'
    valid_img_url = 'https://cdn.2zimu.com/mbd_file_16273832712481627383271244.png'
    r = create_token_class(
        key, secret, name, description, total, valid_img_url)
    print(r.request.url)
    print(r.request.headers)
    print(r.request.body)
    assert r.status_code == 201


def test_create_limited_token_class():
    name = 'Open API Limit Test'
    total = '7'
    r = create_token_class(
        key, secret, name, description, total, valid_img_url)
    assert r.status_code == 201


def test_create_token_class_with_forbidden_renderer():
    name = 'Open API with forbidden renderer'
    renderer = invalid_img_url_with_forbidden_content
    r = create_token_class(key, secret, name, description, total, renderer)
    assert r.status_code == 400
    assert r.json()['code'] == 1049
    assert r.json()['message'] == 'the renderer is blocked'


def test_create_token_class_with_invalid_renderer():
    name = 'Open API with invalid renderer suffix'
    renderer = invalid_img_url_with_incorrect_suffix
    r = create_token_class(key, secret, name, description, total, renderer)
    assert r.status_code == 400
    assert r.json()['code'] == 1049
    assert r.json()['message'] == 'the renderer is blocked'


def test_create_token_class_with_renderer_format_error():
    name = 'Open API with invalid renderer prefix'
    renderer = invalid_img_url_with_incorrect_prefix
    r = create_token_class(key, secret, name, description, total, renderer)
    assert r.status_code == 400
    assert r.json()['code'] == 1049
    assert r.json()['message'] == 'the renderer is blocked'


def test_create_token_class_with_renderer_more_than_255_chars():
    name = 'Open API Test'
    description = 'Open API Test Description'
    total = '7'
    renderer = 'https://' + 'c'*248 + '.jpg'
    r = create_token_class(key, secret, name, description, total, renderer)
    assert r.status_code == 400
    assert r.json()['code'] == 1049
    assert r.json()['message'] == 'the renderer is blocked'


def test_create_token_class_with_empty_renderer():
    name = 'Open API with empty renderer'
    r = create_token_class(key, secret, name, description, total, '')
    assert r.status_code == 400
    assert r.json()['code'] == 1049
    assert r.json()['message'] == 'the renderer is blocked'


def test_create_token_class_with_name_more_than_30_chars():
    name = 'c'*31
    r = create_token_class(
        key, secret, name, description, total, valid_img_url)
    assert r.status_code == 400
    assert r.json()['code'] == 1003
    assert r.json()['message'] == 'the token class name is too long'


def test_create_token_class_with_forbidden_name():
    name = forbidden_content
    r = create_token_class(
        key, secret, name, description, total, valid_img_url)
    assert r.status_code == 400
    assert r.json()['code'] == 1050
    assert r.json()['message'] == 'the content is blocked'


def test_create_token_class_with_empty_name():
    r = create_token_class(key, secret, '', description, total, valid_img_url)
    assert r.status_code == 400
    assert r.json()['code'] == 1002
    assert r.json()['message'] == 'the token class name is missing'


def test_create_token_class_with_description_more_than_200_chars():
    name = 'Open API with long description'
    description = 'c'*201
    r = create_token_class(
        key, secret, name, description, total, valid_img_url)
    assert r.status_code == 400
    assert r.json()['code'] == 1005
    assert r.json()['message'] == 'the token class description is too long'


def test_create_token_class_with_forbidden_description():
    name = 'Open API with forbidden descrption'
    description = forbidden_content
    r = create_token_class(
        key, secret, name, description, total, valid_img_url)
    assert r.status_code == 400
    assert r.json()['code'] == 1050
    assert r.json()['message'] == 'the content is blocked'


def test_create_token_class_with_total_as_negative():
    name = 'Open API with negative total'
    description = 'Open API Test Description'
    total = '-1'
    r = create_token_class(
        key, secret, name, description, total, valid_img_url)
    assert r.status_code == 400
    assert r.json()['code'] == 1011
    assert r.json()['message'] == 'the total is negative'


def test_create_token_class_with_total_as_decimal():
    name = 'Open API with decimal total'
    total = '7.7'
    r = create_token_class(
        key, secret, name, description, total, valid_img_url)
    assert r.status_code == 400
    assert r.json()['code'] == 1033
    assert r.json()['message'] == 'invalid total'


def test_create_token_class_with_empty_total():
    name = 'Open API with empty total'
    r = create_token_class(key, secret, name, description, '', valid_img_url)
    assert r.status_code == 400
    assert r.json()['code'] == 1010
    assert r.json()['message'] == 'the total is missing'
