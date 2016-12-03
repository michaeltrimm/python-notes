#!/usr/bin/python

import os, glob

"""
binary_tree.py
data.py
fibonacci.py
fizz_buzz.py
hero.py
linked_lists.py
ls.py

"""

os.chdir("/Users/michael/Desktop/test/python")
for file in glob.glob("*.py"):
    print file