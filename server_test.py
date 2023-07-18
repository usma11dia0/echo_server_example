import socket

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    conn, address = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            data_str = data.decode('utf-8')
            print(f'data: {data_str}')
            if not data:
                break
            conn.sendall(data)

# tmp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tmp.bind((HOST, PORT))
# tmp.listen(10)

# print(f'tmp: {tmp}')

# conn, address = tmp.accept()

# print(f'conn: {conn}')
# print(f'address: {address}')

# while True:
#     data = conn.recv(1024)
#     print(f'data: {repr(data)}')
#     if not data:
#         break
#     conn.sendall(data)

# print('end')
    



