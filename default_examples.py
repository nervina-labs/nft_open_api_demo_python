from argparse import ArgumentParser, ArgumentError

from utils.config import config
from utils.utils import print_result
from api import default


key = config['default']['key']
secret = config['default']['secret']


parser = ArgumentParser(description='Run open API examples')
parser.version = '1.0'

class_uuid = parser.add_argument(
    '--class_uuid', help='Token class uuid')
token_uuid = parser.add_argument('--token_uuid', help='Token uuid')


# get user created token classes
get_token_classes = parser.add_argument_group('get token classes')
get_token_classes.add_argument('--get_token_classes', action='store_true',
                               help='Get user owned token classes')


# create new token classes
create_token_class = parser.add_argument_group('create token class')
create_token_class.add_argument('--create_token_class', action='store_true',
                                help='Create token class')
create_token_class.add_argument(
    '--name', default='New token class', help='token class name')
create_token_class.add_argument(
    '--description', default='New token class description', help='token class description')
create_token_class.add_argument(
    '--total', default='0', help='Total number of new token class, 0 as unlimited, positive integer as limited')
create_token_class.add_argument(
    '--renderer', default='https://oss.jinse.cc/production/8ee71e29-3b10-4d15-b68c-380c7840c653.jpeg', help='New token class renderer')


# get token class by class uuid
get_token_class_by_uuid = parser.add_argument_group(
    'get token class by class uuid')
get_token_class_by_uuid.add_argument(
    '--get_token_class_by_uuid', action='store_true', help='Get token class by class uuid')


# create and distribute token to address
distribute_token = parser.add_argument_group('create and distribute token')
distribute_token.add_argument('--distribute_token', action='store_true',
                              help='Create and distribute token(s) to ckb address')
address = distribute_token.add_argument(
    '--address', help='Target address of distrubte token')


# get token by token uuid
get_token = parser.add_argument_group('get token by token uuid')
get_token.add_argument('--get_token', action='store_true',
                       help='Get token by token uuid')

# get holder address by token uuid
get_holder_address = parser.add_argument_group(
    'get holder address by token uuid')
get_holder_address.add_argument(
    '--get_holder_address', action='store_true', help='Get holder address by token uuid')

args = parser.parse_args()


if args.get_token_classes:
    r = default.get_user_owned_token_classes(key, secret)
    print_result(r, 200)

if args.create_token_class:
    r = default.create_token_class(key, secret, args.name,
                                   args.description, args.total, args.renderer)
    print_result(r, 201)

if args.get_token_class_by_uuid:
    if not args.class_uuid:
        raise ArgumentError(class_uuid,
                            message='--class_uuid is needed for --get_token_class_by_uuid')
    r = default.get_token_class_by_uuid(key, secret, args.class_uuid)
    print_result(r, 200)

if args.distribute_token:
    if not args.class_uuid:
        raise ArgumentError(class_uuid, message='--class_uuid is needed')
    if not args.address:
        raise ArgumentError(address, message='--address is needed')
    r = default.distribute_token(key, secret, args.class_uuid, args.address)
    print_result(r, 201)

if args.get_token:
    if not args.token_uuid:
        raise ArgumentError(token_uuid, message='--token_uuid is needed')
    r = default.get_token(key, secret, args.token_uuid)
    print_result(r, 200)

if args.get_holder_address:
    if not args.token_uuid:
        raise ArgumentError(token_uuid, message='--token_uuid is needed')
    r = default.get_holder_by_token_uuid(key, secret, args.token_uuid)
    print_result(r, 200)
