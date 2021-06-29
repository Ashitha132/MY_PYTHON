str=input("Enter a line of text :")
wordlist=str.split(' ')
wordset=set(wordlist)
wordlist1=list(wordset)
print("count of each word in the text:")
for i in wordlist1:
        print(i,"=",wordlist.count(i))

