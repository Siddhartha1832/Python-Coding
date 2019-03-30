print("\n *** Check the Year is a Leap Year or Not *** \n")

year = int(input(" Enter year (eg:2019) : "))

if (year % 4) == 0:
	if (year % 100) == 0:
		if (year % 400) == 0:
			print("\n {} is a leap year".format(year))
		else:
			print("\n {} is not a leap year".format(year))
	else:
		print("\n {} is a leap year".format(year))
else:
	print("\n {} is not a leap year".format(year))
