import numpy as np
n = int(input().strip())
aarr = []
barr = []
for i in range(n):
    aarr.append(list(map(int, input().strip().split())))
for i in range(n):
    barr.append(list(map(int, input().strip().split())))
aarr, barr = [np.array(aarr), np.array(barr)]
print(np.dot(aarr, barr))