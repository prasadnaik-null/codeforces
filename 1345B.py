# 1345B ~ prasadnaik-null
import math
for _ in range(int(input())):
    n = int(input())
    c = 0
    while n > 1:
        x = (-1+math.sqrt(1+(4*3*2*n)))//6
        n -= (3*x*x+x)//2
        c += 1
    print(c)