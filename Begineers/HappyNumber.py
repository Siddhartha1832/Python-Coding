print("\n *** Check Happy Number *** \n")
number = int(input(" Enter a Number : "))

def happy(n):
	past = set()      
	while n != 1:
		n = sum(int(i)**2 for i in str(n))
		if n in past:
			return False
		past.add(n)
	return True

if happy(number):
	print("\n {} is a Happy Number".format(number))
else:
	print("\n {} is not a Happy Number".format(number))
