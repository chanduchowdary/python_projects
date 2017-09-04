#take input randomly and dislpay it randomly in sorted order
"""
sample input: red,black,green
output:black,green,red
"""
words_list = input("enter the words with comma separated values:")
words = [word for word in words_list.split(",")]

print(",".join(sorted(list(set(words)))))