#if the input of the string is less than 3 characters leave it unchanged
#or else change the last with ing if it does not end with ing
#or change to ly if it ends with ing
#input is abc o/p should be abcing i/p is string o/p is stringly
import pdb;pdb.set_trace()
def adding(str):
    length = len(str)
    if length < 3:
        return str
    else:
        if str[-3:] == 'ing':
            return str + 'ly'
        else:
            return str + 'ing'
    return str
print(adding('abc'))
print(adding('pugging'))
print('ab')

#method 2
"""
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
"""
