#リファクタリング後
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello World')
    data = s.recv(1024)
print(data)



# # リファクタリング前
# import socket

# HOST = 'localhost'
# PORT = 12345

# socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket2.connect((HOST, PORT))
# socket2.sendall(b'Hello World')

# data = socket2.recv(1024)
# print(data)