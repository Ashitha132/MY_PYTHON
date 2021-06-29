string=input("enter 2 string separated by space :")
pos=string.find(' ')
str=string[pos+1]+string[1:pos]+" "+string[0]+string[pos+2:]
print(str)



