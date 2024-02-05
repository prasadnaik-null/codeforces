# 1466A - Bovine Dilemma
for _ in range(int(input())):
    n, l, a = int(input()), list(map(int, input().split())), []
    for i in range(n):
        x = l[i]
        for j in range(i+1, n):
            f = l[j]-x
            if f not in a:
                a.append(f)
    print(len(a))