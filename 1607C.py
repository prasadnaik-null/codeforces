# 1607C - Minimum Extraction
for _ in range(int(input())):
    n, a = int(input()), sorted(list(map(int, input().split())))
    m = min(a)
    for i in range(1, n):
        m = max(m, a[i]-a[i-1])
    print(m)