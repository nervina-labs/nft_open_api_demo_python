from utils.utils import send_request


def get_tokens_by_holder_address(key, secret, address, page=None):
    method = 'GET'
    if page:
        endpoint = f'/indexer/holder_tokens/{address}?page={page}'
    else:
        endpoint = f'/indexer/holder_tokens/{address}'
    content = ''
    return send_request(key, secret, method, endpoint, content)


def get_tokens_by_args(key, secret, args):
    method = 'GET'
    endpoint = f'/indexer/tokens/{args}'
    content = ''
    return send_request(key, secret, method, endpoint, content)
