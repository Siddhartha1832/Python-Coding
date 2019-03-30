'''
Install below Python Module before You run this code.
>>> pip install requests 
'''

import requests, json
print("\n *** Cricket Match Calendar *** \n")

resp = requests.get('https://cricapi.com/api/matchCalendar?apikey=vMmjfYwgk2P8Z9EIIm5CbkuBIYI2').text
raw_data = json.loads(resp) # convert string to json data

for data in raw_data['data']:
	print(f" Unique ID: {data['unique_id']} || Date: {data['date']} || Name: {data['name']} ")
