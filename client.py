import socket

# サーバーの設定
server_ip = '127.0.0.1'
server_port = 12345

# ソケットを作成
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# サーバーに接続
client_socket.connect((server_ip, server_port))

# サーバーにデータを送信する
client_socket.sendall('Hello, Server!'.encode())

# サーバーからのデータを受信する
data = client_socket.recv(1024)
print(f'受信データ: {data.decode()}')

# ソケットを閉じる
client_socket.close()