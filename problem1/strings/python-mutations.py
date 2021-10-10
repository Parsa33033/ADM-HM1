def mutate_string(string, position, character):
    string = string[0:position] + character + string[position+1:len(string)]
    return string

s = "parsa"
print(mutate_string(s, 1, "b"))