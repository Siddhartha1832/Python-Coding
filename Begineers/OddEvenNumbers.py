print("\n *** Check a Number is Odd or Even *** \n")

def check_odd_even(n):
    if (n % 2) == 0:
        print("\n {} is Even number".format(n))
    else:
        print("\n {} is Odd number".format(n)) 

def generate_odd_even_num(a, b):
    odd_numbers, even_numbers = [], []
    for i in range(a, b+1):
        if (i % 2) == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    print("\n {} Odd numbers between {} and {} are {}".format(len(odd_numbers), a, b, odd_numbers))
    print("\n {} Even numbers between {} and {} are {}".format(len(even_numbers), a, b, even_numbers))


if __name__ == '__main__':
    print(" MainMenu \n 1. Check Number is Odd / Even \n 2. Generate Odd and Even number by User Defined Limits \n 3. Exit ")
    while True:
        choice = int(input("\n Enter your choice (1-3): "))
        if choice == 1:
            num = int(input("\n Enter a number: "))
            check_odd_even(num)
        elif choice == 2:
            start_limit = int(input('\n Enter Start Limit: '))
            end_limit = int(input(' Enter End Limit: '))
            generate_odd_even_num(start_limit, end_limit)
        elif choice == 3:
            print('\n Exiting..')
            exit(0)
        else:
            print('\n Invalid Choice, Please try again..')
