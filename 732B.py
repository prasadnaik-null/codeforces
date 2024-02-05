# 732B - Cormen  The Best Friend Of a Man
[n, k], l, a = list(map(int, input().split())), list(
    map(int, input().split())), 0
for i in range(n-1):
    if l[i]+l[i+1] < k:
        x = k-l[i]-l[i+1]
        l[i+1] += x
        a += x
print(a)
print(*l)