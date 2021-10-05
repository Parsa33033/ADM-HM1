import html.parser as parser

class MyHTMLParser(parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for a, v in attrs:
            print("->", a, ">", v)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for a, v in attrs:
            print("->", a, ">", v)


n = int(input().strip())
s = ""
for i in range(n):
    s += input() + "\n"
p = MyHTMLParser()
p.feed(s)
