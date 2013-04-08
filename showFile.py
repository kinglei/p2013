#!/usr/bin/python
#FileName: showFile.py

import os

fname = raw_input("Enter file name: ")
fobj = open(fname, 'r')

for eachLine in fobj.readlines():
    if str(eachLine)[0] == '#':
        continue
    else:
        print eachLine,

fobj.close()
