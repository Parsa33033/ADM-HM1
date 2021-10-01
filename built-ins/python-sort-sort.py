n, m = list(map(int, input().strip().split()))
l = []
for i in range(n):
    l.append(list(map(int, input().strip().split())))
k = int(input().strip())
for i in sorted(l, key=lambda item: item[k]):
    print(*i)
