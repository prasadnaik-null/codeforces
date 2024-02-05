# 327A - Flipping Game
n, l, z = int(input()), list(map(int, input().split())), []
o, a = l.count(1), -1
for i in range(n):
    if l[i] == 0:
        z.append(i)
for i in range(len(z)):
    cz = 1
    ii = z[i]
    for j in range(i, len(z)):
        a = max((cz*2)-(z[j]-ii+1), a)
        cz += 1
print(o+a)