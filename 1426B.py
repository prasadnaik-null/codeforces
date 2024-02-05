# 1426B - Symmetric Matrix
for _ in range(int(input())):
    [n, m] = list(map(int, input().split()))
    l, k = [None]*n, False
    if m % 2 == 1:
        print("NO")
        for i in range(n):
            input()
            input()
    else:
        for i in range(n):
            l[i] = [list(map(int, input().split()))]
            l[i].append(list(map(int, input().split())))
            if k == False and l[i][0][1] == l[i][1][0]:
                k = True
        if k == True:
            print("YES")
        else:
            print("NO")