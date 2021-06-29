nums=input("Enter integers seprated by space :")
numlist=nums.split(" ")
noevenlist=[i for i in numlist if int(i)%2 !=0 ]
print(noevenlist)
