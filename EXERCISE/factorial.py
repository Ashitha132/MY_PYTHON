def facto(n):
    if n==1 :
        return 1
    else :
        return(n*facto(n-1))

num=int(input("Enter num:"))
print(facto(num))