#!/usr/bin/env python
# -*- coding=utf-8 -*-

import subprocess
def main():
    while True:
        ufonetOptions = raw_input("Ufonet >")
        command = 'python core/main.py %s' % ufonetOptions
        subprocess.call(command,shell=True)
if __name__ == "__main__":
    main()
