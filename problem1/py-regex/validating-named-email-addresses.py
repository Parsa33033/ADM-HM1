import email.utils as em
import re
n = int(input().strip())
for i in range(n):
    email = input().strip()
    email = em.parseaddr(email)
    if re.match(r"^[A-Za-z][A-Za-z0-9\.|\-|\_]*\@[A-Za-z]+\.[A-Za-z]{1,3}$", email[1]):
        print(em.formataddr(email))
