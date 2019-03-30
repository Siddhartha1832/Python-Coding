print("\n *** Display All Possible Combinations from User Input Range *** \n")
result, count = [], 0
getCount = int(input(" Enter a Number: "))

for i in range(0, getCount):
	getValue = int(input(" Enter value {} : ".format(i+1)))
	result.append(getValue)

print("\n Possible combinations are \n")
for i in range(0,getCount):
	for j in range(0,getCount):
		for k in range(0,getCount):
			for l in range(0,getCount):
				for m in range(0,getCount):
					if(i!=j & j!=k & k!=l & l!=m & m!=i):
						print("Iteration {} \t => {} {} {} {} {} ".format(count+1, result[i], result[j], result[k], result[l], result[m]))
						count+=1
