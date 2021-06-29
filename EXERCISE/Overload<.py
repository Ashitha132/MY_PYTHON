class Over:
    x = 0
    y = 0

    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

    def __str__(self):
        return '(%d,%d)' %(self.x,self.y)

    def __lt__(self, other):
        return self.x * self.y < other.x * other.y


o1 = Over(2, 3)
o2 = Over(3, 5)
print(o1)
print(o2)
print(o1 < o2)
if(o1<o2):
    print("Area of Second rectangle is higher ")
else :
    print("Area of first rectangle is higher")

