num=int(input("Enter the count of integers you wish to insert"))
print("Enter",num,"integers")
numlist=[]
for i in range(num):
    j=int(input(""))
    numlist.append(j)
squarelist=[i*i for i in numlist ]
print("The  list of squares of given number is  ",squarelist)