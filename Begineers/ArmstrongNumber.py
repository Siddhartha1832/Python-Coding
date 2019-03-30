print("\n To Find Armstrong number...")
# eg: 663,407
number = int(input("\n Enter value to find armstrong number : "))
sum = 0

temp = number
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if number == sum:
   print("\n {} is an Armstrong number".format(number))
else:
   print("\n {} is not an Armstrong number".format(number))
