# 1304A - Two Rabbits
for _ in range(int(input())):
    [x, y, a, b] = list(map(int, input().split()))
    if (y-x) % (a+b) == 0:
        print((y-x)//(a+b))
    else:
        print(-1)