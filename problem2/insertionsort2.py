#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    for i in range(0, len(arr)):
        j = i;
        while (j > 0 and arr[j] < arr[j-1]):
            temp = arr[j];
            arr[j] = arr[j-1];
            arr[j-1] = temp;
            j -= 1;
        if (i != 0):
            print(" ".join(list(map(str, arr))))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
