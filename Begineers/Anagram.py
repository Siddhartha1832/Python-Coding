print("\n *** Anagram ***\n ")

def isAnagram(first_string, second_string):
	string1 = ''.join(sorted(first_string)).casefold()
	string2 = ''.join(sorted(first_string)).casefold()
	if string1 == string2:
		print("\n Both input strings are Anagram..")
	else:
		print("\n Both input strings are Not Anagram..")

first_string = input(" Enter First String : ")
second_string = input(" Enter Second String : ")

isAnagram(first_string, second_string)
