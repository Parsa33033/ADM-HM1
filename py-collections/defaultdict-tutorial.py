from collections import defaultdict

n, m = list(map(int, input().strip().split()))
def defaultVal():
    return []
a = defaultdict(defaultVal)
for i in range(n):
    a[input().strip()].append(i+1)
for i in range(m):
    x = a[input().strip()]
    if x != None and len(x)>0:
        print(*x)
    else:
        print(-1)
# 5 2
# a
# a
# b
# a
# b
# a
# b