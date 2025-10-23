#  SOCKET PROGRAMMING WEB SERVER PROJECT 

### Overview
This project implements a simple **HTTP Web Server** and **Client** in Python as part of a networking fundamentals exercise.  
The system demonstrates how a client can send an HTTP GET request to a server and how the server responds by delivering an HTML file or a `404 Not Found` message if the file is unavailable.

---

### Features
- Handles multiple client connections (threaded version).
- Responds to HTTP GET requests.
- Serves HTML content to connected clients.
- Returns proper HTTP response codes (`200 OK`, `404 Not Found`).
- Demonstrates socket programming concepts including:
  - TCP connection setup and teardown
  - Data transmission using sockets
  - Error handling for missing files

---

### How to Run

#### 1. Start the Server
Run the server file (single-threaded or multi-threaded version):
  python Server.py
or
  python MultiThreadedServer.py
Make sure to update the serverAddress and serverPort values in the code if necessary.

#### 2. Start the Server
Use the client to request a file from the server:
  python Client.py <server_name> <server_port> <filename>

Example:
  python Client.py 192.168.43.201 8968 index.html

Example HTML File
  <html>
    <head><title>This is title</title></head>
    <body>
      Hello world
      <p>INEF001 Project 1 - HTTP Web Server</p>
      <p>Name: "Shenara De Silva"</p>
      <p>Student Number: "14545786"</p>
    </body>
  </html>

Expected Output
  Client Output (successful request):

HTTP/1.1 200 OK

<html> ... </html>
Server Console:

The Server is Ready to Serve...
File /index.html was sent on Thread-1

Client Output (file not found):
  HTTP/1.1 404 Not Found
  <!doctype html><html><body><h1>404 Not Found</h1></body></html>

---

### Key Learning Outcomes
- Understanding TCP socket programming in Python.
- Implementing basic HTTP request/response mechanisms.
- Developing a multi-threaded server to handle concurrent client requests.
- Demonstrating client-server communication fundamentals.
