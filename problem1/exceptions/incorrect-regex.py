import re
n = int(input().strip())
for i in range(n):
    try:
        re.compile(input().strip());
        print(True)
    except:
        print(False)
