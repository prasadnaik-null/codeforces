# 1362A - Johnny and Ancient Computer
from math import log2
from math import ceil


def func(i, f):
    x = f/i
    if i*int(x) == f:
        z = log2(x)
        if x == 2**round(z):
            print(ceil(round(z)/3))
        else:
            print(-1)
    else:
        print(-1)


for _ in range(int(input())):
    [i, f] = list(map(int, input().split()))
    if f > i:
        func(i, f)
    else:
        func(f, i)