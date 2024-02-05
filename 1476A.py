# 1476A - K-divisible Sum
import math
for _ in range(int(input())):
    [n, k] = list(map(int, input().split()))
    if k > n:
        print(math.ceil(k/n))
    else:
        if n % k == 0:
            print(1)
        else:
            print(2)