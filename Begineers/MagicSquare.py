'''
Install Python Module
>>>  pip instll magic_square
# Reference: http://mathforum.org/alejandre/magic.square/adler/adler.whatsquare.html
'''

from magic_square import *

print("\n ***Magic Square using Python *** \n")

value = int(input(" Enter N*N Magic Square : "))
print("\n Magic Square Matrix {} * {} : \n\n {} ".format(value, value, magic(value)))
