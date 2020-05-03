#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    # Fibonacci_analogue
    # If n = 1 stair -> 1 way, if n = 2 -> 2 ways, if n = 3 -> 4 ways
    # Because 3 - maximum number of stairs, he can climb at once
    wfs_1 = 1
    wfs_2 = 2
    wfs_3 = 4
    for i in range(n-1):
        wfs_1, wfs_2, wfs_3 = wfs_2, wfs_3, wfs_1 + wfs_2 + wfs_3
    return wfs_1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
