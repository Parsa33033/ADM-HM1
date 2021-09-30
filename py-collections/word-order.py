from collections import OrderedDict

d = OrderedDict()
n = int(input().strip())
l = []
for i in range(n):
    word = input().strip()
    l.append(word)
    d[word] = 0
for i in l:
    d[i] += 1
print(len(d))
print(*d.values())
