'''
Install below Python Module before You run this code.
>>> pip install --upgrade requests bs4
# Pyttsx is a Good Text-to-Speech Conversion library in python 
'''

import requests, json, os
from datetime import datetime
from bs4 import BeautifulSoup
print("\n *** Getting Fuel Cost in India by States *** \n")
state_in_india = ['New-Delhi, New Delhi', 'Kolkata, West Bengal', 'Mumbai, Maharashtra', 'Chennai, Tamil Nadu', 'Agartala, Tripura', 'Aizwal, Mizoram', 'Ambala, Haryana', 'Bengaluru, Karnataka', 'Bhopal,Madhya Pradesh', 'Bhubhaneswar, Odisha', 'Chandigarh, Chandigarh', 'Dehradun, Uttarakhand', 'Ahmedabad, Gujarat', 'Gandhinagar, Gujarat', 'Guwahati, Assam', 'Hyderabad, Telangana', 'vijayawada, Andhra Pradesh', 'Itanagar, Arunachal Pradesh', 'Jaipur, Rajasthan', 'Jammu,Jammu And Kashmir', 'Jullunder, Punjab', 'Kohima,Nagaland', 'Lucknow, Uttar Pradesh', 'Panjim, Goa', 'Patna,Bihar', 'Pondicherry, Pondicherry', 'Port Blair,Andaman And Nicobar', 'Raipur, Chattisgarh', 'Ranchi, Jharkhand', 'Shillong, Meghalaya', 'Shimla, Himachal Pradesh', 'Srinagar, Jammu And Kashmir', 'Trivandrum, Kerala', 'Faridabad, Haryana', 'Gurgaon, Haryana', 'Noida, Uttar Pradesh', 'Ghaziabad, Uttar Pradesh', 'Amaravathi, Andhra Pradesh', 'Silvasa, Dadra And Nagar Haveli', 'Gangtok, Sikkim', 'Imphal, Manipur']

for state in state_in_india:
	state_name = state.split(',')[0]
	resp = requests.get(f"https://www.petroldieselprice.com/petrol-diesel-price-in-{state_name}")
	soup = BeautifulSoup(resp.content, 'lxml')
	data = soup.find_all('div', id='order_review')[0].find_all('td')
	print(f" State: {state} || Today: {data[0].get_text()} || Petrol Price: {data[2].get_text()} || Diesel Price: {data[4].get_text()}")
