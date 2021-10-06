string = input().strip()
sub_string = input().strip()

def count_substring(string, sub_string):
    sL = len(string)
    subL = len(sub_string)
    n = 0
    for i in range(sL):
        if sub_string[0] == string[i] and sub_string == string[i: i + subL]:
            n += 1;
    return n

print(count_substring(string, sub_string))