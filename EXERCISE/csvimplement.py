import csv

f = open('file.csv', 'r')
cr = csv.reader(f)
for i in cr:
    print(i)

f.close()
f = open("file.csv", 'a')
cw = csv.writer(f)
d = input("enter the values separetd by space")
l = d.split()
cw.writerow(l)
f.close()
