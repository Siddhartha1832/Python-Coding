def split_len(seq, length):
	return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):
	order = {int(val): num for num, val in enumerate(key)}
	ciphertext = ''
	for index in sorted(order.keys()):
		for part in split_len(plaintext, len(key)):
			try:
				ciphertext += part[order[index]]
			except IndexError:
				continue
	return ciphertext

if __name__ == '__main__':
	print('\n *** Columnar Transposition Cipher *** \n')
	plaintext = input(' Enter plaintext: ')
	ciphertext = encode('3214', plaintext)
	print(f'\n Ciphertext --> {ciphertext}')
