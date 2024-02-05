# 1324A - Yet Another Tetris Problem
for _ in range(int(input())):
    n, a, k = int(input()), list(map(int, input().split())), True
    x = a[0] % 2
    for i in a:
        if i % 2 != x:
            k = False
            print("NO")
            break
    if k == True:
        print("YES")