import threading
import time

# 작업1: 1초 대기 후 실행
def task1():
    print("Task 1 시작")
    time.sleep(5)
    print("Task 1 완료")

# 작업2: 2초 대기 후 실행
def task2():
    print("Task 2 시작")
    time.sleep(9)
    print("Task 2 완료")

# 작업3: 3초 대기 후 실행
def task3():
    print("Task 3 시작")
    time.sleep(2)
    print("Task 3 완료")

# 메인 함수
def main():
    # 스레드 생성
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    thread3 = threading.Thread(target=task3)

    # 스레드 시작
    thread1.start()
    thread2.start()
    thread3.start()

    # 모든 스레드가 종료될 때까지 대기
    thread1.join()
    thread2.join()
    thread3.join()

    print("모든 작업 완료")

if __name__ == "__main__":
    main()
