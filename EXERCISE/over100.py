nums=input("Enter intergers separate by space:")
integerlist=nums.split(' ')
newlist=[]
for i in integerlist:
    if(int(i)>100):
        newlist.append('over')
    else:
        newlist.append(i)
print(newlist)




