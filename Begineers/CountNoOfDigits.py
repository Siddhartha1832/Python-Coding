print("\n *** Count Number of Digits. *** \n")
getNumber = int(input(" Enter Long Number (eg:23464) : "))

def count_digits(getNumber):
	count, temp_var = 0, getNumber
	while getNumber > 0:
		count += 1
		getNumber = getNumber // 10
	print("\n Count of {} is {} ".format(temp_var, count))

count_digits(getNumber)