# 1283B - Candies Division
for _ in range(int(input())):
    [n, k] = list(map(int, input().split()))
    a = (n//k)*k
    n -= a
    if n > k//2:
        n = k//2
    a += n
    print(a)