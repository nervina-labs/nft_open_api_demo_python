import json
from utils import send_request


# there is an error in the doc, token_uuid should be nft_type_args
def generate_new_transfer_tx(key, secret, from_address, to_address, args):
    method = 'GET'
    endpoint = f'/tx/token_transfers/new?from_address={from_address}&to_address={to_address}&nft_type_args={args}'
    content = ''
    return send_request(key, secret, method, endpoint, content)


# Todo
def send_signed_tx(key, secret):
    pass


# tx uuid
def get_transfer_tx_by_tx_uuid(key, secret, uuid):
    method = 'GET'
    endpoint = f'/tx/token_transfers/{uuid}'
    content = ''
    return send_request(key, secret, method, endpoint, content)
