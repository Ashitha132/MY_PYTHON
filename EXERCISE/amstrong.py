def amstrong(n):
    s=0
    t=n
    while(n>0):
        r=n%10
        s+=r**3
        n=n//10
    if s==t :
        print("amstrong")
    else :
        print("not amstrong")

num=int(input("Enter number "))
amstrong(num)