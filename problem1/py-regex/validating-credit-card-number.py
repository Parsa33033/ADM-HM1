import re

def has_repeat(s):
    count = 0
    chars = "1234567890"
    for char in chars:
        count = s.count(char)
        if count > 1:
            print
            char, count
    return True if count!=0 else False

n = int(input().strip())
for i in range(n):
    credit = input().strip()
    # print(re.match(r"(\w)\1{3}", credit)) not working - don't know why
    if re.match(r"((^[456][0-9]{15}$)|(^[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$))", credit) and not has_repeat(credit):
        print("Valid")
    else:
        print("Invalid")