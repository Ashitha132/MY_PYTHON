num=int(input("Enter the count of integers you wish to insert"))
print("Enter",num,"integers")
numlist=[]
for i in range(num):
    j=int(input(""))
    numlist.append(j)
positivenumlist=[i for i in numlist if i>0]
print("The positive list of numbers is ",positivenumlist)