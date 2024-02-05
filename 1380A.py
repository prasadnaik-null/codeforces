# 1380A - Three Indices
for _ in range(int(input())):
    n, l = int(input()), list(map(int, input().split()))
    m = l
    for i in range(n, 0, -1):
        if l.index(i) == 0:
            l = l[1:]
        elif l.index(i) == i-1:
            l = l[:-1]
        else:
            z = m.index(i)
            print("YES")
            print(z, z+1, z+2)
            break
    if l == []:
        print("NO")