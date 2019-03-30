'''
Install below Python Module before You run this code.
>>> pip install requests bs4
'''

import requests, datetime
from bs4 import BeautifulSoup

# Get Month & Date like March7
month_day = datetime.datetime.now().strftime('%B%d')
resp = requests.get(f"https://www.famousbirthdays.com/{month_day.lower()}.html")
soup = BeautifulSoup(resp.content, 'lxml')
dataset = soup.find_all('a', class_='face person-item')

print(f"\n *** Get Birthday List from famousbirthdays.com on {month_day.upper()} *** \n")
for data in dataset:
	name = data.find_all('div', class_='name')[0].get_text().strip()
	title = data.find_all('div', class_='title')[0].get_text()
	print(f" Name (Age): {name} || Title: {title}")
