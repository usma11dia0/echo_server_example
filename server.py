import socket

# サーバーの設定
server_ip = '127.0.0.1'
server_port = 12345

# ソケットを作成
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ソケットのバインド
server_sock.bind((server_ip, server_port))

# ソケットのリッスン
server_sock.listen(1)
print('サーバーが起動しました。')

# クライアントからの接続を待つ
client_sock, client_address = server_sock.accept()
print(f'{client_address}から接続しました。')

# クライアントからのデータを受信する
data = client_sock.recv(1024)
print(f'クライアントからのデータ: {data.decode()}')

# クライアントにデータを送信する
client_sock.sendall('Hello, Client!'.encode())

# ソケットを閉じる
client_sock.close()
server_sock.close()
print('サーバーを停止しました。')