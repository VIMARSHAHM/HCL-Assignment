# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:28:06 2020

@author: VIMARSHA H M
"""
# =============================================================================
# 
# Encoding a string the below format to reduce the size of the string.
# A string of lowercase characters in range ascii[‘a’..’z’]. We want to reduce the string to its shortest length by doing a series of operations. In each operation we select a pair of adjacent lowercase letters that match, and delete them. For instance, the string aab could be shortened to b in one operation. Now we have to delete as many characters as possible using this method and print the resulting string. If the final string is empty, print Empty String
# 
# Function Description
# 
# Complete the MaxReducedString function. It should return the super reduced string or Empty String if the final string is empty.
# 
# superReducedString has the following parameter(s):
# 
# s: a string to reduce
#  
# 
# Output Format
# 
#      If the final string is empty, print Empty String; otherwise, print the final non-reducible string.
# 
# Input à    Output
# 
# aaabccddd will get reduced to→ abccddd  will get reduced to → abddd  will get reduced to → abd
# 
# =============================================================================

def superReducedString(s):
    if not s:
        return "Empty String"
    for i in range(0,len(s)):
        if i < len(s)-1:
            if s[i] == s[i+1]:
                return superReducedString(s[:i]+s[i+2:])
    return s
print(superReducedString("aaabccddd"))