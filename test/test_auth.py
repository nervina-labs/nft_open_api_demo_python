from datetime import datetime, timedelta

from utils.config import config
from utils.utils import get_signature_and_gmt

import pytest
from requests import request

key = config['default']['key']
secret = config['default']['secret']

endpoint = '/api/v1/token_classes'
url = f'{config["default"]["url"]}{endpoint}'
method = 'GET'
content = ''
content_type = 'application/json'


def test_missing_content_type():
    signature, gmt = get_signature_and_gmt(
        secret, method, endpoint, content, content_type)
    headers = {
        'Date': gmt,
        'Authorization': f'NFT {key}:{signature}'
    }
    r = request(method, url, headers=headers, data=content)
    assert r.status_code == 401
    assert r.json()['detail'] == 'Missing Content-Type in header'


def test_missing_date():
    signature, _ = get_signature_and_gmt(
        secret, method, endpoint, content, content_type)
    headers = {
        'Content-Type': content_type,
        'Authorization': f'NFT {key}:{signature}'
    }
    r = request(method, url, headers=headers, data=content)
    assert r.status_code == 401
    assert r.json()['detail'] == 'Missing Date in header'


def test_missing_authorization():
    _, gmt = get_signature_and_gmt(
        secret, method, endpoint, content, content_type)
    headers = {
        'Content-Type': content_type,
        'Date': gmt
    }
    r = request(method, url, headers=headers, data=content)
    assert r.status_code == 401
    assert r.json()['detail'] == 'Missing Authorization in header'


def test_invalid_key():
    key = 'invalid_key'
    signature, gmt = get_signature_and_gmt(
        secret, method, endpoint, content, content_type)
    headers = {
        'Content-Type': content_type,
        'Date': gmt,
        'Authorization': f'NFT {key}:{signature}'
    }

    r = request(method, url, headers=headers, data=content)
    assert r.status_code == 401
    assert r.json()['detail'] == 'Cannot find access key'


def test_invalid_secret():
    secret = 'invalid_secret'
    signature, gmt = get_signature_and_gmt(
        secret, method, endpoint, content, content_type)
    headers = {
        'Content-Type': content_type,
        'Date': gmt,
        'Authorization': f'NFT {key}:{signature}'
    }
    r = request(method, url, headers=headers, data=content)
    assert r.status_code == 401
    assert r.json()['detail'] == 'Signature mismatch'
    assert r.json()[
        'string_to_sign'] == f'GET\n/api/v1/token_classes\n\napplication/json\n{gmt}'


def test_invalid_authorization_format():
    signature, gmt = get_signature_and_gmt(
        secret, method, endpoint, content, content_type)
    headers = {
        'Content-Type': content_type,
        'Date': gmt,
        'Authorization': f'{key};{signature}'
    }

    r = request(method, url, headers=headers, data=content)
    assert r.status_code == 401
    assert r.json()['detail'] == 'Cannot find access key'


def test_date_expired():
    gmt = (datetime.utcnow() - timedelta(minutes=10)
           ).strftime('%a, %d %b %Y %H:%M:%S GMT')
    signature, gmt = get_signature_and_gmt(
        secret, method, endpoint, content, content_type, gmt)
    headers = {
        'Content-Type': content_type,
        'Date': gmt,
        'Authorization': f'NFT {key}:{signature}'
    }

    r = request(method, url, headers=headers, data=content)
    assert r.status_code == 401
    assert r.json()['detail'] == 'Time expired'
