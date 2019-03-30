
print('\n Web scraping is a technique used to extract data from websites through an automated process. \n')

import requests
import bs4 as bs
url = 'http://dataquestio.github.io/web-scraping-pages/simple.html'
page = requests.get(url)
soup = bs.BeautifulSoup(page.content, 'lxml')
print(' Web Page URL : {}'.format(url))
print(' Web Page Status Code : {}'.format(soup.status_code))
print(' Web Page Title : {}'.format(soup.title.string))
print('\n Web Page : \n {}'.format(soup.prettify()))
print('\n Display Top level of Web Page : \n {}'.format(list(soup.children)))

type_elem = [type(item) for item in list(soup.children)]
print('\n Type of element objects : \n {}'.format(type_elem))

html_tags = list(soup.children)[1]
print('\n HTML tags : \n {}'.format(html_tags))

print('\n Childrens inside HTML tags : \n {}'.format(list(html_tags.children)))

body_tags = list(html_tags.children)[3]
print('\n Body tags : \n {}'.format(body_tags))

content = list(body_tags.children)[1]
print('\n Content in Body tag : {}'.format(content.get_text()))

# find_all() to find all instances of a tag at once.
print('\n Content : {}'.format(soup.find_all('p')[0].get_text()))
print('\n Content : {}'.format(soup.find('p').get_text()))


