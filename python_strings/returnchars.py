#to return first two and last two of the characters
def character_showing(str):
    if len(str) < 2:
        return ''

    return str[0:2] + str[-2:]
print(character_showing(str = input("please enter some string: ")))
