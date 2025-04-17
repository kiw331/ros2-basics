#################
#latest modified data : 2024.12.04 by Choonghyun
#################


import socket

# 서버 설정
# HOST = '192.168.123.56'  # 서버 호스트
HOST = '127.0.0.1'  # 서버 호스트
PORT = 12345        # 서버 포트 번호

# UDP 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 서버로 메시지 전송
client_socket.sendto(b"Hello, Server!", (HOST, PORT))

# 서버로부터 응답 수신
data, addr = client_socket.recvfrom(1024)
print(f"서버로부터 받은 메시지: {data.decode()}")
