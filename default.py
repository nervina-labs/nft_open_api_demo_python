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
def create_token_class(key, secret, name, description, total, renderer):
    method = 'POST'
    endpoint = '/token_classes'
    content = {
        'name': name,
        'description': description,
        'total': total,
        'renderer': renderer
    }
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
def get_token(key, secret, uuid, oid):
    method = 'GET'
    endpoint = f'/token_classes/{uuid}/tokens/{oid}'
    content = ''
    return send_request(key, secret, method, endpoint, content)
