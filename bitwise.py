#!/usr/bin/python

"""
Assume you are given two dictionaries d1 and d2, each with integer keys and integer values. You are also given a 
function f, that takes in two integers, performs an unknown operation on them, and returns a value.

Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). The function will return a tuple 
of two dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, 
calculated as follows:

intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of 
the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- 
the value of the common key in d1 is the first parameter to the function and the value of the common key in d2 is 
the second parameter to the function. Do not implement f inside your dict_interdiff code -- assume it is defined 
outside. difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key 
appears only in d1 and not in d2 or (b) every key-value pair in d2 whose key appears only in d2 and not in d1. Here 
are two examples:


If f(a, b) returns a + b

    d1 = {1:30, 2:20, 3:30, 5:80}
    d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90}) If f(a, b) returns a > b

    d1 = {1:30, 2:20, 3:30}
    d2 = {1:40, 2:50, 3:60}

then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})

    def dict_interdiff(d1, d2):
        '''
        d1, d2: dicts whose keys and values are integers
        Returns a tuple of dictionaries according to the instructions above
        '''
        # Your code here

Note that we ask you to write a function only -- you cannot rely on any variables defined outside your function 
for your code to work correctly.

"""


def dict_interdiff(d1, d2, f):
    """
    Args:
        d1 (dict) Dictionary 1
        d2 (dict) Dictionary 2
        f (function) Operation choice for mutating the each of the associative keys
    
    Returns:
        Tuple of 2 dictionaries
    """
    # t1: d1 = {1: 30, 2: 20, 3: 30, 5: 80}
    # t1: d1.viewkeys()) = dict_keys([1, 2, 3, 5])

    # t1: d2 = {1: 40, 2: 50, 3: 60, 4: 70, 6: 90}
    # t1: d2.viewkeys() = dict_keys([1, 2, 3, 4, 6])
    
    """determine the unique keys between d1 and d2"""
    diff  = d1.viewkeys()     ^           d2          # extract keys that only appear in d1 and not d2
    # t1:   [1, 2, 3, 5]     XOR    [1, 2, 3, 4, 6] => [False,  False,  False,  True,  True,  True  ]
    # t1:                                               common  common  common  unique unique unique
    # t1:                                               dropped dropped dropped kept   kept   kept
    # t1: diff = set([4, 5, 6])
    
    """determine the common keys between d1 and d2"""
    inter = d1.viewkeys()      &           d2          # extract keys that appear in BOTH d1 and d2
    # t1:   [1, 2, 3, 5]      AND    [1, 2, 3, 4, 6] => True,  True,  True,  False,  False,  False
    # t1:                                               common common common unique  unique  unique
    # t1:                                               kept   kept   kept   dropped dropped dropped
    # t1: inter = set([1, 2, 3])
    
    """find the functional output of the associative common keys' values and assign them to the intersection key"""
    # Result needs to be a tuple showing the intersection, difference results based on the f() function
    intersection = { 
        key: f( d1[key] , d2[key] ) for key in inter
    }
    # intersection = { intersection_key: f(d1[intersection_key], d2[intersection_key] ), ... }
    #     inter  
    #       1: f(a+b) -> f( 30, 40 ) = 70
    #       2: f(a+b) -> f( 20, 50 ) = 70
    #       3: f(a+b) -> f( 60, 30 ) = 90
    #     result: {
    #       1: 70,
    #       2: 70,
    #       3: 90
    #     }
    
    """determine the common keys between diff and d1's keys"""
    d1_diff_diff =    diff    &  d1.viewkeys()
    # t1:       [4, 5, 6] AND [1, 2, 3, 5]              => find all common elements using bitwise and
    # t1: d1_diff_diff = set([5])
    # t2: d1_diff_diff = set([])
    
    """build a dict that contains the common keys of diff and d1's keys and the associative value in d1"""
    difference = {
        key: d1[key] for key in d1_diff_diff
    }
    # difference = { d1_diff_diff_key: d1[d1_diff_diff[key]], ... }
    #   d1_diff_diff
    #       1: d1[5] => 80
    #   result: {
    #       1: 80
    #   }
    
    # At This Point
    #------------------------------------------
    # ({1: 70, 2: 70, 3: 90}, {5: 80})
    # Failed Test 1
    #
    # ({1: False, 2: False, 3: False}, {})
    # Passed Test 2
    #------------------------------------------
    # aka test 1's difference element is missing d2 data, let's add it
    
    """determine the common keys between diff and d2 keys"""
    d2_diff_diff =   diff     &   d2.viewkeys()
    # t1:          [4, 5, 6] AND [1, 2, 3, 4, 6]        => find all common elements using bitwise AND
    # t1: d2_diff_diff = set([4, 6])
    # t2: d2_diff_diff = set([])
    
    
    """insert the common elements of diff and d2 keys into the difference set"""
    difference.update( {
        key: d2[key] for key in d2_diff_diff
    } )
    # difference = difference + { d2_diff_diff_key: d2[d2_diff_diff[key]], ... }
    #   d2_diff_diff = 
    #       4: d2[4] => 4: 70
    #       6: d2[6] => 6: 90
    #   result = {
    #       4: 70,  # added using .update()
    #       5: 80,  # existing in the result
    #       6: 90   # added using .update()
    #   }
    
    # At This Point
    #------------------------------------------
    # ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
    # Passed Test 1
    #
    # ({1: False, 2: False, 3: False}, {})
    # Passed Test 2
    #------------------------------------------
    # aka all done!
    
    return intersection, difference


###################
## TEST CASE ONE ##
###################

def f(a,b):
    return a+b

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

result = dict_interdiff(d1, d2, f)
print(result)

if(result == ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})):
    print("Passed Test 1")
else:
    print("Failed Test 1")

print("")

###################
## TEST CASE TWO ##
###################

def f(a,b):
    return a>b

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}

result = dict_interdiff(d1,d2,f)
print(result)
if(result == ({1: False, 2: False, 3: False}, {})):
    print("Passed Test 2")
else:
    print("Failed Test 2")


















