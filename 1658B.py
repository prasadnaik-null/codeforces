# 1658B - Marin and Anti-coprime Permutation
import math
for _ in range(int(input())):
    x = int(input())
    if x % 2 == 1:
        print(0)
    else:
        print((math.factorial(x//2)**2) % 998244353)