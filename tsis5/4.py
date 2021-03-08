text = open("text.txt","r")
info = text.readlines()
y = list(reversed(info))
cnt = int(input())
for i in range(cnt):
    print(y[i],end = "")