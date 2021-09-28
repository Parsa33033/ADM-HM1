def print_rangoli(size):
    l = ["a", "b", "c", "d", "e", "f", "g",
         "h", "i", "j", "k", "l", "m", "n",
         "o", "p", "q", "r", "s", "t", "u",
         "v", "w", "x", "y", "z"]
    temp = l[:size]
    temp.reverse()
    n = 2 * size - 1
    m = n * 2 - 1
    def getCharList(i):
        t1 = temp[:i + 1]
        t2 = temp[:i]
        t2.reverse()
        return t1 + t2
    def printStr(i):
        s = getCharList(i)
        s = "-".join(c for c in s)
        print(s.center(m, "-"))
    for i in range(size):
        printStr(i)
    for i in range(size - 2, -1, -1):
        printStr(i)



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)