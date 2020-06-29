# Question Link:
# https://www.hackerrank.com/challenges/30-review-loop/problem
"""
Task
Given a string S of length N that is indexed from  0 to N-1 ,
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line
"""

t = int(input())
for i in range(0, t):
    s = input()
    even_idx_str = []
    odd_idx_str = []

    for i in range(len(s)):
        if i%2 == 0:
            even_idx_str.append(s[i])
        else:
            odd_idx_str.append(s[i])

    print("{}  {}".format(''.join(even_idx_str),''.join(odd_idx_str)))
