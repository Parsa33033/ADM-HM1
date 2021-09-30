import numpy as np
aarr = np.array(list(map(int, input().strip().split())))
barr = np.array(list(map(int, input().strip().split())))
print(np.inner(aarr, barr))
print(np.outer(aarr, barr))