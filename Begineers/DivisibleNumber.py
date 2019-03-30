print("\n *** To Find Numbers Divisible by Another Number.. *** \n ")

start_range = int(input(' Enter Start Range: '))
end_range = int(input(' Enter End Range: '))
numbers = [i+1 for i in range(start_range, end_range)]
print('\n Numbers are {} '.format(numbers))

divisible = int(input("\n Enter the divisible number : "))
numbers = list(filter(lambda x: (x % divisible == 0), numbers))
print("\n Numbers divisible by {} are {} ".format(divisible,numbers))
