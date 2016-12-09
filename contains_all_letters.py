#!/usr/bin/python

# Write a function that takes a string and returns true if the string includes all
# the letters in the alphabet and false otherwise.
# "The quick brown fox jumps over the lazy dog"


def contains_all_letters(string):
    """Return true if the string contains every letter in the alphabet"""
    alpha_chars = list("abcdefghijklmnopqrstuvwxyz")
    str_chars = list(string.lower().replace(" ",""))
    
    for char in alpha_chars:
        if char not in str_chars:
            return False
    return True

x = contains_all_letters("The quick brown fox jumps over the lazy dog")
print(x)

y = contains_all_letters("Write a function that takes a strl")
print(y)

z = contains_all_letters("the letters in the alphabet and false otherwise")
print(z)