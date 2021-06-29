# unique checking of an string without other data structures
str="Ashith"
flag=0
for i in range(0,len(str)):
    for j in range(i+1,len(str)):
        if(str[i]==str[j]):
            flag=1
if(flag==1):
    print("Not unique")
else:
    print("unique")
# take O(n^2) time and O(n) space


