f=open("sam.txt",'r')
o=open("odd.txt",'w')
e=open("even.txt",'w')
d=f.read().split()
for i in map(int,d):
    if(i%2==0):
        e.write(str(i)+' ')
    else:
        o.write(str(i)+' ')
