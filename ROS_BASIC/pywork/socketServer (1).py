import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(1)

connection, address = server_socket.accept()
print(f"클라이언트{address}가 연결되었습니다.")

data = connection.recv(1024)
print(f"클라이언트로 부터 받은 데이터: {data.decode()}")
connection.sendall(b'Hello, Client!')

connection.close()
server_socket.close()
