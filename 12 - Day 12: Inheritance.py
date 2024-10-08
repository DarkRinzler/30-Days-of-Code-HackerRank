# ===================================
#   Problem statement & information
# ===================================

# You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a 
# declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person. Complete the Student class 
# by writing the following:
# • A Student class constructor, which has  parameters:
#   1. A string, firstName.
#   2. A string, lastName.
#   3. An integer, idNumber.
#   4. An integer array (or vector) of test scores, scores.
# •A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#             Solution
# ===================================

#!/bin/python3

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.scores = scores
        super().__init__(firstName, lastName, idNumber)
    
    def calculate(self):
        average_grade = sum(self.scores) / len(self.scores)
        if 90 <= average_grade <= 100:
            return "O"
        elif 80 <= average_grade < 90:
            return "E"
        elif 70 <= average_grade < 80:
            return "A"
        elif 55 <= average_grade < 70:
            return "P"
        elif 40 <= average_grade < 55:
            return "D"
        else:
            return "T"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
