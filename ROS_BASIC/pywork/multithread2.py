import threading
import time

# 스레드에서 실행할 함수
def print_numbers():
    for i in range(1, 20):
        print(f"Number {i}")
        time.sleep(0.5)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter {letter}")
        time.sleep(2)

# 메인 함수
def main():
    # 첫 번째 스레드 생성
    thread1 = threading.Thread(target=print_numbers)
    
    # 두 번째 스레드 생성
    thread2 = threading.Thread(target=print_letters)

    # 스레드 시작
    thread1.start()
    thread2.start()

    # 모든 스레드가 종료될 때까지 대기
    thread1.join()
    thread2.join()

    print("모든 작업 완료")

if __name__ == "__main__":
    main()
