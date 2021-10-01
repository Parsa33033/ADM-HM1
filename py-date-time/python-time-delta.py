from datetime import datetime
t = int(input().strip())
time_format = '%a %d %b %Y %H:%M:%S %z'
for i in range(t):
    date1 = input().strip()
    date2 = input().strip()
    date1 = datetime.strptime(date1, time_format)
    date2 = datetime.strptime(date2, time_format)
    print(int(abs((date1 - date2).total_seconds())))