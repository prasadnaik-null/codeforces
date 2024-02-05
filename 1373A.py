# 1373A - Donut Shops
for _ in range(int(input())):
    [a, b, c] = list(map(int, input().split()))
    if a <= c/b:
        print(1, -1)
    else:
        if a < c:
            print(1, b)
        else:
            print(-1, b)