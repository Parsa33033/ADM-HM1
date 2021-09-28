import re
n = int(input().strip())
lines = ""
for i in range(n):
    lines += input() + "\n"
lines = re.sub(r"(?:(?<=\s))&&(?=\s)", "and", lines)
lines = re.sub(r"(?:(?<=\s))\|\|(?=\s)", "or", lines)
print(lines)

# 1
# x&& &&& && && x || | ||\|| x