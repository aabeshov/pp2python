text = open('text.txt','a')
text.write(input()+ '\n')
text.close

text = open('text.txt','r')
print(text.read())