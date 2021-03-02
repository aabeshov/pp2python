a = list(map(int,input().split()))
b,c = map(int,input().split())
print([i in range(b,c+1) for i in a])