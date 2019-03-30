import datetime
now = datetime.datetime.now()

print("\n *** Current Date and Time using StringFrameFormat() *** \n")
print(" Using strftime() : {} ".format(now.strftime("%Y-%m-%d %H:%M:%S")))

print("\n *** Current Date and Time using Intance Attributes. *** \n")
print(" Current Date -> Day {}, Month {} and Year {}.".format(now.day, now.month, now.year))
print(" Current Time -> Hour {}, Minutes {}, Seconds {} and Microseconds {} \n".format(now.hour, now.minute, now.second, now.microsecond))
