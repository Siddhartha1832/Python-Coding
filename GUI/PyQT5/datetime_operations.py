# example 1 - datetime operations

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

cur_date = QDate.currentDate()
print(f"\n Current Date - PyQt5 Format: {cur_date}")
print(f" Current Date - ISO Format: {cur_date.toString(Qt.ISODate)}")
print(f" Current Date - Default Locale:{cur_date.toString(Qt.DefaultLocaleLongDate)}")
print(f" Days in month: {cur_date.daysInMonth()}")
print(f" Days in year: {cur_date.daysInYear()}")

next_xmas = QDate(2018, 12, 25)
print(f"\n There are {cur_date.daysTo(next_xmas)} days until next Christmas")

print(f"\n Gregorian date for today: {cur_date.toString(Qt.ISODate)}")
print(f"\n Julian day for today: {cur_date.toJulianDay()}") 

cur_datetime = QDateTime.currentDateTime()
print(f"\n Current DateTime - PyQt5 Format: {cur_datetime}")
print(f" Current DateTime - ISO Format: {cur_datetime.toString(Qt.ISODate)}")
print(f" Current DateTime - Default Locale: {cur_datetime.toString(Qt.DefaultLocaleLongDate)}")
print(f" Universal DateTime: {cur_datetime.toUTC().toString(Qt.ISODate)}")
print(f" The offset from UTC is: {cur_datetime.offsetFromUtc()} seconds")

print(f"\n Adding 12 days: {cur_datetime.addDays(12).toString(Qt.DefaultLocaleLongDate)}")
print(f" Subtracting 22 days: {cur_datetime.addDays(-22).toString(Qt.DefaultLocaleLongDate)}")
print(f" Adding 50 seconds: {cur_datetime.addSecs(50).toString(Qt.DefaultLocaleLongDate)}")
print(f" Adding 3 months: {cur_datetime.addMonths(3).toString(Qt.DefaultLocaleLongDate)}")
print(f" Adding 12 years: {cur_datetime.addYears(12).toString(Qt.DefaultLocaleLongDate)}")

print(f"\n DateTime Zone Abbreviation: {cur_datetime.timeZoneAbbreviation()}")
if cur_datetime.isDaylightTime():
    print("\n The current date falls into DST time")
else:
    print("\n The current date does not fall into DST time")

cur_time = QTime.currentTime()
print(f"\n Current Time - PyQt5 Format: {cur_time}")
print(f" Current Time - ISO Format: {cur_time.toString(Qt.ISODate)}")
print(f" Current Time - Default Locale: {cur_time.toString(Qt.DefaultLocaleLongDate)}")

borodino_battle = QDate(1812, 9, 7)
slavkov_battle = QDate(1805, 12, 2)
j_today = cur_date.toJulianDay()
j_borodino = borodino_battle.toJulianDay()
j_slavkov = slavkov_battle.toJulianDay()
print(f"\n Days since Slavkov battle: {j_today - j_slavkov}")
print(f" Days since Borodino battle: {j_today - j_borodino}")
