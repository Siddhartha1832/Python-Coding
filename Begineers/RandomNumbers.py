import random
print("\n *** Generate Random Numbers Between User Defined Range. *** \n")

start_range = int(input(" Enter Start Range : "))
end_range = int(input(" Enter End Range : "))
iterations = int(input("\n How many Random Numbers You want to Generate : "))

print('\n')
for i in range(0, iterations):
	print(" Random number for iteration {} is : {}".format(i+1, random.randint(start_range, end_range)))
