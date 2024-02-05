# 1692A - Marathon
for _ in range(int(input())):
    y = list(map(int, input().split()))
    j = y[0]
    a = 0
    for i in range(1, 4):
        if j < y[i]:
            a += 1
    print(a)