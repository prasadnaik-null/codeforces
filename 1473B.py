# 1473B - String LCM
import math


def lcm(a, b):
    return a*b//math.gcd(a, b)


for _ in range(int(input())):
    [y, x] = sorted([input(), input()])
    f, j, k = "_", 0, False
    for i in range(1, len(x)):
        if len(x) % i == 0:
            if x[:i]*(len(x)//i) == x and x[:i]*(len(y)//i) == y:
                f = x[:i]
                j = i
                k = True
                break
    if k == True:
        l = lcm(len(x)//j, len(y)//j)
        print(f*l)
    else:
        if x == y:
            print(x)
        else:
            print(-1)