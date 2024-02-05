# 1391B - Fix You
for _ in range(int(input())):
    [x, y], l, r = list(map(int, input().split())), [], 0
    for i in range(x):
        l.append(input())
        if l[i][-1] == "R":
            r += 1
    print(r+l[i].count("D"))