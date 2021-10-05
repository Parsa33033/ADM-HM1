import xml.etree.ElementTree as etree


maxdepth = 0
def depth(elem, level):
    global maxdepth
    if maxdepth == level:
        maxdepth += 1
    for t in elem:
        depth(t, level + 1)

if __name__ == '__main__':

    n = int(input().strip())
    s = ""
    for i in range(n):
        s += input() + "\n"

    tree = etree.ElementTree(etree.fromstring(s))
    depth(tree.getroot() - 1, 0)
    print(maxdepth)