# 1535B - Array Reodering
import math
for _ in range(int(input())):
    x, y, a, e, o = int(input()), list(map(int, input().split())), 0, 0, []
    for i in y:
        if i % 2 == 0:
            e += 1
        else:
            o.append(i)
    for i in range(e):
        a += x-i-1
    for i in range(len(o)):
        for j in range(i+1, len(o)):
            if math.gcd(o[i], o[j]) > 1:
                a += 1
    print(a)