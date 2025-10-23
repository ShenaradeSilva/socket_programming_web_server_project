# Student Name : Hettiarachchige Mary Shenara Amodini De Silva
# Student ID : 14545786
# Assignment : Project_1
# Network Fundamentals (CINEF001)

import sys
from socket import *


def http_client(server_name, server_port, filename):
    # Creation of a TCP socket for the client
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Connect to the specified server and port
    clientSocket.connect((server_name, server_port))

    # Creates an HTTP request message
    httprequestmessage = f"GET /{filename} HTTP/1.1\r\nHost: {server_name}\r\n\r\n"

    # Send the HTTP request message to the server
    clientSocket.send(httprequestmessage.encode())

    # Receive and print the HTTP response message from the server
    httpresponsemessage = ""
    while True:
        newmsg = clientSocket.recv(1024).decode()
        if not newmsg:
            break
        httpresponsemessage += newmsg
    print(httpresponsemessage)

    # Close the client socket
    clientSocket.close()


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        message = "Usage : Client.py server_name server_port filename"
        print(message)
        sys.exit(1)

    # Parse command-line arguments
    # noinspection PyUnreachableCode
    server_name = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    # Call the http_client function with the provided arguments
    http_client(server_name, server_port, filename)
