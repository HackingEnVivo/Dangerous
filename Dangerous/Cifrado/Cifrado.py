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
\033[1;40m
\033[1;31m          :::===== ::: :::===== :::====  :::====  :::====  :::==== 
\033[1;31m          :::      ::: :::      :::  === :::  === :::  === :::  ===
\033[1;31m          ===      === ======   =======  ======== ===  === ===  ===
\033[1;31m          ===      === ===      === ===  ===  === ===  === ===  ===
\033[1;31m           ======= === ===      ===  === ===  === =======   ====== 
                                                          
                                                             
                                            

                        \033[1;34mHecho por:\033[1;mJey Zeta
                        \033[1;34mVersion:\033[1;mBeta 1.0
          '''
    print '''
                        \033[1;32m 1.- Cesar
                        \033[1;32m 2.- Vigenere
                        \033[1;32m 3.- Volver al menu principal
        '''

    while True:


        d = raw_input("\033[1;35mCifrado > \033[1;m")

        if d == "1":
           subprocess.call(['python','cesar/cesar.py'])
        if d == "2":
           subprocess.call(['python','vigenere/vigenere.py'])
        if d == "3":
            subprocess.call(['python','Dangerous.py'])
menu()
