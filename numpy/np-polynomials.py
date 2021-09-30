import numpy as np
l = list(map(float, input().strip().split()))
x = int(input().strip())
print(np.polyval(l, x))