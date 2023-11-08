# ===================================
#   Problem statement & information
# ===================================

# Given a 6x6 2D Array, A, we define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation: 
#  a b c
#    d
#  e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#             Solutions
# ===================================

# ===================================
#             Method 1
# ===================================

#!/bin/python3

import math
import os
import random
import re
import sys

def sum_hourglass(arr, max_arr):
    for j in range(4):
        for s in range(4):
            partial_sum = 0
            for k in range(3):
                partial_sum += arr[j][k+s] + arr[j+2][k+s]
            partial_sum = partial_sum + arr[j+1][s+1]
            max_arr.append(partial_sum)
    print(max(max_arr))
    return
        

if __name__ == '__main__':

    arr, max_arr = [], []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    sum_hourglass(arr, max_arr)


# ===================================
#             Method 2
# ===================================

#!/bin/python3

import math
import os
import random
import re
import sys

def sum_hourglass(arr, partial_sum, max_arr):
    for j in range(4):
        for k in range(4):
            partial_sum.extend(arr[j][k:k+3]) 
            partial_sum.append(arr[j+1][k+1])
            partial_sum.extend(arr[j+2][k:k+3])
            max_arr.append(sum(partial_sum))
            partial_sum.clear()
    print(max(max_arr))
    return
        

if __name__ == '__main__':

    arr, partial_sum, max_arr = [], [], []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    sum_hourglass(arr, partial_sum, max_arr)

