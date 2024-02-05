# 1557A - Ezzat and Two Subsequences
for _ in range((int(input()))):
    x, y = int(input()), list(map(int, input().split()))
    m = max(y)
    s = sum(y)-m
    print(m+(s/(x-1)))