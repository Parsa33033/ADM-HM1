from collections import Counter

s = input().strip()
c = dict(Counter(s))
d = dict()
for k, v in c.items():
    d[v] = []
for k, v in c.items():
    d[v].append(k)
j = 3
for k, v in list(reversed(sorted(d.items(), key=lambda item: item[0]))):
    for i in sorted(v):
        if j == 0: break
        print(i, k)
        j -= 1