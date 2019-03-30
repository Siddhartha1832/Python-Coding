print("\n *** Reverse String and Numbers *** \n")

def reverse_string(original_str):
    print("\n Method-1 Using reversed() => {}".format("".join(reversed(original_str))))
    print("\n Method-2 Using string[::-1] => {}".format(original_str[::-1]))

def reverse_number(original_num):
    temp = original_num
    RevNumber = 0
    while(original_num > 0):
        digit = original_num % 10
        RevNumber = RevNumber * 10 + digit
        original_num = original_num // 10
    print("\n Reverse Number of {} is {} ".format(temp, RevNumber))


if __name__ == '__main__':
    print(" MainMenu \n 1. Reverse String \n 2. Reverse Number \n 3. Exit ")
    while True:
        choice = int(input("\n Enter your choice (1-3): "))
        if choice == 1:
            input_str = input("\n Enter Input String to Reverse: ")
            reverse_string(input_str)
        elif choice == 2:
            inpt_num = int(input('\n Enter Input Number to Reverse : '))
            reverse_number(inpt_num)
        elif choice == 3:
            print('\n Exiting..')
            exit(0)
        else:
            print('\n Invalid Choice, Please try again..')