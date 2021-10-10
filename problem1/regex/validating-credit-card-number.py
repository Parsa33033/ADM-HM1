import re

n = int(input().strip())
for i in range(n):
    credit = input().strip()
    credit_sep = credit.split("-")
    has_sep = len(credit_sep) > 1
    credit_sep = "".join(credit_sep)
    if re.search(r"((^[456][0-9]{15}$)|(^[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$))", credit) and not re.search(r"(\d)\1{3}", credit_sep):
        print("Valid")
    else:
        print("Invalid")