# 1354A - Alarm Clock
from math import ceil
for _ in range(int(input())):
    [a, b, c, d] = list(map(int, input().split()))
    a -= b
    if a <= 0:
        print(b)
    else:
        if c <= d:
            print(-1)
        else:
            print(b+ceil(a/(c-d))*c)