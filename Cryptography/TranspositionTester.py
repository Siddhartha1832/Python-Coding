'''
Install below Python Module before You run this code.
>>> pip install pyperclip --upgrade 
'''

import math, pyperclip, random,sys

print("\n *** Transposition Tester using Python *** \n")
def main():
	message = input("\n Enter original message : ")
	myKey = int(input("\n Enter the key number : "))
	ciphertext = encryptMessage(myKey, message)
	print("Transposition Encrypt : ",ciphertext + '|')
	pyperclip.copy(ciphertext)
	plaintext = decryptMessage(myKey, ciphertext)
	print("Transposition Decrypt : ",plaintext + '|')
	pyperclip.copy(plaintext)

def encryptMessage(key, message):
	ciphertext = [''] * key
	for col in range(key):
		pointer = col
		while pointer < len(message):
			ciphertext[col] += message[pointer]
			pointer += key
	return ''.join(ciphertext)

def decryptMessage(key, message):
	numOfColumns = math.ceil(len(message) / key)
	numOfRows = key
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
	plaintext = [''] * numOfColumns
	col,row = 0,0
	for symbol in message:
		plaintext[col] += symbol
		col += 1
		if (col == numOfColumns) or (col == numOfColumns - 1 and row >=numOfRows - numOfShadedBoxes):
			col,row = 0, row+1
	return ''.join(plaintext)

def transpositionTest():
	random.seed(42) # set the random "seed" to a static value
	tests = int(input("Hpw many tests you want to run : "))
	for i in range(tests):
		message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
		message = list(message)
		random.shuffle(message)
		message = ''.join(message) # convert list to string
		print('Test #%s: "%s..."' % (i+1, message[:50]))
		for key in range(1, len(message)):
			encrypted = encryptMessage(key, message)
			decrypted = decryptMessage(key, encrypted)
			if message != decrypted:
				print('Mismatch with key %s and message %s.' % (key,message))
				print(decrypted)
				sys.exit()
	print('Transposition cipher test passed.')

if __name__ == '__main__':
	main()
	print("\n Transposition Tester program started..")
	transpositionTest()
