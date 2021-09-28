www

# x = int(input().strip())
# y = int(input().strip())
# z = int(input().strip())
# n = int(input().strip())
# l = []

a = [1,2,3]

def swap(a, n, m):
    l = a
    temp = l[m]
    l[m] = l[n]
    l[n] = temp
    return l

def permutation(a, n):
    s = len(a)
    if n == s:
        return
    for i in range(n, s):
        li = swap(a, n, i)
        permutation(a, ie)


permutation(a, 0)