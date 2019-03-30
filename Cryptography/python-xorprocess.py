def xor_crypt(plaintext, key, encode = False, decode = False):
	from itertools import izip, cycle
	import base64
	
	if decode:
		plaintext = base64.decodestring(plaintext)
	xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(plaintext, cycle(key)))

	if encode:
		return base64.encodestring(xored).strip()
	return xored


if __name__ == '__main__':
	original_message = input(' Enter Original Message: ')
	key = input(' Enter key string: ')
	ciphertext = xor_crypt(original_message, key, encode = True)
	print(f'\n Ciphertext -- > {ciphertext}')
	plaintext = xor_crypt(xor_crypt(original_message, key, encode =True), key, decode = True)
