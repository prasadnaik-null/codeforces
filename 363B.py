# 363B - Fence
[n, k], h, d = list(map(int, input().split())), list(
    map(int, input().split())), 0
s = sum(h[:k])
m, mn = s, 1
for i in range(k, n):
    s = s-h[i-k]+h[i]
    if s < m:
        m, mn = s, i-k+2
print(mn)