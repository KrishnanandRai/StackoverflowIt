#!/usr/bin/env python3
import os
import sys
import subprocess
import urllib.request
u = urllib.request.urlopen("https://www.google.co.in/?gfe_rd=cr&ei=r62dWYilOKvy8Afs_5L4DQ")


try:
    subprocess.check_call(["python3 kr.py"], shell=True)
except subprocess.CalledProcessError as e:
    print(e)
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
 #   exc_type, exc_obj, exc_tb = sys.exc_info()
  #  fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
  #  print(exc_type)
   # print(fname)
   # print(exc_tb.tb_lineno)
    
#    print("An exception occured!!")
#   subprocess.call("python3 kr.py", shell=True)