#!/usr/bin/python
#
"""
    Script: sss_web_flashcards
    Purpose: Init script for web_flashcards. This script will start, stop or check the status of
             the web_flashcards daemon process that manages the content displayed on a web page.

    This script is provided "as is", without warranty or support of any kind. Permission is granted,
    free of charge, to any person obtaining a copy of this script, to modify its contents without
    restriction, merge, publish or distribute. Enjoy!
"""
import sys
import os
import subprocess

def usage():
    print("\nUsage: start_web_flashcards start|stop|status\n")
    exit()

num_args = len(sys.argv)

if num_args != 2:
    usage()

action = sys.argv[1]

process_name = "web_flashcards"
process_pid = str(subprocess.check_output("ps -e|grep web_flashcards|grep -v grep|awk '{print $1}'", shell=True))
process_pid = process_pid.replace("b'", "")
process_pid = process_pid.replace("\\n'", "")


if action == "start":
    print("Starting web_flashcards")
    cmd_exec = "nohup nice -5 /var/www/cgi-bin/web_flashcards >/dev/null 2>&1 &"
    os.system(cmd_exec)

elif action == "stop":
    print("Stoping web_flashcards")
    print("PID: ", process_pid)
    cmd_exec = "kill -9 " + process_pid
    os.system(cmd_exec)

elif action == "status":
    web_flashcards_status = str(subprocess.check_output("ps -e|grep web_flashcards|grep -v grep|awk '{print $4}'", shell=True))
    web_flashcards_status = web_flashcards_status.replace("b'", "")
    web_flashcards_status = web_flashcards_status.replace("\\n'", "")

    if web_flashcards_status == "web_flashcards":
        print("Status:", web_flashcards_status, "is running.")
    else:
        print("Status: web_flashcards is not running")

elif action != "start" or action != "stop":
    usage()