#!/usr/bin/python

import time

# Method
def square_numbers(numbers):
    results = []
    for num in numbers:
        results.append(num*num)
    return results

numbers = [1, 2, 3, 4, 5]
print square_numbers(numbers)\
# [1, 4, 9, 16, 25]




# Generator
def square_numbers_generator(numbers):
    for num in numbers:
        yield num*num


squared = square_numbers_generator(numbers)

print squared
# <generator object square_numbers_generator at 0x1032b7aa0>

print next(squared)
# 1

print next(squared)
# 4

print next(squared)
# 9

print next(squared)
# 16

print next(squared)
# 25

# print next(squared)
"""
Traceback (most recent call last):
  File "generators.py", line 33, in <module>
    print next(squared)
StopIteration
"""

for squared in square_numbers_generator(numbers):
    print squared
    """
    1
    4
    9
    16
    25
    """

# Can also be completed using list comprehension
squared_results = [x*x for x in [1, 2, 3, 4, 5]]
print squared_results
# [1, 4, 9, 16, 25]

for squared in squared_results:
    print squared
    """
    1
    4
    9
    16
    25
    """

# You can also use ranges here too...
squared_results = [x*x for x in range(1,20)]
print squared_results
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]


print "Timing creation of lists..."
# Time The Results For Lists
to = 10000
start = time.time()
test = [x*x for x in range(1,to)]
end = time.time()
elapsed = end - start
print "Squaring the numbers between 1-{0} took {1}s.".format(to, round(elapsed,4))
# Squaring the numbers between 1-10000 took 0.0014s.

# Time The Results For Lists
to = 10000000
start = time.time()
test = [x*x for x in range(1,to)]
end = time.time()
elapsed = end - start
print "Squaring the numbers between 1-{0} took {1}s.".format(to, round(elapsed,4))
# Squaring the numbers between 1-10000000 took 1.5804s.
print ""


print "Timing creation of generators..."
to = 10000
start = time.time()
test = (x*x for x in range(1,to))
end = time.time()
elapsed = end - start
print "Squaring the numbers between 1-{0} took {1}s.".format(to, round(elapsed,4))
# Squaring the numbers between 1-10000 took 0.0641s.
# Slower with small ranges

to = 10000000
start = time.time()
test = (x*x for x in range(1,to))
end = time.time()
elapsed = end - start
print "Squaring the numbers between 1-{0} took {1}s.".format(to, round(elapsed,4))
# Squaring the numbers between 1-10000000 took 0.1029s.
# Faster with large ranges



# print next(squared_results)
"""
Traceback (most recent call last):
  File "generators.py", line 81, in <module>
    print next(squared_results)
TypeError: list object is not an iterator
"""


for squared in squared_results:
    print squared
    """
    1
    4
    9
    16
    25
    36
    49
    64
    81
    100
    121
    144
    169
    196
    225
    256
    289
    324
    361
    """

# Or you can use shorthand generator syntax

squared_results_generator = (x*x for x in [1,2,3,4,5])
print squared_results_generator
# <generator object <genexpr> at 0x102155b40>

print next(squared_results_generator)
# 1
print next(squared_results_generator)
# 4
print next(squared_results_generator)
# 9
print next(squared_results_generator)
# 16
print next(squared_results_generator)
# 25
# print next(squared_results_generator)
"""
Traceback (most recent call last):
  File "generators.py", line 126, in <module>
    print next(squared_results_generator)
StopIteration
"""


for squared in squared_results_generator:
    print squared
    """
    1
    4
    9
    16
    25
    """

squared_results_generator = (x*x for x in range(1,20))
print squared_results_generator
# <generator object <genexpr> at 0x10e83baf0>

# Convert the generator to a list...
squared_list = list(squared_results_generator)
print squared_list

for squared in squared_results_generator:
    print squared
    """
    1
    4
    9
    16
    25
    36
    49
    64
    81
    100
    121
    144
    169
    196
    225
    256
    289
    324
    361
    """
