'''
Install below Python Module before You run this code.
>>> pip install omdb --upgrade
'''

import omdb
print("\n *** Movie Search in omdb.com *** \n")
api_key = '85772176'
omdb.set_default('apikey', api_key)
movie_name = input('\n Enter Movie Name to Search: ')
raw_data = omdb.search(movie_name)

for data in raw_data:
	print(f" Title: {data['title']} || Year: {data['year']} ||  IMDB ID: {data['imdb_id']} || Type: {data['type']}")
