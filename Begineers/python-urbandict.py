'''
Install below Python Module before You run this code.
>>> pip install requests 
'''

import requests
print(f"\n *** Urban Dictionary using Python. *** \n")

ud_define_url = 'https://api.urbandictionary.com/v0/define?term='
term = input(' Enter word: ')
resp = requests.get(ud_define_url + term)
data = json.loads(resp.text)

for data in data['list']:
	print(f"\n Word: {data['word']}")
	print(f" Definition: {data['definition']}")
	print(f" Example: {data['example']}")
	print(f" ThumpsUp Count: {data['thumbs_up']} || ThumpsDown Count: {data['thumbs_down']}")
