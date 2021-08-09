from argparse import ArgumentParser, ArgumentError

from utils.config import config
from utils.utils import print_result
from api import indexer


key = config['default']['key']
secret = config['default']['secret']


parser = ArgumentParser(description='Run open API examples')
parser.version = '1.0'


# get tokens by address
get_tokens_by_address = parser.add_argument_group(
    'Get tokens by holder address')
get_tokens_by_address.add_argument(
    '--get_tokens_by_address', action='store_true', help='Get tokens by holder address')
address = get_tokens_by_address.add_argument(
    '--address', help='Holder address')

# get token by nft type args
get_token_by_args = parser.add_argument_group('Get token by NFT type args')
get_token_by_args.add_argument(
    '--get_token_by_args', action='store_true', help='Get token by NFT type args')
nft_type_args = get_token_by_args.add_argument(
    '--nft_type_args', help='NFT type args')

args = parser.parse_args()


if args.get_tokens_by_address:
    if not args.address:
        raise ArgumentError(address, '--address is needed')
    r = indexer.get_tokens_by_holder_address(key, secret, args.address)
    print_result(r, 200)

if args.get_token_by_args:
    if not args.nft_type_args:
        raise ArgumentError(nft_type_args, '--nft_type_args is needed')
    r = indexer.get_token_by_nft_type_args(key, secret, args.nft_type_args)
    print_result(r, 200)
