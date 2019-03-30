print("\n *** Sum of Natural Numbers *** \n")
number = int(input(" Enter Number : "))

temp = number
if number < 0:
	print("\n It Should be Positive Number..")
else:
	total = 0
	while(number > 0):
		total += number
		number -= 1
	print("\n The Sum is Natual Number for {} is {} ".format(temp, total))
