import re
n = int(input().strip())
l = []
pattern = "#([0-9ABCDEFabcdef]{6}|[0-9ABCDEFabcdef]{3})"
startedBlock = False
for i in range(n):
    s = input().strip()
    if "{" in s:
        startedBlock = True
        s = s[s.index("{"):]
    elif s.endswith("}"):
        startedBlock = False
        s = s[:s.index("}")]
    if startedBlock:
        x = re.findall(pattern, s)
        if len(x)>0:
            for j in x:
                print("#"+j)