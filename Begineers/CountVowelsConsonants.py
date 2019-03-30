print("\n *** Count Number of Vowels & Consonants From User Input string *** \n")

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

getString = input(" Enter input string: ").lower()
getString = getString.lower()

# Make a Dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels, 0)

# Count the Vowels
for char in getString:
	if char in count:
		count[char] += 1

# Count Number of Vowels
no_of_vowels = sum(getString.count(c)for c in vowels)
# Count Number of Consonants
no_of_consonents = sum(getString.count(c)for c in consonants)

print("\n Vowels Count From Your Input is {} ".format(count))
print("\n Number of Vowels From Your Input is {}".format(no_of_vowels))
print("\n Number of Consonants From Your Input is {}".format(no_of_consonents))
