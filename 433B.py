# 433B - Kuriyama Mirai's Stones
n, v = int(input()), list(map(int, input().split()))
u = sorted(v)
vo, uo = [0], [0]
x = 0
for i in v:
    x += i
    vo.append(x)
x = 0
for i in u:
    x += i
    uo.append(x)
nn = int(input())
m = [[]]*nn
for _ in range(nn):
    [t, l, r] = list(map(int, input().split()))
    if t == 1:
        print(vo[r]-vo[l-1])
    else:
        print(uo[r]-uo[l-1])