# 1430A - Number of Apartments
for _ in range(int(input())):
    i = int(input())
    d, x = i % 3, i//3
    if d == 0:
        print(x, 0, 0)
    elif d == 1:
        if x > 1:
            print(x-2, 0, 1)
        else:
            print(-1)
    else:
        if x > 0:
            print(x-1, 1, 0)
        else:
            print(-1)