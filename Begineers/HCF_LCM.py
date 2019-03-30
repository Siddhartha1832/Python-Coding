print("\n *** Find HCF & LCM of 2 Numbers Using Euclidian Algorithm. *** \n")

first_num = int(input(" Enter First Number : "))
second_num = int(input(" Enter Second Number : "))

# HCF or GCD both are same
def computeHCF(first_num, second_num):
	while(second_num):
		first_num, second_num = second_num, first_num % second_num
	return first_num

def computeLCM(first_num, second_num):
	lcm = (first_num*second_num)//computeHCF(first_num,second_num)
	return lcm

print("\n The HCF of {} and {} is {}.".format(first_num, second_num, computeHCF(first_num, second_num)))
print("\n The LCM of {} and {} is {}.".format(first_num, second_num, computeLCM(first_num, second_num)))
