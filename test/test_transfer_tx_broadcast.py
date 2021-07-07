from utils.config import config
from transfer_tx import generate_new_transfer_tx, broadcast_signed_tx

key = config['default']['key']
secret = config['default']['secret']
token_uuid = 'f40588f2-7ed3-468c-afbf-ef92f2ecf99a'
from_address = 'ckt1qjda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xws7nx9v0ycll73vnzpsc0nvm3rh8jkc5g2a7xm59'
to_address = 'ckt1q3vvtay34wndv9nckl8hah6fzzcltcqwcrx79apwp2a5lkd07fdxxqycw877rwy0uuwspsh9cteaf8kqp8nzjl0dxfp'
nft_type_args = '0xf90f9c38b0ea0815156bbc340c910d0a21ee57cf0000003300000002'
signed_tx = '{"version":"0x0","cell_deps":[{"out_point":{"tx_hash":"0xbd262c87a84c08ea3bc141700cf55c1a285009de0e22c247a8d9597b4fc491e6","index":"0x2"},"dep_type":"code"},{"out_point":{"tx_hash":"0xd346695aa3293a84e9f985448668e9692892c959e7e83d6d8042e59c08b8cf5c","index":"0x0"},"dep_type":"code"},{"out_point":{"tx_hash":"0x03dd2a5594ed2d79196b396c83534e050ba0ad07fa5c1cd61a7094f9fb60a592","index":"0x0"},"dep_type":"code"},{"out_point":{"tx_hash":"0xf8de3bb47d055cdf460d93a2a6e1b05f7432f9777c8c474abf4eec1d4aee5d37","index":"0x0"},"dep_type":"dep_group"}],"header_deps":[],"inputs":[{"previous_output":{"tx_hash":"0x52419c2bf7131908052e7fbed374ca82f3b9a23c091bcfcb487c4ac1c4c90717","index":"0x1"},"since":"0x0"}],"outputs":[{"capacity":"0x31eb3c002","type":{"code_hash":"0xb1837b5ad01a88558731953062d1f5cb547adf89ece01e8934a9f0aeed2d959f","args":"0xf90f9c38b0ea0815156bbc340c910d0a21ee57cf0000003300000002","hash_type":"type"},"lock":{"code_hash":"0x58c5f491aba6d61678b7cf7edf4910b1f5e00ec0cde2f42e0abb4fd9aff25a63","args":"0x009871fde1b88fe71d00c2e5c2f3d49ec009e629","hash_type":"type"}}],"outputs_data":["0x000000000000000000c000"],"witnesses":["0x5500000010000000550000005500000041000000c3e23abd5f3fb6350d138c7e25933c1a7e150d6aa75f8c118e55233101052af079ba116a515180252b73e2cbe02a2924118ed710c7e5c5e80c7e5b80258be45800"]}'


# def test_generate_new_transfer_tx_by_token_uuid():
#     r = generate_new_transfer_tx(
#         key, secret, from_address, to_address, nft_type_args=nft_type_args)
#     assert r.status_code == 200
#     print(r.json())


# def test_broadcast_signed_tx():
#     r = broadcast_signed_tx(key, secret, from_address,
#                             to_address, nft_type_args, token_uuid, signed_tx)
#     print(r.json())
