from collections import Counter
x = int(input().strip())
l = Counter(list(map(int, input().strip().split())))
n = int(input().strip())
earned = 0
for i in range(n):
    shoeSize, xi = list(map(int, input().strip().split()))
    if l.get(shoeSize) and l.get(shoeSize) >= 1:
        earned += xi
        l[shoeSize] -= 1
print(earned)