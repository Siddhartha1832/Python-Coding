'''
Install below Python Module before You run this code.
>>> pip install pyicloud getpass --upgrade 
'''

from pyicloud import PyiCloudService
import getpass
print("\n *** Apple iPhone Info *** \n")

apple_id = input("\n Enter mail id : ")
apple_id_password = getpass.getpass(" Enter password : ")
api = PyiCloudService(apple_id, apple_id_password)

print(" Devices : ",api.devices)
print(" Device[0] :",api.devices[0])
print(" iPhone :",api.iphone)
print(" iPhone Location :",api.iphone.location())
print(" iPhone Status :",api.iphone.status())
print(" iPhone PlaySound :",api.iphone.play_sound())

phone_number = input("\n Enter your Mobile Number with Extension : ")
message = input(" Enter alert message : ")
print(" {} , Wait for 10-15secs to get alert sound ".format(api.iphone.lost_device(phone_number, message)))
