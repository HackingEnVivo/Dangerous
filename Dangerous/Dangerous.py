#!/usr/bin/python

import sys
import os
import webbrowser
import platform
import subprocess
import Cryptool.cryptool
import ftplib
import ConfigParser
import urllib
import gzip
import csv


def limpiar():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')

def menu():

    limpiar()
    print '''
\033[1;32m                                 _____
    |""""""""""""|======[\033[1;31m *** \033[1;m  |  __ \ 
\033[1;32m    |\033[1;38mBy: Jey Zeta\033[1;33m\              | |  | | __ _ _ __   __ _  ___ _ __ ___  _   _ ___ \033[1;m
    |_____________\_______      | |  | |/ _` | '_ \ / _` |/ _ \ '__/ _ \| | | / __|
\033[1;32m    |==[\033[1;38mH4ckSec\033[1;33m >]========\     | |__| | (_| | | | | (_| |  __/ | | (_) | |_| \__ \  \033[1;33m
\033[1;34m    |______________________\    |_____/ \__,_|_| |_|\__, |\___|_|  \___/ \__,_|___/ 
\033[1;40m    \(@)(@)(@)(@)(@)(@)(@)/                          __/ |
     *********************                          |___/
                                                    \033[1;m

         '''

    print '''

  \033[1;32m 1. Footprinting      \033[1;32m 5. IpScanner         \033[1;32m  9. Metadatos     \033[1;32m 13. Hash
  \033[1;32m 2. Fingerprinting    \033[1;32m 6. BruteForce        \033[1;32m 10. DDoS          \033[1;32m 14. Sqli
  \033[1;32m 3. Doxing            \033[1;32m 7. Racp              \033[1;32m 11. Backdoor      \033[1;32m 15. About
  \033[1;32m 4. Dorkscan          \033[1;32m 8. GoSFinder         \033[1;32m 12. Cryptool      \033[1;32m 16. Exit 

    '''
    while True:

       d = raw_input("\033[1;36mDangerous > \033[1;m")

       if d == "1":
           subprocess.call(['python','footprinting/foot.py'])
       if d == "2":
           subprocess.call(['python','fingerprinting/finger.py'])
       if d == "3":
           subprocess.call(['python','dox/doxing.py'])
       if d == "4":
           subprocess.call(['python','Dorkscan/Dorkscan.py'])
       if d == "5":
           subprocess.call(['python','IpScanner/IpScanner.py'])
       if d == "6":
           subprocess.call(['python','cupp/cupp.py'])
       if d == "7":
           subprocess.call(['perl','RACP-master/RACP.pl'])
       if d == "8":
           subprocess.call(['python','GoSFinder/GoSFinder.py'])
       if d == "9":
           subprocess.call(['python','Metadatos/metadatos.py'])
       if d == "10":
           subprocess.call(['python','ddos/ddos.py'])
       if d == "11":
           subprocess.call(['python','weevely/weevely.py'])
       if d == "12":
           subprocess.call(['python','criptografia/s.py'])
       if d == "13":
           subprocess.call(['python','Hash/Hash.py'])
       if d == "14":
           subprocess.call(['python','sqli/sql.py'])
       if d == "15":
           webbrowser.open('https://www.facebook.com/JeyZetaCyberWar/')
       if d == "16":
           sys.exit()

menu()
