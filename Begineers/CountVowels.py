print("\n *** Count Number of Vowels from User Input *** \n")
getString = input(" Enter the sentence : ").lower()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys('aeiou', 0)

# count the vowels
for char in getString:
	if char in count:
		count[char] += 1

print("\n Vowels Count From Your Input is {} ".format(count))
