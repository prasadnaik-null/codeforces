# 1520C - Not Adjacent Matrix
for _ in range((int(input()))):
    x = int(input())
    if x == 2:
        print(-1)
    else:
        l = []
        for i in range(1, (x**2)+1, 2):
            l.append(i)
        for i in range(2, (x**2)+1, 2):
            l.append(i)
        for i in range(0, x**2, x):
            print(*l[i:i+x])