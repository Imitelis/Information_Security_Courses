#!/usr/bin/python3

import socket

# AF_INET for IPv4, SOCK_STREAM for TCP
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = "192.168.0.9"
# host = socket.gethostname()
host = "192.168.0.9"
port = 1404

clientsocket.connect((host, port))
message = clientsocket.recv(1024)

clientsocket.close()
print(message.decode('ascii'))
