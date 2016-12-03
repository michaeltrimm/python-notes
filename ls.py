#!/usr/bin/python

import os, glob
os.chdir("/Users/michael/Desktop/test/python")
for file in glob.glob("*.py"):
    print file