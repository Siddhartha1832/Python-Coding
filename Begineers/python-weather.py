'''
Install below Python Module before You run this code.
>>> pip install requests --upgrade

# Get the API key sign up to open weather map
# https://home.openweathermap.org/users/sign_up

'''

import json, requests
print("\n *** Weather Report using Python *** \n")

api_key = '28a31767a1909138a53410a56233a326'
city = input(' Enter City Name in any Country : ')
resp = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
data = json.loads(resp.text)
print(f" City - {(data['name']).upper()}")
print(f" Coordinates - Latitude {data['coord']['lat']} & Longitude {data['coord']['lon']}")
print(f" Description - {(data['weather'][0]['description']).upper()}")
print(f" Temperature - {data['main']['temp']} F")
print(f" Humidity - {data['main']['humidity']}")
print(f" Wind Speed - {data['wind']['speed']}")