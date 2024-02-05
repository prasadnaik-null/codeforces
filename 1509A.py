# 1509A - Average Height
for _ in range(int(input())):
    x, a = input(), []
    for i in list(map(int, input().split())):
        if i % 2 == 0:
            a = a+[i]
        else:
            a = [i]+a
    print(*a)