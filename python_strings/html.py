#write a program to define html text
def add_tags(tag,word):
    return "<%s>%s" % (tag,word,tag)
print(add_tags('i','python'))
print(add_tags('b','html texture'))