def sumoflist(list1):
    sum = 0
    for i in list1:
        sum += int(i)
    return sum

num=input("Enter the numbers in the list: ")
list =num.split(" ")
print("Sum = ", sumoflist(list))