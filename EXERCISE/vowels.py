word=input("enter a word")
vowel=['A','E','I','O','U','a','e','i','o','u']
s=""
for i in word :
    if i not in vowel :
        s+=i

print("string removing vowels is",s)