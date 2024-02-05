# 598A - Tricky Sum
for _ in range(int(input())):
    n = int(input())
    s = (n*(n+1))//2
    i = 1
    while i <= n:
        s -= i*2
        i *= 2
    print(s)