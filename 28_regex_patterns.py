#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    firstName_list = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if re.search(r"@gmail.com", emailID):
            firstName_list.append(firstName)
    
    for x in sorted(firstName_list):
        print (x)
