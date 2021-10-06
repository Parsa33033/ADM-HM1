s = input().strip()

u = [i for i in s if i.isupper()]
l = [i for i in s if i.islower()]
d = sorted([i for i in s if i.isdigit() and int(i)%2!=0], key= lambda item: item[0]) \
    + sorted([i for i in s if i.isdigit() and int(i)%2==0], key= lambda item: item[0])
u.sort()
l.sort()
print("".join(["".join(l), "".join(u), "".join(d)]))