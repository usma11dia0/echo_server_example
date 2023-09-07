with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, address = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:break
            conn.sendall(data)

# リファクタリング前
# import socket

# HOST = 'localhost'
# PORT = 12345

# socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket1.bind((HOST, PORT))

# socket1.listen(1)
# (conn, address) = socket1.accept()

# print(f'socket1: {socket1}')
# print(f'conn: {conn}')
# print(f'address: {address}')

# while True:
#     data = conn.recv(1024)
#     print(data)
#     if not data:
#         break
#     conn.sendall(data)

# socket1.close()



