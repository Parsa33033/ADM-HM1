import re
n = int(input().strip())
l = []
for i in range(n):
    command = input().strip()
    c = list(map(int, re.split("\s+", command)[1:]))
    if "insert" in command:
        l.insert(c[0], c[1])
    elif "print" in command:
        print(l)
    elif "remove" in command:
        l.remove(c[0])
    elif "append" in command:
        l.append(c[0])
    elif "sort" in command:
        l.sort()
    elif "pop" in command:
        l.pop()
    elif "reverse" in command:
        l.reverse()
