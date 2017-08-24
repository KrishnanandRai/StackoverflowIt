#!/usr/bin/env python3
import sys
from google import search

# fuction to run target file as code itself
def run(runfile):
    with open(runfile,"r") as rnf:
        exec(rnf.read())
try:
    run(sys.argv[1])
except Exception as e:
    error_message = e.msg

    # get error type
    error_class = str(e.__class__).split()[1].strip(" <>'")
    print(error_class)
    print(error_message)

    # query to search
    query = 'stackoverflow python' + error_class +" " + error_message 

    # search
    for j in search(query, tld="co.in", num=10, stop=1, pause=1):
        print(j)
