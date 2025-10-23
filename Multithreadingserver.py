# Student Name : Hettiarachchige Mary Shenara Amodini De Silva
# Student ID : 14545786
# Assignment : Project_1
# Network Fundamentals (CINEF001)

import threading
from socket import *


def startprogram():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverAddress = '192.168.43.201'
    serverPort = 8968

    serverSocket.bind((serverAddress, serverPort))
    serverSocket.listen(4)          # Listen for up to maximum of 4 connections

    print(f"The Sever is Ready to Serve on port {serverPort}")

    while True:
        # Accepts a connection and start a new thread to handle it
        connectionSocket, addr = serverSocket.accept()

        thread = threading.Thread(target=process_client, args=(connectionSocket, addr))
        thread.start()


def process_client(connectionSocket, addr):
    print(f"[NEW_CONNECTION] Connection from {addr} is Connected.")

    connected = True
    while connected:
        try:
            # Receives and processes the client's request
            message = connectionSocket.recv(1024).decode()
            if len(message.split()) < 2:
                connectionSocket.close()
                return

            # Extracts the requested filename from the client's message
            filename = message.split()[1]
            print('File', filename, ' was sent on ', str(threading.current_thread().name))

            # Open and read the requested file in binary mode
            with open(filename[1:], 'rb'):
                outputdata = filename.readlines()

                # Send the content of the requested file to the client
                for line in outputdata:
                    connectionSocket.send(line)

                # Send HTTP header indicating successful response
                connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n").encode()
            filename.close()

            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

        except IOError:
            # Handle file not found error
            not_found_response = "HTTP/1.1 404 Not Found\r\n\r\n"
            connectionSocket.send(not_found_response.encode())

            not_found_html = "<!doctype html><html><head></head><body><h1> 404 Not Found! </h1></body></html>\r\n\r\n"
            connectionSocket.send(not_found_html.encode())
            connectionSocket.close()
        exit()              # Exit the thread


print("The Sever is Ready to Serve...")

if __name__ == "__main__":
    startprogram()
