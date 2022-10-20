#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import os
import argparse
import gzip
# sudo echo -e '*/1 * * * * /root/task/script.py' | sudo crontab -
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("-a", action="store_true", help="This is the 'a' variable")
parser.add_argument("-d", default="/var/log", help="This is the 'b' variable")
args = parser.parse_args()
activate = args.a
dir = args.d

def archiver(dir="/var/log/"):
    dir_name = dir.split("/")[-1]
    os.chdir("..")
    os.system(f"gzip -r {dir_name}")
    os.chdir(dir_name)

    # print(os.path.join(f"{BASE_DIR}{dir}"))
    # os.system("gzip -cf log.gz icon.txt icon2.txt")
    # os.system("gunzip icon.txt.gz icon2.txt.gz")
        
    # my_file = open("BabyFile.txt", "w+")
    # my_file.write(f"Привет, файл! {BASE_DIR}")
    # my_file.close()

def main():
    os.chdir("/")    
    try:
        os.chdir(os.path.join(f"{BASE_DIR + dir}"))
    except:
        print(f"ERROR: Couldn't find the {BASE_DIR + args.d} directory")
        return 1


    if activate:
        archiver(args.d)
    else:
        os.system(f"sudo echo -e '*/1 * * * * {BASE_DIR}/script.py -a -d {dir} ' | sudo crontab -")
        os.system("sudo service cron start")
        


if __name__ == '__main__':
    main()