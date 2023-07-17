import socket

HOST = 'localhost'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(b'Helloooooooooooo, world')

while True:
    data = client.recv(1024)
    if not data:
        break
    print(data)

print('end')


