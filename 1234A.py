# 1234A - Equalize Prices Again
import math
for _ in range(int(input())):
    n, x = int(input()), sum(list(map(int, input().split())))
    print(math.ceil(x/n))