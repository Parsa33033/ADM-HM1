from collections import deque
n = int(input().strip())
d = deque()
for i in range(n):
    l = list(input().strip().split())
    command = l[0]
    if len(l)>1:
        val = l[1]
    if command == "append":
        d.append(val)
    elif command == "appendleft":
        d.appendleft(val)
    elif command == "pop":
        d.pop()
    elif command == "popleft":
        d.popleft()
print(" ".join(d))