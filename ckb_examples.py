import ast
from argparse import ArgumentParser, ArgumentError

from coincurve import PrivateKey
from ckb_toolkit.core import signer
from ckb_toolkit.core.hash import ckb_blake160
from ckb_toolkit.address.address import generateFullAddress, generateShortAddress


parser = ArgumentParser(description='CKB related operation examples')
parser.version = '1.0'


private_key = parser.add_argument('--private_key', help='Private Key')
address_info = parser.add_argument('--address_info', action='store_true',
                                   help='Get short address, full address from private key')
network = parser.add_argument(
    '--network', default='testnet', help='CKB network choice, mainnet or testnet')
sign_tx = parser.add_argument('--sign_tx', action='store_true', help='Sign tx')
unsigned_tx = parser.add_argument('--unsigned_tx', help='Unsighed tx')

args = parser.parse_args()


if args.address_info:
    if not args.private_key:
        raise ArgumentError(private_key, message='--private_key is needed')
    private_key = args.private_key
    network = args.network
    public_key = PrivateKey.from_hex(private_key).public_key.format()
    args = ckb_blake160(public_key)[2:]

    lock = {'code_hash': '9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8',
            'hash_type': 'type', 'args': args}

    short_address = generateShortAddress(args, network=network)
    full_address = generateFullAddress(lock, network=network)

    print(f'Short address: {short_address}')
    print(f'Full address: {full_address}')

if args.sign_tx:
    if not args.private_key:
        raise ArgumentError(private_key, message='--private_key is needed')
    if not args.unsigned_tx:
        raise ArgumentError(unsigned_tx, message='--unsigned_tx is needed')
    signed_tx = signer.sign_tx(ast.literal_eval(
        args.unsigned_tx), args.private_key)
    print(signed_tx)
