
print('\n Web scraping is a technique used to extract data from websites through an automated process. \n')

import requests
import bs4 as bs
url = 'http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html'
page = requests.get(url)
soup = bs.BeautifulSoup(page.content, 'lxml')
print(' Web Page URL : {}'.format(url))
print(' Web Page Status Code : {}'.format(soup.status_code))
print(' Web Page Title : {}'.format(soup.title.string))
print('\n Web Page : \n {}'.format(soup.prettify()))
print('\n Display Top level of Web Page : \n {}'.format(list(soup.children)))

print('\n Search element by "p" tag with class "outer-text" : \n {}'.format(soup.find_all('p', class_='outer-text')))
print('\n Search element by class "outer-text" : \n {}'.format(soup.find_all(class_='outer-text')))
print('\n Search element by ID "first" : \n {}'.format(soup.find_all(id='first')))
print('\n Content by ID "first" : \n {}'.format(soup.find_all(id='first')[0].get_text()))
print('\n Content by Class "outer-text" : \n {}'.format(soup.find_all(class_='outer-text')[0].get_text()))

print('\n\n BeautifulSoup objects support searching a page via CSS selectors using the select() ')
print('\n Search by div & P tag : \n {}'.format(soup.select("div p")))
