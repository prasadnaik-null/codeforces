# 599A - Patrick and Shopping
[d1, d2, d3] = list(map(int, input().split()))
print(min(d1+d2+d3, 2*d1+2*d2, 2*d1+2*d3, 2*d2+2*d3))