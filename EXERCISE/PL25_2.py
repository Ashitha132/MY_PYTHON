numstring=input("Enter list elements separated by space")
l=numstring.split(" ")
print(l)
numlist=list(map(int,l))
n=len(numlist)
m=n//2
numlist.sort()
if n%2 ==0  :
    median=(numlist[m - 1] + numlist[m]) / 2
else :
    median=numlist[m]
print("median of the list of elements is "+str(median))