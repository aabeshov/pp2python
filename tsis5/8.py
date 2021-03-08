text = open("text.txt","r")
info = text.readlines()
maxi = -1
finder = -1
for i in range(len(info)):
    if maxi < len(info[i]):
        maxi = len(info[i])
        finder = i
print(info[finder],end = "")


