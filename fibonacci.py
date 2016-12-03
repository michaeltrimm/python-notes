#!/usr/bin/python

import time

# Bad Way
def fibonacci(n):
    if n <= 1:
        return n
    else: 
        return fibonacci( n - 1 ) + fibonacci( n - 2 )

# Better Way
class Fibonacci(object):
    # Method Example
    def compute(self, index):
        first,second = 0,1
        for number in range(0, index):
            third = first + second
            first = second
            second = third
        return first

    # Generator Example
    def display(self,index):
        first,second = 0,1
        for number in range(0,index):
            yield "{}: {}".format(number+1, first)
            first, second = second, first + second

# Slow Computation Output
print "SLOW"
print "Test | Sequence  | Result"
t1 = time.time()
_fib10 = fibonacci(10)
_t11 = time.time()
print "1:1:2: Fib(10) = {0} ({1}s)".format(_fib10, round(_t11-t1,4))

_fib25 = fibonacci(25)
_t12 = time.time()
print "2:1:2: Fib(25) = {0} ({1}s)".format(_fib25, round(_t12-_t11,4))

_fib35 = fibonacci(35)
_t13 = time.time()

print "3:1:2: Fib(35) = {0} ({1}s)".format(_fib35, round(_t13-_t12,4))
t2 = time.time()
elapsed = t2 - t1
print "Completed in {0}s".format(round(elapsed,4))
print ""

# Fast Computation Output
print "FAST"
print "Test | Sequence  | Result"
t1 = time.time()
fib = Fibonacci()
_fib10 = fib.compute(10)
_t11 = time.time()
print "1:2:2: Fib(10) = {0} ({1}s)".format(_fib10, round(_t11-t1,4))

_fib25 = fib.compute(25)
_t12 = time.time()
print "2:2:2: Fib(25) = {0} ({1}s)".format(_fib25, round(_t12-_t11,4))

_fib35 = fib.compute(35)
_t13 = time.time()
print "3:2:2: Fib(75) = {0} ({1}s)".format(_fib35, round(_t13-_t12,4))

_fib256 = fib.compute(256)
_t14 = time.time()
print "4:2:2: Fib(256) = {0} ({1}s)".format(_fib256, round(_t14-_t13,4))
t2 = time.time()
elapsed = t2 - t1
print "Completed in {0}s".format(round(elapsed,4))
print ""


# Generator Output
print "GENERATOR"
f = Fibonacci()
for item in f.display(10):
    print item
print ""