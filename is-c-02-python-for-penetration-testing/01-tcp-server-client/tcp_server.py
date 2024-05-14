#!/usr/bin/python3

import socket

# AF_INET for IPv4, SOCK_STREAM for TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = "192.168.0.9"
# host = socket.gethostname()
host = "192.168.0.9"
port = 1404

serversocket.bind((host, port))

# Specify number of listeners
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    
    print("received connection from %s" % str(address))
    message = "hello! Thank you for connecting to the server" + "\r\n"
    
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()
