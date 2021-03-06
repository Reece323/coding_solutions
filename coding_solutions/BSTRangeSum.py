"""

You are given the root node of a binary search tree (BST).

You need to write a function that returns the sum of values of all the nodes 

with a value between lower and upper (inclusive).

The BST is guaranteed to have unique values.

"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBSTRangeSum(root, lower, upper):
    
    if root is None:
        return 0
    
    if (root.value < lower) or (root.value > upper):
        root.value = 0
        
    return (root.value + csBSTRangeSum(root.left,lower,upper) + csBSTRangeSum(root.right,lower,upper))