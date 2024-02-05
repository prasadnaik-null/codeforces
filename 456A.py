# 456A - Laptops
n = int(input())
a, b, k = [0]*n, [0]*n, True
for i in range(n):
    [a[i], b[i]] = list(map(int, input().split()))
for i in range(n):
    if b[i] != a[i]:
        k = False
        print("Happy Alex")
        break
if k == True:
    print("Poor Alex")