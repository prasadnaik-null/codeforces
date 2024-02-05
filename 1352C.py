# 1352C - K-th Not Divisible by n
for _ in range(int(input())):
    [n, k] = list(map(int, input().split()))
    x = (k-1)//(n-1)
    print((n*x)+((k-1) % (n-1))+1)