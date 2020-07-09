# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:05:06 2020

@author: VIMARSHA H M
"""

# =============================================================================
# 
# Design a  binary tree and then print the breadth first order traversal of this tree. In breadth first order traversal, we visit the nodes of same height first then go to nodes of next height or level.
#      1
# 
#       \
# 
#        2
# 
#         \
# 
#          5
# 
#         /  \
# 
#        3    6
# 
#         \
# 
#          4 
# 
# For the above tree, the level order traversal is 1 -> 2 -> 5 -> 3 -> 6 -> 4.
# =============================================================================

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# Function to print all nodes of a given level from left to right
def printLevel(root, level):

    # base case
    if root is None:
        return False

    if level == 1:
        print(root.key, end=' ')

        # return true if at-least one node is present at given level
        return True

    left = printLevel(root.left, level - 1)
    right = printLevel.(root.right, level - 1)

    return left or right


# Function to print level order traversal of given binary tree
def levelOrderTraversal(root):

    # start from level 1 -- till height of the tree
    level = 1

    # run till printLevel() returns false
    while printLevel(root, level):
        level = level + 1


if __name__ == '__main__':

    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(6)
    root.right.right.left = Node(3)
    root.right.right.left.right = Node(4)

    levelOrderTraversal(root)