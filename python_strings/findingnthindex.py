def find_nth_index(str,n):
    first_part = str[:n]
    last_part = str[n+1:]
    return first_part + last_part
print(find_nth_index('python',0))
print(find_nth_index('python',2))
print(find_nth_index('python',3))
