from collections import deque
t = int(input())
while t > 0:
    n = int(input().strip())
    l = list(map(int,input().split()))
    l = deque(l)
    right = l.pop()
    left = l.popleft()
    choice = 0
    if left > right:
        choice = left
    else: choice = right

    canBeOrdered = False
    while(len(l)>0):
        if(left >= right and left <= choice):
            choice = left
            left = l.popleft()
            last = left
        elif right > left and right <= choice:
            choice = right
            right = l.pop()
            last = right
        else:
            canBeOrdered= True
            break
    if canBeOrdered or last > choice:
        print("No")
    else:
        print("Yes")
    t -= 1

# 2
# 6
# 4 3 2 1 3 4
# 3
# 1 3 2