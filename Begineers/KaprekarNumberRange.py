print("\n *** Generate Kaprekar Numbers from user Defined Range *** \n")
get_num = int(input(" Enter Upper limit for Kaprekar Numbers : "))

def Kaprekar(n):
	n2 = str(n**2)
	for i in range(len(n2)):
		a, b = int(n2[:i] or 0), int(n2[i:])
		if b and a + b == n:
			return n

print("\n Kaprekar Numbers between the range 1 - {} : {} ".format(get_num,([x for x in range(1,get_num) if Kaprekar(x)])))
