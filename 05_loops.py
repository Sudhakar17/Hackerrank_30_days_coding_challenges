# Question Link:
# https://www.hackerrank.com/challenges/30-loops/problem
"""
Task
Given an integer,n , print its first 10 multiples. Each multiple n x i
(where 1<=i<=10) should be printed on a new line in the form: n x i = result.
"""

import sys
n = int(input().strip())
for i in range(1,11):
    result = n*i
    print("{} x {} = {}".format(n,i,result))