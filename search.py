#!/usr/bin/env python3
import os
import sys
import subprocess


try:
    subprocess.check_call(["python3 kr.py"], shell=True)
except subprocess.CalledProcessError as e:
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type)
    print(fname)
    print(exc_tb.tb_lineno)
    
