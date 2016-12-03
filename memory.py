#!/usr/local/bin/python3

import resource
import sys

"""
List
Squaring numbers 1 to 10,000,000
  Before: 7.312Mb
  After: 332.539Mb
  Consumed = 325.22Mb memory

Generator
Squaring numbers 1 to 10,000,000
  Before: 332.543Mb
  After: 332.543Mb
  Consumed = 0.0Mb memory

"""

# Size of the sample set
to = 10000000 # 10M

def memory_usage_resource():
    rusage_denom = 1024.
    if sys.platform == 'darwin':
        rusage_denom = rusage_denom * rusage_denom
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom

def log_memory(text="Before"):
    print('  {}: {:,}Mb'.format(text, round(memory_usage_resource(),3)))

print("List")
print("Squaring numbers 1 to {:,}".format(to))
log_memory()
mem_before = memory_usage_resource()
squared_results_small = [x*x for x in range(1,to)]
log_memory("After")
mem_after = memory_usage_resource()
mem_diff = mem_after - mem_before
print("  Consumed = {:,}Mb memory".format(round(mem_diff,2)))
print("")


print("Generator")
print("Squaring numbers 1 to {:,}".format(to))
log_memory()
mem_before = memory_usage_resource()
squared_results_large = (x*x for x in range(1,to))
mem_after = memory_usage_resource()
log_memory("After")
mem_diff = mem_after - mem_before
print("  Consumed = {:,}Mb memory".format(round(mem_diff,2)))
print("")