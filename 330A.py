# 330A - Cakeminator
[r, c], g, p, l, m = list(map(int, input().split())), [], 0, [], 0
for i in range(r):
    g.append(input())
    if g[i].count("S") == 0:
        p += c
        m += 1
    else:
        k = 0
        for j in range(c):
            if g[i][j] == "S":
                l.append(j)
                k += 1
                if k == g[i].count("S"):
                    break
n = r-m
for i in range(c):
    if i not in l:
        p += n
print(p)