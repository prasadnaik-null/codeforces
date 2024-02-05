# 1359B - New Theatre Square
for _ in range(int(input())):
    [n, m, x, y], a = list(map(int, input().split())), 0
    if y >= 2*x:
        for _ in range(n):
            z = input()
            a += z.count(".")*x
    else:
        for _ in range(n):
            z = input()
            a += (z.count("..")*y)+((z.count(".")-z.count("..")*2)*x)
    print(a)