import mod1
n=input("enter a string")
print("reversed string is",mod1.strreverse(n))
mod1.cases(n)
l=input("enter list separeted by space")
ll=l.split(" ")
print("new list with unique elements in given list is :",mod1.newlist(ll))
