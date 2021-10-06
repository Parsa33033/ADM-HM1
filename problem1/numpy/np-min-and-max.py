import numpy as np
n, m = list(map(int, input().strip().split()))
arr = []
for i in range(n):
    arr.append(list(map(int, input().strip().split())))
print(np.max(np.min(np.array(arr), axis=1)))