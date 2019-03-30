print("\n *** Multiply Two Matrices *** \n")
	
row_col = int(input(" Enter how many row and columns you want : "))
print("\n Matrax A and B -> {} X {} = {} \n".format(row_col,row_col,row_col*row_col))

A = [[[] for i in range(row_col)] for i in range(row_col)]
for i in range(row_col):
	for j in range(row_col):
		number = int(input(" Enter Elements of Matrix A[{}][{}] : ".format(i,j))) 
		A[i][j] = number

print('\n')

B = [[[] for i in range(row_col)] for i in range(row_col)]
for i in range(row_col):
	for j in range(row_col):
		number = int(input(" Enter Elements of Matrix B[{}][{}] : ".format(i,j))) 
		B[i][j] = number

print("\n Matrix A is {} ".format(A))
print("\n Matrix B is {} ".format(B))

result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*B)] for X_row in A]
storage = [res for res in result]
print("\n The Multiplication of Matrix A and B is  {} ".format(storage))