n = int(input().strip())
sn = set(input().strip().split())
m = int(input().strip())
sm = set(input().strip().split())
print(len(sn ^ sm))