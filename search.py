#!/usr/bin/env python3
import os
import sys
import subprocess
import urllib.request
from google import search

try:
    subprocess.check_call(["python3 lamb.py"], shell=True)
    search.dosome()
except Exception as e:
    print(e)

    to search
    query = 'stackoverflow python' + str(sys.version_info[0]) +" " +  fname + " " +  str(exc_type) + " " 
    for j in search(query, tld="co.in", num=10, stop=1, pause=1):
        print(j)
