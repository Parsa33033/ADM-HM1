import numpy as np
n, m, p = list(map(int, input().strip().split()))
narr = []
marr = []
for i in range(n):
    narr.append(list(map(int, input().strip().split())))
for i in range(m):
    marr.append(list(map(int, input().strip().split())))
narr = np.array(narr)
marr = np.array(marr)
print(np.concatenate((narr, marr)))
