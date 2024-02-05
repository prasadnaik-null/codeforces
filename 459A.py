# 459A - Pashmak and Garden
[x1, y1, x2, y2] = list(map(int, input().split()))
if x1 == x2:
    x = abs(y1-y2)+x1
    print(x, y1, x, y2)
elif y1 == y2:
    y = abs(x1-x2)+y1
    print(x1, y, x2, y)
elif abs(x1-x2) == abs(y1-y2):
    print(x1, y2, x2, y1)
else:
    print(-1)