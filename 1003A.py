# 1003A - Polycarp's Pockets
n, l, i, a = int(input()), sorted(list(map(int, input().split()))), 0, 0
while i < n:
    x = l.count(l[i])
    a = max(a, x)
    i += x
print(a)