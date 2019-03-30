print("\n *** Sort Words in Alphabetic Order *** \n")

getString = input("\n Enter Input Sentence : ")

words = getString.split()
words.sort() # sort the list
result = [word for word in words]

print("\n The Distinct Sorted Words From Input String : {} ".format(set(result)))
