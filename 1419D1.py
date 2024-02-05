# 1491D1 - Sage's Birthday (easy version)
n, l, z = int(input()), sorted(list(map(int, input().split()))), []
print((n-1)//2)
for i in range(n):
    if i % 2 == 0:
        z.append(l[n-1-i//2])
    else:
        z.append(l[i//2])
print(*z)