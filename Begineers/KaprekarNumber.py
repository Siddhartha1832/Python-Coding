print("\n *** Check Kaprekar Number *** \n")
get_num = int(input(" Enter input number : "))

def Kaprekar(n):
	n2 = str(n**2)
	for i in range(len(n2)):
		a, b = int(n2[:i] or 0), int(n2[i:])
		if b and a + b == n:
			return n

if Kaprekar(get_num):
	print("\n {} is Kaprekar Number".format(get_num))
else:
	print("\n {} is Not a Kaprekar Number".format(get_num))
