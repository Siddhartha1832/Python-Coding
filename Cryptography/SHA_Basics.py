'''
Install below Python Module before You run this code.
>>> pip install hashlib --upgrade 
'''

import hashlib
print("\n SHA Algorithm using PYTHON \n\n 1. MD 5 \t 2. SHA 1 \t 3. SHA 224 \t 4. SHA 256 \n 5. SHA 384 \t 6. SHA 512 \t 7. SimpleHash \t 8. Exit \n")
choice = int(input("\n Enter your choice : "))

def hash_func(choice):
	if choice==8:
		print("Exiting...")
		exit(0)

	get_string = input("\n Enter your input string : ")

	if choice==1:
		# Algorithm = MD5
		hex_dig = hashlib.md5(get_string.encode()).hexdigest()
	elif choice==2:
		# Algorithm = SHA 1
		hex_dig = hashlib.sha1(get_string.encode()).hexdigest()
	elif choice==3:
		# Algorithm = SHA 224
		hex_dig = hashlib.sha224(get_string.encode()).hexdigest()
	elif choice==4:
		# Algorithm = SHA 256
		hex_dig = hashlib.sha256(get_string.encode()).hexdigest()
	elif choice==5:
		# Algorithm = SHA 384
		hex_dig = hashlib.sha384(get_string.encode()).hexdigest()
	elif choice==6:
		# Algorithm = SHA 512
		hex_dig = hashlib.sha512(get_string.encode()).hexdigest()
	elif choice==7:
		# Algorithm = Simple Hash
		hex_dig = hash(get_string)
	return hex_dig

result = hash_func(choice)
print("\n SHA value for Option",choice," is : ",result)
