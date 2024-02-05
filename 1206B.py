# 1206B - Make Product Equal One
n, l = int(input()), list(map(int, input().split()))
y, a, m = l.count(0), 0, 0
for i in l:
    if i > 0:
        a += i-1
    elif i == 0:
        a += 1
    else:
        a += abs(i)-1
        m += 1
if m % 2 == 1:
    if y == 0:
        a += 2
print(a)