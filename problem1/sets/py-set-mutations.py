an = int(input().strip())
a = set(map(int, input().strip().split()))
n = int(input().strip())
for i in range(n):
    s = input().strip().split()
    opr = s[0]
    sn = int(s[1])
    l = set(map(int, input().strip().split()))
    if opr == "update":
        a.update(l)
    elif opr == "intersection_update":
        a.intersection_update(l)
    elif opr == "symmetric_difference_update":
        a.symmetric_difference_update(l)
    elif opr == "difference_update":
        a.difference_update(l)
print(sum(a))