import json
from utils.utils import send_request


def get_token_classes_owned_by_user(key, secret):
    method = 'GET'
    endpoint = '/token_classes'
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
