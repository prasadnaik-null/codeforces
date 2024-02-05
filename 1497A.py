# 1497A - Meximization
for _ in range(int(input())):
    n, s, l, a = input(), sorted(list(map(int, input().split()))), [], []
    for i in s:
        if i not in l:
            l.append(i)
        else:
            a.append(i)
    print(*(l+a))