# 1472C - Long Jumps
for _ in range(int(input())):
    n, l = int(input()), list(map(int, input().split()))
    m, k = 0, [0]*n
    for i in range(n-1, -1, -1):
        try:
            x = l[i]+k[i+l[i]]
        except:
            x = l[i]
        k[i] = x
    print(max(k))