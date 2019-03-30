
print('\n Web scraping is a technique used to extract data from websites through an automated process. \n')

import bs4 as bs
import requests
import urllib.request

url = 'C:/APT/Programming/python/WebScraping/index.html'

soup = bs.BeautifulSoup(open(url), 'lxml')

print(' Web Page URL : {}'.format(url))
print(' Web Page Status Code : {}'.format(soup.status_code))
print(' Web Page Title : {}'.format(soup.title.string))
print('\n Web Page : \n {}'.format(soup.prettify()))

print('\n First Hyperlink text in Paragraph tag : {}'.format(soup.find_all(id='learn-link')[0].get_text()))
print('\n Second Hyperlink text in Paragraph tag : {}'.format(soup.select("p a")[1].get_text()))

print('\n First Paragraph and Hyperlink tag text : {}'.format(soup.select("p")[0].get_text()))
print(' Second Paragraph and Hyperlink tag text : {}'.format(soup.select("p")[1].get_text()))
