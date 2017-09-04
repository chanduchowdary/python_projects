#to find the length of the string
#length = input("enter the string: ")
def str_length(length):
    count = 0
    for char in length:
        count += 1
    return count
print(str_length(length = input("enter the string: ")))