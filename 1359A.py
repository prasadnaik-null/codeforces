# 1359A - Berland Poker
import math
for _ in range(int(input())):
    [a, b, c] = list(map(int, input().split()))
    k = a/c
    if b < a/c:
        print(b)
    else:
        print(int(k-math.ceil((b-k)/(c-1))))