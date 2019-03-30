# pip install imdbpy

import imdb
from imdb.Person import Person
from imdb.Movie import Movie
from imdb.Company import Company

def searchMovie(movie_name):
	try:
		for movie in ia.search_movie(movie_name):
			print(f" Movie ID: {movie.movieID} || Movie Name: {movie['title']}")
	except e:
		print(' Something went wrong! I guess internet connection problem or input might be invalid! please try again..')

def searchPerson(person_name):
	try:
		for people in ia.search_person(person_name):
			print(f" People ID: {people.personID} || People Name: {people['name']}")
	except e:
		print(' Something went wrong! I guess internet connection problem or input might be invalid! please try again..')

def searchCompany(company_name):
	try:
		for company in ia.search_company(company_name):
			print(f" Company ID: {company.companyID} || Movie Name: {company['name']}")
	except e:
		print(' Something went wrong! I guess internet connection problem or input might be invalid! please try again..')

def getMovie(movie_id):
	try:
		movie = ia.get_movie(movie_id)
		director = ''.join(director['name'] for director in movie['directors'])
		genre = ''.join(genre for genre in movie['genres'])
		print(f"\n Movie CurrentInfo: {movie.current_info} \n Movie ID: {movie.movieID} \n Movie Name: {movie['title']} \n Movie Director: {director} \n Movie Genre: {genre}")
		print(f" Movie Plot: {movie['plot'][0]} \n Movie Information Set: {movie.infoset2keys['main']} \n Movie Cast: ")
		for actor in movie['cast']:
			print(f" Actor ID: {actor.personID} || Actor Name: {actor['name']} || Role/Character Name: {actor.notes}")
		print('\n Crew Members info: ')
		for crew_memeber in movie['art department']:
			print(f" Crew Member ID: {crew_memeber.personID} || Crew Member Name: {crew_memeber['name']} || Role/Character Name: {crew_memeber.notes}")
	except e:
		print(' Something went wrong! I guess internet connection problem or input might be invalid! please try again..')

def getPerson(person_id):
	try:
		people = ia.get_person(person_id)
		print(f" People ID: {people.personID} \n People Name: {people['name']} \n Person DOB: {people['birth date']}")
	except e:
		print(' Something went wrong! I guess internet connection problem or input might be invalid! please try again..')

def getCompany(company_id):
	try:
		company = ia.get_company(company_id)
		print(f"\n Company ID: {company.companyID} || Movie Name: {company['name']}")
	except e:
		print(' Something went wrong! I guess internet connection problem or input might be invalid! please try again..')

def searchKeyword(keyword):
	try:
		print(f"\n Keywords are {ia.search_keyword(keyword)}")
	except e:
		print(' Something went wrong! I guess internet connection problem or input might be invalid! please try again..')

def getKeyword(keyword):
	try:
		kword = ia.get_keyword(keyword)
		for index in range(len(kword)):
			print(f" Movie ID: {kword[index].movieID} || Movie Name: {kword[index]['title']}")
	except e:
		print(' Something went wrong! I guess internet connection problem or input might be invalid! please try again..')

def informationset():
	try:
		print(f"\n Movie Information Set : {ia.get_movie_infoset()}")
		print(f"\n People Information Set : {ia.get_person_infoset()}")
		print(f"\n Company Information Set : {ia.get_company_infoset()}")
	except e:
		print(' Something went wrong! I guess internet connection problem or input might be invalid! please try again..')

def defaultinfo():
	try:
		print(f"\n Default info for Movie: {Movie.default_info}")
		print(f" Default info for Person: {Person.default_info}")
		print(f" Default info for Company: {Company.default_info}")
	except e:
		print(' Something went wrong! I guess internet connection problem or input might be invalid! please try again..')


if __name__ == '__main__':
	ia = imdb.IMDb()
	# print(Person.default_info) #
	print('\n *** IMDB using Python *** ')
	print(""" 
		1. Search Movie by Name || 2. Search People by Name || 3. Search Company by Name || 4. Search Movie by ID
		5. Search People by ID || 6. Search Company by ID || 7. Search Keyword || 8. Get keywords 
		9. Get Top 250 Movies || 10. get Bottom 100 Movies || 11. Information Set || 12. Default Information || 13. Exit
		""")
	choice = int(input('\n Enter your choice (1-13): '))
	while True:
		if choice == 1:
			movie_name = input('\n Enter Movie name: ')
			searchMovie(movie_name)
		elif choice == 2:
			person_name = input('\n Enter Person name: ')
			searchPerson(person_name)
		elif choice == 3:
			company_name = input('\n Enter Company name: ')
			searchCompany(company_name)
		elif choice == 4:
			movie_id = input('\n Enter Movie ID: ')
			getMovie(movie_id)
		elif choice == 5:
			person_id = input('\n Enter Person ID: ')
			getPerson(person_id)
		elif choice == 6:
			company_id = input('\n Enter Company ID: ')
			getCompany(company_id)
		elif choice == 7:
			keyword = input('\n Enter keyword: ')
			searchKeyword(keyword)
		elif choice == 8:
			keyword = input('\n Enter keyword: ')
			getKeyword(keyword)
		elif choice == 9:
			for movie in ia.get_top250_movies():
				print(f" MovieID : {movie.movieID} || MovieName: {movie['title']}")
		elif choice == 10:
			for movie in ia.get_bottom100_movies():
				print(f" MovieID : {movie.movieID} || MovieName: {movie['title']}")
		elif choice == 11:
			informationset()
		elif choice == 12:
			defaultinfo()
		elif choice == 13:
			print(' Thankyou! Exiting..')
			exit(0)
		else:
			print(' Invalid choice.. PLease try again..')
		choice = int(input('\n Enter your choice (1-13): '))
