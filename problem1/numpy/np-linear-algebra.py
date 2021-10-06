import numpy as np
n = int(input().strip())
arr = []
for i in range(n):
    arr.append(list(map(float, input().strip().split())))
arr = np.array(arr)
print(np.round(np.linalg.det(arr),2))