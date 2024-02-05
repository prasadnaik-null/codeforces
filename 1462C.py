# 1462C - Unique Number
for _ in range(int(input())):
    x = int(input())
    if x > 45:
        print(-1)
    else:
        y, s = x, ""
        while y > 0:
            for i in range(9, 0, -1):
                if y >= i:
                    s = str(i)+s
                    y -= i
        print(s)