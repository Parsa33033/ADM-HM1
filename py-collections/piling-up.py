from collections import deque
t = int(input().strip())
canBeOrdered = True
for i in range(t):
    n = int(input().strip())
    d = deque(input().strip().split())
    for i in range(len(d)//2):
        right = d.pop()
        left = d.popleft()
        print(left, right)


# 2
# 6
# 4 3 2 1 3 4
# 3
# 1 3 2