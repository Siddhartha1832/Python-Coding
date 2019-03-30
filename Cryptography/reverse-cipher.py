'''
Install below Python Module before You run this code.
>>> pip install cryptography --upgrade 
'''

plaintext = 'This is program to explain reverse cipher.'
print(f' Plaintext -> {plaintext}')

# Method1
print(f' Method1 - Ciphertext -> {plaintext[::-1]}')

# Method2
aa = plaintext[::-1]
ciphertext = '' #cipher text is stored in this variable
i = len(plaintext) - 1

while i >= 0:
	ciphertext = ciphertext + plaintext[i]
	i -= 1

print(f' Method2 - Ciphertext -> {ciphertext}')
