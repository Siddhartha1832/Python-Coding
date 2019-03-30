'''
Install below Python Module before You run this code.
>>> pip install vobject --upgrade 
'''

import vobject
from datetime import datetime as dt

source_file = open(r'Akash_Contact.vcf', 'r')

# bwloe for loop will add each contact name and corresponding mobile number.
for vcard in vobject.readComponents(source_file):
	print(f' Mobile Number : {vcard.tel.value} ||  Contact Name : {vcard.fn.value} ')
	