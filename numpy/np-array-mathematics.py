import numpy as np
n, m = list(map(int, input().strip().split()))
aarr = []
barr = []
for i in range(n):
    aarr.append(list(map(int, input().strip().split())))
for i in range(n):
    barr.append(list(map(int, input().strip().split())))
aarr, barr = [np.array(aarr), np.array(barr)]
print(aarr + barr)
print(aarr - barr)
print(aarr * barr)
print(np.floor_divide(aarr, barr))
print(aarr % barr)
print(aarr ** barr)

