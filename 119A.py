# 119A - Epic Game
import math
[a, b, n], c = list(map(int, input().split())), 0
while n >= 0:
    if c % 2 == 0:
        n -= math.gcd(a, n)
    else:
        n -= math.gcd(b, n)
    c += 1
print(c % 2)