#!/usr/bin/python3

import socket

# Creates the socket object
# AF_INET for IPv4, SOCK_STREAM for TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configures port and host
# host = "192.168.0.9"
# host = socket.gethostname()
port = 1404
host = "192.168.0.9"

# Finds the socket
serversocket.bind((host, port))

# Starts TCP server
# Specify number of listeners
serversocket.listen(3)

while True:
    # Accepts incoming connection
    clientsocket, address = serversocket.accept()

    # Prints address
    print("received connection from %s" % str(address))

    # Creates message
    message = "hello! Thank you for connecting to the server" + "\r\n"

    # Sends message
    clientsocket.send(message.encode('ascii'))

    # Closes connection
    clientsocket.close()