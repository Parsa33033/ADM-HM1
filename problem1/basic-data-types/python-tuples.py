import re
n = int(input().strip())
t = tuple(list(map(int, re.split("\s+", input().strip()))))
print(hash(t))
