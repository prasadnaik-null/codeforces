# 588A - Duff and Meat
n = int(input())
a, p = [0]*n, [0]*n
for i in range(n):
    [a[i], p[i]] = list(map(int, input().split()))
i, s = 0, 0
while i <= n:
    m = 0
    x = p[i]
    for j in range(i+1, n):
        if x > p[j]:
            m = j
            break
    if m == 0:
        s += (sum(a[i:])*p[i])
        break
    else:
        s += (sum(a[i:m])*p[i])
        i = m
print(s)