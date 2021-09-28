import re
# Complete the solve function below.
def solve(s):
    return re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), s)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    # fptr.write(result + '\n')
    #
    # fptr.close()
