# Open API Examples

## Install dependencies

`pip install -r requirements.txt`

## Configuration

copy `config.example` as `config`, and edit it with your key/secret

## Run Examples

### Create new NFT token class

```
python default_examples.py --create_token_class \
    --name test \
    --total 7 \
    --description "new token class test" \
    --renderer https://oss.jinse.cc/production/8ee71e29-3b10-4d15-b68c-380c7840c653.jpeg
```

### Get token classes that you created

`python default_examples.py --get_token_classes`

### Get token class by token class uuid

```
python default_examples.py --get_token_class_by_uuid \
    --class_uuid a81ed643-f0e5-49b2-b252-ac23914a4bc1
```

### Create and distribute token

```
python default_examples.py --distribute_token \
    --class_uuid a81ed643-f0e5-49b2-b252-ac23914a4bc1 \
    --address ckt1qjda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xw35wgwtcgew3yk2k6lm2z4plsmahfjc3m6k2zcxg
```

### Get token by token uuid

```
python default_examples.py --get_token \
    --token_uuid 3a3cbdc7-c27b-41d2-9e97-ec1169c1499a
```

### Get holder address by token uuid

```
python default_examples.py --get_holder_address \
    --token_uuid 3a3cbdc7-c27b-41d2-9e97-ec1169c1499a
```

### Get tokens by holder address

```
python indexer_examples.py --get_tokens_by_address \
    --address ckt1qsfy5cxd0x0pl09xvsvkmert8alsajm38qfnmjh2fzfu2804kq47v8j0qjulvfk56l2wtnc6merump3ydfz2ytk0ruz
```

### Get token by nft type args

```
python indexer_examples.py --get_token_by_args \
    --nft_type_args 0xf90f9c38b0ea0815156bbc340c910d0a21ee57cf0000005800000001
```

### Generate new unsigned transfer tx

```
python transfer_examples.py --new_tx \
    --from_address ckt1qjda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xw35wgwtcgew3yk2k6lm2z4plsmahfjc3m6k2zcxg \
    --to_address ckt1qjda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xws7nx9v0ycll73vnzpsc0nvm3rh8jkc5g2a7xm59 \
    --token_uuid 7c1a07d9-e41b-4c61-8b7e-798eed4f5ed9
```

### Broadcast signed transfer tx

```
python transfer_examples.py --broadcast_tx \
    --from_address ckt1qjda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xw35wgwtcgew3yk2k6lm2z4plsmahfjc3m6k2zcxg \
    --to_address ckt1qjda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xws7nx9v0ycll73vnzpsc0nvm3rh8jkc5g2a7xm59 \
    --token_uuid 7c1a07d9-e41b-4c61-8b7e-798eed4f5ed9 \
    --nft_type_args 0xf90f9c38b0ea0815156bbc340c910d0a21ee57cf0000005e00000003 \
    --signed_tx '{"version":"0x0","cell_deps":[{"out_point":{"tx_hash":"0x194a0f84de41d006a07ece07c96a8130100818599fcf0b2ecf49e512b873ed6e","index":"0x2"},"dep_type":"code"},{"out_point":{"tx_hash":"0xd346695aa3293a84e9f985448668e9692892c959e7e83d6d8042e59c08b8cf5c","index":"0x0"},"dep_type":"code"},{"out_point":{"tx_hash":"0x03dd2a5594ed2d79196b396c83534e050ba0ad07fa5c1cd61a7094f9fb60a592","index":"0x0"},"dep_type":"code"},{"out_point":{"tx_hash":"0xf8de3bb47d055cdf460d93a2a6e1b05f7432f9777c8c474abf4eec1d4aee5d37","index":"0x0"},"dep_type":"dep_group"}],"header_deps":[],"inputs":[{"previous_output":{"tx_hash":"0x1cc469e1f2f1e90766dff483bfd2f01c2aaed0c8e6f47ed78a91ac8619807b03","index":"0x0"},"since":"0x0"}],"outputs":[{"capacity":"0x31eb3ba04","type":{"code_hash":"0xb1837b5ad01a88558731953062d1f5cb547adf89ece01e8934a9f0aeed2d959f","args":"0xf90f9c38b0ea0815156bbc340c910d0a21ee57cf0000005e00000003","hash_type":"type"},"lock":{"code_hash":"0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8","args":"0xd1c872f08cba24b2adafed42a87f0df6e99623bd","hash_type":"type"}}],"outputs_data":["0x000000000000000000c000"],"witnesses":["0x55000000100000005500000055000000410000007c7dfc6d6dff302587cb8ef909d438776069ed24f297437741fadcb664f39c263208edbe8a715ed860014c51724a01a24fd8c2a1e954e5984b25916ce3170e9900"]}'
```

### Get tx by tx uuid

```
python transfer_examples.py --get_tx \
    --tx_uuid 6b68f35b-222a-4998-b379-9c29367de6ef
```

## CKB examples

There is also some utils about CKB

### Get short address and full address by private key

```
python ckb_examples.py --address_info \
    --private_key xxxxxxx \
    --network mainnet
```

### Signed tx

```
python ckb_examples.py --sign_tx \
    --private_key xxxxxxx \
    --unsigned_tx "{'version': '0x0', 'cell_deps': [{'out_point': {'tx_hash': '0x194a0f84de41d006a07ece07c96a8130100818599fcf0b2ecf49e512b873ed6e', 'index': '0x2'}, 'dep_type': 'code'}, {'out_point': {'tx_hash': '0xd346695aa3293a84e9f985448668e9692892c959e7e83d6d8042e59c08b8cf5c', 'index': '0x0'}, 'dep_type': 'code'}, {'out_point': {'tx_hash': '0x03dd2a5594ed2d79196b396c83534e050ba0ad07fa5c1cd61a7094f9fb60a592', 'index': '0x0'}, 'dep_type': 'code'}, {'out_point': {'tx_hash': '0xf8de3bb47d055cdf460d93a2a6e1b05f7432f9777c8c474abf4eec1d4aee5d37', 'index': '0x0'}, 'dep_type': 'dep_group'}], 'header_deps': [], 'inputs': [{'previous_output': {'tx_hash': '0x1cc469e1f2f1e90766dff483bfd2f01c2aaed0c8e6f47ed78a91ac8619807b03', 'index': '0x0'}, 'since': '0x0'}], 'outputs': [{'capacity': '0x31eb3ba04', 'lock': {'code_hash': '0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8', 'args': '0xd1c872f08cba24b2adafed42a87f0df6e99623bd', 'hash_type': 'type'}, 'type': {'code_hash': '0xb1837b5ad01a88558731953062d1f5cb547adf89ece01e8934a9f0aeed2d959f', 'args': '0xf90f9c38b0ea0815156bbc340c910d0a21ee57cf0000005e00000003', 'hash_type': 'type'}}], 'outputs_data': ['0x000000000000000000c000'], 'witnesses': ['0x']}"
```
