import math

print("\n *** Compute a Polynomial Equation *** \n")
print(" Enter the Coefficients of the form  =>  ax^3 + bx^2 + cx + d \n")

result = []
for i in range(0,4):
	a = int(input(" Enter coefficient {} : ".format(i+1)))
	result.append(a)

x = int(input(" Enter the value of X : "))
sum_result, j = 0, 3
for i in range(0,3):
	while j > 0:
		sum_result = sum_result + (result[i] * math.pow(x,j))
		break
	j -= 1

sum_result += result[3]
print("\n The value of the polynomial is {} ".format(sum_result))
