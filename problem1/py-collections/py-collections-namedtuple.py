from collections import namedtuple

n = int(input().strip())
Student = namedtuple("Student", input().strip())
markAvg = 0;
l = []
for i in range(n):
    l.append(Student(*list(input().strip().split())))
for i in l:
    markAvg += int(i.MARKS)
print("{:.2f}".format(markAvg/len(l)))