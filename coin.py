from bitcoin import *

from eth_account import Account
import secrets

import requests
base_http='https://www.blockchain.com/'

def btc_add():
    private_key = random_key()
    gen_add = privkey_to_address(private_key)
    r = requests.get(base_http+'btc/address/'+gen_add)
    stat_code = r.status_code
    if stat_code==200:
        return f'{gen_add}'
    else:
        return 'Not Successful'


def eth_add():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acc = Account.from_key(private_key)
    gen_add = acc.address
    r = requests.get(base_http+'eth/address/'+gen_add)
    stat_code = r.status_code
    if stat_code==200:
        return f'{gen_add}'
    else:
        return 'Not Successful'

# import requests

# r = requests.get(base_http+'eth/address/'+gen_add)
# r.status_code

# one_use = ''