def sod(n):
    s=0
    while(n>0):
        r=n%10
        s=s+r
        n=n//10

    return s

num=int(input("Enter number "))
print("Sum of digit=",sod(num))