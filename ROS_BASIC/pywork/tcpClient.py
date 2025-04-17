import socket

# 클라이언트 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결 요청
client_socket.connect(('127.0.0.1', 8080))
# client_socket.connect(('192.168.10.57', 8080)) # Server IP Address
print("서버에 연결되었습니다.")

# 데이터 전송 및 수신
client_socket.sendall(b'Hello, Server!')
data = client_socket.recv(1024)
print(f"서버로부터 받은 데이터: {data.decode()}")

# 소켓 종료
client_socket.close()
