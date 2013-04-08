#!/usr/bin/python

import os
fname = raw_input("Please input the file name: ")
fobj  = open(fname)
num = 0

for i in fobj.readlines():
    num += 1

print num
fobj.close()
