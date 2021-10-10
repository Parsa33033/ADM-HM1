import html.parser as parser
import re

class MyHTMLParser(parser.HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            l = re.split("\n", data)
            for i in l:
                print(i)
        else:
            print(data)
    def handle_data(self, data):
        print(">>> Data")
        print(data)


n = int(input().strip())
i = 0
while i < n:
    s = input().strip()
    if "<!--" in s and "-->" not in s:
        while "-->" not in s:
            s += "\n" + input().strip()
            n -= 1
        print(">>> Multi-line Comment")
    elif "<!--" in s and "-->" in s:
        print(">>> Single-line Comment")
    p = MyHTMLParser()
    p.feed(s)
    i += 1