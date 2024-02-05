# 1607B - Odd Grasshopper
for _ in range(int(input())):
    [xo, n] = list(map(int, input().split()))
    y = n % 4
    if xo % 2 == 0:
        if y == 0:
            print(xo)
        elif y == 1:
            print(xo-n)
        elif y == 2:
            print(xo+1)
        else:
            print(xo+1+n)
    else:
        if y == 0:
            print(xo)
        elif y == 1:
            print(xo+n)
        elif y == 2:
            print(xo-1)
        else:
            print(xo-1-n)