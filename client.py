import socket

HOST = 'localhost'
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.sendall(b'Hello world')
# data = sock.recv(1024)
# print(data)