<h1 align="center">Directory archiver every 30 days</h1>

<a href="https://github.com/airyou-code/archiver_schedule" target="_blank">github</a> 

## Description
- python3 script that will automatically run as a Linux cron job.

# Stack technology
- Python3

# Installation
- `git clone https://github.com/airyou-code/archiver_schedule.git `
- `sudo chmod +x script.py`

## Usage
usage: script.py [-h] [-a | -u] [-s] [-d D] [-t T]
- examle: `./script.py -d /var/mail -t 15` (every 15 days the script will archive all files in the /var/mail folder)

archives in a folder every t=30 days, standard directory: /var/log

optional arguments:
  - -h, --help  show this help message and exit
  - -a &ensp compress now
  - -u &ensp         uncompress now
  - -s          stop cron
  - -d D        Сhange the directory (standart directory == /var/log)
  - -t T        Change the time after which the script will be activated (standart time == 30days)
