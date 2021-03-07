x = [int(i) for i in input().split()]

for i in x:
    if i < 0:
        x.remove(i)
        continue
print(min(x))
    