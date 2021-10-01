n, x = list(map(int, input().strip().split()))
l = []
for i in range(x):
    l.append(list(map(float, input().strip().split())))
for i in zip(*l):
    print(sum(i)/len(i))