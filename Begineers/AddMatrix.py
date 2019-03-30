print("\n *** Addition of Two Matrices *** \n")
storage = []
	
row_col = int(input(" Enter how many row and columns you want : "))
print("\n Matrax A and B -> {} X {} = {} \n".format(row_col,row_col,row_col*row_col))

A=[[[] for i in range(row_col)] for i in range(row_col)]
for i in range(row_col):
	for j in range(row_col):
		number = int(input(" Enter Elements of Matrix A[{}][{}] : ".format(i,j))) 
		A[i][j] = number

B=[[[] for i in range(row_col)] for i in range(row_col)]
for i in range(row_col):
	for j in range(row_col):
		number = int(input(" Enter Elements of Matrix B[{}][{}] : ".format(i,j))) 
		B[i][j] = number

print("\n Matrix A is {} ".format(A))
print("\n Matrix B is {} ".format(B))

result = [[A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]

storage = [res for res in result]

print("\n The Addition of Matrix A and B is {} ".format(storage))
