import json
from utils.utils import send_request


def get_user_owned_token_classes(key, secret, count=None, cursor=None):
    method = 'GET'
    if not (count or cursor):
        endpoint = '/token_classes'
    elif count and cursor:
        endpoint = f'/token_classes?count={count}&cursor={cursor}'
    elif count:
        endpoint = f'/token_classes?count={count}'
    else:
        endpoint = f'/token_classes?cursor={cursor}'

    content = ''
    return send_request(key, secret, method, endpoint, content)


# total = 0 as unlimited; total > 0 as limited
def create_token_class(key, secret, name, description, total, renderer, configure=None):
    method = 'POST'
    endpoint = '/token_classes'
    content = {
        'name': name,
        'description': description,
        'total': total,
        'renderer': renderer
    }
    if configure:
        content['configure'] = configure
    return send_request(key, secret, method, endpoint, json.dumps(content))


# token class uuid
def get_token_class_by_uuid(key, secret, uuid):
    method = 'GET'
    endpoint = f'/token_classes/{uuid}'
    content = ''
    return send_request(key, secret, method, endpoint, content)


# token class uuid
def distribute_token(key, secret, uuid, *address):
    method = 'POST'
    endpoint = f'/token_classes/{uuid}/tokens'
    content = {
        'addresses': list(address)
    }
    return send_request(key, secret, method, endpoint, json.dumps(content))


# token class uuid; and oid as token id
def get_token(key, secret, token_uuid):
    method = 'GET'
    endpoint = f'/tokens/{token_uuid}'
    content = ''
    return send_request(key, secret, method, endpoint, content)


def get_holder_by_token_uuid(key, secret, token_uuid):
    method = 'GET'
    endpoint = f'/tokens/{token_uuid}/address'
    content = ''
    return send_request(key, secret, method, endpoint, content)
