import os, base64
from pprint import pformat
os.system("clear")
alphabet = [
    "\U0001f600",
    "\U0001f603",
    "\U0001f604",
    "\U0001f601",
    "\U0001f605",
    "\U0001f923",
    "\U0001f602",
    "\U0001f609",
    "\U0001f60A",
    "\U0001f61b",
]
MAX_STR_LEN = 70
OFFSET = 10
N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
P="\033[0;35m"
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '+' + G + '] '
success = G + '[' + W + '+' + G + '] '
error = R + '[' + W + '⚠️' + R + ']'

def obfuscate(VARIABLE_NAME, file_content):
    b64_content = base64.b64encode(file_content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code


def chunk_string(in_s, n):
    """Chunk string to max length of n"""
    return "\n".join(
        "{}\\".format(in_s[i : i + n]) for i in range(0, len(in_s), n)
    ).rstrip("\\")


def encode_string(in_s, alphabet):
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (
        'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")])))\n'.format(
            pformat(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(ord(c))) for c in in_s),
                MAX_STR_LEN,
            ),
        )
    )



        

def encryptem():
    in_file= input("\n\n"+ask + C + "Input File " + G + "> " + B)
    if not os.path.exists(in_file):
            print(error+' File not found')
            os.system("sleep 2")
            encryptem()
    out_file=(in_file+"MCK-A.py")
    if os.path.exists(in_file):
        with open(in_file) as in_f, open(out_file, "w") as out_f:
            out_f.write("# Encrypted by MD ALAMIN CHOWDOWRY\n# Github- https://github.com/HANTER2\n\n")
            out_f.write(encode_string(in_f.read(), alphabet))
            print(success+out_file+" saved in current directory")
            if os.path.exists("/sdcard/Download"):
                os.system("cp -r "+out_file+" /sdcard/Download")
                print(success+ out_file + " copied to Download or /sdcard/Download")
            if os.path.exists("/home/Downloads"):
                os.system("cp -r "+out_file+" /home/Downloads")
                print(success+ out_file + " copied to Downloads or /home/Downloads")
                print("save This file"+out_file) 
            os.system("sleep 3")
            a=input("Do You Went manu: ")
            main()
    elif not os.path.isfile(in_file) or not path.endswith('.py'):
        print(error+'Invalid file')
        exit()
    elif IOError:
        print(error+"File not found")
    else:
        print(error+"Error!")
        exit()

os.system("clear")
import requests


import os,requests
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
black="\033[0;30m"
pink="\x1b[95m"
blue="\x1b[94m"
underline='\x1b[4m'
colouroff="\x1b[00m"

os.system('clear')
r=requests.get('https://pastebin.com/raw/Ga6ej4mA').text
logu=(pink+f"""
\t  ____      _   _      ____
\t / ___|    | | | |    | __ )
\t| |        | |_| |    |  _ \    """+colouroff+underline+"""CYBER HUNTER BD"""+colouroff+pink+"""
\t| |___     |  _  |    | |_) |
\t \____|    |_| |_|    |____/ 
\n"""+blue+"""           Focous on Your Aim, You Will winner""")


line=end+"\n__________________________________________________________"
def a():
	print(logu+"\n\n	"+green+"   Developed By : MD ALAMIN CHOWDORY"+green+"\n\n 	"+red+"   Version :"+r+"Python code encrpt "+line)

a()

    
    
 

encryptem()          
