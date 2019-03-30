'''
Install below Python Module before You run this code.
>>> pip install getpass moviepy InstagramAPI --upgrade
'''

from InstagramAPI import InstagramAPI
import getpass
print("\n *** Instagram API using Python *** \n")

username = input(' Enter Instagram UserName: ')
password = getpass.getpass(' Enter Instagram password: ')
api = InstagramAPI(username, password)

if api.login():
	print("Login succes!")
else:
	print("Can't login!")

api.getUsernameInfo(api.username_id)
details = api.LastJson
print(f" UserID: {details['user']['pk']} || UserName: {details['user']['username']} || FullName: {details['user']['full_name']} || Total Posts : {details['user']['media_count']} || Total Followers : {details['user']['follower_count']} || Total Followings : {details['user']['following_count']} || Private? : {details['user']['is_private']} || Biography: {details['user']['biography']}")

print('\n Following: \n')
api.getUserFollowings(api.username_id)
details1 = api.LastJson
for data in details1['users']:
	print(f" UserID: {data['pk']} || UserName: {data['username']} || FullName: {data['full_name']} || Private Account? : {data['is_private']} || Is Favourite: {data['is_favorite']}")

print('\n Followers: \n')
api.getUserFollowers(api.username_id)
details2 = api.LastJson
for data in details2['users']:
	print(f" UserID: {data['pk']} || UserName: {data['username']} || FullName: {data['full_name']} || Private Account? : {data['is_private']}")
