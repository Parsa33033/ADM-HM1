from collections import OrderedDict
d = OrderedDict()
n = int(input().strip())
x = []
for i in range(n):
    l = input().strip().split()
    item = " ".join(l[0:len(l) - 1])
    netWorth = int(l[len(l) - 1])
    x.append((item, netWorth))
    d[item] = 0

for i in x:
    d[i[0]] += i[1]
for i,j in zip(d.keys(),d.values()):
    print(" ".join([i,str(j)]))