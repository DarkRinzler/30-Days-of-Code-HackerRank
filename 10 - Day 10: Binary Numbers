# ===================================
#   Problem statement & information
# ===================================

# Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 
# 1's in n's binary representation. 

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

def binary(num, arr):
    if num <= 1:
        arr.append(1)
        return arr
    else:
        arr.append(num % 2)
        return binary(num // 2, arr)

if __name__ == '__main__':
    
    n = int(input().strip())
    
    array1, array2 = [], []
    
    binary_form = binary(n, array1)
    
    counter = 0
    
    for k in range(len(binary_form)):
        if binary_form[k] == 1:
            counter +=1
        else:
            counter = 0
        array2.append(counter)
    print(max(array2))


# ===================================
#             Method 2
# ===================================

#!/bin/python3

import math
import os
import random
import re
import sys

def binary(num, arr):
    if num <= 1:
        arr.append(1)
        return arr
    else:
        arr.append(num % 2)
        return binary(num // 2, arr)

if __name__ == '__main__':
    
    n = int(input().strip())
    
    array1 = []
    
    counter, max_num = 0, 0
    
    binary_form = binary(n, array1)
    
    for k in binary_form:
        if k == 1:
            counter +=1
        else:
            max_num = max(max_num, counter)
            counter = 0
    print(max(max_num, counter))


# ===================================
#             Method 3
# ===================================

#!/bin/python3

import math
import os
import random
import re
import sys

def binary(num, counter, max_num):
    if num <= 1:
        counter += 1
        max_num = max(max_num, counter)
        return max_num
    else:
        if num % 2 == 1:
            counter += 1
            max_num = max(max_num, counter)
        else:
            counter = 0
        return binary(num // 2, counter, max_num)

if __name__ == '__main__':
    
    n = int(input().strip())
    
    counter, max_num = 0, 0
    
    print(binary(n, counter, max_num))
