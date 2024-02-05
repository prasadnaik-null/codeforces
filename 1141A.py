# 1141A - Game 23
[i, f], a, k = list(map(int, input().split())), 0, True
z = f/i
if z % 1 == 0:
    while z > 1:
        if z % 6 == 0:
            z //= 6
            a += 2
        elif z % 2 == 0:
            z //= 2
            a += 1
        elif z % 3 == 0:
            z //= 3
            a += 1
        else:
            print(-1)
            k = False
            break
    if k == True:
        print(a)
else:
    print(-1)