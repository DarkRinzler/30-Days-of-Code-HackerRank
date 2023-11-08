# ===================================
#   Problem statement & information
# ===================================

# Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a parameter. The constructor must assign 
# initialAge to age after confirming the argument passed as initialAge is not negative; if a negative argument is passed as initialAge, the constructor 
# should set age to 0 and print 'Age is not valid, setting age to 0'. In addition, you must write the following instance methods:
# 1. yearPasses() should increase the age instance variable by 1.
# 2. amIOld() should perform the following conditional actions:
#   a) If age < 13, print 'You are young.'.
#   b) If age >= 13 and age < 18, print 'You are a teenager.'.
#   c) Otherwise, print 'You are old.'.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#             Solution
# ===================================


class Person:
    def __init__(self, initialAge):
        if initialAge > 0:
            self.initialAge = age
        else:
            self.initialAge = 0
            print('Age is not valid, setting age to 0.')
            
    def amIOld(self):
        if self.initialAge < 13:
            print('You are young.')
        elif self.initialAge in range(13, 18):
            print('You are a teenager.')
        else:
            print('You are old.')
            
    def yearPasses(self):
        self.initialAge = self.initialAge + 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
