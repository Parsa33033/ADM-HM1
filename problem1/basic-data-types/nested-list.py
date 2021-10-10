n = int(input().strip())
l = []
for i in range(n):
    s = []
    s.append(input().strip())
    s.append(float(input()))
    l.append(s)
d = dict()
for i in l:
    if d.get(i[1]) == None:
        d[i[1]] = [i[0]]
    else:
        d[i[1]].append(i[0])
grades = list(d.keys())

min1 = grades[0]
min2 = 100
for i in range(1, len(grades)):
    if grades[i] < min1:
        min2 = min1
        min1 = grades[i]
    elif grades[i] > min1 and grades[i] < min2:
        min2 = grades[i]

for i in sorted(d[min2]):
    print(i)
