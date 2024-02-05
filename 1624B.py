# 1624B - Make AP
for i in range(int(input())):
    [a, b, c] = list(map(int, input().split()))
    m, M = min(a, c), max(a, c)
    if (m < b and b < M) or b<m:
        if (c+a) % (2*b) == 0:
            print("YES")
        elif ((2*b-M)>0 and (2*b-M) % m == 0) or ((2*b-m)>0 and (2*b-m) % M == 0):
            print("YES")
        else:
            print("NO")
    elif b == m:
        if (c+a) % (2*b) == 0:
            print("YES")
        else:
            print("NO")
    else:
        if ((2*b-M)>0 and (2*b-M) % m == 0) or ((2*b-m)>0 and (2*b-m) % M == 0):
            print("YES")
        else:
            print("NO")