# 1350A - Orac and Factors
def ans(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i


for _ in range(int(input())):
    [n, k] = list(map(int, input().split()))
    while n % 2 == 1 and k > 0:
        n += ans(n)
        k -= 1
    if n % 2 == 0:
        n += (2*k)
    print(n)