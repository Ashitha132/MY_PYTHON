
def strreverse(s):
    ss=""
    for i in s:
        ss=i+ss
    return ss

def newlist(l):
    sl=set(l)
    nl=list(sl)
    return nl
def aliquott(num):
    aliquotnum = 0
    for i in range(1, num - 1, 1):
        if num % i == 0:
            aliquotnum += i
    print("corresponding aliquot number is", aliquotnum)

def cases(s):
    u=0
    l=0
    for i in s:
        if ord(i)>=65 and ord(i)<=90 :
            u=u+1

        if ord(i)>=97 and ord(i)<=122 :
            l=l+1
    print("number of uppercase letters:", u)
    print("number of lowercase letters:",l)
