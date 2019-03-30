print("\n *** Check Prime Number *** \n")

def check_prime_number(check_prime):
	if check_prime > 1:
		for i in range(2,check_prime):
			if (check_prime % i) == 0:
				print("\n ",check_prime,"is not a prime number because ",check_prime,"= ",i," * ",check_prime//i)
				break
		else:
			print("\n {} is Prime Number ".format(check_prime))
	else:
		print("\n {} is Not Prime Number ".format(check_prime))

def generate_prime_numbers(a, b):
	result = []
	for num in range(a, b + 1):
		if num > 1:
			for i in range(2,num):
				if num % i == 0:
					break
			else:
				result.append(num)

	print("\n Prime numbers between {} and {} is {} ".format(a, b, result))


if __name__ == '__main__':
    print(" MainMenu \n 1. Check Number is Prime? \n 2. Generate Prime Numbers by User Defined Limits \n 3. Exit ")
    while True:
        choice = int(input("\n Enter your choice (1-3): "))
        if choice == 1:
            num = int(input("\n Enter a number: "))
            check_prime_number(num)
        elif choice == 2:
            start_limit = int(input('\n Enter Start Limit: '))
            end_limit = int(input(' Enter End Limit: '))
            generate_prime_numbers(start_limit, end_limit)
        elif choice == 3:
            print('\n Exiting..')
            exit(0)
        else:
            print('\n Invalid Choice, Please try again..')
