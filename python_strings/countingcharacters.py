def character_count(characters):
    dict = {}
    for n in characters:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(character_count(characters= input("enter something which you like: ")))