# 1554A - Cherry
for _ in range(int(input())):
    x, y, m = int(input()), list(map(int, input().split())), 0
    for i in range(x-1):
        m = max(m, y[i]*y[i+1])
    print(m)