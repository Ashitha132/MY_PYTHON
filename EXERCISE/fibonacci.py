def fibofun(n):
    fibonaccilist=[0,1]
    i=2
    while i<n:
        c = fibonaccilist[-1] + fibonaccilist[-2]
        fibonaccilist.append(c)
        i=i+1
    return fibonaccilist

num=int(input(" Enter the no of terms"))
print(fibofun(num))