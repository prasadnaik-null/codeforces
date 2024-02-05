# 1490B - Balanced Remainders
for _ in range(int(input())):
    n, l, c0, c1, c2, m = int(input()), list(
        map(int, input().split())), 0, 0, 0, 0
    for i in l:
        if i % 3 == 0:
            c0 += 1
        elif i % 3 == 1:
            c1 += 1
        else:
            c2 += 1
    while c0 > n//3:
        if c1 < n//3:
            m += 1
            c1 += 1
            c0 -= 1
        elif c2 < n//3:
            m += 2
            c2 += 1
            c0 -= 1
    while c1 > n//3:
        if c0 < n//3:
            m += 2
            c0 += 1
            c1 -= 1
        elif c2 < n//3:
            m += 1
            c2 += 1
            c1 -= 1
    while c2 > n//3:
        if c0 < n//3:
            m += 1
            c0 += 1
            c2 -= 1
        elif c1 < n//3:
            m += 2
            c1 += 1
            c2 -= 1
    print(m)