import socket   
hostname=socket.gethostname()   
IP_Address=socket.gethostbyname(hostname)   
print("\n Your Computer Name is : "+hostname)   
print("\n Your Computer IP Address is : "+IP_Address)