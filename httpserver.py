import socket
import os

OK_RESULT = b"HTTP/1.1 200 OK\n\n"
PAGE_NOTFOUND = b"HTTP/1.1 404 Not Found\n\n"
CURRENT_DIR = os.path.dirname(os.path.realpath("__file__"))

HOST, PORT = 'localhost', 8888
BUFFER_SIZE = 1024

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print ('Serving HTTP server:\n')
print ('HOST: %s\n' %HOST)
print ('PORT: %s\n' %PORT)
while True:
    c_connection, c_address = listen_socket.accept()
    request = c_connection.recv(BUFFER_SIZE)
    print (request)

    if c_address == "/" or "/index.html":
        file = open(CURRENT_DIR + "/index.html", "rb")
        c_connection.send(OK_RESULT + file.read())
        file.close()

    elif c_address == "/about/aboutme.html":
        file = open(CURRENT_DIR + "/about/aboutme.html", "rb")
        c_connection.send(OK_RESULT + file.read())
        file.close()
    
    else:
        c_connection.send(PAGE_NOTFOUND)
        file.close()
    
    c_connection.close()

listen_socket.close()