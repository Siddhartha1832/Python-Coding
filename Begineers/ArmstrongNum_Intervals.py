print("\n *** Armstrong Numbers Between User Defined Ranges. *** \n")

start_range = int(input(" Enter Start Range : "))
end_range = int(input(" Enter End Range : "))
result = []

for num in range(start_range, end_range + 1):
	order = len(str(num))
	total = 0
	temp = num
	while temp > 0:
		digit = temp % 10
		total += digit ** order
		temp //= 10
	if num == total:
		result.append(num)

print("\n Armstrong between {} and {} is {} ".format(start_range, end_range, result))

## example - start range 10 and end range 1000
