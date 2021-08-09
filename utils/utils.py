import base64
import hmac
import hashlib
from datetime import datetime
from utils.config import config

import requests


def str_to_bytes(str):
    return str.encode('utf-8')


def bytes_to_str(bytes):
    return bytes.decode('utf-8')


def get_signature_and_gmt(secret, method, endpoint, content, content_type='application/json'):
    if content:
        content_md5 = bytes_to_str(base64.b64encode(
            hashlib.md5(str_to_bytes(content)).digest()))
    else:
        content_md5 = ''
    gmt = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    msg = str_to_bytes(
        f'{method}\n{endpoint}\n{content_md5}\n{content_type}\n{gmt}')

    signature = bytes_to_str(base64.b64encode(hmac.digest(
        str_to_bytes(secret), msg, hashlib.sha1)))

    return (signature, gmt)


def send_request(key, secret, method, endpoint, content, content_type='application/json'):
    endpoint = f'/api/v1/{endpoint.strip("/")}'
    url = f'{config["default"]["url"]}{endpoint}'
    signature, gmt = get_signature_and_gmt(
        secret, method, endpoint, content, content_type)
    headers = {
        'Content-Type': content_type,
        'Date': gmt,
        'Authorization': f'NFT {key}:{signature}'
    }

    return requests.request(method, url, headers=headers, data=content)


def print_result(r, expected_status_code):
    if r.status_code == expected_status_code:
        print(r.json())
    else:
        print(f'URL: {r.request.url}')
        print(f'Headers: {r.request.headers}')
        print(f'Body: {r.request.body}')
        print(f'Status Code: {r.status_code}')
        print(f'Response: {r.text}')


if __name__ == '__main__':
    key = 'ybpkZPBZSMp4I7CF'
    secret = 'da13e9de58221195ead7a06d9ca84885b18e704201d7ff2d44585ceb85f7dc71'
    endpoint = '/token_classes'
    content = ''
    print(get_signature_and_gmt(secret, 'GET', endpoint, content))
