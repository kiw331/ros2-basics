## socketClient.py 수정
import socket
import sys

args = sys.argv
if len(sys.argv) < 2:
    print("No arguments were provided.")

server_ip = sys.argv[1]
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, 8080))
    print("서버에 연결되었습니다.")

    client_socket.sendall(b'Hello, Server!')
    data = client_socket.recv(1024)
    print(f"서버로부터 받은 데이터: {data.decode()}")

except Exception as e:
    print(f"오류 발생: {e}")

finally:
    client_socket.close()
    
    



