t = int(input().strip())
for i in range(t):
    an = int(input().strip())
    al = set(map(int, input().strip().split()))
    bn = int(input().strip())
    bl = set(map(int, input().strip().split()))
    if al.intersection(bl) == al:
        print(True)
    else:
        print(False)