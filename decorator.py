#!/usr/bin/python

def simple_decorator(decorator):
    def new_decorator(f):
        d = decorator(f)
        d.__name__ = f.__name__
        d.__doc__ = f.__doc__
        d.__dict__.update(f.__dict__)
        return d
    
    new_decorator.__name__ = decorator.__name__
    new_decorator.__doc__ = decorator.__doc__
    new_decorator.__dict__.update(decorator.__dict__)
    return new_decorator

@simple_decorator
def double(x):
    'Doubles a number.'
    return 2 * x

print(double(155))