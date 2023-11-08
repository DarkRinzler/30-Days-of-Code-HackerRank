# ===================================
#   Problem statement & information
# ===================================

# Given an integer, n, print its first 10 multiples. Each multiple n x i (where 1 <= i <= 10) should be printed on a new line in the form: n x i = result.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

Solution:

#!/bin/python3

import math
import os
import random
import re
import sys

def time_tables(number):
    for k in range(1, 11):
        result = number * k
        print("{0} x {1} = {2}".format(number, k, result))
    return
    

if __name__ == '__main__':
    
    n = int(input().strip())
    
    time_tables(n)
