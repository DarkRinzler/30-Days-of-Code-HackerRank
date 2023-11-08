# ===================================
#   Problem statement & information
# ===================================

# Complete the factorial function in the editor below. Be sure to use recursion.
#
#Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#             Solution
# ===================================

#!/bin/python3

import os

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
