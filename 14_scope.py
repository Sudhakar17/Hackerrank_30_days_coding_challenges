# Question Link:
# https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    maximumDifference = 0
    def computeDifference(self):
        self.__elements = sorted(self.__elements)
        for i in range(len(self.__elements)-1):
            tmp = abs(self.__elements[0] - self.__elements[i + 1])
            if  tmp > self.maximumDifference:
                self.maximumDifference = tmp

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)