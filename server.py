import socket

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on {HOST}:{PORT}")
    
    conn, address = s.accept()
    with conn:
        print(f"Connected by {address}")
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            print(data.decode('utf-8'))

            with open("www/index.html", "r") as f:
                html_content = f.read()

                http_response = "HTTP/1.1 200 OK\r\n"
                http_response += "Content-Type: text/html\r\n"
                http_response += "Connection: close\r\n" #keep-aliveとの違い
                http_response += "\r\n"
                http_response += html_content
                # http_response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{html_content}"

            conn.sendall(http_response.encode('utf-8'))




