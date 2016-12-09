#!/usr/bin/python
"""

We define a word as any sequence of one or more lower-case letters (no numbers, no punctuation) 
where words are separated by white space.

Write a program to read all the words (on every line) from standard input, and to produce, in order, 
on separate lines:

the count of words in the input
the word "words"
each unique word, and the count of times it occurs in the input (listed in alphabetical order, each on its own 
                                                                line, with a space between the word and count)
the word "letters"
for every letter from a to z, the letter, and the count of times that letter occurred IN A WORD in the input 
                                                                (listed in alphabetical order, each on its own line, 
                                                                with a space between the letter and count).

There must be "whitespace" separating valid words in the input -- actual spaces, and newlines.  
If your program finds something that is not whitespace, and not a word, it should skip until it 
comes to a valid word (or the end of the input).  Finding a non-word character next to word-characters 
makes the whole sequence a non-word.


NOTE: When inside stdin prompt, after you're done entering your text, press <RETURN> then <CTR-D> to end stdin mode

"""

import sys

def sort_dict(dict):
    ref = []
    for key in sorted(dict):
        ref.append({key: dict[key]})
    return ref

def count_words_and_letters(line):
    """
    count_of_words
    words
    word1 times_shows_up
    letters
    letter1_in_word1 times_it_shows_up
    letter2_in_word1 times_it_shows_up
    word2 times_shows_up
    letters
    letter1_in_word2 times_it_shows_up
    letter2_in_word2 times_it_shows_up
    """
    
    lines = line.split("\n")

    output = ""

    words = []
    for l in lines:
        for w in l.split(" "):
            if len(w) > 0:
                words.insert(0, w.lower())
    
    output += "{}\n".format(len(words))
    output += "words\n"
    
    results = {}
    for word in words:
        times = words.count(word)
        results[word] = times
    
    keys = results.keys()
    keys.sort()
    for k in keys:
        output += "{} {}\n".format(k, results[k])
        output += "letters\n"
        letters = {}
        for char in list(k):
            if char not in letters:
                letters.update({char: 1})
            else:
                letters["{}".format(char)] += 1
        letters = sort_dict(letters)
        for letter in letters:
            for char in letter:
                output += "{} {}\n".format(char, letter[char])
    return output

lines = ""
for line in sys.stdin:
    lines = lines + line

x = count_words_and_letters(lines)
print(x)

"""
DEMO

INPUT: 
    this is an example that will use this is an example
    to determine how many unique words this example has
    in a multiline comment

OUTPUT:

    24
    words
    a 1
    letters
    a 1
    an 2
    letters
    a 1
    n 1
    comment 1
    letters
    c 1
    e 1
    m 2
    n 1
    o 1
    t 1
    determine 1
    letters
    d 1
    e 3
    i 1
    m 1
    n 1
    r 1
    t 1
    example 3
    letters
    a 1
    e 2
    l 1
    m 1
    p 1
    x 1
    has 1
    letters
    a 1
    h 1
    s 1
    how 1
    letters
    h 1
    o 1
    w 1
    in 1
    letters
    i 1
    n 1
    is 2
    letters
    i 1
    s 1
    many 1
    letters
    a 1
    m 1
    n 1
    y 1
    multiline 1
    letters
    e 1
    i 2
    l 2
    m 1
    n 1
    t 1
    u 1
    that 1
    letters
    a 1
    h 1
    t 2
    this 3
    letters
    h 1
    i 1
    s 1
    t 1
    to 1
    letters
    o 1
    t 1
    unique 1
    letters
    e 1
    i 1
    n 1
    q 1
    u 2
    use 1
    letters
    e 1
    s 1
    u 1
    will 1
    letters
    i 1
    l 2
    w 1
    words 1
    letters
    d 1
    o 1
    r 1
    s 1
    w 1

"""


