#!/usr/bin/python

"""
Write a function that combines overlaping segments into a flattened list.

x = [[2,5],[100,200],[15,20],[4,16]]

    Line graph: 0-----------------------------------------n
                   2-----5          15-----------20         100--200
                       4---------------16

Should reduce down to: 

    Line graph: 0-----------------------------------------n
                                    15-----------20         100--200
                   2-------------------16

Should reduce down to: 

    Line graph: 0-----------------------------------------n
                   2-----------------------------20         100--200

The result should be: 

[[2,20],[100,200]]
"""


def combine_overlaps(sets):
    sets = sorted(sets, key=lambda x: x[1])
 
    for i, current in enumerate(sets):
        next_index = i+1;
        if next_index < len(sets):
            next_data = sets[i+1]
            # can we merge current + next together?
            if next_data[0] >= current[0] and next_data[0] <= current[1]:
                new_record = [current[0], next_data[1]]
                sets.remove(current)
                sets.remove(next_data)
                sets.append(new_record)
                return combine_overlaps(sets)
            else:
                return sets


test1 = [[2,5],[100,200],[15,20],[4,16]]
print(combine_overlaps(test1))
