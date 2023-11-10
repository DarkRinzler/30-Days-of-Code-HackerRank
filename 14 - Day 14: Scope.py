# ===================================
#   Problem statement & information
# ===================================

# The absolute difference between two integers, a and b, is written as |a-b|. The maximum absolute difference between two integers in a set of 
# positive integers, elements, is the largest absolute difference between any two integers in __elements. 
# Complete the Difference class by writing the following:
# • A class constructor that takes an array of integers as a parameter and saves it to the  instance variable.
# • A computeDifference method that finds the maximum absolute difference between any numbers in __elements and stores it in the maximumDifference
#   instance variable.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#             Solution
# ===================================

#!/bin/python3

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    
    def computeDifference(self):
        for k in range(len(self.__elements)):
            for s in range(k+1, len(self.__elements)):
                diff = abs(self.__elements[k] - self.__elements[s])
                self.maximumDifference = max(self.maximumDifference, diff)
        return self.maximumDifference
                

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
