'''
Install below Python Module before You run this code.
>>> pip install cryptography --upgrade 
'''

from cryptography.fernet import Fernet
original_msg = input('\n Enter message to encrypt: ')
key = Fernet.generate_key()
cipher_suite = Fernet(key)
ciphertext = cipher_suite.encrypt(original_msg)
print(f'\n Ciphertext --> {ciphertext}')
plaintext = cipher_suite.decrypt(ciphertext)
print(f'\n Plaintext --> {plaintext}')
