import socket, sys
from datetime import datetime

print("\n *** Port Scanner *** \n")
remoteServer = input(" Enter Remote Host to Scan : ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("\n Please Wait, Scanning Remote Host ({} => {}) \n".format(remoteServer,remoteServerIP))

try:
    # Here it will Scans All Ports Between 1 and 1024
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {} : Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("\n You pressed Ctrl+C")
    exit(0)

except socket.gaierror:
    print("\n Hostname could not be resolved. Exiting")
    exit(0)

except socket.error:
    print("\n Couldn't connect to server")
    exit(0)
