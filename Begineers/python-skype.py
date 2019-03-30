'''
Install below Python Module before You run this code.
>>> pip install skpy getpass --upgrade 
'''

from skpy import Skype
import os, getpass

print('\n *** Skype using Python *** \n')
username = input(' Enter Skype Email ID: ')
password = getpass.getpass(' Enter Skype Password: ')
sk = Skype(username, password) # connect to Skype
print(f'\n Current Username: {sk.user}')
print(f' My Skype Contacts: {sk.contacts}')
print(f' My Skype Chats Conversation: {sk.chats}')