# 1406A - Subset Mex

for _ in range(int(input())):
    n, l = int(input()), list(map(int, input().split()))
    i, a, b = 0, -1, -1
    while True:
        if l.count(i) == 0:
            if a == -1:
                a = i
            b = i
            break
        elif l.count(i) == 1:
            if a == -1:
                a = i
        i += 1
    print(a+b)