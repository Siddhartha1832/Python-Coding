'''
Install below Python Module before You run this code.
>>> pip install --upgrade pygithib getpass

# Github Login - https://github.com/login
# Github SignUp - https://github.com/join
'''

import os, getpass
from github import Github
print("\n *** Github API using Python *** \n")
username = input(' Enter your Github Username: ')
password = getpass.getpass(' Enter yout Github Password:')
ghub = Github(username, password)
current_user = ghub.get_user()
print(f"\n Current GitHub User Name: {current_user.login}")
print(f" Current GitHub User FullName: {current_user.name}")
print(f" Total Repositories for Current GitHub User: {current_user.public_repos}")
repositories = [repo.name for repo in ghub.get_user().get_repos()]
print(f" Repositories for Current GitHub User: {repositories}")
