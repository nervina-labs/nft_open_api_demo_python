from unsigned_tx_generators import generate_new_transfer_tx

if __name__ == '__main__':
    key = ''
    secret = ''
    from_address = ''
    to_address = ''
    nft_type_args = ''
    print(generate_new_transfer_tx(key, secret,
                                   from_address, to_address, nft_type_args).json())
