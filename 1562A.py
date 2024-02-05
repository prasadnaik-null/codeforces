# 1562A - The Miracle and the Sleeper
for _ in range(int(input())):
    [l, r] = list(map(int, input().split()))
    if (r+1)//2 >= l:
        print((r-1)//2)
    else:
        print(r-l)