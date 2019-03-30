'''
Install below Python Module before You run this code.
>>> pip install codecs --upgrade 

# ROT13 cipher refers to the abbreviated form Rotate by 13 places. 
# It is a special case of Caesar Cipher in which shift is always 13. 
# Every letter is shifted by 13 places to encrypt or decrypt the message.
'''

import codecs
plaintext = input(' Enter plaintext: ')
ciphertext = codecs.encode(plaintext, 'rot_13')
print(f' Ciphertext --> {ciphertext}')