import re
n = int(input().strip())
d = dict()
for i in range(n):
    l = re.split("\s+" ,str(input()).strip())
    d[l[0]] = [*list(map(float, l[1:]))]
q = input().strip()
q = d[q]
print("{:.2f}".format(sum(q)/len(q)))

