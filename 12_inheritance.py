# Question Link:
# https://www.hackerrank.com/challenges/30-inheritance/problem

"""
Task:

You are given two classes, Person and Student, where Person is the base class and Student is the derived class.
Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student
inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
A string, firstName.
A string, lastName.
An integer, id .
An integer array (or vector) of test scores, scores .
A char calculate() method that calculates a Student object's average and returns the grade character representative
of their calculated average:
"""


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):


    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    def __init__(self, firstName, lastName, idNum, scores):
        super(Student, self).__init__(firstName, lastName, idNum)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    def calculate(self):
        avg_score = sum(self.scores) / len(self.scores)
        if 90 <= avg_score <= 100:
            return "O"
        elif 80 <= avg_score <= 90:
            return "E"
        elif 70 <= avg_score <= 80:
            return "A"
        elif 55 <= avg_score <= 70:
            return "P"
        elif 40 <= avg_score <= 55:
            return "D"
        elif avg_score < 40:
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