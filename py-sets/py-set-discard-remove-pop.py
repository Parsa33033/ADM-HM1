n = int(input().strip())
s = set(map(int, input().strip().split()))
N = int(input().strip())
for i in range(N):
    command = list(input().strip().split())
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        try:
            s.remove(int(command[1]))
        except:
            continue
    elif command[0] == "discard":
        s.discard(int(command[1]))
print(sum(s))