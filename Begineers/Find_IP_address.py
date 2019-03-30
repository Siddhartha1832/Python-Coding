import socket   
hostname = socket.gethostname()   
IP_Address = socket.gethostbyname(hostname)   
print("\n Your Computer HostName is : " + hostname)   
print("\n Your Computer IP Address is : " + IP_Address)
