import html.parser as parser

# create a subclass and override the handler methods
class MyHTMLParser(parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start".ljust(5),":", tag)
        for i in attrs:
            print("->", i[0], ">", i[1])
    def handle_endtag(self, tag):
        print("End".ljust(5),":", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty".ljust(5),":", tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

# instantiate the parser and fed it some HTML
n = int(input().strip())
isComment = False
i = 0
while i < n:
    s = input().strip()
    if "<!--" in s and "-->" in s:
        isComment = False
        s = s[:s.index("<!--") + 4] + s[s.index("-->")+3:]
    elif "<!--" in s:
        isComment = True
        s = s[:s.index("<!--") + 4]
    elif "-->" in s:
        isComment = False
        s = s[s.index("-->")+3:]
    if "<" in s and not "<!--" in s and not ">" in s:
        s += " " + input().strip()
        n -= 1
    if not isComment:
        parser = MyHTMLParser()
        parser.feed(s)
    i += 1