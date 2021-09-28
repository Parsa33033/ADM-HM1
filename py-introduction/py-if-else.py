n = int(input().strip())
isEven = n % 2 == 0
if not isEven:
    print("Weird")
elif isEven and 2 <= n <= 5:
    print("Not Weird")
elif isEven and 6 <= n <= 20:
    print("Weird")
elif isEven and n > 20:
    print("Not Weird")