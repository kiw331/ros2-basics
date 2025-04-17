import argparse

# main 함수 정의
def main():
    # ArgumentParser 객체 생성
    parser = argparse.ArgumentParser(description="Command line argument example")

    # 명령줄 인수 정의
    parser.add_argument("name", help="Your name")
    parser.add_argument("age", type=int, help="Your age")
    
    # 선택적인 인수 추가 (예: 기본값을 제공)
    parser.add_argument("-g", "--greeting", type=str, default="Hello", help="Greeting message")

    # 명령줄 인수 파싱
    args = parser.parse_args()

    # 인수 사용
    print(f"{args.greeting}, {args.name}! You are {args.age} years old.")

# 프로그램이 직접 실행될 때만 main 함수 실행
if __name__ == "__main__":
    main()