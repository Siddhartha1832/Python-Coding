import string
from random import *
print("\n *** Generate Random Passwords *** \n")
limit = int(input(" How many Random Passwords you want to Generate : "))

print('\n')
for i in range(0, limit):
	characters = string.ascii_letters + string.digits + string.punctuation
	password =  "".join(choice(characters) for x in range(randint(8,16)))
	print(" Random password  of Iteration {} => {} ".format(i+1, password))
