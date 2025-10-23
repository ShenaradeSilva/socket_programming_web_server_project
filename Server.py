# Student Name : Hettiarachchige Mary Shenara Amodini De Silva
# Student ID : 14545786
# Assignment : Project_1
# Network Fundamentals (CINEF001)

import sys              # Importing sys module to terminate the program
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

# Sever socket preparation
serverAddress = '192.168.43.201'       # Setting up the device IP address as the server IP address
serverPort = 8968           # Setting up the port number of the server

serverSocket.bind((serverAddress, serverPort))      # Binding the server address and port
serverSocket.listen(1)                          # Listening for incoming connections

try:
    while True:
        # Connection establishment
        print('The Server is Ready to Serve...')
        connectionSocket, addr = serverSocket.accept()  # Accepting the incoming connection
        try:
            message = connectionSocket.recv(1024).decode()
            if len(message.split()) < 2:
                connectionSocket.close()            # if the message is incomplete close the connection
                continue
            filename = message.split()[1]
            with open(filename[1:], 'r') as f:      # Open and read the requested file
                outputdata = f.readlines()

            # Send HTTP header indicating successful response
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

            # Send the client the content of the requested file
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())

        except IOError:
            # response message for file not found
            not_found_response = "HTTP/1.1 404 Not Found\r\n\r\n"
            connectionSocket.send(not_found_response.encode())

            not_found_html = "<!doctype html><html><head></head><body><h1> 404 Not Found </h1></body></html>\r\n\r\n"
            connectionSocket.send(not_found_html.encode())

            # client socket close
            connectionSocket.close()

except KeyboardInterrupt:
    serverSocket.close()
    sys.exit()      # Terminate the program after handling the KeyboardInterrupt
