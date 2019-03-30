'''
Install below Python Module before You run this code.
>>> pip install requests 
'''

import requests
url = 'https://rest.coinapi.io/v1/exchanges'
headers = {'X-CoinAPI-Key' : '7DCD93E7-1E74-4738-A80D-82C3B3906162'}
response = requests.get(url, headers=headers)
raw_data = response.json()
print(raw_data)