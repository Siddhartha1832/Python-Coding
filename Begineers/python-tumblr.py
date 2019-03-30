'''
Install below Python Module before You run this code.
>>> pip install PyTumblr --upgrade 

# Register New Tumblr Account - https://www.tumblr.com/register
# Login Tumblr Account - https://www.tumblr.com/login
# Get your Tumblr API - https://www.tumblr.com/oauth/apps
'''

import pytumblr
# Replace below 4 attributes by your account keys. 
consumer_key = 'Fujij0qLDIZvvCSvszjDjJNwHS0HG7AvEDLVc9HjZ3QrLOVzeV'
consumer_secret = 'ElV3ycTGrPoqs1ps8hgK6YhSIM8IXhzEfMzEdjNlqwU9fkygq6'
oauth_token = '9mddjfpBPA5M9evglsfcJq39XWIIqEyziOmV8EIzywJgfHEIp8'
oauth_token_secret = 'QeD9qi5zNcTZrJCfX8CfxsJZj5T6V819uxL3QQjN1GnwpZr8VI'

client = pytumblr.TumblrRestClient(consumer_key, consumer_secret, oauth_token, oauth_token_secret)

print(f"\n User Info: {client.info()}")
print(f"\n Dashboard: {client.dashboard()}")
print(f"\n Likes: {client.likes()}")
print(f"\n Following: {client.following()}")
