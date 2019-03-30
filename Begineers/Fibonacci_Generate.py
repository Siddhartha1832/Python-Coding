print("\n *** Display Fibonacci Sequence Between User Defined Limits *** \n")

end_limit = int(input(" Enter End limit : "))
i, first_value, second_value, result = 0, 0, 1, []
           
while(i < end_limit):
	if(i <= 1):
		next_num = i
	else:
		next_num = first_value + second_value
		first_value = second_value
		second_value = next_num
	result.append(next_num)
	i += 1

print("\n The Fibonacci sequence from iteration 0 to {} : {}".format(end_limit, result))
