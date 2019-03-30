print("\n *** String Comparison *** \n")

def string_compare(str1, str2):
	str1, str2 = str1.lower(), str2.lower()
	if str1 == str2:
		print("\n TRUE -> Both strings are equal")
	else:
		print("\n FALSE -> Both strings are not equal")

getString1 = input(" Enter First String : ")
getString2 = input(" Enter Second String : ")

string_compare(getString1, getString2)