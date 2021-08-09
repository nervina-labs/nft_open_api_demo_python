import json
from utils.utils import send_request


# could be token_uuid or nft_type_args
def generate_new_transfer_tx(key, secret, from_address, to_address, nft_type_args=None, token_uuid=None):
    method = 'GET'
    if nft_type_args:
        endpoint = f'/tx/token_transfers/new?from_address={from_address}&to_address={to_address}&nft_type_args={nft_type_args}'
    elif token_uuid:
        endpoint = f'/tx/token_transfers/new?from_address={from_address}&to_address={to_address}&token_uuid={token_uuid}'
    else:
        raise KeyError
    content = ''
    return send_request(key, secret, method, endpoint, content)


def broadcast_signed_tx(key, secret, from_address, to_address, nft_type_args, token_uuid, signed_tx):
    method = 'POST'
    endpoint = '/tx/token_transfers'
    content = {
        'from_address': from_address,
        'to_address': to_address,
        'nft_type_args': nft_type_args,
        'token_uuid': token_uuid,
        'signed_tx': signed_tx
    }
    return send_request(key, secret, method, endpoint, json.dumps(content))


# tx uuid
def get_tx_by_tx_uuid(key, secret, uuid):
    method = 'GET'
    endpoint = f'/tx/token_transfers/{uuid}'
    content = ''
    return send_request(key, secret, method, endpoint, content)
