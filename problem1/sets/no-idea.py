n, m = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
a = set(map(int, input().strip().split()))
b = set(map(int, input().strip().split()))
h = 0
for i in arr:
    if i in a:
        h += 1
    elif i in b:
        h -= 1
print(h)