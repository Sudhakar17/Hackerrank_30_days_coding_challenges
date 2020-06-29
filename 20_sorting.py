# Question Link:
# https://www.hackerrank.com/challenges/30-sorting/problem


# bubble sorting

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap_counter = 0
for i in range(n):
    
    for j in range(n-1):
        if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            swap_counter +=1
            
print ("Array is sorted in {} swaps.".format(swap_counter))
print ("First Element: {}".format(a[0]))
print ("Last Element: {}".format(a[n-1]))