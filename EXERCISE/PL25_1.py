class student:
    rollno_25=1
    mark1=20
    mark2=18 #default values
    def readData(self,r,m1,m2):
        self.rollno=r
        self.mark1=m1
        self.mark2=m2
    def computeTotal(self):
        return (self.mark1+self.mark2)
    def printDetails(self):
        print("RollNo:",self.rollno)
        print("Mark1:", self.mark1)
        print("Mark2:", self.mark2)
        print("Total:", self.mark1+self.mark2)
        print("**********************")



s1= student()
s2= student()
s3= student()
s1.readData(1,20,19)
s2.readData(1,10,30)
s3.readData(1,20,15)
s1.printDetails()
s2.printDetails()
s3.printDetails()
t1=s1.computeTotal()
t2=s2.computeTotal()
t3=s3.computeTotal()
if t1>t2 and t1>t3 :
    print("First Student is Topper")
elif t2>t3:
    print("Second student is the Topper")
else :
    print("Third stuent is the Topper")