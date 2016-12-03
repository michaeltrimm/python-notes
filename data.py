#!/usr/bin/python


my_list = [1,2,3,4,5,6]
for i in my_list:
    print i


my_tup = (1,2,3,4,5,6,1,2,3,4,5,6)
for i in my_tup:
    print i

my_dict = {
    "name": "Michael",
    "gender": "male"
}
for key,value in my_dict.iteritems():
    print "{0} is a {1}".format(value, key)

my_set = {1,2,3,4,5,6,1,2,3,4,5,6}
for i in my_set:
    print i

numbers = [1,2,3,4,5,6,7,8]
squares = [num*num for num in numbers]
print squares