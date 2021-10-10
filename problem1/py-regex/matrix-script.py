#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
s = ""
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for z in zip(*matrix):
    s += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", s))