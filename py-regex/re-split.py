import re
s = input().strip()
l = re.split("[,.]", s)
for i in l:
    print(i)