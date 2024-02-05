# 1433C - Dominant Piranha
for _ in range(int(input())):
    n, a = int(input()), list(map(int, input().split()))
    if a == [a[1]]*n:
        print(-1)
    else:
        a += [0]
        z = a.index(max(a))
        if z == 0:
            while True:
                if a[z] == a[z+1]:
                    z += 1
                else:
                    break
        print(z+1)