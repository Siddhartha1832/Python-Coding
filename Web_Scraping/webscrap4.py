
print('\n Web scraping is a technique used to extract data from websites through an automated process. \n')

import requests
import pandas as pd
import bs4 as bs
url = 'http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'
page = requests.get(url)
soup = bs.BeautifulSoup(page.content, 'lxml')
print(' Web Page URL : {}'.format(url))
print(' Web Page Status Code : {}'.format(soup.status_code))
print(' Web Page Title : {}'.format(soup.title.string))

seven_day = soup.find(id='seven-day-forecast')
forecast_items = seven_day.find_all(class_='tombstone-container')
tonight = forecast_items[0]
print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
desc = tonight.find('img')['title']

print('Forecast item : {}'.format(period))
print('Condition : {}'.format(short_desc))
print('Temperature : {}'.format(temp))
print('Description : {}'.format(desc))

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(short_descs)
print(temps)
print(descs)

weather = pd.DataFrame({"period": periods, "short_desc": short_descs, "temp": temps, "desc":descs})
print(weather)

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
print(temp_nums)

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
print(is_night)

print(weather)