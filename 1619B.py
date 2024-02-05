# 1619B - Squares and Cubes
import math
for _ in range(int(input())):
    x = int(input())
    s, c = x**(1./2), x**(1./3)
    if round(s)**2 == x:
        s = round(s)
    else:
        s = int(s)
    if round(c)**3 == x:
        c = round(c)
    else:
        c = int(c)
    d = c**(1./2)
    if round(d)**2 == c:
        d = round(d)
    else:
        d = int(d)
    print(s+c-d)