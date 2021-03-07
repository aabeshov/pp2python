x = str(input())
summ = 0
product = 1
for i in range(len(x)):
    summ += int(x[i])
    product *= int(x[i])
print(product - summ)