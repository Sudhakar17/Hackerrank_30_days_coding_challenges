
"""Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base-10 integer
denoting the maximum number of consecutive 1's in n's binary representation."""

import sys


def func(num):
  return max(map(len, bin(num)[2:].split('0')))


n = int(input().strip())
print(func(n))