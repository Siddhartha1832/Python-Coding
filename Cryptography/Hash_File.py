'''
Install below Python Module before You run this code.
>>> pip install hashlib --upgrade 
'''

import hashlib
print("\n To Find Hash of user input File..")
filename = input("\n Enter the file name which is in the same directory (eg: sample.txt) : ")

def hash_file(filename):
   # make a hash object
   h = hashlib.sha1()
   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   # return the hex representation of digest
   return h.hexdigest()

message = hash_file(filename)
print("\n The hash of the file ({}) is {} ".format(filename,message))
