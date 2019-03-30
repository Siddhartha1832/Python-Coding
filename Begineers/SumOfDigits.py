print("\n *** Sum of Digits *** \n")

def sum_digits(value):
	total, temp = 0, value
	while value > 0:
		remainder = value % 10
		total += remainder
		value //= 10
	print("\n Sum of Digits for {} is {} ".format(temp, total))

getValue = int(input(" Enter Long Number : "))
sum_digits(getValue)