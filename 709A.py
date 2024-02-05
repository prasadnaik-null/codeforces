# 709A - Juicer
[n, b, d], l, c, a = list(map(int, input().split())), list(
    map(int, input().split())), 0, 0
for i in l:
    if i <= b:
        c += i
    if c > d:
        a += 1
        c = 0
print(a)