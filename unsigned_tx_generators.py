from utils import send_request


# could be token_uuid or nft_type_args
def generate_new_transfer_tx(key, secret, from_address, to_address, args=None, token_uuid=None):
    method = 'GET'
    if args:
        endpoint = f'/tx/token_transfers/new?from_address={from_address}&to_address={to_address}&nft_type_args={args}'
    elif token_uuid:
        endpoint = f'/tx/token_transfers/new?from_address={from_address}&to_address={to_address}&token_uuid={token_uuid}'
    else:
        raise KeyError
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
