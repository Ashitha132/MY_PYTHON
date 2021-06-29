def pas(s):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"

str=input("Enter the string")
strist=str.split()

for i in  str:
    if i not  in alphabet:
        print("not pangram ")


