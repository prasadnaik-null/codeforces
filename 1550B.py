# 1550B - Maximum Cost Deletion
for _ in range(int(input())):
    [n, a, b] = list(map(int, input().split()))
    y = input()
    if b >= 0:
        print((a+b)*n)
    else:
        l = [0, 0]
        x = y[0]
        for i in y:
            if i != x:
                l[int(x)] += 1
                x = i
        l[int(x)] += 1
        print(a*n+b*(min(l)+1))