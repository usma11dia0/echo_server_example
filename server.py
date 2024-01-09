import socket

HOST = 'localhost'
PORT = 12345

# 拡張子とMIMEタイプのマッピング
EXTENSION_TO_MIME = {
    'html': 'text/html',
    'txt': 'text/plain',
    'png': 'image/png',
    'jpg': 'image/jpg',
    'jpeg': 'image/jpeg',
    'gif': 'image/gif',
    'css': 'text/css',
    'js': 'text/javascript'
}

def content_type(path):
    # ファイルの拡張子を取得
    ext = path.split('.')[-1]
    # 拡張子に対応するMIMEタイプを返す
    return EXTENSION_TO_MIME.get(ext, 'text/plain')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    # リスニングソケット(サーバーソケット)
    print(f'----------Listening socket(server socket): {s}------------')
    print(f"Listening on {HOST}:{PORT}")
    
    while True:
        conn, address = s.accept()
        # 接続ソケット(クライアントソケット)
        print(f'----------connect socket : {conn}------------')
        with conn:
            print(f"Connected by {address}")
            while True:
                data = conn.recv(1024)
                print(data)
                if not data:
                    break
                print(data.decode('utf-8'))

                # リクエストの解析
                request_lines = data.decode('utf-8').split('\r\n')
                request_line = request_lines[0]
                method, path, version = request_line.split(' ')
                
                # ドキュメントルートへのリクエスト対応
                if path == "/":
                    path = "/index.html"

                mime_type = content_type(path)

                print(f'request_line:{request_line}')
                print(f'method:{method},path:{path},version:{version},mime_type:{mime_type}')

                if method == "GET":
                    if path == "/index.html":
                        with open("www/index.html", "r") as f:
                            html_content = f.read()

                            http_response = "HTTP/1.1 200 OK\r\n"
                            http_response += f'Content-Type: {mime_type}\r\n'
                            http_response += "Connection: keep-alive\r\n"
                            http_response += "\r\n"
                            http_response += html_content
                    
                     # ウェブブラウザにより自動的に送られるfaviconのGETリクエスト対応
                    if path == "/favicon.ico":
                        with open("www/favicon.ico", "rb") as f:
                            icon_data = f.read()
                        
                        http_response = "HTTP/1.1 200 OK\r\n"
                        http_response += "Content-Type: image/x-icon\r\n"
                        http_response += "Content-Length: {}\r\n".format(len(icon_data))
                        http_response += "Connection: keep-alive\r\n"
                        http_response += "\r\n"

                        conn.sendall(http_response.encode('utf-8') + icon_data)

                    # レスポンスを送信
                    conn.sendall(http_response.encode('utf-8'))
                
                # データ送信が完了したらbreakでループを抜ける
                print(f'----------response end------------')
                break


# 参考URL
# https://kei-kmj.hatenablog.com/entry/2023/06/19/125411
