# ===================================
#   Problem statement & information
# ===================================

# Given an integer n, perform the following conditional actions:
# 1. If n is odd, print 'Weird'
# 2. If n is even and in the inclusive range of  to , print 'Not Weird'
# 3. If n is even and in the inclusive range of  to , print 'Weird'
# 4. If n is even and greater than 20, print 'Not Weird'

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#             Solution
# ===================================

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    N = int(input().strip())
    if N % 2 != 0:
        print("Weird")
    else:
        if N in range(2, 6):
            print("Not Weird")
        elif N in range(6, 21):
            print("Weird")
        elif N > 20: 
            print("Not Weird")
