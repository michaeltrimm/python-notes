#!/usr/bin/python



def square(x):
    return x * x;

f = square


"""
<function square at 0x1075ed320>
25
"""
print(square)
print(f(5))



def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])


"""
[1, 4, 9, 16, 25]
"""
print squares

squares = map(square, [1,2,3,4,5])

"""
[1, 4, 9, 16, 25]
"""
print squares


def cube(x):
    return x * x * x

