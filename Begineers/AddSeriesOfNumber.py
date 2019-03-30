print("\n *** Read a Number N and Compute the Series '1 + 2 + … + n = ' *** \n")
result = []
get_number = int(input(" How many numbers you want : "))

for i in range(1, get_number+1):
	print(i, end = " ")
	if( i < get_number):
		print("+",end = " ")
	result.append(i)

print(" = {}".format(sum(result)))