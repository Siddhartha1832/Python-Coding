import bs4 as bs
import requests
import pandas as pd
# Website Quotes
url = 'https://www.brainyquote.com/topics/website'

sauce = requests.get(url)
soup = bs.BeautifulSoup(sauce.content, 'lxml')

print(' Web Page URL : {}'.format(url))
print(' Web Page Status Code : {}'.format(soup.status_code))
print(' Web Page Title : {}'.format(soup.title.string))

quote = [quote.get_text() for quote in soup.find_all(title='view quote')]
author = [author.get_text() for author in soup.find_all(title='view author')]

quotes_data = pd.DataFrame({"Author": author, "Quote": quote})
print(quotes_data)
quotes_data.to_excel('quotes_data.xlsx', index=False)
print('\n Exported data into excel sucessfully..')