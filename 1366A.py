# 1366A - Shovels and Swords
for _ in range(int(input())):
    [s, d] = list(map(int, input().split()))
    if s > d:
        if s >= 2*d:
            print(d)
        else:
            x = s-d
            d -= x
            x += ((d//3)*2)+((d % 3)//2)
            print(x)
    else:
        if d >= 2*s:
            print(s)
        else:
            x = d-s
            s -= x
            x += ((s//3)*2)+((s % 3)//2)
            print(x)