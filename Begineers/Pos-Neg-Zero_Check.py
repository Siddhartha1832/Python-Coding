print("\n *** Check If a Number is Positive, Negative or Zero \n")

number = int(input(" Enter a number to check +ve, -ve or zero : "))
if number > 0:
	print("\n {} is a Positive number".format(number))
elif number == 0:
	print("\n Zero")
else:
	print("\n {} is a Negative number".format(number))
