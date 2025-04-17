import socket

def client_program():
    # host = "192.168.123.56"  # 서버 IP 주소 (localhost)
    host = "127.0.0.1"  # 서버 IP 주소 (localhost)
    port = 12345        # 서버 포트 번호

    # 클라이언트 소켓 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))  # 서버에 연결

    print(f"Connected to server {host}:{port}")

    while True:
        client_message = input("You: ")
        client_socket.send(client_message.encode())
        if client_message.lower() == "bye":
            print("Closing connection.")
            break

        # 서버 메시지 수신
        server_message = client_socket.recv(1024).decode()
        if server_message.lower() == "bye":
            print("Server disconnected.")
            break
        print(f"Server: {server_message}")

    client_socket.close()  # 연결 닫기

if __name__ == "__main__":
    client_program()
