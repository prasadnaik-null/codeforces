# 450A - Jzzhu and Children
[n, m], l, d = list(map(int, input().split())), list(
    map(int, input().split())), {}
for i in range(n):
    d[i+1] = l[i]
while len(d) > 1:
    if list(map(int, d.values()))[0] <= m:
        d.pop(list(map(int, d.keys()))[0])
    else:
        k, v = list(map(int, d.keys()))[0], list(map(int, d.values()))[0]
        d.pop(k)
        d[k] = v-m
print(list(map(int, d.keys()))[0])