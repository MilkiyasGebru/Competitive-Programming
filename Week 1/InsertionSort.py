#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    x = arr[n-1]
    for var in range(n-1,-1,-1):
        if not var==0 and  arr[var-1] > x:
            arr[var] = arr[var-1]
        if not var==0 and x >arr[var-1] :    
            arr[var] =x
            print(*arr)
            break
        if var==0 and n>1 and x < arr[var+1]:    
            arr[0]=x
        print(*arr)    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
