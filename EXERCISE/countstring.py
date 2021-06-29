def strcount(s):
    c=0
    for i in s:
        c=c+1

    return c

str=input("Enter the string:")
print("THE number of characters in the string:",strcount(str))