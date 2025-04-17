import sys

def main():
    # sys.argv[0]은 스크립트 파일의 이름이므로, 실제 인수는 sys.argv[1:]에 저장됩니다.
    args = sys.argv[1:]

    # 인수가 하나 이상일 경우 출력
    print(f'\nSource code is {sys.argv[0]}\n')

    if len(args) >= 2:
        print(f'{args[0]+ " " + args[1]}\n')
    else:
        print("No arguments were provided.")
  
if __name__ == "__main__":
    main()
