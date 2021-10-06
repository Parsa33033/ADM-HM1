import re
l = [print(p[1]) for p in re.findall("(?=([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]))", input().strip())]
if len(l) == 0 : print(-1)
