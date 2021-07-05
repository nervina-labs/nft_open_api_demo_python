import base64
import hmac
import hashlib
from datetime import datetime

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
    url = f'https://api.test.nervina.cn{endpoint}'
    signature, gmt = get_signature_and_gmt(
        secret, method, endpoint, content, content_type)
    headers = {
        'Content-Type': content_type,
        'Date': gmt,
        'Authorization': f'NFT {key}:{signature}'
    }

    return requests.request(method, url, headers=headers, data=content)
