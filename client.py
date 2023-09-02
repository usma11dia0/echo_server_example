import socket

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
    data = s.recv(1024)

print(data.decode('utf-8'))