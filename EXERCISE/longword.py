def funlong(slist):
    l=0
    for i in slist:
        if len(i) >l:
            l=len(i)

    return l

word=input("Enter words separated by space ")
s=word.split(" ")
print("Length of longest word is",funlong(s))