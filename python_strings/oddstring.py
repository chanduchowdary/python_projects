def oddoneout(str):
    result=  " "
    for i in range(len(str)):
        if i % 2:
            result = result + str[i]
    return result
print(oddoneout("abcdef"))
print(oddoneout("uvwxyz"))