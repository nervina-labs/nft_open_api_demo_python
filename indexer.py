from utils import send_request


def get_tokens_by_holder_address(key, secret, address):
    method = 'GET'
    endpoint = f'/indexer/holder_tokens/{address}'
    content = ''
    return send_request(key, secret, method, endpoint, content)


# return 500
def get_tokens_by_args(key, secret, args):
    method = 'GET'
    endpoint = f'/indexer/tokens/{args}'
    content = ''
    return send_request(key, secret, method, endpoint, content)
