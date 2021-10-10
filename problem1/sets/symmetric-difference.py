M = int(input().strip())
ml = set(map(int, input().strip().split()))
N = int(input().strip())
nl = set(map(int, input().strip().split()))
l = list(ml.difference(nl).union(nl.difference(ml)))
l.sort()
for i in l:
    print(i)