import pytest
from utils.config import config
from api.indexer import get_tokens_by_holder_address

key = config['default']['key']
secret = config['default']['secret']
# address = 'ckt1q3vvtay34wndv9nckl8hah6fzzcltcqwcrx79apwp2a5lkd07fdxxqycw877rwy0uuwspsh9cteaf8kqp8nzjl0dxfp'
address = 'ckt1q3vvtay34wndv9nckl8hah6fzzcltcqwcrx79apwp2a5lkd07fdxxqycw877rwy0uuwspsh9cteaf8kqp8nzjl0dxfp'
empty_address = 'ckb1qjl58smqy32hnrq6vxjedcxe2fugvnz497h7yvwqvwel40uh4rltc83ujp65w9nddj4utx7w396q3r8f59yjgxczfrw'


@pytest.mark.test
def test_get_tokens_by_holder_address():
    r = get_tokens_by_holder_address(key, secret, address)
    # print(r.json())
    print(r.request.url)
    print(r.request.headers)
    assert r.status_code == 200


def test_get_all_tokens_by_holder_address():
    total = 0
    max_page = 2
    current_page = 1
    all = []
    while current_page <= max_page:
        r = get_tokens_by_holder_address(
            key, secret, address, page=current_page)
        max_page = r.json()['meta']['max_page']
        current_page += 1
        total += len(r.json()['token_list'])
        all += r.json()['token_list']
    assert r.status_code == 200
    assert r.json()['meta']['total_count'] == total
    assert r.json()['holder_address'] == address


def test_get_tokens_by_holder_address_without_token():
    r = get_tokens_by_holder_address(key, secret, empty_address)
    print(r.json())
    assert r.status_code == 200
    assert r.json()['holder_address'] == empty_address
    assert r.json()['meta']['total_count'] == 0
    assert r.json()['token_list'] == []


def test_get_tokens_by_holder_address_with_wrong_address():
    r = get_tokens_by_holder_address(key, secret, 'wrong_address')
    # this should be 400
    assert r.status_code == 200
