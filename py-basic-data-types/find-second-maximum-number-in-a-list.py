import re
n = int(input().strip())
scores = list(map(int, re.split("\s+", str(input().strip()))))
max1 = scores[0]
max2 = -100
for i in range(1, len(scores)):
    if scores[i] > max1:
        max2 = max1
        max1 = scores[i]
    elif scores[i] > max2 and scores[i] < max1:
        max2 = scores[i]

print(max2)