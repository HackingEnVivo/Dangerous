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

\033[1;31m                                |""""""""""""|======[***
\033[1;31m                                |By: JEY ZETA\ 
\033[1;39m                                |_____________\_______ 
\033[1;39m                                |==[123 >]============\ 
\033[1;39m                                |______________________\ 
\033[1;31m                                \(@)(@)(@)(@)(@)(@)(@)/ 
\033[1;31m                                 ********************* 


         '''

    print '''

\033[1;32m 1. Calculadora       \033[1;32m 4. IpScanner         \033[1;32m 7. Sqlmap         \033[1;32m 10. Hash

\033[1;32m 2. GoSFinder         \033[1;32m 5. TheHarvester      \033[1;32m 8. Weevely        \033[1;32m 11. DDoS

\033[1;32m 3. Dorkscan          \033[1;32m 6. Golismero         \033[1;32m 9. Cifrado        \033[1;32m 12. Index

    '''
    while True:

       d = raw_input("\033[1;40mDangerous > \033[1;m")

       if d == "1":
           subprocess.call(['python','Calculadora/Calculadora.py'])
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
           subprocess.call(['python','DDoS/DDoS.py'])
       if d == "12":
           subprocess.call(['python','Index/index.py'])
       if d == "exit":
           sys.exit()

menu()