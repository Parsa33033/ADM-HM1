import xml.etree.ElementTree as etree

def get_attr_number(node):
    lattr = 0
    for t in node:
        lattr += get_attr_number(t)
    return lattr + len(node.attrib)

if __name__ == '__main__':

    n = int(input().strip())
    s = ""
    for i in range(n):
        s += input() + "\n"

    tree = etree.ElementTree(etree.fromstring(s))
    print(get_attr_number(tree.getroot()))