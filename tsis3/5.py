a = input().split()
j = int(input())
j *= (-1)
print(j)
j %= len(a)
print(j)
print(a)
a = a[j:] + a[:j]
print(a)
for x in a:
  print(x, end = " ")