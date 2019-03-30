print("\n *** Remove Punctuations From User Defined String *** \n")

getString = input(" Enter some sentence with punctuations : ")
# Define Punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

no_punct = ""
for char in getString:
	if char not in punctuations:
		no_punct = no_punct + char

print("\n Sentence After Remove Punctuation : {} ".format(no_punct))
