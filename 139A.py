# 139A - Petr and Book
n, w = int(input()), list(map(int, input().split()))
s = sum(w)
n = n % s
if n == 0:
    for i in range(6, -1, -1):
        if w[i] != 0:
            print(i+1)
            break
else:
    for i in range(7):
        if n-w[i] > 0:
            n -= w[i]
        else:
            print(i+1)
            break