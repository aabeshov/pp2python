text = open("text.txt","r")
cnt = int(input())
for i in range(cnt):
    print(text.readline(),end = "")
text.close()