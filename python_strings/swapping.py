#take two inputs and swap first two characters in each string and replace them
#example 'abc' 'xyz' expected output is 'xyc' 'abz'
def swapping(str1,str2):
    char1 = str1[0:2]
    char2 = str2[0:2]
    str1 = str1.replace(char1,char2)
    str2 = str2.replace(char2,char1)
    return str1,str2
print(swapping(str1 =input("please enter string 1: "),str2 = input("please enter string 2: ")))

"""
method 2 using slicing
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))

"""
