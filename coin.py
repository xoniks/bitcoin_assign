from bitcoin import *

from eth_account import Account
import secrets

import requests
#base url to check if the addresses created is valid
base_http='https://www.blockchain.com/'

#this function creates address for bitcoin using bitcoin module without any private key
def btc_add():
    private_key = random_key()
    gen_add = privkey_to_address(private_key)
    r = requests.get(base_http+'btc/address/'+gen_add)
    stat_code = r.status_code
    #this part validates if the created address exists on blockchain
    if stat_code==200:
        return f'{gen_add}'
    else:
        return 'Not Successful'

#this function creates address for etherium using web3 and secrets module without any private key
def eth_add():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acc = Account.from_key(private_key)
    gen_add = acc.address
    r = requests.get(base_http+'eth/address/'+gen_add)
    stat_code = r.status_code
    #this part validates if the created address exists on blockchain
    if stat_code==200:
        return f'{gen_add}'
    else:
        return 'Not Successful'

