print("\n *** Average, Maximum and Minimum of Numbers.. *** \n")

limit = int(input(" How many numbers : "))
result = []
for i in range(0, limit):
	get_value = int(input(" Enter the value {} : ".format(i+1)))
	result.append(get_value)

print("\n Numbers are {}".format(result))
print("\n Average of above numbers : {} ".format(sum(result)/limit))
print("\n Maximum is {} and Minimum is {} ".format(max(result),min(result)))
