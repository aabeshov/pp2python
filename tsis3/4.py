m = [int(i) for i in input().split()]
for i in m:
    if i != 0:
        print(i, end = " ")
        continue
for i in m:
    if i == 0:
        print(i, end = " ")