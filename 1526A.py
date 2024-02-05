# 1526A - Mean Inequality
for _ in range(int(input())):
    n, l, a = int(input()), sorted(
        list(map(int, input().split()))), []
    for i in range(n):
        a.append(l[i])
        a.append(l[n+i])
    print(*a)