import datetime

import requests
import time

url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=USD,EUR'

data = requests.get(url=url)
data = data.json()
btc = data['BTC']['USD']
eth = data['ETH']['USD']
ltc = data['LTC']['USD']

mensage = f'BTC: $ {btc} \nETH: $ {eth} \nLTC: $ {ltc}'
print(mensage)
print(datetime.datetime(hour=24))

