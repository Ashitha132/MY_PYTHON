def gcdfunction(a,b):
    if(a<b):
        s=a
    else :
        s=b
    for i in range(1,s+1):
        if(a%i==0 and b%i==0):
            g=i

    return g

x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
print("gcd=",gcdfunction(x,y))