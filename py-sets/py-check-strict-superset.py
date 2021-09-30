a = set(map(int, input().strip().split()))
n = int(input().strip())
isStrict = True
for i in range(n):
    b = set(map(int, input().strip().split()))
    if not(b.intersection(a) == b and b!=a):
        isStrict = False
print(isStrict)