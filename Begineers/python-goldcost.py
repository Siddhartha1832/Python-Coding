import requests, json, os
from datetime import datetime
from bs4 import BeautifulSoup

print("\n *** Getting Gold Rates TODAY in India Major Cities *** \n")

resp = requests.get('https://www.goodreturns.in/gold-rates/')
soup = BeautifulSoup(resp.content, 'lxml')

data = [data.get_text() for data in soup.find_all('div', class_='gold_silver_table')[2].find_all('td')]
data = [data[i:i+3] for i in range(0, len(data), 3)]
for data in data[1:]:
	print(f" City: {data[0]} || 22 Carat Gold Today: {data[1]} || 24 Carat Gold Today: {data[2]}")
