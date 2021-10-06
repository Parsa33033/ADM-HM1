n = int(input().strip())
l = list(map(int, input().strip().split()))
d = dict()
for i in l:
    try:
        d[i] += 1
    except:
        d[i] = 1
print(list(d.keys())[list(d.values()).index(1)])
