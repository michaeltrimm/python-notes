#!/usr/bin/python

"""
1
2
3
4
5
6
"""
my_list = [1,2,3,4,5,6]
for i in my_list:
    print i

# -------------------------------------------------------

"""
1
2
3
4
5
6
1
2
3
4
5
6
"""
my_tup = (1,2,3,4,5,6,1,2,3,4,5,6)
for i in my_tup:
    print i

# -------------------------------------------------------

"""
male is a gender
Michael is a name
"""
my_dict = {
    "name": "Michael",
    "gender": "male"
}
for key,value in my_dict.iteritems():
    print "{0} is a {1}".format(value, key)

# -------------------------------------------------------

"""
1
2
3
4
5
6
"""
my_set = {1,2,3,4,5,6,1,2,3,4,5,6}
for i in my_set:
    print i

# -------------------------------------------------------

"""
[1, 4, 9, 16, 25, 36, 49, 64]
"""
numbers = [1,2,3,4,5,6,7,8]
squares = [num*num for num in numbers]
print squares