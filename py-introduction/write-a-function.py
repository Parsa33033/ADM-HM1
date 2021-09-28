n = int(input().strip())
def is_leap(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0: return True
            return False
        return True
    return False

print(is_leap(n))