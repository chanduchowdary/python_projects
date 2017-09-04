#to replace the character with $ except the first one which is repeating
#example restart should be resta$t
def replacing(str):
    char = str[0]
    length = len(str)
    str = str.replace(char,'$')
    str = char + str[1:]
    return str

print(replacing(str = input("please enter the input string to apply: ")))