#!/usr/bin/python3

import socket

# Creates the socket object
# AF_INET for IPv4, SOCK_STREAM for TCP
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configures port and host
# host = "192.168.0.9"
# host = socket.gethostname()
port = 1404
host = "192.168.0.9"

# Establishes connection
clientsocket.connect((host, port))

# Receives data from server
message = clientsocket.recv(1024)

# Closes socket
clientsocket.close()

# Prints message
print(message.decode('ascii'))