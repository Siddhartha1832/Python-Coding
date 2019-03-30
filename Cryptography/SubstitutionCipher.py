import string, random
chars = string.printable

def generate_key():
	"""Generate an key for our cipher"""
	shuffled = sorted(chars, key=lambda k: random.random())
	return dict(zip(chars, shuffled))

def encrypt(key, plaintext):
	"""Encrypt the string and return the ciphertext"""
	return ''.join(key[l] for l in plaintext)

def decrypt(key, ciphertext):
	"""Decrypt the string and return the plaintext"""
	flipped = {v: k for k, v in key.items()}
	return ''.join(flipped[l] for l in ciphertext)

if __name__ == '__main__':
	print('\n Substitution Cipher\n')
	plaintext = input(' Enter plaintext: ')
	key = generate_key()
	encrypted = encrypt(key, plaintext)
	decrypted = decrypt(key, encrypted)
	print(f' Key --> {key}')
	print(f' Plaintext --> {plaintext}')
	print(f' Encrypted --> {encrypted}')
	print(f' Decrypted --> {decrypted}')

