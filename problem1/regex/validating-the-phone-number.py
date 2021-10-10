regex_pattern = r"^(7|8|9)[0-9]{9}$"    # Do not delete 'r'.

import re

n = int(input().strip())
l = []
for i in range(n):
    l.append(input().strip())
for i in l:
    print(str("YES" if bool(re.match(regex_pattern, i)) else "NO"))