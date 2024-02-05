# 1405B - Array Cancellation
for _ in range(int(input())):
    n, l = int(input()), list(map(int, input().split()))
    a, m = 0, 0
    for i in l:
        a += i
        m = min(m, a)
    print(-m)