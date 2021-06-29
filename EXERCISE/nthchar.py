string=input("Enter the string :")
if len(string)==0 :
    print("String is empty")
else:
    index=int(input("Enter the index of character you wish to remove :"))
    if index<0 or index >=len(string) :
        print("Wrong index")
    else :
       print("The resultant string is ",string[:index]+string[index+1:len(string)])
