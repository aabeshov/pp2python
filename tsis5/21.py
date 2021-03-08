import os
alpha = list(input().split())
f = open("alphabet.txt","w")
for i in range(len(alpha)):
    f.write(str(i+1) + ")" + alpha[i] + "\n", )
