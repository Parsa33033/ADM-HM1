import re
s = input()
k = input()
import re
pattern = re.compile(k)
searched = pattern.search(s)
found = False
while searched:
    print((searched.start(), searched.end() - 1))
    searched = pattern.search(s,searched.start() + 1)
    found = True
if not found:
    print((-1, -1))