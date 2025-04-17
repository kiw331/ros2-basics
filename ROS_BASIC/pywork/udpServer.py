import socket

# 서버 설정
HOST = '0.0.0.0'  # 로컬 호스트
PORT = 12345        # 포트 번호

# UDP 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

print("UDP 서버가 대기 중입니다...")

# 클라이언트로부터 데이터 수신
data, addr = server_socket.recvfrom(1024)
print(f"{addr}에서 받은 메시지: {data.decode()}")

# 클라이언트로 응답 전송
server_socket.sendto(b"Hello, Client! This is UDP Socket!", addr)
