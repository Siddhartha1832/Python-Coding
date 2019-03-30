print("\n *** Check String & Number is Palindrome or Not \n")

def string_check_palindrime(original_str):
    # reverse the string
    rev_str = reversed(original_str)
    if list(original_str) == list(rev_str):
        print("\n {} is Palindrome ".format(original_str))
    else:
        print("\n {} is Not Palindrome ".format(original_str))

def number_check_palndrome(original_num):
    temp, rev = original_num, 0
    while original_num > 0:
        dig = original_num % 10
        rev = rev * 10 + dig
        original_num //= 10

    if temp == rev:
        print("\n Number {} is Palindrome".format(temp))
    else:
        print("\n Number {} is Not Palindrome".format(temp))


if __name__ == '__main__':
    print(" MainMenu \n 1. Check String is Palindrome? \n 2. Check Number is Palindrome? \n 3. Exit ")
    while True:
        choice = int(input("\n Enter your choice (1-3): "))
        if choice == 1:
            getString = input("\n Enter Input String : ").upper()
            string_check_palindrime(getString)
        elif choice == 2:
            getNumber = int(input('\n Enter Input Number : '))
            number_check_palndrome(getNumber)
        elif choice == 3:
            print('\n Exiting..')
            exit(0)
        else:
            print('\n Invalid Choice, Please try again..')
