print("\n *** Identity Matrix. *** \n")

get_num = int(input(" How Many Numbers You Want : "))
print("\n")

for i in range(0, get_num):
	for j in range(0, get_num):
		if i == j:
			print("1", sep=" ", end=" ")
		else:
			print("0", sep=" ", end=" ")
	print("\n")
