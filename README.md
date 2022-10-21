<h1 align="center">Directory archiver every 30 days</h1>

<a href="https://github.com/airyou-code/archiver_schedule" target="_blank">github</a> 

## Description
- python3 script that will automatically run as a Linux cron job.

# Stack technology
- Python3

# Installation
- `git clone https://github.com/airyou-code/archiver_schedule.git `

## Usage
usage: script.py [-h] [-a | -u] [-s] [-d D] [-t T]

archives in a folder every t=30 days, standard directory: /var/log

optional arguments:
  - -h, --help  show this help message and exit
  - -a          compress now
  - -u          uncompress now
  - -s          stop cron
  - -d D        Сhange the directory
  - -t T        Change the time after which the script will be activated
