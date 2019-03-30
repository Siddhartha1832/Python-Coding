'''
Install below Python Module before You run this code.
>>> pip install requests 
'''

import requests
supported_currencies = 'https://api.coindesk.com/v1/bpi/supported-currencies.json'
coindesk_api = 'https://api.coindesk.com/v1/bpi/currentprice.json'

resp1 = requests.get(coindesk_api)
resp2 = requests.get(supported_currencies)

print(f"\n *** Last Updates - Bitcoin Price Index -  {resp1.json()['time']['updated']} *** \n")
country_code = [code['currency'] for code in resp2.json()]

for code in country_code:
	resp3 = requests.get(f'https://api.coindesk.com/v1/bpi/currentprice/{code}.json')
	extract = resp3.json()['bpi'][code]
	print(f" Bitcoin Price Index for {code} || Price : {resp3.json()['bpi'][code]['rate']} || Description : {resp3.json()['bpi'][code]['description']} ")
