print("\n *** Generate Happy Number betoween User Defined Range. *** \n")

number = int(input(" Enter the Upper Limit for happy numbers : "))

def happy(n):
	past = set()
	while n != 1:
		n = sum(int(i)**2 for i in str(n))
		if n in past:
			return False
		past.add(n)
		return True

happyn = [x for x in range(1, number) if happy(x)]
print(" \n Happy Numbers between the range 1 - {} : {} ".format(str(number), happyn))
print(" \n happy Numbers Count : {}".format(len(happyn)))