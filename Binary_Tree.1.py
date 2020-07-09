# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:16:32 2020

@author: VIMARSHA H M
"""


# =============================================================================
# Design a binary tree and then write an algorithm to print the least(nearest) two common parent(if 2 parents exist otherwise 1  common parent) node between 2 nodes of a binary tree for given 2 key values which are present in binary tree.
# Input  :  If below tree and values 1 and 5 given
# 
# Output : 2
# 
# Input  :  If below tree and values 3 and 6 given
# 
# Output : 2 
# 
# Input  :  If below tree and values 4 and 6 given
# 
# Output : 2 and 3
# =============================================================================


# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Function to check if given node is present in binary tree or not
def isNodePresent(root, node):

    # base case
    if root is None:
        return False

    # if node is found, return true
    if root == node:
        return True

    # return true if node is found in the left subtree or right subtree
    return isNodePresent(root.left, node) or isNodePresent(root.right, node)



def findlca(root, lca, x, y):

    # base case 1: return false if tree is empty
    if root is None:
        return False, lca

    # base case 2: return true if either x or y is found
    # with lca set to the current node
    if root == x or root == y:
        return True, root

    # recursively check if x or y exists in the left subtree
    left, lca = findlca(root.left, lca, x, y)

    # recursively check if x or y exists in the right subtree
    right, lca = findlca(root.right, lca, x, y)

    # if x is found in one subtree and y is found in other subtree,
    # update lca to current node
    if left and right:
        lca = root

    # return true if x or y is found in either left or right subtree
    return (left or right), lca


# Function to find lowest common ancestor of nodes x and y
def findLCA(root, x, y):

    # lca stores lowest common ancestor
    lca = None

    # call LCA procedure only if both x and y are present in the tree
    if isNodePresent(root, y) and isNodePresent(root, x):
        lca = findlca(root, lca, x, y)[1]

    # if LCA exists, print it
    if lca:
        print("LCA is", lca.data)
    else:
        print("LCA do not exist")


if __name__ == '__main__':
    

    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    #root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(5)
    #root.right.left.left = Node(7)
    root.right.right.right = Node(6)

    findLCA(root, root.left, root.right.right)
    findLCA(root, root.right, root.right.right.right )
    findLCA(root, root.right.left, root.right.right.right)
    