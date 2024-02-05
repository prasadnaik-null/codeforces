# 1631A - Min Max Swap
for _ in range(int(input())):
    x, y, z = int(input()), list(map(int, input().split())
                                 ), list(map(int, input().split()))
    for i in range(x):
        if (y[i] > z[i]):
            y[i], z[i] = z[i], y[i]
    print(max(y)*max(z))