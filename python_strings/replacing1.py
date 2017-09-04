#to find if poor and bad is there in the substring and change if not and poor to good
#str = 'not that poor' o/p = 'good'
def replacing(str):
    str1 = str.find('not')
    str2 = str.find('poor')
    if str2 > str1:
        str = str.replace(str[str1:(str2+4)],'good')
    return str
print(replacing(str = input("please enter the string:")))
