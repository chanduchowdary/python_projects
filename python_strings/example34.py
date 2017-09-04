#Write a Python program to print the following integers
# with '*' on the right of specified width
x = 34
y = 123
print("\nOriginal Value = ",x)
print("Formatted number with right padding with * : "+"{:*<3d}".format(x));
print("\nOriginal Value = ",y)
print("Formatted number with right padding with * : "+"{:*<6d}".format(y));


