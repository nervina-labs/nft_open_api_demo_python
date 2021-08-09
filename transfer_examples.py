import ast
from argparse import ArgumentParser, ArgumentError

from utils.config import config
from utils.utils import print_result
from api import transfer_tx


key = config['default']['key']
secret = config['default']['secret']


parser = ArgumentParser(description='Run open API examples')
parser.version = '1.0'

from_address = parser.add_argument(
    '--from_address', help='Transfer tx from address')
to_address = parser.add_argument('--to_address', help='Transfer tx to address')
token_uuid = parser.add_argument('--token_uuid', help='Token uuid')
nft_type_args = parser.add_argument('--nft_type_args', help='Token type args')


# generate new unsigned transfer tx
unsigned_tx = parser.add_argument_group('Generate unsigned transfer tx')
unsigned_tx.add_argument('--new_tx', action='store_true',
                         help='Generate new unsigned transfer tx')


# broadcast signed transfer tx
broadcast_tx = parser.add_argument_group('Broadcast transfer tx')
broadcast_tx.add_argument(
    '--broadcast_tx', action='store_true', help='Broadcast signed transfer tx')
signed_tx = broadcast_tx.add_argument('--signed_tx', help='signed transfer tx')


# get tx by tx uuid
get_tx = parser.add_argument_group('Get tx by tx uuid')
get_tx.add_argument('--get_tx', action='store_true', help='get tx by tx uuid')
tx_uuid = get_tx.add_argument('--tx_uuid', help='tx uuid')

args = parser.parse_args()


if args.new_tx:
    if not args.from_address:
        raise ArgumentError(from_address, message='--from_address is needed')
    if not args.to_address:
        raise ArgumentError(to_address, message='--to_address is needed')
    if not args.token_uuid:
        raise ArgumentError(token_uuid, message='--token_uuid is needed')
    r = transfer_tx.generate_new_transfer_tx(
        key, secret, args.from_address, args.to_address, None, args.token_uuid)
    print_result(r, 200)


if args.broadcast_tx:
    if not args.from_address:
        raise ArgumentError(from_address, message='--from_address is needed')
    if not args.to_address:
        raise ArgumentError(to_address, message='--to_address is needed')
    if not args.nft_type_args:
        raise ArgumentError(nft_type_args, message='--nft_type_args is needed')
    if not args.token_uuid:
        raise ArgumentError(token_uuid, message='--token_uuid is needed')
    if not args.signed_tx:
        raise ArgumentError(signed_tx, message='--signed_tx is needed')
    signed_tx = args.signed_tx
    r = transfer_tx.broadcast_signed_tx(
        key, secret, args.from_address, args.to_address, args.nft_type_args, args.token_uuid, signed_tx)
    print_result(r, 200)


if args.get_tx:
    if not args.tx_uuid:
        raise ArgumentError(tx_uuid, message='--tx_uuid is needed')
    r = transfer_tx.get_tx_by_tx_uuid(key, secret, args.tx_uuid)
    print_result(r, 200)
