'''
Client Server Program using Socket in Python!
- Open 2 Command Prompt(s) or Terminal(s)
- Save 2 Files (Server.py, Client.py) in Same Folder/Location.
- First Terminal >> Run Server Program  
>>> python Server.py
- Second Terminal >> Run Client Program  
>>> python Client.py
'''

# Server.py
import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
while True:
	c, addr = s.accept()
	print('Got connection from', addr)
	c.send(b'Thank you for connecting')
	c.close()
   
  
# Client.py
import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
print(s.recv(1024))
s.close()
