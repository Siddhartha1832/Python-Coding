'''
Install below Python Module before You run this code.
>>> pip install request bs4 
'''

import requests, json
from bs4 import BeautifulSoup
from datetime import datetime
print("\n *** Latest Technology News from inshorts.com *** ")

resp = requests.get('https://inshorts.com/en/read/technology')
soup = BeautifulSoup(resp.content, 'lxml')
raw_data = soup.find_all('div', class_='news-card z-depth-1')
for data in raw_data:
	news_title = data.find('div', class_='news-card-title news-right-box').find('a').get_text().replace('\n','')
	news_content = data.find('div', class_='news-card-content news-right-box').find('div').get_text()
	news_date = datetime.strptime(data.find('span', class_='time')['content'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d-%m-%Y %I:%M:%S %p")
	print(f"\n Title: {news_title} \n Published Date: {news_date} \n Content: {news_content} ")
