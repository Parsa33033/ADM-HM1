import re
t = int(input().strip())
for i in range(t):
    n = input().strip()
    print(True if re.match(r"^[+-]?[0-9]*\.[0-9]+$", n) else False)
