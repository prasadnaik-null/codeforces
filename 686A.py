# 686A - Free Ice Cream
[n, x] = list(map(int, input().split()))
d = 0
for i in range(n):
    [a, b] = list(map(str, input().split()))
    b = int(b)
    if a == "+":
        x += b
    else:
        if x >= b:
            x -= b
        else:
            d += 1
print(x, d)