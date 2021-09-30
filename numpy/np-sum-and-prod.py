import numpy as np
n, m = list(map(int, input().strip().split()))
arr = []
for i in range(n):
   arr.append(list(map(int, input().strip().split())))
print(np.prod(np.sum(np.array(arr), axis=0)))