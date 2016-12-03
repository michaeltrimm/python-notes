#!/usr/bin/python

# Normal
def square(x):
    return x**x

print square(8)
# 64

square_anonymous = lambda x: x**x

print square_anonymous(8)
# 64


# Finding Numbers Divisible By 3

nums = [2, 18, 9, 22, 17, 24, 8, 12, 27]

# Make a Method
def divisible_by_three(x):
    if x % 3 == 0:
        return True
    return False

print divisible_by_three(18)
# True

# Use a Lambda
divisible_by_three_anonymous = lambda x: x % 3 == 0

print divisible_by_three_anonymous(18)
# True

print map(divisible_by_three_anonymous, nums)
# [False, True, True, False, False, True, False, True, True]

print map(lambda x: x % 3 == 0, nums)
# [False, True, True, False, False, True, False, True, True]

print filter(divisible_by_three_anonymous, nums)
# [18, 9, 24, 12, 27]


print filter(lambda x: x % 3 == 0, nums)
# [18, 9, 24, 12, 27]


# Word lengths
sentence = "In the summer I enjoy swimming"
words = sentence.split(" ")
print words
# ['In', 'the', 'summer', 'I', 'enjoy', 'swimming']

lengths = map(lambda word: len(word), words)
print lengths
# [2, 3, 6, 1, 5, 8]

def word_length(word):
    return len(word)
lengths = map(word_length, words)
print lengths
# [2, 3, 6, 1, 5, 8]

print map(lambda word: len(word), "Only during winter do I drink hot chocolate".split())
# [4, 6, 6, 2, 1, 5, 3, 9]
