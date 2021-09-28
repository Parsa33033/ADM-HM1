import re
n, m = list(map(int, re.split("\s+", input().strip())))
c = ".|."

for i in range(n):
    if i < n//2:
        print((c * (2*i + 1)).center(m, "-"))
    elif i == n//2:
        print("WELCOME".center(m, "-"))
    else:
        j = n - i - 1
        print((c * (2*j + 1)).center(m, "-"))