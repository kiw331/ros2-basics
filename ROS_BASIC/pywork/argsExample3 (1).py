import sys

def main():
    # sys.argv[0]은 스크립트 파일의 이름이므로, 실제 인수는 sys.argv[1:]에 저장됩니다.
    args = sys.argv[1:]

    sum = 0

    # 인수가 하나 이상일 경우 출력
    if len(args) > 0:
        for arg in args:
            sum = int(arg) + sum
            print(f"{arg}")
    else:
        print("No arguments were provided.")

    print(f'\nsum = {sum}\n')
if __name__ == "__main__":
    main()
