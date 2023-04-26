#!/bin/python3
import shutil # for copy file
import os     # For GetFileSize and Check if file exist
import sys    # For CLI Argument

# purge_logs.py mylog.txt 10 5
if (len(sys.arg) < 4):
    print('Missing arguments! Usage is script.py 10 5')
    exit(1)

