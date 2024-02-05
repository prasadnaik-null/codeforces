# 1629A - Download More RAM
for _ in range(int(input())):
    [n, k], a, b, l = list(map(int, input().split())), list(map(
        int, input().split())), list(map(int, input().split())), []
    for i in range(n):
        l.append((a[i], b[i]))
    l.sort()
    for i in range(n):
        if l[i][0] <= k:
            k += l[i][1]
        else:
            break
    print(k)