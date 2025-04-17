import subprocess

def dir():
    result = subprocess.run(['dir'], capture_output=True, text=True, shell=True)
    print("Output of 'dir' command:")
    print(result.stdout)

def ipconfig():
    result = subprocess.run(['ipconfig'], capture_output=True, text=True, shell=True)
    print("Output of 'ipconfig' command:")
    print(result.stdout)

def notepad():
    result = subprocess.run(['notepad.exe'], capture_output=True, text=True, shell=True)
    print("Output of 'notepad' command:")
    print(result.stdout)

def pbrush():
    result = subprocess.run(['pbrush.exe'], capture_output=True, text=True, shell=True)
    print("Output of 'pbrush' command:")
    print(result.stdout)

def calc():
    result = subprocess.run(['calc.exe'], capture_output=True, text=True, shell=True)
    print("Output of 'calc' command:")
    print(result.stdout)

if __name__ == "__main__":
    dir()
    # # ipconfig()
    # notepad()
    # pbrush()
    # # calc()
