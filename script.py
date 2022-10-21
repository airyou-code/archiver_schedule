#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import os
import argparse
import gzip
# sudo echo -e '*/1 * * * * /root/task/script.py' | sudo crontab -
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
parser = argparse.ArgumentParser(description='archives in a folder every t=30 days,\nstandard directory: /var/log')
group = parser.add_mutually_exclusive_group()
group.add_argument("-a", action="store_true", help="compress now")
group.add_argument("-u", action="store_true", help="uncompress now")
parser.add_argument("-s", action="store_true", help="stop cron")
parser.add_argument("-d", default="/var/log", help="Сhange the directory")
parser.add_argument("-t", default=30, type=int, help="Change the time after which the script will be activated t = n(day)")

args = parser.parse_args()
activate = args.a
s = args.s
u = args.u
dir = args.d

def archiver(dir="/var/log/"):
    dir_name = dir.split("/")[-1]
    os.chdir("..")
    os.system(f"gzip -r {dir_name}")
    os.chdir(dir_name)

def uncompress(dir="/var/log/"):
    dir_name = dir.split("/")[-1]
    os.chdir("..")
    os.system(f"gunzip -r {dir_name}")
    os.chdir(dir_name)

def main():
    os.chdir("/")    
    try:
        os.chdir(os.path.join(f"{BASE_DIR + dir}"))
    except:
        print(f"ERROR: Couldn't find the {BASE_DIR + args.d} directory")
        return 1

    if s:
        ans = input("This action will DELETE ALL the cron tasks of the root user\nView tasks, command: sudo crontab -u root -e\nEnter Y or N: ")
        if ans.lower() == 'y':
            os.system("sudo crontab -u root -r")
        return 0

    if u:
        uncompress(args.d)
        return 0

    if activate:
        archiver(args.d)
    else:
        os.system(f"sudo echo -e '* * */{args.t} * * {BASE_DIR}/script.py -a -d {dir} ' | sudo crontab -")
        os.system("sudo service cron start")
        


if __name__ == '__main__':
    main()
