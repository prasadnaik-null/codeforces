# 1358B - Maria Breaks the Self-isolation
for _ in range(int(input())):
    n, l = int(input()), [0]+sorted(list(map(int, input().split())))
    for i in range(len(l)-1, -1, -1):
        if l[i] <= i:
            print(i+1)
            break