def minion_game(string):
    vowels = ["A", "E", "I", "O", "U"]
    stuart = 0 #constonance
    kevin = 0 #start with vowel
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
            kevin += length - i
            print(kevin)
            print(string[i:])
        else:
            stuart += length - i
    if stuart == kevin:
        print("Draw")
    else:
        print("Stuart",stuart) if stuart > kevin else print("Kevin", kevin)


if __name__ == '__main__':
    s = input()
    minion_game(s)