'''
Install below Python Module before You run this code.
>>> pip install pyperclip --upgrade 
'''
import pyperclip

def encryptMessage(plaintext, key):
	ciphertext = [''] * key
	for col in range(key):
		position = col
		while position < len(plaintext):
			ciphertext[col] += plaintext[position]
			position += key
	return ''.join(ciphertext) #Cipher text

if __name__ == '__main__':
	print('\n *** Encryption of Transposition Cipher using Pyperclip *** \n')
	plaintext = input(' Enter plaintext: ')
	key = int(input(' Enter key: '))
	ciphertext = encryptMessage(plaintext, key)
	print(f' Ciphertext --> {ciphertext} |')
	pyperclip.copy(ciphertext)
