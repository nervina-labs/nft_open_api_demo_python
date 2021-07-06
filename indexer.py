from utils.utils import send_request


def get_tokens_by_holder_address(key, secret, address, page=None):
    method = 'GET'
    if page:
        endpoint = f'/indexer/holder_tokens/{address}?page={page}'
    else:
        endpoint = f'/indexer/holder_tokens/{address}'
    content = ''
    return send_request(key, secret, method, endpoint, content)


def get_token_by_nft_type_args(key, secret, nft_type_args):
    method = 'GET'
    endpoint = f'/indexer/tokens/{nft_type_args}'
    content = ''
    return send_request(key, secret, method, endpoint, content)
