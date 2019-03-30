'''
Install below Python Module before You run this code.
>>> pip install base64 --upgrade 
'''

# Base64 encoding converts the binary data into text format, which is passed 
# through communication channel where a user can handle text safely. 
# Base64 is also called as Privacy enhanced Electronic mail (PEM) and is primarily 
# used in email encryption process.

import base64
print('\n *** Base64 Encoding and Decoding *** \n')
plaintext = input(' Enter plaintext: ')
encoded_data = base64.b64encode(plaintext.encode('utf-8'))
print(f'\n Encoded Data --> {encoded_data}')
decoded_data = base64.b64decode(encoded_data).decode('utf-8')
print(f'\n Decoded Data --> {decoded_data}')
