# 1326B - Maximums
n, l, l1, m = int(input()), list(map(int, input().split())), [], 0
for i in l:
    l1.append(i+m)
    if i > 0:
        m += i
print(*l1)