def palin(n):
    s=0
    t=n
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    print(s)
    if s==t :
        print("palindroem")
    else :
        print("not plaindrome")

num=int(input("Enter number "))
palin(num)