bin=int(input("enter the binary number"))
dec=0
i=0
while(bin!=0):
    r=bin%10
    dec=dec+(r*pow(2,i))
    i=i+1
    bin=bin//10
print("corresponding decimal"
      " number is ",dec)

