#!/usr/bin/python

import logging
logging.basicConfig(filename="closure.log", level=logging.INFO)

def logger(func):
    def log(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log


def square(x):
    return x*x

def cube(x):
    return x*x*x

square_logger = logger(square)
cube_logger = logger(cube)

square_logger(2)
# 4

cube_logger(2)
# 8