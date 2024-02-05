# 1333A - Little Artem
for _ in range(int(input())):
    [x, y], a, b = list(map(int, input().split())), "", ""
    for i in range(y):
        if i % 2 == 0:
            a += "B"
            b += "W"
        else:
            a += "W"
            b += "B"
    if x % 2 == 0 or y % 2 == 0:
        for i in range(x):
            if i % 2 == 0:
                if i == x-1:
                    print("BB"+a[2:])
                else:
                    print(a)
            else:
                if i == x-1:
                    print("B"+b[1:])
                else:
                    print(b)
    else:
        for i in range(x):
            if i % 2 == 0:
                print(a)
            else:
                print(b)