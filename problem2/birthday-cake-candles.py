#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    tempMax = 0
    countmax = 0
    for i in candles:
        if i > tempMax:
            tempMax = i
    for i in candles:
        if i == tempMax:
            countmax += 1
    return countmax

if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(result)
