'''
Install below Python Module before You run this code.
>>> pip install pylyrics 
'''

from PyLyrics import *
print("\n *** Get Song Lyrics using Python *** \n")

singer_name = input(" Enter Singer Name : ")
song_name = input(' Enter Song Name: ')

print("\n Artist: {} || Song Name: {} \n".format(singer_name.upper(), song_name.upper()))
print(PyLyrics.getLyrics(singer_name, song_name))