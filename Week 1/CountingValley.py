#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    steps = len(path)
    num = 0
    valley=0
    x=0
    while num < len(path) :
        if path[num] == 'D':
            if  x==0 :
                valley=valley+1    
            x=x+1
        if path[num] =='U' :
            x=x-1
        num=num+1    
    return valley        
            
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
