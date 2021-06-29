def d1(a):
    s=[]
    while(a>0):
        r=a%2
        s.append(r)
        a=a//2
    ss=s[::-1]
    for i in ss:
        print(i,end=" ")

number=int(input("enter the number "))
d1(number)


