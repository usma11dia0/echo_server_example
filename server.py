import socket

HOST = 'localhost'
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

sock.listen(1)
conn, address = sock.accept()

print(f'sock:{sock}')
print(f'conn:{conn}')
print(f'address:{address}')

while True:
    pass
    # data = conn.recv(1024)
    # print(f'data: {data}')
    # # conn.sendall(data)
    # # if not data:
    # #     break

