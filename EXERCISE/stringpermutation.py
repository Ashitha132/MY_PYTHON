str1=input("Enter the string one")
str2=input("enter the string two")
f=0
l1=list(str1)
l2=list(str2)
l1.sort()
l2.sort()
if(len(l1)==len(l2)):
    for i in range(0, len(l1), ):
        if (l1[i] != l2[i]):
            f = 1

    if (f == 1):
        print("is not permuatation")
    else:
        print("permuation")
else:
    print("not permutation")
