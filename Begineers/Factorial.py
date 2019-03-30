print("\n *** Find the factorial of given Number *** \n")

num = int(input(" Enter Number to Find Factorial : "))
factorial = 1

# check if the number is negative, positive or zero
if num < 0:
	print("\n Sorry, Factorial Does Not Exist for Negative Numbers..")
elif num == 0:
	print("\n The Factorial of 0 is 1")
else:
	for i in range(1, num + 1):
		factorial = factorial * i
	print("\n The Factorial of {} is {} ".format(num,factorial))
