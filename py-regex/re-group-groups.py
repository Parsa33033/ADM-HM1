import re
s = input().strip()
p = re.compile(r"([A-Za-z0-9])\1{1,}")
s = p.search(s)
print(s.group(0)[0] if s != None else -1)
