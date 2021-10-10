# str = input().strip()
# n = len(str)
# l = "".join([c.lower() if c.isupper() else c.upper() if c.islower() else c for c in str])
# print(l)

def swap_case(s):
    return "".join([c.lower() if c.isupper() else c.upper() if c.islower() else c for c in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)