str=input("Enter a string  :")
first=str[0]
nstr=str.replace(first,'$')
print(nstr.replace('$',first,1))
