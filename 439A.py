# 439A - Devu, the Singer and Churu, the Joker
[n, d], l = list(map(int, input().split())), sum(
    list(map(int, input().split())))
if d < (l+(n-1)*10):
    print(-1)
else:
    print((d-l)//5)