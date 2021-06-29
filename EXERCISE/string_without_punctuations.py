


def punctuationfun(s):
   punclist=[',','.','?','!',';',':','-','_','(',')','{','}','[',']','"',"'",]
   s1=""
   for i in s :
     if i not in punclist :
         s1+=i

   print("string without puntuations:",s1)


ss=input("Enter the string with punctuations:")
punctuationfun(ss)