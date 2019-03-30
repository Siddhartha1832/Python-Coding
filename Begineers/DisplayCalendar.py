import calendar  
print("\n *** Display a Calendar *** \n")

year = int(input(" Enter Year (eg: 2019) : "))  
month = int(input(" Enter Month (eg: 1-12) : "))  

print("\n The calendar for the month {} and year {} is \n\n {} ".format(month, year, calendar.month(year,month)))