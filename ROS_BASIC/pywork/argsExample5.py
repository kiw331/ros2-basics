import sys

def main():
    args = sys.argv[1:]
    strings = ""
    number = 0

    if len(args) > 0:
        print("Received arguments:")
        for arg in args:
            if arg.isdigit():  # 숫자인지 확인
                number += int(arg)
                print(f"Number: {arg}")
            else:
                print(f"String: {arg}")           
                strings += arg

        print(f'Strings : {strings}')
#        print(f"String : {args[2]+args[3]}") # 숫자로 형변환 하지 않는 경우 문자열로 연결됨
        
#        number = int(args[2]) + int(args[3])    
#        print(f"Number : {number}")

    else:
        print("No arguments were provided.")

if __name__ == "__main__":
    main()
