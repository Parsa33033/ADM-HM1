import numpy as np
n, m = list(map(int, input().strip().split()))
l = []
for i in range(n):
    l.append(list(map(int, input().strip().split())))
arr = np.array(l)
print(arr.transpose())
print(arr.flatten())