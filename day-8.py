# day 8 of learning python

#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target= socket.gethostbyname(sys.argv[1]) #for translating host name to IPv4

else:
    print("Invalid Argument")
    print("Syntax: python3 day-8.py")

# adding a pretty banner

print("_"*50)
print("Scanner target:" +target)
print("Time started:" +str(datetime.now()))
print("_"*50)

try:
    for port in range(50,85):
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = s.connect_ex((target,port))
        if result== 0 :
            print(f"port {port} is open")
        s.close()
    
except KeyboardInterrupt:
    print("\n exiting program.....")
    sys.exit()

except socket.gaierror:
    print("hostname could not be resolved")
    sys.exit()

except socket.error:
    print("could connect to server")
    sys.exit()