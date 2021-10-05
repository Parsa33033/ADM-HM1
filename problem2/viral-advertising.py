#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
l = []
def viralAdvertising(n):
    if n == 1: return 5
    p = (viralAdvertising(n-1)//2)
    l.append(p)
    return p*3

if __name__ == '__main__':

    n = int(input().strip())

    result = viralAdvertising(n)
    l.append(result//2)
    print(sum(l))
