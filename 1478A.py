# 1478A - Nezzar and Colorful Balls
for _ in range(int(input())):
    x, y, o, m = int(input()), list(map(int, input().split())), [], 0
    for i in y:
        if i not in o:
            m = max(y.count(i), m)
            o.append(i)
    print(m)