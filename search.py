#!/usr/bin/env python3


def run(runfile):
    with open(runfile,"r") as rnf:
        exec(rnf.read())
try:
    run('kr.py')
except Exception as e:
    print("printing error")
    print(str(e))
