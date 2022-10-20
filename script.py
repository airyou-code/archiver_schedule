#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import os
import argparse
# sudo echo -e '*/1 * * * * /root/task/script.py' | sudo crontab -
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("-a", action="store_true", help="This is the 'a' variable")
parser.add_argument("-d", default="/", help="This is the 'b' variable")
args = parser.parse_args()
a = args.a
b = args.d

def sendmessage(dir="/var/log/"):
    # print(os.path.join(f"{BASE_DIR}{dir}"))
        
    my_file = open("BabyFile.txt", "w+")
    my_file.write(f"Привет, файл! {BASE_DIR}")
    my_file.close()

def main():
    os.chdir("/")    
    try:
        os.chdir(os.path.join(f"{BASE_DIR + args.d}"))
    except:
        print(f"ERROR: Couldn't find the {BASE_DIR + args.d} directory")
        return 1

    if a:
        sendmessage(args.d)
    else:
        os.system(f"sudo echo -e '*/1 * * * * {BASE_DIR}/script.py -a' | sudo crontab -")
        os.system("sudo service cron start")

if __name__ == '__main__':
    main()