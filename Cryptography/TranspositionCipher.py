'''
Install below Python Module before You run this code.
>>> pip install pyperclip --upgrade 
'''
import math, pyperclip

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

if __name__ == '__main__':
	print("\n *** Transposition Encryption & Decryption using Python *** \n")
	message = input("\n Enter original message : ")
	myKey = int(input("\n Enter the key number : "))
	ciphertext = encryptMessage(myKey, message)
	print("Transposition Encrypt : ",ciphertext + '|')
	pyperclip.copy(ciphertext)
	plaintext = decryptMessage(myKey, ciphertext)
	print("Transposition Decrypt : ",plaintext + '|')
	pyperclip.copy(plaintext)
