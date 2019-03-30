print("\n *** Arithmetic operarions *** \n")
first_number = int(input(" Enter the first number : "))
second_number = int(input(" Enter the second number : "))

print("\n Addition of {} and {} is {}".format(first_number,second_number,first_number+second_number))
print(" Subraction of {} and {} is {}".format(first_number,second_number,first_number-second_number))
print(" Multiplication of {} and {} is {}".format(first_number,second_number,first_number*second_number))
print(" Division of {} and {} is {}".format(first_number,second_number,float(first_number+second_number)))
print(" Square root of {} is {} \n".format(first_number,float(first_number**0.5)))

exponential = int(input("Enter the exponential value for first number : "))
print("\n Answer: {} ^ {} = {}".format(first_number, exponential, first_number**exponential))
