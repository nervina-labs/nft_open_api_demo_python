from urllib.parse import urlencode

from _pytest.mark import param
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


def get_tokens_by_token_class(key, secret, token_class_id, holder_address=None, page=None, limit=None):
    method = 'GET'
    params = {}
    if holder_address:
        params['holder_address'] = holder_address
    if page:
        params['page'] = page
    if limit:
        params['limit'] = limit
    endpoint = f'/indexer/token_classes/{token_class_id}/tokens'
    if params:
        endpoint = endpoint + '?' + urlencode(params)
    content = ''
    return send_request(key, secret, method, endpoint, content)
