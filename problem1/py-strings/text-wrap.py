# str = input().strip()
# x = int(input().strip())
# l = list(str)
# i = x
# while i < len(str):
#     l.insert(i, "\n")
#     i += x + 1
# print("".join(l))

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    str = input().strip()
    x = int(input().strip())
    print(wrap(str, x))