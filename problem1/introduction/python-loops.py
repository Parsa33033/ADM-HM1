n = int(input().strip())
print(*[str(i ** 2).strip() for i in range(n)], sep="\n")