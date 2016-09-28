#!/usr/bin/python

import sys
import os
import webbrowser
import platform
import subprocess

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

\033[1;32m 1. Index             \033[1;32m 4. IpScanner         \033[1;32m 7. Sqlmap         \033[1;32m 10. Hash

\033[1;32m 2. GoSFinder         \033[1;32m 5. TheHarvester      \033[1;32m 8. Weevely        \033[1;32m 11. DDoS

\033[1;32m 3. Dorkscan          \033[1;32m 6. Golismero         \033[1;32m 9. Cifrado        \033[1;32m 12. Extra

    '''
    while True:

       d = raw_input("\033[1;36mDangerous > \033[1;m")

       if d == "1":
           subprocess.call(['python','Index/index.py'])
       if d == "2":
           subprocess.call(['python','GoSFinder-master/GoSFinder.py'])
       if d == "3":
           subprocess.call(['python','Dorkscan/Dorkscan.py'])
       if d == "4":
           subprocess.call(['python','IpScanner/IpScanner.py'])
       if d == "5":
           subprocess.call(['python','TheHarvester/theHarvester.py'])
       if d == "6":
           subprocess.call(['python','Golismero/golismero.py'])
       if d == "7":
           subprocess.call(['python','sqlmap/sqlmap.py'])
       if d == "8":
           subprocess.call(['python','Weevely/weevely.py'])
       if d == "9":
           subprocess.call(['python','Cifrado/Cifrado.py'])
       if d == "10":
           subprocess.call(['python','Hash/Hash.py'])
       if d == "11":
           url = raw_input("Url a la que quieres atacar.. :")
           subprocess.call(['perl','ddos/slowloris.pl','-dns',url])
       if d == "12":
           subprocess.call(['python','Calculadora/Calculadora.py'])
       if d == "exit":
           sys.exit()

menu()
