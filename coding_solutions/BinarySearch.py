"""

Given a sorted (in ascending order) integer array nums of n elements 

and a target value, write a function to search for target in nums. If 

target exists, then return its index, otherwise, return -1.

"""

def csBinarySearch(nums, target):
    for index,num in enumerate(nums):
        if target == num:
            return index
    return -1