# Open the file in read mode
text = open("sample.txt", "r")

words=[]
# Loop through each line of the file
for line in text:
    for j in line.split(" "):
        words.append(j)

    words.sort()
    for i in words:
        # Check if the word is already in dictionary

            print(i+"="+str(len(i)))

