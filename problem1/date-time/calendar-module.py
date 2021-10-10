import calendar
w = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',]
w = [i.upper() for i in w]
mm, dd, yy = list(map(int, input().strip().split()))
print(w[calendar.weekday(yy, mm, dd)])