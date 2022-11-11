import cryptos as cp
""" The aim of this module was to extend the capability of the api for extra coins using cryptos module.
    But it seems that the except Bitcoin`s adrresses other coins addrress is not valid in blockchain. """
    
coin_list = [cp.Bitcoin(),cp.BitcoinCash(),cp.Litecoin(),cp.Dash(),cp.Doge()]
acr_coin =['btc/','bch/','ltc/','dash/','doge/']

for crpt,acr in zip(coin_list,acr_coin):    
    crypto = crpt
    priv = cp.sha256('a big long brainwallet password'+str(49))
    pub = crypto.privtopub(priv)
    addr = crypto.pubtoaddr(pub)
    r = requests.get('https://www.blockchain.com/'+acr+'address/'+addr)
    st_code = r.status_code
    print(f'{acr},{addr},{st_code}')