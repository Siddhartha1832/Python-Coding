print("\n *** Display Multiplication Table *** \n")

which_table = int(input(" Enter Multiplication Table : "))
limit = int(input(" Enter Limit : "))

for i in range(1, limit+1):
   print(" {} X {} = {}".format(which_table, i, which_table * i))
