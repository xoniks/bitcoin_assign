import cryptos as cp

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