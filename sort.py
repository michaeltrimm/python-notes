#!/usr/bin/python

def sort(arr, unique=False):
    result = []
    while arr:
        minimum = arr[0]
        for x in arr:
            if x < minimum:
                minimum = x
        result.append(minimum)
        arr.remove(minimum)
            
    return result

def sort_unique(arr, unique=False):
    result = []
    while arr:
        minimum = arr[0]
        for x in arr:
            if x < minimum:
                minimum = x
        if unique is True:
            if minimum not in result:
                result.append(minimum)
                arr.remove(minimum)
            else:
                arr.remove(minimum)
        else:
            result.append(minimum)
            arr.remove(minimum)
            
    return result

test1 = [2, 4, 8, 5, 1, 7, 6, 9, 10, 3, -20, -30, -10, -5, 3, 4, 91, 293, 0, -392]
result = sort(test1)
print(result)


test2 = [2, 4, 8, 5, 1, 7, 6, 9, 10, 3, -20, -30, -10, -5, 3, 4, 91, 293, 0, -392]
unique = sort_unique(test2, True)
print(unique)