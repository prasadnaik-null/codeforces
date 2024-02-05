# 1328B - K-th Beautiful String
for _ in range(int(input())):
    [n, k] = list(map(int, input().split()))
    l = k-1
    a = ""
    while True:
        if ((1+(8*l))**0.5) % 1 == 0:
            m = int((-1+(1+(8*l))**0.5)//2)
            break
        else:
            l -= 1
    a += "a"*(n-2-m)+"b"+"a"*(m-k+l+1)+"b"+"a"*(k-l-1)
    print(a)