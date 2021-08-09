from utils.config import config
from api.default import get_user_owned_token_classes

key = config['default']['key']
secret = config['default']['secret']
token_class_uuid = config['default']['token_class_uuid']


def test_get_user_owned_token_classes():
    r = get_user_owned_token_classes(key, secret, count=100)
    assert r.status_code == 200


def test_get_user_owned_token_classes_with_count():
    r = get_user_owned_token_classes(key, secret, count=2)
    assert r.status_code == 200
    assert len(r.json()['token_classes']) == 2


def test_get_user_owned_token_classes_with_cursor():
    total = []
    count = 15
    cursor = -1
    while count >= 15 and cursor != 0:
        if cursor == -1:
            cursor = 0
        r = get_user_owned_token_classes(key, secret, cursor=cursor)
        assert r.status_code == 200
        count = len(r.json()['token_classes'])
        total += [i['uuid'] for i in r.json()['token_classes']]
        cursor = r.json()['meta']['next_cursor']
    assert token_class_uuid in total
