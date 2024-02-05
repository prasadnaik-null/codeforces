# 1471A - Strange Partition
from math import ceil
for _ in range(int(input())):
    [n, x] = list(map(int, input().split()))
    l, a, d = list(map(int, input().split())), 0, 0
    for i in range(n):
        a += ceil(l[i]/x)
        d += l[i]
    print(ceil(d/x), a)