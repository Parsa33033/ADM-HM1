t = int(input().strip())
for i in range(t):
    try:
        a, b = list(map(int, input().strip().split()))
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except Exception as e:
        print("Error Code:",e)