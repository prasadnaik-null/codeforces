# 489B - BerSU Ball
nb, b = int(input()), sorted(list(map(int, input().split())))
ng, g = int(input()), sorted(list(map(int, input().split())))
i, j, a = 0, 0, []
for i in b:
    for j in g:
        if abs(i-j) < 2:
            g.remove(j)
            a.append([i, j])
            break
print(len(a))