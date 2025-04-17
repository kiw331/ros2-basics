import sys

def main():
    # sys.argv[0]은 스크립트 파일의 이름이므로, 실제 인수는 sys.argv[1:]에 저장됩니다.
    args = sys.argv[1:]
    print(f'\nSource code is "{sys.argv[0]}"\n')

    # print(args) # 전체 Parameter 출력
    if len(args) < 2:
        print("Usage: python example.py <name> <number>")
        sys.exit(1)

    name = args[0]

    try:
        number = int(args[1])  # 두 번째 인수는 번호로 처리
    except ValueError:
        print("Number should be an integer.")
        sys.exit(1)

    # 결과 출력
    print(f"Hello, {name}! Your number is {number}.\n")
 
# 프로그램이 직접 실행될 때만 main 함수 실행
if __name__ == "__main__":
    main()
