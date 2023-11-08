# ===================================
#   Problem statement & information
# ===================================

# Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

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

def print_array(array):
    for k in range(len(array)):
        print(array[len(array)-k-1], end=' ')
    return

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    print_array(arr)


# ===================================
#             Method 2
# ===================================

#!/bin/python3

import math
import os
import random
import re
import sys

def print_array(array):
    array.reverse()
    for k in range(len(array)):
        print(array[k], end=' ')
    return

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    print_array(arr)


# ===================================
#             Method 3
# ===================================

#!/bin/python3

import math
import os
import random
import re
import sys

def print_array(array):
    left = 0
    right = len(array) - 1
    while left < right:
        temp_value = array[left]
        array[left] = array[right]
        array[right] = temp_value
        left +=1
        right -=1
    print(' '.join(map(str, array)))
    return

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    print_array(arr)

