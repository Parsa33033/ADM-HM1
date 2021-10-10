
def print_formatted(number):
    pad = len("{0:b}".format(n)) + 1

    for i in range(1, number + 1):
        decimal = str(i).rjust(pad - 1, " ")
        octal = "{0:o}".format(i).rjust(pad, " ")
        h = "{0:2x}".format(i).rjust(pad, " ").upper()
        bin = "{0:b}".format(i).rjust(pad, " ")
        print(decimal + octal + h + bin)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)