def superDigit(n, k):
    # if k == 1:
    #     return n
    # ni = int(n)
    # s = 0
    # while ni > 0:
    #     s += ni % 10
    #     ni //= 10
    # return superDigit(str(s), len(str(s)))
    return 1 + (k * sum(int(x) for x in n) - 1) % 9

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])
    # n = n * k
    result = superDigit(n, k)

    print(result)
