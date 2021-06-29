def fibofun(n):
    if(n==1):
        return 0;
    else:
        fibonaccilist = [0, 1]
        i = 2
        while i < n:
            c = fibonaccilist[-1] + fibonaccilist[-2]
            fibonaccilist.append(c)
            i = i + 1

    return fibonaccilist

num=int(input(" Enter the no of terms"))
if(num>0):
    {
    print(fibofun(num))
    }
else:
    {
        print("Can't be less than 1")
    }
