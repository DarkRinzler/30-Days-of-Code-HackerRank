# ===================================
#   Problem statement & information
# ===================================

# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent 
# (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    total_cost = meal_cost + (tip_percent*meal_cost/100) + (tax_percent*meal_cost/100)
    total_cost = round(total_cost)
    print(total_cost)
    

if __name__ == '__main__':

    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
