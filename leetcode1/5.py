n = int(input("Введите n"))
multiple = 1
summa = 0
while n != 0:
    multiple = multiple * n//100
    print(multiple)
    summa += n//100
    print(summa)
    n = n//10
    print(n)
answer = (multiple - summa)
print(answer)