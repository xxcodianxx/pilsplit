#!/usr/bin/python3
import os
import subprocess
import argparse

if os.name != 'posix':
    print('This script is only intended for use on Linux.\nSee README file.')
    exit(-1)

parser = argparse.ArgumentParser(description='Configure PilSplit.', prog='configure.py')
parser.add_argument('--install', action='store_true')
parser.add_argument('--remove', action='store_true')
args = parser.parse_args()

install = True

if args.install and args.remove:
    parser.error('you cannot install and remove at the same time, pick one')
    exit(-1)
elif not (args.install or args.remove):
    print('no argument specified, defaulting to install')
else:
    install = args.install

print('Pilsplit configuration\n'+'-'*12)

if install:
    print('[ installing pilsplit ]\n')
    
    print('Resolving dependencies...', end='')
    try:
        import PIL
    except:
        print('fail')
        print('[!] Pillow is not installed, installing with `pip`.')
        if subprocess.call('pip install pillow', shell=True) != 0:
            print('[!] Could not auto-install pillow, please install it manually.')
            exit(-1)
    else:
        print('ok')

    print('Copying pilsplit to /usr/bin...')
    if subprocess.call('cp ./pilsplit.py /usr/bin/pilsplit', shell=True) != 0:
        exit(-1)
    

    print('Setting permissions...')
    if subprocess.call('chmod +x /usr/bin/pilsplit', shell=True) != 0:
        exit(-1)

    print('\nSuccess! You can use the program with the `pilsplit` command now.')
else:
    print('[ removing pilsplit ]\n')
    
    print('Removing from /usr/bin...')
    if subprocess.call('rm -v /usr/bin/pilsplit', shell=True) != 0:
        exit(-1)
    
    print('\nSuccess! PilSplit has been removed from your computer.')
